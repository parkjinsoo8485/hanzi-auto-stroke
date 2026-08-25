"""
참고 영상 완벽 재현:
- 전통 화선지 텍스처 배경 (#F4F1EA)
- 1인칭 POV 실사 손+붓글씨 (Hand Holding Calligraphy Brush)
- AnimCJK 정통 해서체(정자체/번체) 획순 매끄러운 붓터치 애니메이션
- 상단/하단 카드 디자인 (한글/영문 듀얼 훈음 & 실생활 단어)
- 붓끝(Tip)과 획 노출 전면부(Ink Front) 100% 수학적 서브픽셀 일치
"""
import os
import sys
import re
import json
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

def svg_to_manim_point(x, y, grid_center, scale_factor=4.8):
    mx = grid_center[0] + (x / 1024.0 - 0.5) * scale_factor
    my = grid_center[1] - (y / 1024.0 - 0.5) * scale_factor
    return np.array([mx, my, 0.0])

class HanziShortScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from hanzi_data import HANZI_DATABASE
        from animcjk_loader import parse_animcjk_strokes
        
        # 환경변수 HANZI_CHAR 또는 current_scene_meta.json에서 타깃 한자 확인
        env_char = os.environ.get("HANZI_CHAR", "").strip()
        char_key = env_char if env_char else "大"
        self.huneum_dur = 3.2
        self.word_dur = 4.5
        
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        meta_file = os.path.join(project_root, "assets", "current_scene_meta.json")
        if os.path.exists(meta_file):
            try:
                with open(meta_file, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                    if not env_char:
                        char_key = meta.get("char", "大")
                    self.huneum_dur = float(meta.get("huneum_duration", 3.2))
                    self.word_dur = float(meta.get("word_duration", 4.5))
            except Exception:
                pass

        self.char_data = HANZI_DATABASE.get(char_key, HANZI_DATABASE["大"])
        self.animcjk_info = parse_animcjk_strokes(char_key)
        self.hand_brush_path = os.path.join(project_root, "assets", "hand_brush_clean.png")

    def construct(self):
        char = self.char_data["char"]
        hun_eum = self.char_data["hun_eum"]
        hun_eum_en = self.char_data["hun_eum_en"].replace("/", ", ")
        example_word = self.char_data["example_word"]
        example_desc = self.char_data["example_word_desc"].replace("/", ", ")
        total_strokes = len(self.animcjk_info["strokes"])

        # ==========================================
        # 1. 상단 정보 헤더 (0.0s ~ 0.6s)
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
        # 2. 그림 픽토그램 제시 & 상형문자 모핑 (0.6s ~ 6.9s)
        # ==========================================
        morph_center = UP * 2.0

        clean_char = char.replace("/", "_")
        drawing_svg_path = f"assets/svg_drawings/{clean_char}_drawing.svg"
        os.makedirs(os.path.dirname(drawing_svg_path), exist_ok=True)
        if not os.path.exists(drawing_svg_path) or os.path.getsize(drawing_svg_path) < 10:
            with open(drawing_svg_path, "w", encoding="utf-8") as f:
                f.write(self.char_data["drawing_svg"])

        # 원본 일러스트 컬러 보존
        pictogram = SVGMobject(drawing_svg_path).scale(2.5).move_to(morph_center)
        
        caption_box = RoundedRectangle(
            corner_radius=0.15, width=7.4, height=0.8,
            fill_color="#DC2626", fill_opacity=0.92, stroke_width=0
        ).move_to(DOWN * 0.2)
        caption_text = Text(f"💡 {self.char_data['sound_desc']}", font="Malgun Gothic", font_size=26, color="#FFFFFF", weight=BOLD)
        caption_text.move_to(caption_box.get_center())

        # 0.6s ~ 1.4s
        self.play(
            FadeIn(pictogram, scale=0.8),
            FadeIn(caption_box, shift=UP*0.2),
            Write(caption_text),
            run_time=0.8
        )
        # 1.4s ~ 3.4s (상형 원리 유추 시간 2.0초)
        self.wait(2.0)

        # 코발트 블루 해서체 한자
        full_hanzi_mob = SVGMobject(self.animcjk_info["full_svg_path"]).scale(2.4).move_to(morph_center).set_color("#1D4ED8")

        morph_caption_box = RoundedRectangle(
            corner_radius=0.15, width=7.4, height=0.8,
            fill_color="#059669", fill_opacity=0.95, stroke_width=0
        ).move_to(DOWN * 0.2)
        morph_caption_text = Text(f"➡️ 글자로 완성: 「{char}」", font="Malgun Gothic", font_size=28, color="#FFFFFF", weight=BOLD)
        morph_caption_text.move_to(morph_caption_box.get_center())

        # 3.4s ~ 4.8s: 모핑 애니메이션
        self.play(
            ReplacementTransform(pictogram, full_hanzi_mob),
            ReplacementTransform(caption_box, morph_caption_box),
            ReplacementTransform(caption_text, morph_caption_text),
            run_time=1.4
        )
        # 4.8s ~ 5.4s: 한자 강조
        self.play(Indicate(full_hanzi_mob, scale_factor=1.06, color="#2563EB"), run_time=0.6)
        # 5.4s ~ 6.4s: 감상 여유 시간
        self.wait(1.0)

        # 6.4s ~ 6.9s: 헤더 전환
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
        # 3. 서예 격자판 & 붓글씨 쓰기 (6.9s ~ )
        # ==========================================
        grid_pos = UP * 2.0
        grid_box = Square(side_length=4.8, stroke_color="#94A3B8", stroke_width=2.0, fill_color="#FAF9F6", fill_opacity=0.9).move_to(grid_pos)
        grid_dash_h = DashedLine(grid_box.get_left(), grid_box.get_right(), dash_length=0.18, stroke_color="#CBD5E1", stroke_width=1.5)
        grid_dash_v = DashedLine(grid_box.get_top(), grid_box.get_bottom(), dash_length=0.18, stroke_color="#CBD5E1", stroke_width=1.5)
        grid_dash_d1 = DashedLine(grid_box.get_corner(UL), grid_box.get_corner(DR), dash_length=0.18, stroke_color="#E2E8F0", stroke_width=1.2)
        grid_dash_d2 = DashedLine(grid_box.get_corner(UR), grid_box.get_corner(DL), dash_length=0.18, stroke_color="#E2E8F0", stroke_width=1.2)
        grid_group = VGroup(grid_box, grid_dash_h, grid_dash_v, grid_dash_d1, grid_dash_d2)

        # 6.9s ~ 7.3s: 격자판 등장
        self.play(FadeIn(grid_group), run_time=0.4)

        from stroke_mask_renderer import generate_stroke_reveal_frames, get_stroke_medial_points, get_brush_tip_relative

        brush_mob = ImageMobject("assets/hand_brush_clean.png").scale_to_fit_height(4.5).set_z_index(100)
        norm_tip_x, norm_tip_y = get_brush_tip_relative("assets/hand_brush_clean.png")
        # 붓끝(Tip) -> 이미지 중심(Center) 오프셋 벡터 (서브픽셀 정밀 고정)
        tip_offset = np.array([(0.5 - norm_tip_x) * brush_mob.width, (norm_tip_y - 0.5) * brush_mob.height, 0.0])

        rendered_strokes = []
        is_first_stroke = True

        for s_idx, stroke_item in enumerate(self.animcjk_info["strokes"]):
            order = stroke_item["order"]
            stroke_svg = stroke_item["stroke_svg_path"]
            medial_svg = stroke_item.get("medial_svg_path")
            medial_d = stroke_item.get("medial_d", "")

            spline_pts = get_stroke_medial_points(medial_svg, num_samples=500) if medial_svg else []
            if not spline_pts:
                spline_pts = parse_svg_path_points(medial_d)

            if spline_pts:
                manim_pts = [svg_to_manim_point(px, py, grid_pos, scale_factor=4.8) for px, py in spline_pts]
                start_pt = manim_pts[0]
                end_pt = manim_pts[-1]
                
                # 61개(0~60) 60fps 초고밀도 프레임 시퀀스 생성 (Frame 0: 100% 빈 캔버스)
                reveal_frame_paths = generate_stroke_reveal_frames(
                    char=char,
                    order=order,
                    outline_svg_path=stroke_svg,
                    medial_svg_path=medial_svg,
                    num_frames=60
                )

                # 메모리에 프레임 픽셀 배열 사전 로드 (애니메이션 중 I/O 렉 방지)
                frame_pixel_arrays = [ImageMobject(p).pixel_array for p in reveal_frame_paths]

                stroke_reveal_mob = ImageMobject(reveal_frame_paths[0]).scale_to_fit_width(4.8).move_to(grid_pos).set_z_index(10 + order)
                hover_offset = UP * 0.38 + RIGHT * 0.24

                if is_first_stroke:
                    # 1획: 7.3s ~ 7.8s (정확히 7.80s에 쓰기 시작)
                    brush_mob.move_to(start_pt + tip_offset + hover_offset)
                    self.play(FadeIn(brush_mob, shift=DR * 0.25), run_time=0.30)
                    self.play(
                        brush_mob.animate.move_to(start_pt + tip_offset),
                        run_time=0.20,
                        rate_func=ease_out_quad
                    )
                    is_first_stroke = False
                else:
                    # 다음 획: 공중 이동 및 정밀 착지
                    self.play(
                        brush_mob.animate.move_to(start_pt + tip_offset + hover_offset),
                        run_time=0.20,
                        rate_func=ease_in_out_quad
                    )
                    self.play(
                        brush_mob.animate.move_to(start_pt + tip_offset),
                        run_time=0.10,
                        rate_func=ease_out_quad
                    )

                self.add(stroke_reveal_mob)

                # 📌 [붓끝 & 먹물 전면부 1:1 서브픽셀 완벽 동기화 엔진]
                progress_tracker = ValueTracker(0.0)

                def update_writing(mob):
                    prog = np.clip(progress_tracker.get_value(), 0.0, 1.0)
                    
                    # 1. 먹물 노출 프레임 인덱스 (0 ~ 60)
                    f_idx = min(int(round(prog * (len(frame_pixel_arrays) - 1))), len(frame_pixel_arrays) - 1)
                    stroke_reveal_mob.pixel_array = frame_pixel_arrays[f_idx]
                    
                    # 2. 붓끝 위치 서브픽셀 선형 보간 (붓끝이 절단면 선단과 100% 동일하게 일치)
                    float_idx = prog * (len(manim_pts) - 1)
                    i0 = int(float_idx)
                    i1 = min(i0 + 1, len(manim_pts) - 1)
                    t_sub = float_idx - i0
                    curr_pt = (1.0 - t_sub) * manim_pts[i0] + t_sub * manim_pts[i1]
                    mob.move_to(curr_pt + tip_offset)

                brush_mob.add_updater(update_writing)

                # 1.00초 정밀 서예 라이팅 애니메이션 실행
                self.play(
                    progress_tracker.animate.set_value(1.0),
                    run_time=1.00,
                    rate_func=linear
                )

                brush_mob.remove_updater(update_writing)
                # 마지막 프레임 고정 (100% 완성)
                stroke_reveal_mob.pixel_array = frame_pixel_arrays[-1]
                brush_mob.move_to(end_pt + tip_offset)
                rendered_strokes.append(stroke_reveal_mob)

                # 붓 리프트 (0.20s): 크기 왜곡 없는 정밀 위치 이동
                self.play(
                    brush_mob.animate.move_to(end_pt + tip_offset + hover_offset),
                    run_time=0.20,
                    rate_func=ease_out_cubic
                )
            else:
                stroke_mob = SVGMobject(stroke_svg).scale(2.4).move_to(grid_pos).set_color("#1D4ED8")
                self.play(FadeIn(stroke_mob, run_time=1.0), run_time=1.0)
                rendered_strokes.append(stroke_mob)

            # 획간 정밀 텀 (0.10s)
            self.wait(0.10)

        # 붓글씨 완성 후 손 퇴장 (0.50s)
        self.play(FadeOut(brush_mob, shift=DR*0.8), run_time=0.50)

        # 전체 글자 완성 축하 블루 플래시 (0.60s)
        self.play(
            Flash(grid_pos, color="#2563EB", line_length=0.6, num_lines=24),
            run_time=0.60
        )
        self.wait(0.40)

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
        
        # 영어 라벨
        en_badge = RoundedRectangle(corner_radius=0.08, width=0.8, height=0.42, fill_color="#3B82F6", fill_opacity=0.9, stroke_width=0)
        en_badge_txt = Text("EN", font="Arial", font_size=16, color="#FFFFFF", weight=BOLD).move_to(en_badge.get_center())
        en_txt = Text(f"{hun_eum_en}", font="Arial", font_size=24, color="#93C5FD", weight=BOLD)
        en_line = VGroup(VGroup(en_badge, en_badge_txt), en_txt).arrange(RIGHT, buff=0.15)

        huneum_text_group = VGroup(huneum_main, en_line).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        huneum_content = VGroup(huneum_badge_group, huneum_text_group).arrange(RIGHT, buff=0.4).move_to(huneum_card.get_center())

        # 훈음 카드 등장 (0.60s)
        self.play(
            FadeIn(huneum_card, shift=UP*0.3),
            GrowFromCenter(huneum_content),
            run_time=0.60
        )
        # 훈음 음성 길이만큼 대기 (+ 0.4s 여유)
        wait_huneum = max(self.huneum_dur, 2.5) + 0.4
        self.wait(wait_huneum)

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

        # 단어 카드 등장 (0.80s)
        self.play(
            FadeIn(word_card, shift=UP*0.3),
            Write(word_content),
            run_time=0.80
        )
        # 단어 음성 길이만큼 대기 (+ 1.0s 여유)
        wait_word = max(self.word_dur, 3.5) + 1.0
        self.wait(wait_word)

        # 최종 마무리 강조 (0.80s)
        self.play(
            Indicate(word_title, scale_factor=1.05, color="#38BDF8"),
            Indicate(huneum_main, scale_factor=1.05, color="#FDE047"),
            run_time=0.80
        )
        self.wait(0.50)
