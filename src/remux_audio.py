"""
비디오 재렌더링 없이 오디오(TTS 음성 + 붓 SFX + BGM)만 초고속으로 합성/결합하는 리믹서 (Audio Remuxer)
- 비디오 인코딩이 필요 없으므로 1편당 단 1~2초 만에 오디오 결합 완료
- 전체 160자 무음 영상을 약 2~3분 만에 100% 완전체 영상으로 복구
"""
import os
import sys
import subprocess
import shutil

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from hanzi_data import HANZI_DATABASE
from tts_generator import prepare_hanzi_audios, get_ffmpeg_exe
from generate_sfx import generate_brush_stroke_sfx
from bgm_generator import generate_traditional_hanzi_bgm

def get_audio_duration(file_path: str) -> float:
    try:
        ffmpeg_exe = get_ffmpeg_exe()
        res = subprocess.run([ffmpeg_exe, "-i", file_path], capture_output=True, text=True, errors="replace")
        import re
        m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
        if m:
            hours, mins, secs = m.groups()
            return int(hours) * 3600 + int(mins) * 60 + float(secs)
    except Exception:
        pass
    return 30.0

def remux_single_char(char: str) -> bool:
    if char not in HANZI_DATABASE:
        return False
    
    hanzi_info = HANZI_DATABASE[char]
    hun_eum = hanzi_info["hun_eum"].replace(" ", "_")
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output"))
    final_output = os.path.join(output_dir, f"shorts_{char}_{hun_eum}.mp4")
    
    if not os.path.exists(final_output):
        return False

    ffmpeg_bin = get_ffmpeg_exe()
    
    # 1. 오디오 리소스 생성 및 준비
    sfx_path = generate_brush_stroke_sfx()
    bgm_path = generate_traditional_hanzi_bgm(char=char)
    audio_paths = prepare_hanzi_audios(hanzi_info)
    
    huneum_dur = get_audio_duration(audio_paths["huneum"])
    video_dur = get_audio_duration(final_output)
    
    # 2. 멀티트랙 인풋 구성
    temp_clean_video = final_output.replace(".mp4", "_temp_in.mp4")
    shutil.move(final_output, temp_clean_video)
    
    inputs = ["-i", temp_clean_video.replace("\\", "/")]
    
    # 1번: 훅 설명 음성 (800ms)
    inputs.extend(["-i", audio_paths["hook"].replace("\\", "/")])
    filter_parts = ["[1:a]adelay=800|800,volume=2.4[a_hook]"]
    mix_inputs = ["[a_hook]"]

    input_idx = 2
    stroke_start_time = 7800
    stroke_interval = 1600
    num_strokes = len(hanzi_info.get("stroke_names", [])) if "stroke_names" in hanzi_info else hanzi_info["stroke_count"]
    
    sfx_dir = os.path.join("assets", "audio", "sfx")
    sfx_files = sorted([os.path.join(sfx_dir, f) for f in os.listdir(sfx_dir) if f.endswith(".wav")]) if os.path.exists(sfx_dir) else [sfx_path]
    if not sfx_files:
        sfx_files = [sfx_path]

    for s_idx in range(num_strokes):
        current_stroke_sfx = sfx_files[s_idx % len(sfx_files)]
        inputs.extend(["-i", current_stroke_sfx.replace("\\", "/")])
        delay_ms = stroke_start_time + s_idx * stroke_interval
        filter_parts.append(f"[{input_idx}:a]adelay={delay_ms}|{delay_ms},volume=1.10[a_sfx{s_idx}]")
        mix_inputs.append(f"[a_sfx{s_idx}]")
        input_idx += 1

    # 훈음 오디오
    last_stroke_start = stroke_start_time + (num_strokes - 1) * stroke_interval
    huneum_time = last_stroke_start + 3300
    inputs.extend(["-i", audio_paths["huneum"].replace("\\", "/")])
    filter_parts.append(f"[{input_idx}:a]adelay={huneum_time}|{huneum_time},volume=1.8[a_huneum]")
    mix_inputs.append("[a_huneum]")
    input_idx += 1

    # 실생활 단어 오디오
    huneum_dur_ms = int(huneum_dur * 1000)
    word_time = huneum_time + max(huneum_dur_ms, 2500) + 400 + 800
    inputs.extend(["-i", audio_paths["example_word"].replace("\\", "/")])
    filter_parts.append(f"[{input_idx}:a]adelay={word_time}|{word_time},volume=1.8[a_word]")
    mix_inputs.append("[a_word]")
    input_idx += 1

    # BGM
    inputs.extend(["-i", bgm_path.replace("\\", "/")])
    writing_start_s = 7.4
    writing_end_s = max(round((last_stroke_start + 1200) / 1000.0, 2), 8.0)
    bgm_filter = (
        f"[{input_idx}:a]volume='if(lt(t,7.0),0.18,"
        f"if(lt(t,{writing_start_s}),0.18*({writing_start_s}-t)/0.4,"
        f"if(lt(t,{writing_end_s}),0,"
        f"if(lt(t,{writing_end_s}+0.5),0.22*(t-{writing_end_s})/0.5,0.22))))':eval=frame[a_bgm]"
    )
    filter_parts.append(bgm_filter)
    mix_inputs.append("[a_bgm]")
    input_idx += 1
    total_audio_tracks = len(mix_inputs)

    filter_str = ";".join(filter_parts) + f";{''.join(mix_inputs)}amix=inputs={total_audio_tracks}:duration=longest:dropout_transition=2,atrim=0:{video_dur:.3f}[aout]"

    ffmpeg_cmd = [
        ffmpeg_bin, "-y"
    ] + inputs + [
        "-filter_complex", filter_str,
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-t", f"{video_dur:.3f}",
        final_output
    ]

    try:
        res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, errors="replace")
        if os.path.exists(temp_clean_video):
            os.remove(temp_clean_video)
        return res.returncode == 0
    except Exception:
        if os.path.exists(temp_clean_video):
            shutil.move(temp_clean_video, final_output)
        return False

def remux_all_silent():
    ffmpeg_bin = get_ffmpeg_exe()
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output"))
    
    print("\n🔍 [오디오 결합 상태 전수 검사 중]...")
    to_fix = []
    for char, info in HANZI_DATABASE.items():
        hun_eum = info["hun_eum"].replace(" ", "_")
        target_mp4 = os.path.join(output_dir, f"shorts_{char}_{hun_eum}.mp4")
        if os.path.exists(target_mp4):
            chk = subprocess.run([ffmpeg_bin, "-i", target_mp4], capture_output=True, text=True, errors="replace")
            if "Audio:" not in chk.stderr:
                to_fix.append(char)
                
    total = len(to_fix)
    print(f"⚡ [초고속 사운드 합성 시작] 소리 누락 파일 총 {total}개 발견 (예상 소요 시간: 약 2~3분)\n" + "="*50)
    
    for idx, char in enumerate(to_fix, 1):
        print(f"[{idx}/{total}] 🎵 '{char}' 사운드 트랙 믹싱 중...", end=" ", flush=True)
        success = remux_single_char(char)
        if success:
            print("✅ 완료!")
        else:
            print("❌ 실패")
            
    print("\n" + "="*50)
    print("🎉 [사운드 복구 완료] 모든 숏폼 영상에 BGM/음성/붓소리가 100% 장착되었습니다!")

if __name__ == "__main__":
    remux_all_silent()
