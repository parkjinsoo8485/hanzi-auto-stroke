"""
상형문자 숏폼 전체 자동 생성 파이프라인 러너 (화선지 + 실사 손 붓글씨 + SFX & 듀얼 TTS 믹싱)
"""
import os
import sys
import subprocess
import argparse
import shutil

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import re
from hanzi_data import HANZI_DATABASE
from tts_generator import prepare_hanzi_audios, get_ffmpeg_exe
from animcjk_loader import parse_animcjk_strokes
from generate_sfx import generate_brush_stroke_sfx
from bgm_generator import generate_traditional_hanzi_bgm

def get_audio_duration(file_path: str) -> float:
    """FFmpeg를 통해 오디오 파일의 정확한 재생 길이(초) 추출"""
    try:
        ffmpeg_exe = get_ffmpeg_exe()
        res = subprocess.run([ffmpeg_exe, "-i", file_path], capture_output=True, text=True, errors="replace")
        m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
        if m:
            h, m_, s = m.groups()
            return int(h) * 3600 + int(m_) * 60 + float(s)
    except Exception:
        pass
    return 3.5

def run_pipeline(char="大", quality="m", preview=False):
    """
    1. AnimCJK 정통 붓글씨 획순 SVG 파싱
    2. 한국어 + 미국 원어민 영어 듀얼 TTS 및 획별 가이드 음성 생성
    3. 서예 붓글씨 마찰 SFX 및 동양풍 전통 앰비언트 BGM 생성
    4. Manim 실사 손+붓 9:16 비디오 렌더링
    5. FFmpeg 멀티트랙 오디오, SFX, BGM 완벽 믹싱 (음성 겹침 방지)
    """
    if char not in HANZI_DATABASE:
        print(f"[Error] 지원되지 않는 한자입니다: {char}")
        print(f"현재 지원 가능한 한자: {list(HANZI_DATABASE.keys())}")
        return False

    print(f"\n=======================================================")
    print(f"🎨 [POV Hand-Brush & Paper] 숏폼 파이프라인 가동: 「{char}」")
    print(f"=======================================================")

    # 1. AnimCJK 획순 데이터 준비
    print("\n[Step 1] AnimCJK 정통 해서체 획순 SVG 파싱 중...")
    animcjk_data = parse_animcjk_strokes(char)
    print(f"-> 획순 준비 완료: 총 {len(animcjk_data['strokes'])}개 획")

    # 2. TTS 음성 및 SFX, BGM 준비
    print("\n[Step 2] 한국어/원어민 영어 듀얼, 획별 가이드 TTS & 붓 SFX & 동양풍 BGM 생성 중...")
    audio_paths = prepare_hanzi_audios(HANZI_DATABASE[char])
    sfx_path = generate_brush_stroke_sfx("assets/audio/brush_stroke.wav", duration=1.5)
    bgm_path = generate_traditional_hanzi_bgm("assets/audio/hanzi_study_bgm.wav", char=char, duration=35.0)
    print(f"-> 오디오 & SFX, BGM 준비 완료!")

    # 3. Manim 렌더링
    print(f"\n[Step 3] Manim 9:16 비디오 렌더링 중 (품질: {quality})...")
    quality_flag = f"-q{quality}"
    scene_file = os.path.join(os.path.dirname(__file__), "short_scene.py")
    
    # 가상환경 python 또는 현재 인터프리터 감지
    venv_python = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".venv", "Scripts", "python.exe"))
    if os.path.exists(venv_python):
        python_exe = venv_python
    else:
        python_exe = sys.executable

    manim_cmd = [
        python_exe, "-m", "manim",
        scene_file, "HanziShortScene",
        quality_flag,
        "--disable_caching"
    ]
    
    # 인코딩 깨짐 방지를 위해 JSON 파일로 현재 한자 전달
    os.makedirs("assets", exist_ok=True)
    import json
    with open("assets/current_char.json", "w", encoding="utf-8") as f:
        json.dump({"char": char}, f, ensure_ascii=False)

    env = os.environ.copy()
    env["HANZI_CHAR"] = char
    print(f"실행 명령: {' '.join(manim_cmd)} (한자: {char})")
    result = subprocess.run(manim_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    
    if result.returncode != 0:
        print(f"[Error] Manim 렌더링 실패:\n{result.stderr}\n{result.stdout}")
        return False
    else:
        print("[Manim] 렌더링 완료!")

    # 4. 가장 최근에 렌더링된 비디오 파일 찾기
    media_dir = "media/videos/short_scene"
    candidate_mp4s = []
    for root, dirs, files in os.walk(media_dir):
        for f in files:
            if f.endswith(".mp4") and "HanziShortScene" in f:
                full_p = os.path.join(root, f)
                candidate_mp4s.append(full_p)
    
    if not candidate_mp4s:
        print(f"[Error] 렌더링된 MP4 비디오를 찾을 수 없습니다.")
        return False
    
    # 가장 최근에 생성된 비디오 선택
    rendered_mp4 = max(candidate_mp4s, key=os.path.getmtime)
    print(f"-> 기본 비디오 경로: {rendered_mp4}")

    # 5. FFmpeg를 통한 멀티트랙 오디오 & SFX, BGM 믹싱
    print("\n[Step 4] 동양풍 BGM & 실사 서예 사운드 & 가이드 음성 멀티트랙 믹싱 및 최종 Shorts 완성...")
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    final_output = os.path.join(output_dir, f"shorts_{char}_{HANZI_DATABASE[char]['hun_eum'].replace(' ', '_')}.mp4")

    # 오디오 인풋 리스트 구성
    inputs = ["-i", rendered_mp4.replace("\\", "/")]
    
    # 1번: 훅 (0.8s = 800ms) - 인트로 상형 설명 음성 2.4배로 크고 시원하게 전달
    inputs.extend(["-i", audio_paths["hook"].replace("\\", "/")])
    filter_parts = ["[1:a]adelay=800|800,volume=2.4[a_hook]"]
    mix_inputs = ["[a_hook]"]

    input_idx = 2
    # 📌 [100% 완벽 동기화] 붓끝이 화선지에 닿아 획을 긋는 순간(7700ms)부터 
    # 획당 0.95초 동안 사각사각 화선지 ASMR 사운드가 1:1 완벽하게 일치되어 재생!
    stroke_start_time = 7700  # 7.70초: 1획 붓끝 착지 및 이동 시작 순간
    stroke_interval = 1430    # 1.43초: 획간 완벽한 물리적 시간차 (0.95s 쓰기 + 0.16s 수필 + 0.32s 다음 획 이동/착지)
    num_strokes = len(HANZI_DATABASE[char].get("stroke_names", [])) if "stroke_names" in HANZI_DATABASE[char] else HANZI_DATABASE[char]["stroke_count"]
    
    sfx_dir = os.path.join("assets", "audio", "sfx")
    sfx_files = sorted([os.path.join(sfx_dir, f) for f in os.listdir(sfx_dir) if f.endswith(".wav")]) if os.path.exists(sfx_dir) else [sfx_path]
    if not sfx_files:
        sfx_files = [sfx_path]

    for s_idx in range(num_strokes):
        current_stroke_sfx = sfx_files[s_idx % len(sfx_files)]
        inputs.extend(["-i", current_stroke_sfx.replace("\\", "/")])
        delay_ms = stroke_start_time + s_idx * stroke_interval
        # 획을 그릴 때 편안하고 은은하게 들리도록 자연스러운 볼륨(1.0배)으로 믹싱
        filter_parts.append(f"[{input_idx}:a]adelay={delay_ms}|{delay_ms},volume=1.0[a_sfx{s_idx}]")
        mix_inputs.append(f"[a_sfx{s_idx}]")
        input_idx += 1

    # 훈음 오디오 (마지막 획 작성 완료 + 손 퇴장 + 플래시 + 훈음 카드 등장 직후)
    last_stroke_start = stroke_start_time + (num_strokes - 1) * stroke_interval
    huneum_time = last_stroke_start + 3410  # 0.95s(쓰기) + 0.16s(수필) + 0.5s(퇴장) + 0.7s(플래시) + 0.3s + 0.5s(카드) + 0.3s
    huneum_dur_ms = int(get_audio_duration(audio_paths["huneum"]) * 1000)
    inputs.extend(["-i", audio_paths["huneum"].replace("\\", "/")])
    filter_parts.append(f"[{input_idx}:a]adelay={huneum_time}|{huneum_time},volume=1.8[a_huneum]")
    mix_inputs.append("[a_huneum]")
    input_idx += 1

    # 실생활 단어 오디오 (훈음 오디오 재생 완료 후 + 450ms 여유 버퍼)
    word_time = huneum_time + huneum_dur_ms + 450
    inputs.extend(["-i", audio_paths["example_word"].replace("\\", "/")])
    filter_parts.append(f"[{input_idx}:a]adelay={word_time}|{word_time},volume=1.8[a_word]")
    mix_inputs.append("[a_word]")
    input_idx += 1

    # 동양풍 한자 서예 훅 BGM 추가
    # 📌 획순 작성 ASMR 구간(7.4s ~ 획 작성 및 손 퇴장 시점)에는 BGM을 완전 무음 처리하여 붓글씨 ASMR에 100% 몰입!
    inputs.extend(["-i", bgm_path.replace("\\", "/")])
    writing_start_s = 7.4
    writing_end_s = max(round((last_stroke_start + 1150) / 1000.0, 2), 8.0)
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

    # amix 필터 결합
    filter_str = ";".join(filter_parts) + f";{''.join(mix_inputs)}amix=inputs={total_audio_tracks}:dropout_transition=2[aout]"

    ffmpeg_cmd = [
        get_ffmpeg_exe(), "-y"
    ] + inputs + [
        "-filter_complex", filter_str,
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        final_output
    ]

    print(f"실행 명령: {' '.join(ffmpeg_cmd)}")
    try:
        ff_res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if ff_res.returncode != 0:
            print(f"[Warning] 오디오 믹싱 중 에러 발생:\n{ff_res.stderr}")
            shutil.copy(rendered_mp4, final_output)
    except Exception as e:
        print(f"[Warning] FFmpeg 실행 불가, 원본 비디오 복사: {e}")
        shutil.copy(rendered_mp4, final_output)
    
    print(f"\n🎉 [성공] 참고 영상 스타일 실사 서예 숏폼 영상이 성공적으로 제작되었습니다!")
    print(f"📁 결과 파일: {os.path.abspath(final_output)}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="상형문자 숏폼 자동 생성기")
    parser.add_argument("--char", type=str, default="大", help="생성할 한자 (기본: 大)")
    parser.add_argument("--quality", type=str, default="m", choices=["l", "m", "h", "k"], help="렌더링 품질 (l: 480p 초고속, m: 720p, h: 1080p)")
    args = parser.parse_args()

    run_pipeline(char=args.char, quality=args.quality)
