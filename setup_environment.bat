@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ==============================================================================
echo  🎨 Hanzi Auto Stroke (상형한자 숏폼 자동 생성기) 환경 원클릭 자동 설치 마법사
echo ==============================================================================
echo.

:: 1. 관리자 권한 확인 (선택적)
echo [1/4] 시스템 환경 확인 중...

:: 2. winget을 통한 FFmpeg 자동 감지 및 설치
where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    echo [*] 영상 렌더링 필수 도구인 FFmpeg가 설치되어 있지 않습니다.
    echo [*] winget(Windows 패키지 관리자)을 통해 FFmpeg 설치를 시도합니다...
    winget install "Gyan.FFmpeg" --accept-source-agreements --accept-package-agreements
    if %errorlevel% neq 0 (
        echo [경고] winget 자동 설치 실패. 수동 설치 링크: https://www.gyan.dev/ffmpeg/builds/
    ) else (
        echo [V] FFmpeg 설치 완료! (환경변수 적용을 위해 설치 후 창을 다시 열어야 할 수 있습니다.)
    )
) else (
    echo [V] FFmpeg가 이미 시스템에 설치되어 있습니다.
)

:: 3. Python 가상환경 구성
echo.
echo [2/4] Python 가상환경(.venv) 구성 중...
if not exist ".venv" (
    echo [*] .venv 폴더 생성 중...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo [오류] Python이 설치되어 있지 않거나 경로에 등록되지 않았습니다. Python 3.10 이상을 먼저 설치해주세요.
        pause
        exit /b 1
    )
) else (
    echo [V] 가상환경(.venv)이 이미 존재합니다.
)

:: 4. 필수 Python 라이브러리 자동 설치
echo.
echo [3/4] 필수 Python 패키지(Manim, Edge-TTS, OpenCV, Pillow 등) 설치 중...
call .\.venv\Scripts\python.exe -m pip install --upgrade pip
call .\.venv\Scripts\pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [오류] 패키지 설치 중 오류가 발생했습니다.
    pause
    exit /b 1
)

:: 5. 160개 상형한자 최적화 SVG 및 데이터베이스 동기화
echo.
echo [4/4] 160개 상형한자 직관적 이미지 에셋 및 데이터베이스 점검/동기화 중...
call .\.venv\Scripts\python.exe download_all_svg_drawings.py

echo.
echo ==============================================================================
echo  🎉 모든 필수 프로그램 및 에셋 설치가 완벽하게 완료되었습니다!
echo ==============================================================================
echo.
echo [사용 방법]
echo  - 단일 한자 숏폼 생성 예시:
echo    .\.venv\Scripts\python.exe run_generator.py --char 大 --quality m
echo.
echo  - 160개 전체 자동 일괄 렌더링:
echo    auto_resume_render.bat 실행
echo.
pause
