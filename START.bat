@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

title [Sweet Hanzi Auto Shorts] 원클릭 시작 및 환경 자동 점검 마법사
cd /d "%~dp0"

echo ==============================================================================
echo  🎨 Sweet Hanzi Auto Shorts: 원클릭 스마트 시작 & 환경 자동 진단
echo ==============================================================================
echo.

set NEED_SETUP=0

:: 1. FFmpeg 설치 여부 점검
where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] FFmpeg가 시스템에 없습니다. (영상 믹싱에 필수)
    set NEED_SETUP=1
)

:: 2. 가상환경 및 Python 패키지 점검
if not exist ".venv\Scripts\python.exe" (
    echo [!] Python 가상환경(.venv)이 구성되지 않았습니다.
    set NEED_SETUP=1
) else (
    .\.venv\Scripts\python.exe -c "import manim, edge_tts, cv2, PIL, pygame" >nul 2>nul
    if !errorlevel! neq 0 (
        echo [!] 필수 패키지가 일부 누락되었습니다.
        set NEED_SETUP=1
    )
)

:: 3. 160개 상형문자 SVG 에셋 점검
if not exist "assets\svg_drawings\車_drawing.svg" (
    echo [!] 160개 상형문자 직관적 이미지 에셋이 아직 동기화되지 않았습니다.
    set NEED_SETUP=1
)

:: 환경 설치가 필요한 경우 자동으로 setup_environment.bat 호출
if %NEED_SETUP% equ 1 (
    echo.
    echo [*] 새 컴퓨터 환경이 감지되었습니다!
    echo [*] 필수 프로그램과 라이브러리를 전자동으로 설치합니다. 잠시만 기다려주세요...
    echo ------------------------------------------------------------------------------
    call setup_environment.bat
    if %errorlevel% neq 0 (
        echo [오류] 자동 설치 중 문제가 발생했습니다. 창을 닫기 전 메시지를 확인해주세요.
        pause
        exit /b 1
    )
    echo ------------------------------------------------------------------------------
    echo [V] 환경 점검 및 자동 설치 완료!
    echo.
) else (
    echo [V] 모든 필수 프로그램(FFmpeg, Python 가상환경, 패키지, 160자 에셋)이 완벽하게 준비되어 있습니다!
    echo.
)

:: 4. 숏폼 생성 모드 선택 메뉴
echo [실행할 작업을 선택하세요]
echo  1. 상형한자 160자 전체 자동 연속 렌더링 (이미 제작된 것은 자동 건너뜀)
echo  2. 특정 한자 1개만 테스트 렌더링 (예: 車, 田, 日, 木 등)
echo  3. 환경 설정만 다시 점검/재설치
echo  4. 종료
echo.
set /p CHOICE="선택 번호 입력 (1/2/3/4) [기본값: 1]: "

if "%CHOICE%"=="" set CHOICE=1

if "%CHOICE%"=="1" (
    echo.
    echo 🚀 160자 전체 자동 렌더링을 시작합니다...
    .\.venv\Scripts\python.exe run_generator.py --all --quality m
) else if "%CHOICE%"=="2" (
    echo.
    set /p TARGET_CHAR="렌더링할 한자를 입력하세요 (예: 車): "
    if "!TARGET_CHAR!"=="" set TARGET_CHAR=車
    echo.
    echo 🚀 '!TARGET_CHAR!' 숏폼 렌더링 시작...
    .\.venv\Scripts\python.exe run_generator.py --char !TARGET_CHAR! --quality m
) else if "%CHOICE%"=="3" (
    call setup_environment.bat
) else (
    echo 프로그램을 종료합니다.
    exit /b 0
)

echo.
echo ==============================================================================
echo  🎉 작업이 완료되었습니다! (결과물 위치: output/videos/)
echo ==============================================================================
pause
