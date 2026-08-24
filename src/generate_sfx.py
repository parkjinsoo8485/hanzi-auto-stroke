"""
고화질 실사 서예 화선지 붓글씨 마찰음(Authentic Calligraphy Brush ASMR SFX) 생성 모듈
- 획 애니메이션 시간(0.95s)과 100% 동기화
"""
import os
import wave
import numpy as np

SAMPLE_RATE = 44100

def generate_brush_stroke_sfx(output_path="assets/audio/brush_stroke.wav", duration=0.95, sample_rate=44100):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    # 붓 착지 틱
    attack_samples = int(0.05 * sample_rate)
    at = np.linspace(0, 0.05, attack_samples, endpoint=False)
    touch_click = np.sin(2 * np.pi * 110.0 * at) * np.exp(-at * 90.0) * 0.12
    touch_noise = np.random.uniform(-0.12, 0.12, attack_samples) * np.exp(-at * 120.0)
    touch_layer = np.zeros(num_samples)
    touch_layer[:attack_samples] = touch_click + touch_noise

    # 화선지 결 마찰음
    raw_noise = np.random.uniform(-1.0, 1.0, num_samples)
    w1, w2 = 10, 42
    c1 = np.convolve(raw_noise, np.ones(w1)/w1, mode='same')
    c2 = np.convolve(raw_noise, np.ones(w2)/w2, mode='same')
    f_high = (c1 - c2) * 2.5
    env = (np.sin(np.pi * (t / duration) ** 0.75) ** 1.6)
    glide = f_high * env

    # 부드러운 붓 뗌
    release_samples = int(0.05 * sample_rate)
    rt = np.linspace(0, 0.05, release_samples, endpoint=False)
    lift_click = np.sin(2 * np.pi * 180.0 * rt) * np.exp(-rt * 100.0) * 0.08

    full_audio = (touch_layer * 0.30) + glide
    if num_samples > release_samples:
        full_audio[-release_samples:] += lift_click

    fi = int(0.04 * sample_rate)
    fo = int(0.06 * sample_rate)
    full_audio[:fi] *= np.linspace(0, 1, fi)
    full_audio[-fo:] *= np.linspace(1, 0, fo)

    max_val = np.max(np.abs(full_audio))
    if max_val > 0:
        full_audio = (full_audio / max_val) * 0.55

    audio_int16 = (full_audio * 32767).astype(np.int16)
    with wave.open(output_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_int16.tobytes())
    return output_path

if __name__ == "__main__":
    generate_brush_stroke_sfx()
