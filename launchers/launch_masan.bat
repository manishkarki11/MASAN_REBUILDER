@echo off
color 4
cls
echo.
echo  ███    ███  █████  ███████  █████  ███    ██ 
echo  ████  ████ ██   ██ ██      ██   ██ ████   ██ 
echo  ██ ████ ██ ███████ ███████ ███████ ██ ██  ██ 
echo  ██  ██  ██ ██   ██      ██ ██   ██ ██  ██ ██ 
echo  ██      ██ ██   ██ ███████ ██   ██ ██   ████ 
echo         MASAN TOOLKIT - Windows Launcher
echo.
echo Launching MASAN Toolkit...
timeout /t 2 /nobreak >nul
python core\core.py
pause
