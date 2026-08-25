"""
전체 한자 일괄 대량 생성 스크립트 (Batch Runner)
- Unicode / UTF-8 인코딩 완벽 대응
- 전체 160자 또는 지정 범위 한자 순차 자동 렌더링
- 에러 발생 시 건너뛰고 계속 진행
"""
import sys
import os
import argparse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# src 경로 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from hanzi_data import HANZI_DATABASE
from pipeline import run_pipeline

def run_batch(quality="m", start_idx=0, limit=None):
    all_chars = list(HANZI_DATABASE.keys())
    if limit is not None:
        target_chars = all_chars[start_idx:start_idx + limit]
    else:
        target_chars = all_chars[start_idx:]
    
    total = len(target_chars)
    print(f"\n🚀 [대량 생성 시작] 총 {total}개 한자 일괄 생성 시작 (품질: {quality})\n" + "="*50)
    
    success_count = 0
    fail_list = []
    
    for i, char in enumerate(target_chars, 1):
        print(f"\n[{i}/{total}] >>> '{char}' 숏폼 생성 진행 중...")
        try:
            res = run_pipeline(char=char, quality=quality)
            if res:
                success_count += 1
            else:
                fail_list.append(char)
        except Exception as e:
            print(f"❌ [에러 발생] '{char}' 생성 실패: {e}")
            fail_list.append(char)
            
    print("\n" + "="*50)
    print(f"🏁 [대량 생성 완료] 총 {total}개 중 성공: {success_count}개, 실패: {len(fail_list)}개")
    if fail_list:
        print(f"⚠️ 실패 목록: {', '.join(fail_list)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="상형문자 숏폼 일괄 대량 생성기")
    parser.add_argument("--quality", type=str, default="m", choices=["l", "m", "h", "k"], help="렌더링 품질 (l: 480p, m: 720p, h: 1080p)")
    parser.add_argument("--start", type=int, default=0, help="시작 인덱스 (기본: 0)")
    parser.add_argument("--limit", type=int, default=None, help="생성할 개수 제한 (기본: 전체)")
    args = parser.parse_args()
    
    run_batch(quality=args.quality, start_idx=args.start, limit=args.limit)
