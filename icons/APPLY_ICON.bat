@echo off
REM Quick Icon Refresh for StoryScript
REM Updates the file association to use the new icon

echo ========================================
echo StoryScript Icon Refresh
echo ========================================
echo.
echo This will update .story files to use the new icon.
echo.

REM Get the absolute path to this script's directory
set "SCRIPT_DIR=%~dp0"
set "ICON_PATH=%SCRIPT_DIR%storyscript_icon.ico"

echo Icon location: %ICON_PATH%
echo.

if not exist "%ICON_PATH%" (
    echo ERROR: Icon file not found!
    echo Expected location: %ICON_PATH%
    echo.
    echo Please make sure storyscript_icon.ico exists in the icons folder.
    pause
    exit /b 1
)

echo [1/3] Updating registry...
powershell -ExecutionPolicy Bypass -Command ^
    "New-Item -Path 'HKCU:\Software\Classes\.story' -Force | Out-Null; ^
     Set-ItemProperty -Path 'HKCU:\Software\Classes\.story' -Name '(Default)' -Value 'StoryScript.File'; ^
     New-Item -Path 'HKCU:\Software\Classes\StoryScript.File' -Force | Out-Null; ^
     Set-ItemProperty -Path 'HKCU:\Software\Classes\StoryScript.File' -Name '(Default)' -Value 'StoryScript Program'; ^
     New-Item -Path 'HKCU:\Software\Classes\StoryScript.File\DefaultIcon' -Force | Out-Null; ^
     Set-ItemProperty -Path 'HKCU:\Software\Classes\StoryScript.File\DefaultIcon' -Name '(Default)' -Value '%ICON_PATH%,0'; ^
     Write-Host '  Registry updated successfully!' -ForegroundColor Green"

echo.
echo [2/3] Clearing icon cache...
ie4uinit.exe -show
timeout /t 2 /nobreak >nul

echo.
echo [3/3] Restarting Windows Explorer...
taskkill /f /im explorer.exe >nul 2>&1
start explorer.exe

echo.
echo ========================================
echo Icon Refresh Complete!
echo ========================================
echo.
echo Your .story files should now display the new icon!
echo.
echo If you don't see the icon change immediately:
echo   1. Navigate away from the folder and back
echo   2. Press F5 to refresh File Explorer
echo   3. Restart your computer (if needed)
echo.
pause
