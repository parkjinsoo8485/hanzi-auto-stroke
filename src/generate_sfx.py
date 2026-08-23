"""
실제 화선지 붓글씨 마찰음(Authentic Calligraphy Paper Stroke SFX) 관리 모듈
"""
import os
import wave
import numpy as np

def generate_brush_stroke_sfx(output_path="assets/audio/brush_stroke.wav", duration=1.5, sample_rate=44100):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        return output_path

    num_samples = int(duration * sample_rate)
    # 부드러운 화선지 마찰 텍스처 합성
    white_noise = np.random.uniform(-1, 1, num_samples)
    window_size = 20
    smooth_noise = np.convolve(white_noise, np.ones(window_size)/window_size, mode='same')
    
    t = np.linspace(0, 1, num_samples)
    envelope = np.sin(np.pi * (t ** 0.85))
    audio = smooth_noise * envelope * 0.75
    audio_int16 = (audio * 32767).astype(np.int16)
    
    with wave.open(output_path, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_int16.tobytes())
        
    return output_path

if __name__ == "__main__":
    generate_brush_stroke_sfx()
