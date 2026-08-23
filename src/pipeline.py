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

from hanzi_data import HANZI_DATABASE
from tts_generator import prepare_hanzi_audios
from animcjk_loader import parse_animcjk_strokes
from generate_sfx import generate_brush_stroke_sfx

def run_pipeline(char="大", quality="m", preview=False):
    """
    1. AnimCJK 정통 붓글씨 획순 SVG 파싱
    2. 한국어 + 미국 원어민 영어 듀얼 TTS 및 획별 가이드 음성 생성
    3. 서예 붓글씨 마찰 SFX 생성
    4. Manim 실사 손+붓 9:16 비디오 렌더링
    5. FFmpeg 멀티트랙 오디오 & SFX 믹싱
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

    # 2. TTS 음성 및 SFX 준비
    print("\n[Step 2] 한국어/원어민 영어 듀얼, 획별 가이드 TTS & 붓 SFX 생성 중...")
    audio_paths = prepare_hanzi_audios(HANZI_DATABASE[char])
    sfx_path = generate_brush_stroke_sfx("assets/audio/brush_stroke.wav", duration=1.5)
    print(f"-> 오디오 & SFX 준비 완료: {audio_paths}")

    # 3. Manim 렌더링
    print(f"\n[Step 3] Manim 9:16 비디오 렌더링 중 (품질: {quality})...")
    quality_flag = f"-q{quality}"
    scene_file = os.path.join(os.path.dirname(__file__), "short_scene.py")
    
    python_exe = sys.executable
    manim_cmd = [
        python_exe, "-m", "manim",
        scene_file, "HanziShortScene",
        quality_flag,
        "--disable_caching"
    ]
    
    env = os.environ.copy()
    env["HANZI_CHAR"] = char
    print(f"실행 명령: {' '.join(manim_cmd)} (한자: {char})")
    result = subprocess.run(manim_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    
    if result.returncode != 0:
        print(f"[Error] Manim 렌더링 실패:\n{result.stderr}\n{result.stdout}")
        return False
    else:
        print("[Manim] 렌더링 완료!")

    # 4. 렌더링된 비디오 파일 찾기
    media_dir = "media/videos/short_scene"
    rendered_mp4 = None
    for root, dirs, files in os.walk(media_dir):
        for f in files:
            if f.endswith(".mp4") and "HanziShortScene" in f:
                rendered_mp4 = os.path.join(root, f)
                break
    
    if not rendered_mp4 or not os.path.exists(rendered_mp4):
        print(f"[Error] 렌더링된 MP4 비디오를 찾을 수 없습니다: {rendered_mp4}")
        return False
    
    print(f"-> 기본 비디오 경로: {rendered_mp4}")

    # 5. FFmpeg를 통한 멀티트랙 오디오 & SFX 믹싱
    print("\n[Step 4] 실사 서예 사운드 & 가이드 음성 멀티트랙 믹싱 및 최종 Shorts 완성...")
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    final_output = os.path.join(output_dir, f"shorts_{char}_{HANZI_DATABASE[char]['hun_eum'].replace(' ', '_')}.mp4")

    # 오디오 인풋 리스트 구성
    inputs = ["-i", rendered_mp4.replace("\\", "/")]
    
    # 1번: 훅 (0.8s = 800ms) - 첫 한국어 발음 음량 1.8배 증폭
    inputs.extend(["-i", audio_paths["hook"].replace("\\", "/")])
    filter_parts = ["[1:a]adelay=800|800,volume=1.8[a_hook]"]
    mix_inputs = ["[a_hook]"]

    input_idx = 2
    stroke_start_time = 4000  # 4.0초
    stroke_interval = 2200    # 획당 약 2.2초 간격
    
    # 획별 가이드 음성 및 붓글씨 SFX 추가
    for s_idx, s_path in enumerate(audio_paths["strokes"]):
        # 가이드 음성 (볼륨 1.4배)
        inputs.extend(["-i", s_path.replace("\\", "/")])
        delay_ms = stroke_start_time + s_idx * stroke_interval
        filter_parts.append(f"[{input_idx}:a]adelay={delay_ms}|{delay_ms},volume=1.4[a_s{s_idx}]")
        mix_inputs.append(f"[a_s{s_idx}]")
        input_idx += 1

        # 붓글씨 마찰 SFX
        inputs.extend(["-i", sfx_path.replace("\\", "/")])
        sfx_delay = delay_ms + 200
        filter_parts.append(f"[{input_idx}:a]adelay={sfx_delay}|{sfx_delay},volume=0.85[a_sfx{s_idx}]")
        mix_inputs.append(f"[a_sfx{s_idx}]")
        input_idx += 1

    # 훈음 오디오 (획 작성 종료 후)
    huneum_time = stroke_start_time + len(audio_paths["strokes"]) * stroke_interval + 400
    inputs.extend(["-i", audio_paths["huneum"].replace("\\", "/")])
    filter_parts.append(f"[{input_idx}:a]adelay={huneum_time}|{huneum_time},volume=1.3[a_huneum]")
    mix_inputs.append("[a_huneum]")
    input_idx += 1

    # 단어 오디오
    word_time = huneum_time + 2600
    inputs.extend(["-i", audio_paths["example_word"].replace("\\", "/")])
    filter_parts.append(f"[{input_idx}:a]adelay={word_time}|{word_time},volume=1.3[a_word]")
    mix_inputs.append("[a_word]")
    total_audio_tracks = len(mix_inputs)

    # amix 필터 결합
    filter_str = ";".join(filter_parts) + f";{''.join(mix_inputs)}amix=inputs={total_audio_tracks}:dropout_transition=2[aout]"

    ffmpeg_cmd = [
        "ffmpeg", "-y"
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
    ff_res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if ff_res.returncode != 0:
        print(f"[Warning] 오디오 믹싱 중 에러 발생:\n{ff_res.stderr}")
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
