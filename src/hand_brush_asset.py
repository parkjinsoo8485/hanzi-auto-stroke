"""
손으로 서예 붓을 쥐고 있는 1인칭 탑다운 시점(Hand holding Brush) 투명 PNG 생성기
"""
import os
import math
from PIL import Image, ImageDraw, ImageFilter

def generate_hand_brush(output_path="assets/hand_brush.png", size=(700, 700)):
    """
    참고 영상처럼 오른손으로 붓을 쥐고 있는 자연스러운 손 + 서예 붓 투명 PNG 생성
    - 붓촉 끝점(Tip): 좌상단 (120, 160)
    - 손 위치: 우하단에서 붓을 쥐고 뻗어나오는 형태
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 붓촉 끝점
    tip_x, tip_y = 120, 160
    
    # 붓대 각도 (약 40도)
    brush_axis_start = (tip_x, tip_y)
    brush_axis_end = (620, 580)
    
    # 1. 붓대 본체 (밝은 원목 / 대나무 붓대)
    # 페룰(이음새): (180, 210) ~ (220, 245)
    ferrule_start = (180, 210)
    ferrule_end = (220, 245)
    
    # 붓대 (손 뒤로 뻗어나가는 부분)
    draw.line([(220, 245), (620, 580)], fill=(185, 140, 90, 255), width=28)
    draw.line([(218, 243), (618, 578)], fill=(220, 180, 130, 255), width=10) # 하이라이트

    # 2. 페룰 (블랙 메탈/황금 이음새)
    draw.line([ferrule_start, ferrule_end], fill=(30, 30, 30, 255), width=30)
    draw.line([ferrule_start, ferrule_end], fill=(218, 165, 32, 255), width=6)

    # 3. 붓촉 (진한 파란색 / 코발트 블루 잉크 머금은 서예 붓촉)
    # 페룰 끝 (180, 210) -> 팁 (120, 160)
    bristle_points = [
        (190, 200),
        (170, 220),
        (150, 210),
        (tip_x, tip_y),
        (140, 170),
        (170, 185),
    ]
    draw.polygon(bristle_points, fill=(29, 78, 216, 255)) # 딥 블루 잉크 붓촉
    draw.line([(180, 205), (tip_x, tip_y)], fill=(37, 99, 235, 255), width=4)
    # 촉 끝 잉크 방울 하이라이트
    draw.circle((tip_x, tip_y), 5, fill=(96, 165, 250, 255))
    draw.circle((tip_x, tip_y), 2, fill=(255, 255, 255, 255))

    # 4. 붓을 쥐고 있는 오른손 (자연스러운 피부 톤 살색 레이어)
    # 엄지 손가락 (붓대를 위에서 누름)
    thumb_points = [
        (260, 240),
        (310, 210),
        (380, 230),
        (400, 280),
        (340, 320),
        (270, 280),
    ]
    draw.polygon(thumb_points, fill=(245, 205, 175, 255)) # 피부 베이스
    # 엄지 손톱 (자연스러운 반짝임)
    draw.ellipse([270, 240, 300, 270], fill=(255, 230, 220, 255))
    draw.ellipse([275, 245, 290, 260], fill=(255, 255, 255, 200))

    # 검지 & 중지 손가락 (붓대를 감싸 쥠)
    index_points = [
        (290, 290),
        (350, 310),
        (420, 370),
        (460, 450),
        (380, 480),
        (320, 400),
        (280, 340),
    ]
    draw.polygon(index_points, fill=(235, 195, 165, 255))

    # 손등 및 손목 (우하단 화면 밖으로 연결)
    hand_palm = [
        (350, 310),
        (480, 380),
        (650, 520),
        (700, 680),
        (500, 700),
        (380, 480),
    ]
    draw.polygon(hand_palm, fill=(225, 185, 155, 255))

    # 손가락 관절 부드러운 음영 쉐이딩
    draw.line([(320, 230), (370, 250)], fill=(210, 160, 130, 180), width=4)
    draw.line([(350, 330), (410, 380)], fill=(200, 150, 120, 180), width=5)
    draw.line([(420, 420), (520, 500)], fill=(190, 140, 110, 180), width=6)

    # 붓대 위에 얹힌 손가락 끝 그림자
    draw.ellipse([250, 260, 280, 290], fill=(180, 130, 100, 120))

    # 이미지 안티에일리어싱 처리
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img.save(output_path, "PNG")
    print(f"[Hand Brush Asset] Real hand holding brush saved to {output_path}")
    return output_path

if __name__ == "__main__":
    generate_hand_brush()
