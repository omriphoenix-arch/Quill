@echo off
echo ========================================
echo    Manual Icon Fix
echo ========================================
echo.
echo This will manually set the .quill file icon.
echo.
pause

echo.
echo Setting registry keys...
echo.

REM Set the file association
reg add "HKCU\Software\Classes\.quill" /ve /t REG_SZ /d "Quill.File" /f

REM Set the file type description  
reg add "HKCU\Software\Classes\Quill.File" /ve /t REG_SZ /d "Quill Program" /f

REM Set the icon
reg add "HKCU\Software\Classes\Quill.File\DefaultIcon" /ve /t REG_SZ /d "%LOCALAPPDATA%\Quill\quill_icon.ico,0" /f

REM Set the open command
reg add "HKCU\Software\Classes\Quill.File\shell\open\command" /ve /t REG_SZ /d "python \"%LOCALAPPDATA%\Quill\Quill.py\" \"%%1\"" /f

echo.
echo Registry updated!
echo.
echo Now clearing icon cache...
echo.

REM Delete icon cache
del /f /q "%LOCALAPPDATA%\IconCache.db" 2>nul
del /f /q "%LOCALAPPDATA%\Microsoft\Windows\Explorer\iconcache*.db" 2>nul

echo.
echo Restarting Explorer...
taskkill /f /im explorer.exe
start explorer.exe

echo.
echo ========================================
echo Done!
echo ========================================
echo.
echo Check your .quill files now!
echo.
echo If still no icon, try:
echo   1. Restarting your computer
echo   2. Right-click a .quill file -^> Properties
echo      and check what icon is shown
echo.
pause
