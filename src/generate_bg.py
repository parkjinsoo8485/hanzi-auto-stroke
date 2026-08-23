"""
전통 화선지 / 한지(Rice Paper) 고화질 텍스처 배경 생성기
"""
import os
import numpy as np
from PIL import Image, ImageFilter

def generate_hanji_background(output_path="assets/hanji_bg.png", width=1080, height=1920):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 1. 따뜻하고 밝은 화선지 기본 베이지/미색 톤 (RGB: 242, 240, 235)
    base = np.full((height, width, 3), [242, 240, 235], dtype=np.uint8)
    
    # 2. 미세한 종이 섬유 및 노이즈 생성
    noise = np.random.normal(0, 5, (height, width, 3)).astype(np.int16)
    bg = np.clip(base + noise, 0, 255).astype(np.uint8)
    
    img = Image.fromarray(bg)
    # 가로/세로 미세 화선지 결(Fiber) 효과
    img = img.filter(ImageFilter.GaussianBlur(0.8))
    
    img.save(output_path, "PNG")
    print(f"[Hanji BG] Paper texture saved to {output_path}")
    return output_path

if __name__ == "__main__":
    generate_hanji_background()
