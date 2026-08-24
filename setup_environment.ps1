# 🎨 Hanzi Auto Stroke 환경 자동 설치 스크립트 (PowerShell)
# UTF-8 인코딩 지원
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host " 🎨 Hanzi Auto Stroke (상형한자 숏폼 자동 생성기) 환경 원클릭 자동 설치" -ForegroundColor Cyan
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. FFmpeg 확인 및 설치
Write-Host "[1/4] FFmpeg 영상 처리 도구 점검..." -ForegroundColor Yellow
$ffmpegCmd = Get-Command ffmpeg -ErrorAction SilentlyContinue
if (-not $ffmpegCmd) {
    Write-Host "[*] FFmpeg가 설치되어 있지 않습니다. winget으로 자동 설치를 진행합니다..." -ForegroundColor White
    try {
        winget install Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
        Write-Host "[V] FFmpeg 설치 완료!" -ForegroundColor Green
    } catch {
        Write-Host "[!] winget 설치 실패. 직접 다운로드 필요 (https://www.gyan.dev/ffmpeg/builds/)" -ForegroundColor Red
    }
} else {
    Write-Host "[V] FFmpeg가 이미 설치되어 있습니다: $($ffmpegCmd.Source)" -ForegroundColor Green
}

# 2. Python 가상환경 구성
Write-Host ""
Write-Host "[2/4] Python 가상환경(.venv) 설정..." -ForegroundColor Yellow
if (-not (Test-Path ".venv")) {
    Write-Host "[*] .venv 가상환경을 생성합니다..." -ForegroundColor White
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[!] Python이 설치되어 있지 않거나 환경변수에 등록되지 않았습니다." -ForegroundColor Red
        Exit
    }
} else {
    Write-Host "[V] 가상환경(.venv)이 준비되어 있습니다." -ForegroundColor Green
}

# 3. Python 의존성 라이브러리 설치
Write-Host ""
Write-Host "[3/4] 필수 패키지(Manim, Edge-TTS, OpenCV, Pillow, Pygame 등) 설치..." -ForegroundColor Yellow
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\pip install -r requirements.txt

# 4. 160개 상형문자 직관적 이미지 에셋 동기화
Write-Host ""
Write-Host "[4/4] 160개 직관적 상형한자 이미지 에셋 및 데이터베이스 최적화..." -ForegroundColor Yellow
& .\.venv\Scripts\python.exe download_all_svg_drawings.py

Write-Host ""
Write-Host "==============================================================================" -ForegroundColor Green
Write-Host " 🎉 모든 환경 설정 및 에셋 최적화가 성공적으로 완료되었습니다!" -ForegroundColor Green
Write-Host "==============================================================================" -ForegroundColor Green
Write-Host ""
Write-Host "실행 방법: .\.venv\Scripts\python.exe run_generator.py --char 大 --quality m" -ForegroundColor Cyan
