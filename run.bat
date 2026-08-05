@echo off
:: Change directory to the folder containing this batch file (essential if run as Admin)
cd /d "%~dp0"

title R.O.R. Signals Quiz and Trainer
echo Starting R.O.R. Signals Quiz and Trainer Server...
start /B python server.py
timeout /t 2 >nul
echo Opening application in your web browser...
start http://localhost:8000
echo.
echo ==============================================
echo  Server is running at http://localhost:8000
echo  To stop the server, close this command window.
echo ==============================================
echo.
pause
