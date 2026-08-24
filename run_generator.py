"""
상형문자 숏폼 원클릭 자동 생성 CLI
사용법:
  python run_generator.py --char 大
  python run_generator.py --char 日 --quality h
"""
import sys
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# src 경로 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from hanzi_data import HANZI_DATABASE
from pipeline import run_pipeline
import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="✨ 상형문자 모핑 & 한국식 번체 한자 획순 15초 숏폼 자동 생성기 (대량 일괄 생성 지원)")
    parser.add_argument("--char", type=str, default="大", help="생성할 한자 (단일: 日 / 다중: 日,木,山 / 전체: all)")
    parser.add_argument("--all", action="store_true", help="데이터베이스 내의 모든 한자 숏폼 일괄 대량 생성")
    parser.add_argument("--quality", type=str, default="m", choices=["l", "m", "h", "k"], help="렌더링 품질 (l: 480p 초고속, m: 720p, h: 1080p)")
    parser.add_argument("--force", action="store_true", help="기존 생성 파일이 있어도 덮어쓰고 새로 재생성")
    args = parser.parse_args()

    # 대상 한자 목록 추출
    if args.all or args.char.strip().lower() == "all":
        target_chars = list(HANZI_DATABASE.keys())
    else:
        # 콤마 또는 공백으로 구분된 여러 한자 지원
        raw_chars = args.char.replace(",", " ").split()
        target_chars = [c.strip() for c in raw_chars if c.strip()]

    print("\n=======================================================")
    print(f"🚀 [Sweet Hanzi Auto Shorts] 상형문자 숏폼 생성기 가동 (총 {len(target_chars)}개)")
    print(f"📌 대상 한자: {', '.join(target_chars)} | 품질: {args.quality} | 강제재생성: {args.force}")
    print("=======================================================\n")

    start_time = time.time()
    success_list = []
    fail_list = []

    for idx, c in enumerate(target_chars, 1):
        print(f"\n[{idx}/{len(target_chars)}] ▶ 「{c}」 숏폼 검사 및 제작 시작...")
        if c not in HANZI_DATABASE:
            print(f"⚠️ [Skip] 지원되지 않는 한자입니다: {c}")
            fail_list.append(c)
            continue

        hun_eum_name = HANZI_DATABASE[c]['hun_eum'].replace(' ', '_')
        expected_output = os.path.join("output", f"shorts_{c}_{hun_eum_name}.mp4")
        if not args.force and os.path.exists(expected_output):
            print(f"⏩ [이미 생성됨] {expected_output} 파일이 이미 존재하므로 건너뜁니다. (--force 시 재생성)")
            success_list.append(c)
            continue

        try:
            ok = run_pipeline(char=c, quality=args.quality)
            if ok:
                success_list.append(c)
            else:
                fail_list.append(c)
        except Exception as e:
            print(f"❌ [Error] {c} 생성 중 예외 발생: {e}")
            fail_list.append(c)

    elapsed = time.time() - start_time
    print("\n=======================================================")
    print(f"📊 [일괄 생성 완료 보고서]")
    print(f"✅ 성공 ({len(success_list)}개): {', '.join(success_list) if success_list else '없음'}")
    if fail_list:
        print(f"❌ 실패 ({len(fail_list)}개): {', '.join(fail_list)}")
    print(f"⏱️ 총 소요 시간: {elapsed:.1f}초")
    print(f"📁 결과물 폴더: {os.path.abspath('output')}")
    print("=======================================================\n")
