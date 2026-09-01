"""
edge-tts 기반 한국어 성우 + 미국 프리미엄 원어민 성우 듀얼 음성 및 획별 획순 가이드 음성 자동 생성 모듈
- 한자별 정확한 획 명칭(가로, 세로, 삐침, 파임 등) 음성 지원
- 고급스럽고 자연스러운 프리미엄 미국 영문 내레이션 (en-US-AriaNeural)
- 슬래시(/) 등 특수문자를 자연스러운 쉼표 및 호흡으로 처리하여 '슬래시' 발음 원천 차단
"""
import os
import sys
import re
import asyncio
import edge_tts
import subprocess
import shutil

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def get_ffmpeg_exe():
    # 1. imageio_ffmpeg 라이브러리 직접 호출
    try:
        import imageio_ffmpeg
        fpath = imageio_ffmpeg.get_ffmpeg_exe()
        if fpath and os.path.exists(fpath):
            return fpath
    except Exception:
        pass

    # 2. 로컬 가상환경(.venv) 내부 바이너리 직접 탐색
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    venv_binaries_dir = os.path.join(project_root, ".venv", "Lib", "site-packages", "imageio_ffmpeg", "binaries")
    if os.path.exists(venv_binaries_dir):
        for fname in os.listdir(venv_binaries_dir):
            if fname.startswith("ffmpeg") and fname.endswith(".exe"):
                full_p = os.path.join(venv_binaries_dir, fname)
                if os.path.exists(full_p):
                    return full_p

    # 3. 시스템 환경 변수 및 표준 설치 경로 탐색
    exe = shutil.which("ffmpeg")
    if exe and os.path.exists(exe):
        return exe
        
    try:
        from manim import config
        if config.ffmpeg_executable and os.path.exists(config.ffmpeg_executable):
            return config.ffmpeg_executable
    except Exception:
        pass

    for path in [
        r"C:\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        os.path.expanduser(r"~\scoop\apps\ffmpeg\current\bin\ffmpeg.exe"),
        os.path.expanduser(r"~\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe")
    ]:
        if os.path.exists(path):
            return path
            
    return "ffmpeg"

# 한국어 성우 (밝고 또렷한 톤)
VOICE_KO = "ko-KR-SunHiNeural"
# 미국 원어민 고급 성우 (자연스럽고 세련된 프리미엄 내레이션)
VOICE_EN = "en-US-AriaNeural"

def clean_hook_text(text: str) -> str:
    """처음 한자 의미 설명(훅) 낭독 시에만 괄호 () 안의 한글을 생략하고 자연스러운 쉼표 띄어 읽기 적용"""
    if not text:
        return ""
    # 괄호 및 괄호 안의 텍스트 생략 (예: (태양) -> 생략)
    text = re.sub(r'\([^)]*\)', '', text)
    # 슬래시 치환
    text = text.replace("/", ", ")
    # 접속 조사(와, 과, 및) 뒤에 쉼표가 없으면 자연스러운 호흡(띄어 읽기)을 위해 쉼표 추가
    text = re.sub(r'([가-힣]+(?:와|과|및))\s+(?![,\.!])', r'\1, ', text)
    # 중복 쉼표 및 다중 공백 정리
    text = re.sub(r',\s*,+', ', ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_spoken_text(text: str) -> str:
    """일반 TTS 음성 낭독 시 슬래시(/) 치환 및 공백 정리 (괄호 임의 삭제 방지)"""
    if not text:
        return ""
    text = text.replace("/", ", ")
    text = re.sub(r'\s+', ' ', text).strip()
    return text

async def generate_speech_async(text: str, output_path: str, voice: str = VOICE_KO, rate: str = "+0%", pitch: str = "+0Hz", volume: str = "+25%"):
    """텍스트를 고품질 신경망 음성 파일(mp3)로 생성 (볼륨 증폭 지원)"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    clean_text = clean_spoken_text(text)
    communicate = edge_tts.Communicate(clean_text, voice, rate=rate, pitch=pitch, volume=volume)
    await communicate.save(output_path)
    print(f"[TTS ({voice})] Generated: {output_path} -> \"{clean_text}\"")

def generate_speech(text: str, output_path: str, voice: str = VOICE_KO, rate: str = "+0%", pitch: str = "+0Hz", volume: str = "+25%"):
    """동기식 래퍼 함수"""
    asyncio.run(generate_speech_async(text, output_path, voice, rate, pitch, volume))

KOREAN_ORDINALS = {
    1: "첫 번째", 2: "두 번째", 3: "세 번째", 4: "네 번째", 5: "다섯 번째",
    6: "여섯 번째", 7: "일곱 번째", 8: "여덟 번째", 9: "아홉 번째", 10: "열 번째",
    11: "열한 번째", 12: "열두 번째", 13: "열세 번째", 14: "열네 번째", 15: "열다섯 번째",
    16: "열여섯 번째", 17: "열일곱 번째", 18: "열여덟 번째", 19: "열아홉 번째", 20: "스무 번째",
    21: "스물한 번째", 22: "스물두 번째", 23: "스물세 번째", 24: "스물네 번째", 25: "스물다섯 번째",
    26: "스물여섯 번째", 27: "스물일곱 번째", 28: "스물여덟 번째", 29: "스물아홉 번째", 30: "서른 번째"
}

def format_korean_stroke_text(raw_text: str, order: int) -> str:
    """한번째 획 등 어색한 수사 발음을 '첫 번째 획!', '두 번째 획!' 순우리말 서수사로 완벽 변환"""
    if raw_text:
        # 역순으로 치환하여 11번째가 1번째로 잘못 부분치환되는 현상 방지
        for num in sorted(KOREAN_ORDINALS.keys(), reverse=True):
            ord_kr = KOREAN_ORDINALS[num]
            raw_text = raw_text.replace(f"{num}번째", f"{ord_kr}")
            raw_text = raw_text.replace(f"{num} 번째", f"{ord_kr}")
        if not raw_text.endswith("!"):
            raw_text += "!"
        return raw_text
    return f"{KOREAN_ORDINALS.get(order, f'{order}번째')} 획!"

def prepare_hanzi_audios(hanzi_info: dict, base_dir: str = "assets/audio"):
    """한자 항목에 필요한 한국어/원어민 영어 듀얼 오디오 생성 (획별 '첫 번째, 두 번째' 음성 생략 버전)"""
    char = hanzi_info["char"]
    char_audio_dir = os.path.join(base_dir, f"char_{char}")
    os.makedirs(char_audio_dir, exist_ok=True)

    # 1. 훅 오디오 (처음 한자 의미 설명: 또렷하고 웅장하게 들리도록 볼륨 +50% 및 자연스러운 속도 적용)
    hook_path = os.path.join(char_audio_dir, "hook.mp3")
    spoken_hook = clean_hook_text(hanzi_info['sound_desc'])
    generate_speech(f"{spoken_hook}!", hook_path, voice=VOICE_KO, rate="+4%", pitch="+2Hz", volume="+50%")

    # 2. 훈음 파트: [한국어] "날, 일!" + [미국 원어민] "Day, Sun."
    huneum_ko_path = os.path.join(char_audio_dir, "huneum_ko.mp3")
    huneum_en_path = os.path.join(char_audio_dir, "huneum_en.mp3")
    combined_huneum_path = os.path.join(char_audio_dir, "huneum_combined.mp3")

    hun_eum_raw = hanzi_info['hun_eum']
    if " " in hun_eum_raw:
        hun_part, eum_part = hun_eum_raw.rsplit(" ", 1)
        spoken_hun_eum = f"{hun_part}, {eum_part}!"
    else:
        spoken_hun_eum = f"{hun_eum_raw}!"

    generate_speech(spoken_hun_eum, huneum_ko_path, voice=VOICE_KO, rate="+4%", pitch="+2Hz", volume="+30%")
    # 영문 훈음
    clean_en_huneum = clean_spoken_text(hanzi_info['hun_eum_en'])
    generate_speech(f"{clean_en_huneum}.", huneum_en_path, voice=VOICE_EN, rate="+0%", volume="+25%")

    # 한국어 + 영어 순차 연결
    ffmpeg_bin = get_ffmpeg_exe()
    try:
        concat_cmd_1 = [
            ffmpeg_bin, "-y",
            "-i", huneum_ko_path,
            "-i", huneum_en_path,
            "-filter_complex", "[0:0][1:0]concat=n=2:v=0:a=1[out]",
            "-map", "[out]",
            combined_huneum_path
        ]
        subprocess.run(concat_cmd_1, capture_output=True)
    except Exception as e:
        print(f"[Warning] 훈음 오디오 결합 실패: {e}")

    # 4. 단어 파트: [한국어] "대인! 마음이 넓고 훌륭한 사람." + [미국 원어민] "Adult, Great person."
    word_ko_path = os.path.join(char_audio_dir, "word_ko.mp3")
    word_en_path = os.path.join(char_audio_dir, "word_en.mp3")
    combined_word_path = os.path.join(char_audio_dir, "word_combined.mp3")

    # 한국어 단어 (예: "大人 (대인)" -> "대인")
    clean_word_ko = hanzi_info['example_word'].split('(')[-1].replace(')', '').strip()
    # 한국어 설명 (예: "태양의 날, 한 주의 첫날 (Sunday)" -> "태양의 날, 한 주의 첫날")
    ko_desc = hanzi_info['example_word_desc'].split('(')[0].strip()
    generate_speech(f"{clean_word_ko}! {ko_desc}.", word_ko_path, voice=VOICE_KO, rate="+5%", volume="+25%")
    
    # 괄호 안의 영어 텍스트 추출 (예: "(Sunday)" -> "Sunday")
    en_desc = hanzi_info['example_word_desc']
    if '(' in en_desc and ')' in en_desc:
        raw_en_word = en_desc.split('(')[-1].replace(')', '').strip()
    else:
        raw_en_word = hanzi_info['hun_eum_en']
    
    clean_en_word = clean_spoken_text(raw_en_word)
    generate_speech(f"{clean_en_word}.", word_en_path, voice=VOICE_EN, rate="+0%", volume="+25%")

    try:
        concat_cmd_2 = [
            ffmpeg_bin, "-y",
            "-i", word_ko_path,
            "-i", word_en_path,
            "-filter_complex", "[0:0][1:0]concat=n=2:v=0:a=1[out]",
            "-map", "[out]",
            combined_word_path
        ]
        subprocess.run(concat_cmd_2, capture_output=True)
    except Exception as e:
        print(f"[Warning] 단어 오디오 결합 실패: {e}")

    return {
        "hook": hook_path,
        "strokes": [],
        "huneum": combined_huneum_path if os.path.exists(combined_huneum_path) else huneum_ko_path,
        "example_word": combined_word_path if os.path.exists(combined_word_path) else word_ko_path
    }

if __name__ == "__main__":
    from hanzi_data import HANZI_DATABASE
    res = prepare_hanzi_audios(HANZI_DATABASE["大"])
    print("Prepared audio files:", res)
