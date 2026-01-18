@echo off
chcp 65001 >nul
echo ========================================
echo   CÀI ĐẶT NGROK TỰ ĐỘNG
echo ========================================
echo.

REM Kiểm tra xem ngrok đã được cài chưa
where ngrok >nul 2>&1
if %errorlevel% equ 0 (
    echo [✓] Ngrok đã được cài đặt!
    ngrok version
    echo.
    goto :config
)

echo [i] Đang kiểm tra winget...
where winget >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Winget không có sẵn.
    echo [i] Đang tải ngrok thủ công...
    goto :manual_download
)

echo [i] Đang cài đặt ngrok qua winget...
winget install ngrok -e --silent
if %errorlevel% equ 0 (
    echo [✓] Cài đặt ngrok thành công!
    goto :config
) else (
    echo [!] Cài đặt qua winget thất bại.
    goto :manual_download
)

:manual_download
echo.
echo ========================================
echo   TẢI NGROK THỦ CÔNG
echo ========================================
echo.
echo Vui lòng làm theo các bước sau:
echo.
echo 1. Mở trình duyệt và truy cập:
echo    https://ngrok.com/download
echo.
echo 2. Tải file ZIP cho Windows
echo.
echo 3. Giải nén file ngrok.exe vào thư mục:
echo    %~dp0
echo.
echo 4. Chạy lại file này sau khi giải nén
echo.
pause
exit /b 1

:config
echo.
echo ========================================
echo   CẤU HÌNH AUTHTOKEN
echo ========================================
echo.
echo Để sử dụng ngrok, bạn cần authtoken từ ngrok.com
echo.
echo Các bước lấy authtoken:
echo 1. Truy cập: https://dashboard.ngrok.com/signup
echo 2. Đăng ký/Đăng nhập tài khoản miễn phí
echo 3. Copy authtoken từ dashboard
echo.
set /p token="Nhập authtoken của bạn (hoặc Enter để bỏ qua): "

if "%token%"=="" (
    echo [i] Bỏ qua cấu hình authtoken
    echo [!] Bạn cần cấu hình sau bằng lệnh:
    echo     ngrok config add-authtoken YOUR_TOKEN
    goto :end
)

echo [i] Đang cấu hình authtoken...
ngrok config add-authtoken %token%
if %errorlevel% equ 0 (
    echo [✓] Cấu hình authtoken thành công!
) else (
    echo [!] Cấu hình authtoken thất bại
)

:end
echo.
echo ========================================
echo   HOÀN TẤT
echo ========================================
echo.
echo Bạn có thể sử dụng ngrok bằng lệnh:
echo   ngrok http 8000
echo.
pause
