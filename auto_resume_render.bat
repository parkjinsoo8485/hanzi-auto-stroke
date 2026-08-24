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

if exist ".venv\Scripts\python.exe" (
    set PYTHON_EXE=.venv\Scripts\python.exe
) else (
    set PYTHON_EXE=python
)

%PYTHON_EXE% run_generator.py --all --quality m

echo.
echo ========================================================
echo 🎉 모든 160자 숏폼 렌더링이 완료되었습니다!
echo ========================================================
pause
