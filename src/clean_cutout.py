"""
실사 손+붓 이미지 정밀 누끼(Background Cutout) 생성기
"""
import cv2
import numpy as np
import os

def clean_hand_cutout(src_frame="output/ref_frame_03.png", out_path="assets/hand_brush_clean.png"):
    img = cv2.imread(src_frame)
    h, w, _ = img.shape
    
    # 붓과 손 영역
    ymin, ymax = int(h * 0.31), int(h * 0.88)
    xmin, xmax = int(w * 0.17), int(w * 0.99)
    crop = img[ymin:ymax, xmin:xmax]
    ch, cw, _ = crop.shape

    # GrabCut을 이용한 정밀 분리
    mask = np.zeros((ch, cw), np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    
    rect = (15, 10, cw - 25, ch - 20)
    cv2.grabCut(crop, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    
    # 0, 2: 배경, 1, 3: 전경
    final_mask = np.where((mask == 1) | (mask == 3), 255, 0).astype('uint8')
    
    # 붓촉 끝점(좌상단) 살리기
    # 피부색 및 붓 색상 영역 보존
    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    # 피부색 (Hue: 0~25 or 160~180, Sat: 30~255)
    skin_mask1 = cv2.inRange(hsv, np.array([0, 25, 60]), np.array([30, 255, 255]))
    skin_mask2 = cv2.inRange(hsv, np.array([160, 25, 60]), np.array([180, 255, 255]))
    # 붓촉(파란색) & 붓대(황토색)
    brush_tip_mask = cv2.inRange(hsv, np.array([100, 70, 70]), np.array([135, 255, 255]))
    brush_body_mask = cv2.inRange(hsv, np.array([15, 40, 50]), np.array([40, 255, 255]))
    
    color_mask = skin_mask1 | skin_mask2 | brush_tip_mask | brush_body_mask
    
    # 합성 마스크
    combined = cv2.bitwise_and(final_mask, color_mask)
    
    # 닫힘 연산으로 내부 채우기
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    combined = cv2.morphologyEx(combined, cv2.MORPH_CLOSE, kernel, iterations=4)
    
    # 가장 큰 컨투어(손+붓)만 추출
    contours, _ = cv2.findContours(combined, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    clean_mask = np.zeros_like(combined)
    if contours:
        c = max(contours, key=cv2.contourArea)
        cv2.drawContours(clean_mask, [c], -1, 255, thickness=cv2.FILLED)
    
    # 부드러운 가장자리 블러
    clean_mask = cv2.GaussianBlur(clean_mask, (7, 7), 0)
    
    b, g, r = cv2.split(crop)
    rgba = cv2.merge([b, g, r, clean_mask])
    
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    cv2.imwrite(out_path, rgba)
    print(f"[Hand Brush] Clean cutout saved to {out_path}")
    return out_path

if __name__ == "__main__":
    clean_hand_cutout()
