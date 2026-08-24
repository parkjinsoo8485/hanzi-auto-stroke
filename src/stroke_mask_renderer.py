"""
한자 획( 해서체 정통 윤곽선 )을 AnimCJK 붓 경로(Medial)를 따라
실시간으로 점진적 노출(Masked Reveal)하는 고품질 RGBA 시퀀스 생성기
"""
import os
import cv2
import numpy as np
import svgelements

def cv2_imwrite_utf8(path: str, img: np.ndarray) -> bool:
    ext = os.path.splitext(path)[1]
    ret, encoded = cv2.imencode(ext, img)
    if ret:
        with open(path, 'wb') as f:
            encoded.tofile(f)
        return True
    return False

def get_brush_tip_relative(image_path: str = "assets/hand_brush_clean.png") -> tuple[float, float]:
    """붓 이미지(RGBA)에서 실제 붓끝(Tip)의 정밀 정규화 좌표 (norm_x, norm_y) 계산"""
    if not os.path.exists(image_path):
        return 0.015, 0.985
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img is None or img.shape[2] < 4:
        return 0.015, 0.985
    alpha = img[:, :, 3]
    y_idx, x_idx = np.where(alpha > 60)
    if len(y_idx) == 0:
        return 0.015, 0.985
    max_y = np.max(y_idx)
    lowest_mask = (y_idx >= max_y - 12)
    tip_x = np.min(x_idx[lowest_mask])
    tip_y = max_y
    return float(tip_x) / img.shape[1], float(tip_y) / img.shape[0]

def get_stroke_medial_points(medial_svg_path: str, num_samples: int = 160) -> list[tuple[float, float]]:
    """정밀 SVG 스플라인 기반 붓 진행 경로 포인트 목록 추출"""
    if not medial_svg_path or not os.path.exists(medial_svg_path):
        return []
    doc_medial = svgelements.SVG.parse(medial_svg_path)
    medial_elems = [e for e in doc_medial.elements() if isinstance(e, svgelements.Path) and e.stroke is not None and e.length() > 10]
    if not medial_elems:
        return []
    medial_elem = medial_elems[-1]
    pts = []
    for i in range(num_samples + 1):
        pt = medial_elem.point(i / float(num_samples))
        pts.append((float(pt.x), float(pt.y)))
    return pts

def generate_stroke_reveal_frames(char: str, order: int, outline_svg_path: str, medial_svg_path: str, num_frames: int = 30) -> list[str]:
    """
    정통 해서체 획의 outline SVG와 medial SVG를 파싱하여
    처음부터 완성형 글씨 모양 그대로 붓끝 이동에 맞춰 매끄럽게 칠해지는
    RGBA 이미지 프레임 시퀀스를 생성합니다.
    """
    codepoint = ord(char)
    cache_dir = f"assets/reveal_cache/{codepoint}"
    os.makedirs(cache_dir, exist_ok=True)

    # 1. 외곽선 SVG 파싱 및 다각형 마스크(1024x1024) 생성
    doc_outline = svgelements.SVG.parse(outline_svg_path)
    outline_elems = [e for e in doc_outline.elements() if isinstance(e, svgelements.Path) and e.fill is not None and e.fill.value != 0]
    if not outline_elems:
        return []
    outline_elem = outline_elems[-1]

    poly_pts = []
    for seg in outline_elem:
        for t in np.linspace(0, 1, 25):
            try:
                pt = seg.point(t)
                poly_pts.append([int(round(pt.x)), int(round(pt.y))])
            except Exception:
                pass

    outline_mask = np.zeros((1024, 1024), dtype=np.uint8)
    if poly_pts:
        cv2.fillPoly(outline_mask, [np.array(poly_pts, dtype=np.int32)], 255)

    # 2. 붓 진행 중심선(Medial) 파싱
    m_pts = []
    if medial_svg_path and os.path.exists(medial_svg_path):
        doc_medial = svgelements.SVG.parse(medial_svg_path)
        medial_elems = [e for e in doc_medial.elements() if isinstance(e, svgelements.Path) and e.stroke is not None and e.length() > 10]
        if medial_elems:
            medial_elem = medial_elems[-1]
            num_samples = 160
            for i in range(num_samples + 1):
                pt = medial_elem.point(i / float(num_samples))
                m_pts.append((int(round(pt.x)), int(round(pt.y))))

    if not m_pts:
        # Fallback: 전체 외곽선 1장
        frame_path = f"{cache_dir}/s{order}_full.png"
        rgba = np.zeros((1024, 1024, 4), dtype=np.uint8)
        rgba[:, :, 0] = 216  # Blue
        rgba[:, :, 1] = 78   # Green
        rgba[:, :, 2] = 29   # Red
        rgba[:, :, 3] = outline_mask
        cv2_imwrite_utf8(frame_path, rgba)
        return [frame_path] * num_frames

    # 3. 딥 코발트 블루 먹물 컬러 (RGB: #1D4ED8 -> BGR: (216, 78, 29))
    ink_bgr = (216, 78, 29)
    frame_files = []

    for f in range(num_frames):
        alpha_t = (f + 1) / float(num_frames)
        idx_max = max(1, int(round(alpha_t * len(m_pts))))

        sweep_mask = np.zeros((1024, 1024), dtype=np.uint8)
        # 붓끝 반경을 넉넉히 주어 외곽선 내부를 완벽하고 부드럽게 감쌈
        brush_radius = 95
        for k in range(idx_max):
            cv2.circle(sweep_mask, m_pts[k], brush_radius, 255, -1)
            if k > 0:
                cv2.line(sweep_mask, m_pts[k-1], m_pts[k], 255, brush_radius * 2)

        # 핵심: 정통 해서체 외곽선 마스크 ∩ 붓이 지나간 영역
        revealed_mask = cv2.bitwise_and(outline_mask, sweep_mask)
        # 부드러운 안티앨리어싱
        revealed_alpha = cv2.GaussianBlur(revealed_mask, (3, 3), 0)

        rgba = np.zeros((1024, 1024, 4), dtype=np.uint8)
        rgba[:, :, 0] = ink_bgr[0]
        rgba[:, :, 1] = ink_bgr[1]
        rgba[:, :, 2] = ink_bgr[2]
        rgba[:, :, 3] = revealed_alpha

        frame_path = f"{cache_dir}/s{order}_f{f:02d}.png"
        cv2_imwrite_utf8(frame_path, rgba)
        frame_files.append(frame_path)

    return frame_files
