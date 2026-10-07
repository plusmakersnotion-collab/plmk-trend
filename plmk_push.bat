@echo off
REM ============================================================
REM  PLMK Trend - auto commit & push  (v2)
REM
REM  Claude writes the new files into this repo; this script
REM  commits and pushes them so Netlify redeploys.
REM
REM  v2 changes:
REM   - always checks for unpushed commits, even when there are
REM     no new file changes  (v1 exited with "no changes" and
REM     never retried a push that had failed earlier)
REM   - rebases onto origin/main before pushing, so a diverged
REM     branch recovers by itself instead of failing forever
REM   - reports the real reason a push failed instead of always
REM     blaming missing credentials
REM ============================================================
setlocal enabledelayedexpansion

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

REM --- STEP 1: commit, only if something is staged ---
git diff --cached --quiet
if errorlevel 1 (
  echo [%date% %time%] --- commit --- >> "%LOG%"
  git commit -F "%MSGFILE%" >> "%LOG%" 2>&1
  if errorlevel 1 (
    echo [%date% %time%] ERROR: commit failed >> "%LOG%"
    exit /b 1
  )
)

REM --- STEP 2: always compare against the remote ---
REM  This runs even when nothing was committed just now, so a push
REM  that failed on an earlier run gets retried.
git fetch origin main >nul 2>&1
if errorlevel 1 (
  echo [%date% %time%] ERROR: fetch failed - no network, or credentials not stored. >> "%LOG%"
  echo [%date% %time%]        Fix: run plmk_setup_auth.bat, or push once from GitHub Desktop. >> "%LOG%"
  exit /b 1
)

set "AHEAD=0"
set "BEHIND=0"
for /f %%i in ('git rev-list --count origin/main..HEAD') do set "AHEAD=%%i"
for /f %%i in ('git rev-list --count HEAD..origin/main') do set "BEHIND=%%i"

if "!AHEAD!"=="0" if "!BEHIND!"=="0" (
  echo [%date% %time%] up to date >> "%LOG%"
  exit /b 0
)

if "!AHEAD!"=="0" (
  echo [%date% %time%] behind origin by !BEHIND! - fast-forwarding >> "%LOG%"
  git merge --ff-only origin/main >> "%LOG%" 2>&1
  exit /b 0
)

REM --- STEP 3: local is ahead. If it also diverged, rebase first. ---
if not "!BEHIND!"=="0" (
  echo [%date% %time%] diverged - ahead !AHEAD!, behind !BEHIND! - rebasing onto origin/main >> "%LOG%"
  git rebase origin/main >> "%LOG%" 2>&1
  if errorlevel 1 (
    git rebase --abort >nul 2>&1
    echo [%date% %time%] ERROR: rebase hit a conflict - needs a human. Nothing was changed. >> "%LOG%"
    exit /b 1
  )
)

REM --- STEP 4: push ---
echo [%date% %time%] --- push - !AHEAD! commit^(s^) ahead --- >> "%LOG%"
git push origin main >> "%LOG%" 2>&1
if errorlevel 1 (
  echo [%date% %time%] ERROR: push failed - read the git output just above. >> "%LOG%"
  echo [%date% %time%]        "rejected / fetch first"  = remote moved again; next run will rebase and retry. >> "%LOG%"
  echo [%date% %time%]        "Authentication failed"   = run plmk_setup_auth.bat, or push once from GitHub Desktop. >> "%LOG%"
  exit /b 1
)

echo [%date% %time%] pushed OK - !AHEAD! commit^(s^) >> "%LOG%"
exit /b 0
