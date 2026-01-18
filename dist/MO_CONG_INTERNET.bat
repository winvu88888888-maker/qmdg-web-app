@echo off
color 0B
echo ======================================================
echo   BUOC 2: DANG MO CONG INTERNET (DUNG CHO 4G)
echo ======================================================
echo.
echo QUAN TRONG: Hay dam bao file 'qmdg_web_server.py' dang chay!
echo.

set "NGROK_EXE=ngrok.exe"
if not exist "%NGROK_EXE%" set "NGROK_EXE=C:\ngrok\ngrok.exe"

"%NGROK_EXE%" http 5000 --host-header=rewrite

echo.
echo [!] Neu cua so bi tat, hay kiem tra lai ma Token o Buoc 1.
pause