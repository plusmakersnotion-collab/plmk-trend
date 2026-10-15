@echo off
setlocal
set "REPO=%USERPROFILE%\Documents\GitHub\plmk-trend"

echo ============================================================
echo   PLMK 트렌드 - 충돌 정리 (1회만 실행)
echo ------------------------------------------------------------
echo   10/14 제28호가 PC와 클라우드 양쪽에서 각각 만들어져
echo   충돌했습니다. 클라우드판이 이미 사이트에 올라가 있으므로
echo   PC에 남은 쪽을 버리고 원격과 똑같이 맞춥니다.
echo ============================================================
echo.

cd /d "%REPO%" 2>nul
if errorlevel 1 (
  echo [오류] 저장소 폴더를 찾을 수 없습니다: %REPO%
  echo.
  pause
  exit /b 1
)

echo [현재 로컬 상태]
git log --oneline -1
echo.

echo [1/4] 혹시 중단된 rebase 가 있으면 정리합니다...
git rebase --abort >nul 2>&1
echo       완료.
echo.

echo [2/4] 원격 최신 이력을 가져옵니다...
git fetch origin main
if errorlevel 1 (
  echo.
  echo [오류] fetch 실패. 인터넷 또는 GitHub 인증을 확인하세요.
  echo.
  pause
  exit /b 1
)
echo       완료.
echo.

echo [3/4] 되돌릴 수 있게 백업 브랜치를 만듭니다...
git branch -f plmk-backup-1014 HEAD
echo       백업 브랜치: plmk-backup-1014
echo.

echo [4/4] 로컬을 원격(origin/main)과 똑같이 맞춥니다...
git reset --hard origin/main
if errorlevel 1 (
  echo.
  echo [오류] reset 실패.
  echo.
  pause
  exit /b 1
)
echo.

echo ============================================================
echo   정리 완료
echo ============================================================
git log --oneline -1
echo.
echo 이제 plmk_push.bat 이 다시 정상 동작합니다.
echo 이 파일은 더 실행할 필요 없습니다.
echo.
pause
exit /b 0
