@echo off
chcp 65001 > nul
title [Sweet Hanzi Auto Shorts] 자동 이어하기 렌더러

echo ========================================================
echo 🚀 [상형한자 160자 숏폼 자동 이어하기 렌더러]
echo ========================================================
echo.
echo 📌 이미 생성된 영상은 건너뛰고, 남은 한자들을 이어서 제작합니다.
echo.

cd /d "%~dp0"

:: 1. 필수 환경 점검 (가상환경이나 패키지가 없으면 자동 설치 실행)
if not exist ".venv\Scripts\python.exe" (
    echo [*] 새 컴퓨터 환경 감지: 필수 환경 자동 설치를 시작합니다...
    call setup_environment.bat
)

set PYTHON_EXE=.venv\Scripts\python.exe

%PYTHON_EXE% run_generator.py --all --quality m

echo.
echo ========================================================
echo 🎉 모든 160자 숏폼 렌더링이 완료되었습니다!
echo ========================================================
pause
