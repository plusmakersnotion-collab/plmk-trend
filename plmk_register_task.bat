@echo off
REM ============================================================
REM  Registers the daily push as a Windows scheduled task.
REM  Run this ONCE by double-clicking it.
REM  First attempt 08:20, then retries every 30 min for 4 hours
REM  so a late boot still gets published.
REM ============================================================
setlocal

set "SCRIPT=%USERPROFILE%\Documents\GitHub\plmk-trend\plmk_push.bat"

if not exist "%SCRIPT%" (
  echo.
  echo   plmk_push.bat not found:
  echo   %SCRIPT%
  echo.
  pause
  exit /b 1
)

schtasks /create ^
  /tn "PLMK Trend Auto Push" ^
  /tr "\"%SCRIPT%\"" ^
  /sc daily /st 08:20 /ri 30 /du 0004:00 ^
  /f

if errorlevel 1 (
  echo.
  echo   Registration FAILED.
  echo.
  pause
  exit /b 1
)

echo.
echo   Registered: "PLMK Trend Auto Push"
echo   Daily 08:20, retrying every 30 min until 12:20.
echo.
echo   Check it any time with:
echo     schtasks /query /tn "PLMK Trend Auto Push"
echo   Test it right now with:
echo     schtasks /run  /tn "PLMK Trend Auto Push"
echo.
pause
