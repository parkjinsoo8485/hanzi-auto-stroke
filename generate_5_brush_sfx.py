"""
실사 서예 화선지 붓글씨 차분하고 은은한 자연 ASMR 효과음 5종 전문 생성기
- 획 그리는 애니메이션(1.00초, 30fps)과 100% 프레임 퍼펙트 동기화
- 붓이 지면에 닿아 획을 긋는 순간부터 뗄 때까지 사각사각 화선지 결 마찰음 1:1 일치
- 은은하고 차분한 힐링 볼륨 레벨
"""
import os
import sys
import wave
import numpy as np

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

SAMPLE_RATE = 44100

def create_calm_natural_brush_sfx(style_idx: int, duration: float = 1.00):
    """
    획 애니메이션(1.00초)과 1:1 완벽 동기화되는 차분하고 자연스러운 서예 붓글씨 마찰음 합성
    """
    num_samples = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    # 1. 붓 착지 틱 (부드러운 붓끝 안착감: 0.0 ~ 0.05s)
    attack_samples = int(0.05 * SAMPLE_RATE)
    at = np.linspace(0, 0.05, attack_samples, endpoint=False)
    touch_click = np.sin(2 * np.pi * 110.0 * at) * np.exp(-at * 90.0) * 0.12
    touch_noise = np.random.uniform(-0.12, 0.12, attack_samples) * np.exp(-at * 120.0)
    touch_layer = np.zeros(num_samples)
    touch_layer[:attack_samples] = touch_click + touch_noise

    # 2. 부드럽고 촉촉한 화선지 결 스침 (Smooth Mulberry Paper Friction)
    raw_noise = np.random.uniform(-1.0, 1.0, num_samples)
    
    if style_idx == 1:
        # [01. 은은한 한지 묵향 붓터치]: 부드럽고 온화한 순지 위 스침음
        w1, w2 = 16, 60
        c1 = np.convolve(raw_noise, np.ones(w1)/w1, mode='same')
        c2 = np.convolve(raw_noise, np.ones(w2)/w2, mode='same')
        f_mid = (c1 - c2) * 2.2
        glide = f_mid
        env = (np.sin(np.pi * (t / duration) ** 0.8) ** 1.5)
    elif style_idx == 2:
        # [02. 차분한 닥종이 사각사각 결 ASMR - 대표 추천]: 맑고 은은하게 결이 스치는 힐링 사운드
        w1, w2 = 10, 42
        c1 = np.convolve(raw_noise, np.ones(w1)/w1, mode='same')
        c2 = np.convolve(raw_noise, np.ones(w2)/w2, mode='same')
        f_high = (c1 - c2) * 2.5
        glide = f_high
        env = (np.sin(np.pi * (t / duration) ** 0.75) ** 1.6)
    elif style_idx == 3:
        # [03. 묵직하고 고요한 일필]: 깊이 있고 점잖은 서예 호흡
        w1, w2 = 14, 55
        c1 = np.convolve(raw_noise, np.ones(w1)/w1, mode='same')
        c2 = np.convolve(raw_noise, np.ones(w2)/w2, mode='same')
        f_body = (c1 - c2) * 2.0
        low_body = np.convolve(raw_noise, np.ones(100)/100, mode='same') * 1.1
        glide = f_body + low_body
        env = (np.sin(np.pi * (t / duration) ** 0.85) ** 1.4)
    elif style_idx == 4:
        # [04. 유려한 붓끝 곡선 흐름]: 부드럽게 돌아나가는 우아한 붓의 유영
        w1, w2 = 8, 36
        c1 = np.convolve(raw_noise, np.ones(w1)/w1, mode='same')
        c2 = np.convolve(raw_noise, np.ones(w2)/w2, mode='same')
        f_sharp = (c1 - c2) * 2.4
        glide = f_sharp
        env = (np.sin(np.pi * (t / duration) ** 0.7) ** 1.5)
    else:
        # [05. 다도(茶道) 속 정갈한 먹물 터치]: 조용하고 맑은 차분한 터치감
        w1, w2 = 12, 48
        c1 = np.convolve(raw_noise, np.ones(w1)/w1, mode='same')
        c2 = np.convolve(raw_noise, np.ones(w2)/w2, mode='same')
        f_zen = (c1 - c2) * 2.1
        glide = f_zen
        env = (np.sin(np.pi * (t / duration) ** 0.75) ** 1.5)

    # 3. 부드러운 붓 뗌 (Soft Gentle Release: 마지막 0.05s)
    release_samples = int(0.05 * SAMPLE_RATE)
    rt = np.linspace(0, 0.05, release_samples, endpoint=False)
    lift_click = np.sin(2 * np.pi * 180.0 * rt) * np.exp(-rt * 100.0) * 0.08
    
    # 결합
    full_audio = (touch_layer * 0.30) + (glide * env)
    if num_samples > release_samples:
        full_audio[-release_samples:] += lift_click
        
    # 시작과 끝 부드러운 페이드 (시작 0.04s, 끝 0.06s)
    fi = int(0.04 * SAMPLE_RATE)
    fo = int(0.06 * SAMPLE_RATE)
    full_audio[:fi] *= np.linspace(0, 1, fi)
    full_audio[-fo:] *= np.linspace(1, 0, fo)
    
    # 차분하고 편안한 음량 정규화
    max_val = np.max(np.abs(full_audio))
    if max_val > 0:
        full_audio = (full_audio / max_val) * 0.55
        
    return (full_audio * 32767).astype(np.int16)

def generate_all_5_brush_sfx(out_dir="assets/audio/sfx"):
    os.makedirs(out_dir, exist_ok=True)
    
    sfx_info = [
        ("01_soft_hanji_glide.wav", 1, 1.00, "은은한 한지 묵향 붓터치 (부드럽고 온화함)"),
        ("02_crisp_mulberry_scratch.wav", 2, 1.00, "차분한 닥종이 사각사각 결 ASMR (은은하고 자연스러움)"),
        ("03_bold_ink_strike.wav", 3, 1.00, "묵직하고 고요한 일필 (깊이 있는 서예 호흡)"),
        ("04_delicate_tip_flick.wav", 4, 1.00, "유려한 붓끝 곡선 흐름 (우아한 여운)"),
        ("05_zen_bamboo_brush.wav", 5, 1.00, "다도 속 정갈한 먹물 터치 (조용하고 맑은 터치)")
    ]
    
    print("🖌️ 1.00초 획 동기화 실사 서예 ASMR 5종 합성 시작...\n")
    for fname, s_idx, dur, desc in sfx_info:
        audio_int16 = create_calm_natural_brush_sfx(s_idx, duration=dur)
        filepath = os.path.join(out_dir, fname)
        with wave.open(filepath, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(audio_int16.tobytes())
        print(f"✅ 생성 완료: {filepath} [{desc}] ({dur:.2f}초)")
        
    # 기본 단일 sfx 동기화
    default_path = "assets/audio/brush_stroke.wav"
    audio_int16 = create_calm_natural_brush_sfx(2, duration=1.00)
    with wave.open(default_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_int16.tobytes())
    print(f"✨ 기본 실사 ASMR 동기화 완료: {default_path}\n")

if __name__ == "__main__":
    generate_all_5_brush_sfx()
