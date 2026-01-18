@echo off
setlocal enabledelayedexpansion
color 0A
echo ======================================================
echo   HE THONG TU DONG KHOI CHAY KY MON DON GIAP
echo ======================================================
echo.

echo [1/4] Dang kiem tra va cai dat thu vien Python...
pip install flask flask-cors Pillow

echo.
echo [2/4] Dang kiem tra file Ngrok...
set "NGROK_EXE=ngrok.exe"
if not exist "!NGROK_EXE!" set "NGROK_EXE=C:\ngrok\ngrok.exe"

if not exist "!NGROK_EXE!" (
    echo [!] CANH BAO: Khong tim thay ngrok.exe. 
    echo Hay dam bao ban da giai nen Ngrok vao thu muc nay.
)

echo.
echo [3/4] Dang khoi chay Server Ky Mon...
start "QMDG_Server" python qmdg_web_server.py

echo.
echo [4/4] Dang mo cong Internet (Dung cho 4G)...
start "Ngrok_Tunnel" cmd /c "MO_CONG_INTERNET.bat"

echo.
echo ======================================================
echo   MOI THU DA SAN SANG! 
echo   Hay doi cua so Ngrok hien link (https://...) roi vao.
echo ======================================================
timeout /t 10