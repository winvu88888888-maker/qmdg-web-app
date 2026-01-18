@echo off
color 0E
echo ======================================================
echo   BUOC 1: CAI DAT MA XAC THUC NGROK (AUTHTOKEN)
echo ======================================================
echo.
echo 1. Dang nhap lay ma tai: https://dashboard.ngrok.com/get-started/your-authtoken
echo 2. Copy chuoi ky tu dai (vi du: 2nS...)
echo.
set /p token="==> NHAP CHUOT PHAI DE DAN (PASTE) MA VAO DAY ROI NHAN ENTER: "

set "NGROK_EXE=ngrok.exe"
if not exist "%NGROK_EXE%" set "NGROK_EXE=C:\ngrok\ngrok.exe"

if not exist "%NGROK_EXE%" (
    echo [!] LOI: Khong tim thay file ngrok.exe o thu muc nay hoac C:\ngrok\
    echo Vui long giai nen file ngrok.zip da tai ve vao day.
    pause & exit
)

"%NGROK_EXE%" config add-authtoken %token%

echo.
echo ======================================================
echo   DA LUU TOKEN! BAY GIO BAN CO THE CHAY 'MO_CONG_INTERNET.bat'
echo ======================================================
pause