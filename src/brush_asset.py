"""
실제 서예용 세필 붓(Calligraphy Brush) 고화질 투명 PNG 정밀 생성기
"""
import os
import math
from PIL import Image, ImageDraw, ImageFilter

def generate_brush_image(output_path="assets/brush_real.png", size=(512, 512)):
    """
    날렵하고 세련된 전통 세필 서예 붓 생성:
    - 붓촉 끝점(Tip): 좌하단 (60, 452)
    - 붓 각도: 60도로 날렵하게 세워진 형태
    - 긴 흑단/로즈우드 붓대 + 황금빛 장식 + 섬세한 붓촉 털 질감
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 붓촉 끝점 (글씨를 쓰는 팁)
    tip_x, tip_y = 60, 452

    # 붓의 진행 축 벡터 (60도 각도: 우상단 420, 60 방향)
    top_x, top_y = 420, 60
    angle = math.atan2(tip_y - top_y, tip_x - top_x) # 붓의 축 각도

    # 1. 붓대 (대나무/흑단 슬림 붓대)
    # 시작: (180, 320) -> 끝: (420, 60)
    handle_start = (180, 320)
    handle_end = (420, 60)
    handle_len = math.hypot(handle_end[0] - handle_start[0], handle_end[1] - handle_start[1])

    # 붓대 본체 그리기 (입체감 있는 로즈우드 원통)
    for w in range(16, 0, -2):
        shade = int(90 + 70 * (w / 16.0))
        red_shade = int(50 + 40 * (w / 16.0))
        draw.line([handle_start, handle_end], fill=(shade, red_shade, 20, 255), width=w)
    
    # 붓대 하이라이트 (빛 반사 선)
    draw.line([(handle_start[0]-2, handle_start[1]-2), (handle_end[0]-2, handle_end[1]-2)], fill=(180, 120, 60, 200), width=3)

    # 붓대 끝 황금 캡 & 고리
    draw.ellipse([handle_end[0]-8, handle_end[1]-8, handle_end[0]+8, handle_end[1]+8], fill=(218, 165, 32, 255))
    draw.ellipse([handle_end[0]-4, handle_end[1]-4, handle_end[0]+4, handle_end[1]+4], fill=(255, 215, 0, 255))

    # 2. 황금 금속 이음새 (Ferrule)
    # 위치: (150, 355) ~ (180, 320)
    ferrule_start = (150, 355)
    ferrule_end = (180, 320)
    for w in range(18, 0, -2):
        draw.line([ferrule_start, ferrule_end], fill=(218, 165, 32, 255), width=w)
    draw.line([ferrule_start, ferrule_end], fill=(255, 235, 120, 255), width=4)

    # 3. 붓털 (촉 - 날렵하고 섬세한 먹물 붓촉)
    # Ferrule 끝 (150, 355)에서 Tip (60, 452)까지
    # 중심선 기준 좌우 폭이 붓 배에서 최대 14px, 팁에서 0px로 좁아짐
    num_steps = 30
    for s in range(num_steps):
        t = s / float(num_steps) # 0.0(이음새) -> 1.0(팁)
        # 중심선 좌표
        cx = ferrule_start[0] * (1 - t) + tip_x * t
        cy = ferrule_start[1] * (1 - t) + tip_y * t
        
        # 붓촉 폭 프로파일: 중간(t=0.25)에서 약간 볼록하고 팁(t=1.0)으로 가면서 날렵해짐
        if t < 0.25:
            width = 16 * (1 - t/0.25) + 20 * (t/0.25)
        else:
            width = 20 * (1 - (t - 0.25) / 0.75) ** 1.3
        
        # 수직 방향 오프셋
        perp_angle = angle + math.pi / 2
        px = math.cos(perp_angle) * width / 2
        py = math.sin(perp_angle) * width / 2
        
        # 붓털 색상: 짙은 묵색 + 팁 부분은 먹물 골드
        r = int(25 * (1 - t) + 245 * (t ** 2))
        g = int(25 * (1 - t) + 158 * (t ** 2))
        b = int(25 * (1 - t) + 11 * (t ** 2))
        
        draw.line([(cx - px, cy - py), (cx + px, cy + py)], fill=(r, g, b, 255), width=3)

    # 붓촉 끝점 골드/먹물 하이라이트 팁
    draw.ellipse([tip_x - 3, tip_y - 3, tip_x + 3, tip_y + 3], fill=(253, 224, 71, 255))

    # 부드러운 안티에일리어싱 적용
    img = img.resize((512, 512), Image.Resampling.LANCZOS)
    img.save(output_path, "PNG")
    print(f"[Brush Generator] Refined slim calligraphy brush saved to {output_path}")
    return output_path

if __name__ == "__main__":
    generate_brush_image()
