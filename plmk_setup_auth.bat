@echo off
REM ============================================================
REM  ONE-TIME SETUP
REM  Teaches command-line git how to log in to GitHub, so the
REM  daily automatic push can run without asking anything.
REM  A GitHub login window will appear once. Complete it.
REM ============================================================
setlocal

set "REPO=%USERPROFILE%\Documents\GitHub\plmk-trend"
cd /d "%REPO%" 2>nul
if errorlevel 1 (
  echo   Repo not found: %REPO%
  pause
  exit /b 1
)

echo.
echo  === Step 1: enabling the Windows credential helper ===
git config --global credential.helper manager
git config --global credential.https://github.com.provider github

echo.
echo  === Step 2: pushing once ===
echo  A GitHub login window should appear. Please complete it.
echo.

git push
if errorlevel 1 goto :retry

echo.
echo  ===============================================
echo   SUCCESS - credentials are stored.
echo   The daily automatic push will now work.
echo  ===============================================
echo.
pause
exit /b 0

:retry
echo.
echo  First attempt failed. Trying the older helper name...
git config --global credential.helper manager-core
git push
if errorlevel 1 goto :failed

echo.
echo  ===============================================
echo   SUCCESS - credentials are stored.
echo  ===============================================
echo.
pause
exit /b 0

:failed
echo.
echo  ===============================================
echo   STILL FAILING.
echo   Copy the messages above and send them to Claude.
echo  ===============================================
echo.
pause
exit /b 1
