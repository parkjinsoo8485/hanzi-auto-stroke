"""
참고 영상 완벽 재현:
- 전통 화선지 텍스처 배경 (#EFECE6)
- 1인칭 POV 실사 손+붓글씨 (Hand Holding Calligraphy Brush)
- AnimCJK 정통 해서체(정자체/번체) 획순 매끄러운 붓터치 애니메이션
- 상단/하단 카드 디자인 (한글/영문 듀얼 훈음 & 실생활 단어)
"""
import os
import sys
import re
import numpy as np
from manim import *

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 9:16 세로 숏폼 해상도 (1080x1920)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.background_color = "#F4F1EA"  # 전통 화선지 베이지

def parse_svg_path_points(d_str):
    if not d_str:
        return []
    coords = re.findall(r'([-\d\.]+)[,\s]+([-\d\.]+)', d_str)
    return [(float(x), float(y)) for x, y in coords]

def svg_to_manim_point(x, y, grid_center, scale_factor=4.6):
    mx = grid_center[0] + (x / 1024.0 - 0.5) * scale_factor
    my = grid_center[1] - (y / 1024.0 - 0.5) * scale_factor
    return np.array([mx, my, 0.0])

class HanziShortScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from hanzi_data import HANZI_DATABASE
        from animcjk_loader import parse_animcjk_strokes
        
        char_key = os.environ.get("HANZI_CHAR", "大")
        self.char_data = HANZI_DATABASE.get(char_key, HANZI_DATABASE["大"])
        self.animcjk_info = parse_animcjk_strokes(char_key)
        self.hand_brush_path = "assets/hand_brush_clean.png"

    def construct(self):
        char = self.char_data["char"]
        hun_eum = self.char_data["hun_eum"]
        hun_eum_en = self.char_data["hun_eum_en"].replace("/", ", ")
        example_word = self.char_data["example_word"]
        example_desc = self.char_data["example_word_desc"].replace("/", ", ")
        total_strokes = len(self.animcjk_info["strokes"])

        # ==========================================
        # 1. 상단 정보 헤더 (첫 페이지: 10초 만에 깨우치는 한자)
        # ==========================================
        header_bar = RoundedRectangle(
            corner_radius=0.18, width=8.4, height=1.6,
            fill_color="#0F172A", fill_opacity=0.94, stroke_color="#0284C7", stroke_width=2.5
        ).move_to(UP * 6.5)

        sub_header_txt_1 = Text("기초 상형문자 탐구", font="Malgun Gothic", font_size=24, color="#94A3B8", weight=BOLD)
        main_header_txt_1 = Text("10초 만에 깨우치는 한자", font="Malgun Gothic", font_size=36, color="#FDE047", weight=BOLD)
        header_content_1 = VGroup(sub_header_txt_1, main_header_txt_1).arrange(DOWN, buff=0.12).move_to(header_bar.get_center())

        self.play(FadeIn(header_bar, shift=DOWN*0.3), Write(header_content_1), run_time=0.6)

        # ==========================================
        # 2. 그림 픽토그램 제시 & 상형문자 모핑 (0.6s ~ 3.5s)
        # ==========================================
        morph_center = UP * 2.0

        drawing_svg_path = f"assets/svg_drawings/{char}_drawing.svg"
        os.makedirs(os.path.dirname(drawing_svg_path), exist_ok=True)
        with open(drawing_svg_path, "w", encoding="utf-8") as f:
            f.write(self.char_data["drawing_svg"])

        pictogram = SVGMobject(drawing_svg_path).scale(2.3).move_to(morph_center).set_color("#1E3A8A")
        
        caption_box = RoundedRectangle(
            corner_radius=0.15, width=7.4, height=0.8,
            fill_color="#DC2626", fill_opacity=0.92, stroke_width=0
        ).move_to(DOWN * 0.2)
        caption_text = Text(f"💡 {self.char_data['sound_desc']}", font="Malgun Gothic", font_size=26, color="#FFFFFF", weight=BOLD)
        caption_text.move_to(caption_box.get_center())

        self.play(
            FadeIn(pictogram, scale=0.8),
            FadeIn(caption_box, shift=UP*0.2),
            Write(caption_text),
            run_time=0.8
        )
        self.wait(0.7)

        # 코발트 블루 해서체 한자
        full_hanzi_mob = SVGMobject(self.animcjk_info["full_svg_path"]).scale(2.4).move_to(morph_center).set_color("#1D4ED8")

        morph_caption_box = RoundedRectangle(
            corner_radius=0.15, width=7.4, height=0.8,
            fill_color="#059669", fill_opacity=0.95, stroke_width=0
        ).move_to(DOWN * 0.2)
        morph_caption_text = Text(f"➡️ 글자로 완성: 「{char}」", font="Malgun Gothic", font_size=28, color="#FFFFFF", weight=BOLD)
        morph_caption_text.move_to(morph_caption_box.get_center())

        self.play(
            ReplacementTransform(pictogram, full_hanzi_mob),
            ReplacementTransform(caption_box, morph_caption_box),
            ReplacementTransform(caption_text, morph_caption_text),
            run_time=1.2
        )
        self.play(Indicate(full_hanzi_mob, scale_factor=1.06, color="#2563EB"), run_time=0.5)
        self.wait(0.3)

        # 헤더를 획순 정보(부수 / 총 N획 / 한자 훈음)로 매끄럽게 전환
        sub_header_txt_2 = Text(f"부수 {char}  |  총 {total_strokes}획", font="Malgun Gothic", font_size=24, color="#94A3B8", weight=BOLD)
        main_header_txt_2 = Text(f"{char}  {hun_eum}", font="Malgun Gothic", font_size=38, color="#FDE047", weight=BOLD)
        header_content_2 = VGroup(sub_header_txt_2, main_header_txt_2).arrange(DOWN, buff=0.12).move_to(header_bar.get_center())

        self.play(
            FadeOut(full_hanzi_mob, scale=0.9),
            FadeOut(morph_caption_box),
            FadeOut(morph_caption_text),
            ReplacementTransform(header_content_1, header_content_2),
            run_time=0.4
        )

        # ==========================================
        # 3. 화선지 서예 격자판 & 실사 손+붓 라이팅 (1인칭 POV)
        # ==========================================
        grid_pos = UP * 2.0
        grid_box = Square(side_length=4.8, stroke_color="#94A3B8", stroke_width=2.0, fill_color="#FAF9F6", fill_opacity=0.9).move_to(grid_pos)
        grid_dash_h = DashedLine(grid_box.get_left(), grid_box.get_right(), dash_length=0.18, stroke_color="#CBD5E1", stroke_width=1.5)
        grid_dash_v = DashedLine(grid_box.get_top(), grid_box.get_bottom(), dash_length=0.18, stroke_color="#CBD5E1", stroke_width=1.5)
        grid_dash_d1 = DashedLine(grid_box.get_corner(UL), grid_box.get_corner(DR), dash_length=0.18, stroke_color="#E2E8F0", stroke_width=1.2)
        grid_dash_d2 = DashedLine(grid_box.get_corner(UR), grid_box.get_corner(DL), dash_length=0.18, stroke_color="#E2E8F0", stroke_width=1.2)
        grid_group = VGroup(grid_box, grid_dash_h, grid_dash_v, grid_dash_d1, grid_dash_d2)

        self.play(FadeIn(grid_group), run_time=0.4)

        # 초고화질 실사 손+붓 ImageMobject
        hand_brush = ImageMobject(self.hand_brush_path).scale_to_fit_height(4.5).set_z_index(100)
        
        # 붓촉 끝점 오프셋 (DL 끝점에서 이미지 중심까지의 벡터)
        # tip_x = 0.0124 * width, tip_y = 0.9881 * height
        tip_offset = np.array([hand_brush.width * 0.4876, hand_brush.height * 0.4881, 0.0])

        rendered_strokes = []
        is_first_stroke = True

        for s_idx, stroke_item in enumerate(self.animcjk_info["strokes"]):
            order = stroke_item["order"]
            stroke_svg = stroke_item["stroke_svg_path"]
            medial_d = stroke_item.get("medial_d", "")

            # 딥 코발트 블루 서예 먹물 컬러 (`#1D4ED8`)
            stroke_mob = SVGMobject(stroke_svg).scale(2.4).move_to(grid_pos).set_color("#1D4ED8")

            # 붓 진행 경로 포인트 계산
            raw_pts = parse_svg_path_points(medial_d)
            if raw_pts:
                manim_pts = [svg_to_manim_point(px, py, grid_pos, scale_factor=4.8) for px, py in raw_pts]
                hand_pts = [pt + tip_offset for pt in manim_pts]
                hand_curve = VMobject().set_points_as_corners(hand_pts)
                start_hand_pos = hand_pts[0]

                if is_first_stroke:
                    # 1획 시작점에 손과 붓이 우하단에서 자연스럽게 착지
                    self.play(
                        FadeIn(hand_brush.move_to(start_hand_pos), shift=DR*0.6),
                        run_time=0.5
                    )
                    is_first_stroke = False
                else:
                    # 다음 획 시작점으로 손이 부드럽게 이동
                    self.play(
                        hand_brush.animate.move_to(start_hand_pos),
                        run_time=0.4
                    )

                # 손이 획을 따라가며 붓글씨 획이 실시간으로 쓰여짐
                self.play(
                    MoveAlongPath(hand_brush, hand_curve, rate_func=smooth),
                    FadeIn(stroke_mob, rate_func=smooth),
                    run_time=1.5
                )
            else:
                self.play(
                    FadeIn(stroke_mob, run_time=1.5),
                    run_time=1.5
                )

            self.play(Indicate(stroke_mob, scale_factor=1.02, color="#2563EB"), run_time=0.3)
            rendered_strokes.append(stroke_mob)
            self.wait(0.2)

        # 붓글씨 완성 후 손 퇴장
        self.play(FadeOut(hand_brush, shift=DR*0.8), run_time=0.6)

        # 전체 글자 완성 축하 블루 플래시
        self.play(
            Flash(grid_pos, color="#2563EB", line_length=0.6, num_lines=24),
            run_time=0.7
        )
        self.wait(0.3)

        # ==========================================
        # 4. 하단 훈음 & 실생활 활용 단어 카드
        # ==========================================
        huneum_card = RoundedRectangle(
            corner_radius=0.2, width=8.4, height=2.2,
            fill_color="#1E293B", fill_opacity=0.95, stroke_color="#F59E0B", stroke_width=2.5
        ).move_to(DOWN * 2.0)

        huneum_char_badge = RoundedRectangle(
            corner_radius=0.15, width=1.5, height=1.5,
            fill_color="#D97706", fill_opacity=0.95, stroke_width=0
        )
        huneum_char_txt = Text(char, font="Batang", font_size=56, color="#FFFFFF", weight=BOLD).move_to(huneum_char_badge.get_center())
        huneum_badge_group = VGroup(huneum_char_badge, huneum_char_txt)

        huneum_main = Text(hun_eum, font="Malgun Gothic", font_size=44, color="#FDE047", weight=BOLD)
        
        # 영어 라벨 (이모지 깨짐 방지: [EN] 배지 스타일)
        en_badge = RoundedRectangle(corner_radius=0.08, width=0.8, height=0.42, fill_color="#3B82F6", fill_opacity=0.9, stroke_width=0)
        en_badge_txt = Text("EN", font="Arial", font_size=16, color="#FFFFFF", weight=BOLD).move_to(en_badge.get_center())
        en_txt = Text(f"{hun_eum_en}", font="Arial", font_size=24, color="#93C5FD", weight=BOLD)
        en_line = VGroup(VGroup(en_badge, en_badge_txt), en_txt).arrange(RIGHT, buff=0.15)

        huneum_text_group = VGroup(huneum_main, en_line).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        huneum_content = VGroup(huneum_badge_group, huneum_text_group).arrange(RIGHT, buff=0.4).move_to(huneum_card.get_center())

        self.play(
            FadeIn(huneum_card, shift=UP*0.3),
            GrowFromCenter(huneum_content),
            run_time=0.7
        )
        self.wait(0.8)

        # 실생활 단어 카드
        word_card = RoundedRectangle(
            corner_radius=0.2, width=8.4, height=2.1,
            fill_color="#0F172A", fill_opacity=0.95, stroke_color="#0284C7", stroke_width=2.5
        ).move_to(DOWN * 4.8)

        word_badge = RoundedRectangle(
            corner_radius=0.1, width=2.2, height=0.5,
            fill_color="#0284C7", fill_opacity=0.9, stroke_width=0
        )
        word_badge_txt = Text("📚 실생활 단어", font="Malgun Gothic", font_size=18, color="#FFFFFF", weight=BOLD).move_to(word_badge.get_center())
        word_badge_grp = VGroup(word_badge, word_badge_txt)

        word_title = Text(f"{example_word}", font="Malgun Gothic", font_size=32, color="#38BDF8", weight=BOLD)
        word_desc = Text(f"• {example_desc}", font="Malgun Gothic", font_size=22, color="#E2E8F0")
        
        word_content = VGroup(word_badge_grp, word_title, word_desc).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(word_card.get_center()).shift(LEFT * 0.2)

        self.play(
            FadeIn(word_card, shift=UP*0.3),
            Write(word_content),
            run_time=0.8
        )
        self.wait(1.5)

        self.play(
            Indicate(word_title, scale_factor=1.05, color="#38BDF8"),
            Indicate(huneum_main, scale_factor=1.05, color="#FDE047"),
            run_time=0.8
        )
        self.wait(0.5)
