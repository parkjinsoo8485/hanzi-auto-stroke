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
from manim.utils.rate_functions import ease_out_quad, ease_in_out_quad, ease_out_cubic, linear

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
        
        import json
        char_key = "大"
        current_char_file = "assets/current_char.json"
        if os.path.exists(current_char_file):
            try:
                with open(current_char_file, "r", encoding="utf-8") as f:
                    char_key = json.load(f).get("char", "大")
            except Exception:
                char_key = os.environ.get("HANZI_CHAR", "大")
        else:
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
        # 2. 그림 픽토그램 제시 & 상형문자 모핑 (여유 있는 생각할 시간 부여)
        # ==========================================
        morph_center = UP * 2.0

        clean_char = char.replace("/", "_")
        drawing_svg_path = f"assets/svg_drawings/{clean_char}_drawing.svg"
        os.makedirs(os.path.dirname(drawing_svg_path), exist_ok=True)
        with open(drawing_svg_path, "w", encoding="utf-8") as f:
            f.write(self.char_data["drawing_svg"])

        # 원본 일러스트 컬러를 그대로 보존
        pictogram = SVGMobject(drawing_svg_path).scale(2.5).move_to(morph_center)
        
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
        # 📌 [핵심 개선] 그림을 보고 상형 원리를 충분히 생각하고 유추할 수 있도록 2.0초의 넉넉한 여유 시간 부여
        self.wait(2.0)

        # 코발트 블루 해서체 한자
        full_hanzi_mob = SVGMobject(self.animcjk_info["full_svg_path"]).scale(2.4).move_to(morph_center).set_color("#1D4ED8")

        morph_caption_box = RoundedRectangle(
            corner_radius=0.15, width=7.4, height=0.8,
            fill_color="#059669", fill_opacity=0.95, stroke_width=0
        ).move_to(DOWN * 0.2)
        morph_caption_text = Text(f"➡️ 글자로 완성: 「{char}」", font="Malgun Gothic", font_size=28, color="#FFFFFF", weight=BOLD)
        morph_caption_text.move_to(morph_caption_box.get_center())

        # 상형 그림이 한자로 변하는 모핑 애니메이션
        self.play(
            ReplacementTransform(pictogram, full_hanzi_mob),
            ReplacementTransform(caption_box, morph_caption_box),
            ReplacementTransform(caption_text, morph_caption_text),
            run_time=1.4
        )
        self.play(Indicate(full_hanzi_mob, scale_factor=1.06, color="#2563EB"), run_time=0.6)
        # 📌 완성된 한자를 충분히 인지할 수 있도록 1.0초 감상 시간 부여
        self.wait(1.0)

        # 헤더를 획순 정보(부수 / 총 N획 / 한자 훈음)로 매끄럽게 전환
        sub_header_txt_2 = Text(f"부수 {char}  |  총 {total_strokes}획", font="Malgun Gothic", font_size=24, color="#94A3B8", weight=BOLD)
        main_header_txt_2 = Text(f"{char}  {hun_eum}", font="Malgun Gothic", font_size=38, color="#FDE047", weight=BOLD)
        header_content_2 = VGroup(sub_header_txt_2, main_header_txt_2).arrange(DOWN, buff=0.12).move_to(header_bar.get_center())

        self.play(
            FadeOut(full_hanzi_mob, scale=0.9),
            FadeOut(morph_caption_box),
            FadeOut(morph_caption_text),
            ReplacementTransform(header_content_1, header_content_2),
            run_time=0.5
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

        from stroke_mask_renderer import generate_stroke_reveal_frames, get_stroke_medial_points, get_brush_tip_relative

        # 초고화질 실사 손+붓 ImageMobject (단일 원본 에셋으로 고스팅/잔상 완전 방지)
        brush_mob = ImageMobject("assets/hand_brush_clean.png").scale_to_fit_height(4.5).set_z_index(100)
        
        # 붓 이미지에서 실제 붓끝(Tip)의 정확한 상대 위치 파악
        norm_tip_x, norm_tip_y = get_brush_tip_relative("assets/hand_brush_clean.png")
        # 붓끝에서 이미지 중심까지의 벡터 (Tip -> Center)
        tip_offset = np.array([(0.5 - norm_tip_x) * brush_mob.width, (norm_tip_y - 0.5) * brush_mob.height, 0.0])

        rendered_strokes = []
        is_first_stroke = True

        for s_idx, stroke_item in enumerate(self.animcjk_info["strokes"]):
            order = stroke_item["order"]
            stroke_svg = stroke_item["stroke_svg_path"]
            medial_svg = stroke_item.get("medial_svg_path")
            medial_d = stroke_item.get("medial_d", "")

            # 1. 정밀 SVG 스플라인 포인트 추출 (stroke_mask_renderer와 100% 동일한 수학적 곡선)
            spline_pts = get_stroke_medial_points(medial_svg, num_samples=160) if medial_svg else []
            if not spline_pts:
                spline_pts = parse_svg_path_points(medial_d)

            if spline_pts:
                # 2. SVG 좌표 -> Manim 좌표계 1:1 변환
                manim_pts = [svg_to_manim_point(px, py, grid_pos, scale_factor=4.8) for px, py in spline_pts]
                start_pt = manim_pts[0]
                end_pt = manim_pts[-1]
                
                # 3. 해서체 정통 윤곽선 기반 실시간 노출 프레임 생성 (30프레임)
                reveal_frame_paths = generate_stroke_reveal_frames(
                    char=char,
                    order=order,
                    outline_svg_path=stroke_svg,
                    medial_svg_path=medial_svg,
                    num_frames=30
                )

                # 획 이미지 컨테이너 (격자판에 완벽 정렬)
                stroke_reveal_mob = ImageMobject(reveal_frame_paths[0]).scale_to_fit_width(4.8).move_to(grid_pos).set_z_index(10 + order)

                # 4. 붓 이동 궤적 (붓끝이 manim_pts를 0.001mm 오차도 없이 1:1 완벽 추종)
                hand_pts = [pt + tip_offset for pt in manim_pts]
                hand_curve = VMobject().set_points_as_corners(hand_pts)

                hover_offset = UP * 0.38 + RIGHT * 0.24

                if is_first_stroke:
                    # 1획: 상공 대기 위치에서 신속하고 부드럽게 등장
                    brush_mob.move_to(start_pt + tip_offset + hover_offset)
                    self.play(FadeIn(brush_mob, shift=DR * 0.25), run_time=0.20)

                    # [기필/착지 1단계]: 붓끝이 지면 시작점에 정밀 하강하여 접촉
                    self.play(
                        brush_mob.animate.move_to(start_pt + tip_offset),
                        run_time=0.12,
                        rate_func=ease_out_quad
                    )

                    # [돈필/지면 안착 2단계]: 붓끝 고정 상태에서 탄성 누름
                    self.play(
                        brush_mob.animate.scale(np.array([1.02, 0.94, 1.0]), about_point=start_pt + tip_offset),
                        run_time=0.08,
                        rate_func=ease_in_out_quad
                    )
                    is_first_stroke = False
                else:
                    # 이전 획 끝에서 공중으로 떠서 이번 획 상공으로 호를 그리며 쾌속 이동
                    self.play(
                        brush_mob.animate.move_to(start_pt + tip_offset + hover_offset),
                        run_time=0.16,
                        rate_func=ease_in_out_quad
                    )

                    # [기필/착지 1단계]: 붓끝이 지면 시작점으로 정밀 하강
                    self.play(
                        brush_mob.animate.move_to(start_pt + tip_offset),
                        run_time=0.10,
                        rate_func=ease_out_quad
                    )

                    # [돈필/지면 안착 2단계]: 붓끝 탄성 누름
                    self.play(
                        brush_mob.animate.scale(np.array([1.02, 0.94, 1.0]), about_point=start_pt + tip_offset),
                        run_time=0.06,
                        rate_func=ease_in_out_quad
                    )

                self.add(stroke_reveal_mob)

                # 붓이 이동하는 동안 해서체 완성형 획이 붓끝 위치에 맞춰 실시간으로 먹물이 채워짐
                progress_tracker = ValueTracker(0.0)

                def update_stroke_frame(mob):
                    prog = np.clip(progress_tracker.get_value(), 0.0, 1.0)
                    f_idx = min(int(round(prog * (len(reveal_frame_paths) - 1))), len(reveal_frame_paths) - 1)
                    mob.pixel_array = ImageMobject(reveal_frame_paths[f_idx]).pixel_array

                stroke_reveal_mob.add_updater(update_stroke_frame)

                # 📌 [핵심 개선] 붓 써지는 속도를 자연스럽고 우아한 호흡(0.95s)으로 조절하여 서예의 깊이감과 ASMR 몰입감 극대화
                self.play(
                    MoveAlongPath(brush_mob, hand_curve, rate_func=linear),
                    progress_tracker.animate.set_value(1.0),
                    run_time=0.95,
                    rate_func=linear
                )

                stroke_reveal_mob.remove_updater(update_stroke_frame)
                rendered_strokes.append(stroke_reveal_mob)

                # [수필/회봉 & 도약]: 획 종료 후 붓 탄성 복원 및 부드러운 리프트
                self.play(
                    brush_mob.animate.scale(np.array([1.0 / 1.02, 1.0 / 0.94, 1.0]), about_point=end_pt + tip_offset).shift(hover_offset),
                    run_time=0.12,
                    rate_func=ease_out_cubic
                )
            else:
                stroke_mob = SVGMobject(stroke_svg).scale(2.4).move_to(grid_pos).set_color("#1D4ED8")
                self.play(FadeIn(stroke_mob, run_time=0.8), run_time=0.8)
                rendered_strokes.append(stroke_mob)

            self.wait(0.04)

        # 붓글씨 완성 후 손 퇴장 (자연스럽게 우하단으로 퇴장)
        self.play(FadeOut(brush_mob, shift=DR*0.8), run_time=0.5)

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
        self.wait(3.5)

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
        self.wait(5.2)

        self.play(
            Indicate(word_title, scale_factor=1.05, color="#38BDF8"),
            Indicate(huneum_main, scale_factor=1.05, color="#FDE047"),
            run_time=0.8
        )
        self.wait(0.5)
