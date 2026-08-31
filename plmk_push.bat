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

REM --- never hang on a hidden credential prompt: fail fast instead ---
set GIT_TERMINAL_PROMPT=0
set GCM_INTERACTIVE=never

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
REM --- keep the log and the message file out of the repo ---
git rm --cached --ignore-unmatch -q push.log .commitmsg >nul 2>&1

git diff --cached --quiet
if not errorlevel 1 (
  echo [%date% %time%] no changes >> "%LOG%"
  exit /b 0
)

echo [%date% %time%] --- commit --- >> "%LOG%"
git commit -F "%MSGFILE%" >> "%LOG%" 2>&1
if errorlevel 1 (
  echo [%date% %time%] ERROR: commit failed >> "%LOG%"
  exit /b 1
)

echo [%date% %time%] --- push --- >> "%LOG%"
git push >> "%LOG%" 2>&1
if errorlevel 1 (
  echo [%date% %time%] ERROR: push failed - GitHub credentials missing. >> "%LOG%"
  echo [%date% %time%]        Open GitHub Desktop and push once to store them. >> "%LOG%"
  exit /b 1
)

echo [%date% %time%] pushed OK >> "%LOG%"
exit /b 0
