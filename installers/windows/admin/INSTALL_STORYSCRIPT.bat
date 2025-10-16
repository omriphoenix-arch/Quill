@echo off
REM StoryScript Easy Installer Launcher
REM This launches the installer with admin privileges

echo ========================================
echo    StoryScript Installer
echo ========================================
echo.
echo This will install StoryScript on your computer.
echo.
echo Installing to: C:\Program Files\StoryScript
echo.
echo You will be asked for administrator permission.
echo.
pause

REM Run PowerShell installer as admin
powershell -ExecutionPolicy Bypass -File "%~dp0install.ps1"

pause
