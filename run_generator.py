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

from pipeline import run_pipeline
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="✨ 상형문자 모핑 & 한국식 번체 한자 획순 15초 숏폼 자동 생성기")
    parser.add_argument("--char", type=str, default="大", help="생성할 상형문자 (예: 大, 日)")
    parser.add_argument("--quality", type=str, default="m", choices=["l", "m", "h", "k"], help="렌더링 품질 (l: 480p 초고속, m: 720p, h: 1080p)")
    args = parser.parse_args()

    print("\n=======================================================")
    print("🚀 [Sweet Hanzi Auto Shorts] 상형문자 숏폼 생성기 가동")
    print("=======================================================")
    run_pipeline(char=args.char, quality=args.quality)
