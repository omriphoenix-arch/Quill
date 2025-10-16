@echo off
echo ========================================
echo StoryScript User Installer
echo (No Admin Required!)
echo ========================================
echo.
echo This installer will install StoryScript to:
echo %LOCALAPPDATA%\StoryScript
echo.
echo This location does NOT require admin privileges.
echo.
pause
echo.
echo Starting installation...
echo.

PowerShell -ExecutionPolicy Bypass -File "%~dp0install_user.ps1"

echo.
echo Installation complete!
echo.
pause
