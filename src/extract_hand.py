"""
참조 영상(ref_frame_03.png)에서 실제 서예 붓을 쥔 손을 크롭하고 투명 배경 PNG로 추출
"""
import os
import cv2
import numpy as np
from PIL import Image

def extract_real_hand_brush(src_frame="output/ref_frame_03.png", out_path="assets/hand_brush_real.png"):
    if not os.path.exists(src_frame):
        print(f"Source frame not found: {src_frame}")
        return None
    
    # 1. 원본 이미지 로드
    img = cv2.imread(src_frame)
    h, w, _ = img.shape
    
    # 2. 붓과 손 영역 크롭 (중앙 하단 ~ 우하단)
    # 붓촉 끝점: 약 (180, 600) 부근, 손: 우하단 전체
    crop_ymin, crop_ymax = int(h * 0.28), int(h * 0.88)
    crop_xmin, crop_xmax = int(w * 0.15), int(w * 0.98)
    cropped = img[crop_ymin:crop_ymax, crop_xmin:crop_xmax]
    
    # 3. 배경(화선지 그레이/베이지) 분리 마스크 생성
    # 화선지 배경은 명도가 높고 채도가 낮음 (Grayish)
    # 손과 붓은 파란색 붓촉, 노란 대나무 붓대, 살색 손
    hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
    
    # 화선지 배경 색상 범위 (회색조)
    # 화선지가 아닌 영역(손+붓) 추출
    lower_gray = np.array([0, 0, 110])
    upper_gray = np.array([180, 45, 230])
    paper_mask = cv2.inRange(hsv, lower_gray, upper_gray)
    
    # 마스크 반전 (객체 영역 = 흰색)
    fg_mask = cv2.bitwise_not(paper_mask)
    
    # 모폴로지 연산으로 손 내부 구멍 메우기
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel, iterations=3)
    fg_mask = cv2.GaussianBlur(fg_mask, (5, 5), 0)
    
    # RGBA 이미지 합성
    b, g, r = cv2.split(cropped)
    rgba = cv2.merge([b, g, r, fg_mask])
    
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    cv2.imwrite(out_path, rgba)
    print(f"[Hand Brush Extractor] Real hand holding brush extracted to {out_path}")
    return out_path

if __name__ == "__main__":
    extract_real_hand_brush()
