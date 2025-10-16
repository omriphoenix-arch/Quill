@echo off
REM Install StoryScript VS Code Extension

echo ========================================
echo StoryScript VS Code Extension Installer
echo ========================================
echo.

REM Get VS Code extensions directory
set "VSCODE_EXT=%USERPROFILE%\.vscode\extensions"
set "EXT_DIR=%VSCODE_EXT%\storyscript-1.1.0"

echo Installing to: %EXT_DIR%
echo.

REM Create extension directory
if exist "%EXT_DIR%" (
    echo Removing old version...
    rmdir /s /q "%EXT_DIR%"
)
mkdir "%EXT_DIR%"

REM Copy extension files
echo Copying extension files...
xcopy /E /I /Y "%~dp0" "%EXT_DIR%" >nul

REM Remove installation scripts from the installed extension
del "%EXT_DIR%\INSTALL_EXTENSION.bat" 2>nul
del "%EXT_DIR%\convert_icon.py" 2>nul

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo The StoryScript extension has been installed!
echo.
echo To activate it:
echo   1. Close ALL VS Code windows
echo   2. Reopen VS Code
echo   3. Your .story files will now have custom icons!
echo.
echo To enable the icon theme:
echo   1. Press Ctrl+Shift+P
echo   2. Type "File Icon Theme"
echo   3. Select "StoryScript File Icons"
echo.
pause
