@echo off

if "%~1" == "" goto :eof
if not exist "%~1" (
	echo Could not find file '%~1'.
	goto :error
)

if "%~2" == "" (
    "%~dp0Narchive.exe" extract "%~1"
) else (
    "%~dp0Narchive.exe" extract --output "%~2" "%~1"
)

if %errorlevel% neq 0 goto :error

goto :eof

:error
pause
