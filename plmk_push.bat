@echo off
REM ============================================================
REM  PLMK Trend - auto commit & push
REM  Claude writes the new HTML into this repo; this script
REM  commits and pushes it so Netlify redeploys.
REM  Exits quietly when there is nothing new.
REM ============================================================
setlocal

set "REPO=%USERPROFILE%\Documents\GitHub\plmk-trend"
set "MSGFILE=%TEMP%\plmk_commit_msg.txt"
set "LOG=%REPO%\push.log"

cd /d "%REPO%" 2>nul
if errorlevel 1 (
  echo [%date% %time%] ERROR: repo not found: %REPO% >> "%USERPROFILE%\plmk_push_error.log"
  exit /b 1
)

REM --- commit message: use the one Claude left, else a default ---
if exist ".commitmsg" (
  move /y ".commitmsg" "%MSGFILE%" >nul
) else (
  echo auto publish> "%MSGFILE%"
)

git add -A

REM --- nothing staged? stop here, no empty commits ---
git diff --cached --quiet
if not errorlevel 1 (
  echo [%date% %time%] no changes >> "%LOG%"
  exit /b 0
)

git commit -F "%MSGFILE%" >> "%LOG%" 2>&1
if errorlevel 1 (
  echo [%date% %time%] ERROR: commit failed >> "%LOG%"
  exit /b 1
)

git push >> "%LOG%" 2>&1
if errorlevel 1 (
  echo [%date% %time%] ERROR: push failed - check credentials >> "%LOG%"
  exit /b 1
)

echo [%date% %time%] pushed OK >> "%LOG%"
exit /b 0
