# 🔮 Kỳ Môn Độn Giáp - Web Application

Ứng dụng Kỳ Môn Độn Giáp chạy 24/7 trên web, hỗ trợ 3 phương pháp bói toán:
- 🔮 Kỳ Môn Độn Giáp (1059 chủ đề)
- 📖 Mai Hoa Dịch Số (64 Quẻ Kinh Dịch)
- ☯️ Lục Hào Kinh Dịch

## 🚀 Chạy Local

### Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

### Chạy ứng dụng:
```bash
streamlit run app.py
```

Ứng dụng sẽ mở tại: `http://localhost:8501`

**Mật khẩu:** `1987`

## 🌐 Deploy lên Streamlit Cloud (MIỄN PHÍ 24/7)

### Bước 1: Tạo GitHub Repository

1. Vào https://github.com/new
2. Đặt tên repository (ví dụ: `qmdg-web`)
3. Chọn **Public**
4. Click **Create repository**

### Bước 2: Upload Code lên GitHub

```bash
# Mở terminal tại thư mục dự án
cd "c:\Users\GHC\Desktop\python1 - Copy"

# Khởi tạo Git
git init

# Thêm tất cả files
git add .

# Commit
git commit -m "Initial commit - Ky Mon Dun Giap Web App"

# Kết nối với GitHub (thay YOUR_USERNAME và YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push lên GitHub
git branch -M main
git push -u origin main
```

### Bước 3: Deploy lên Streamlit Cloud

1. Vào https://share.streamlit.io/
2. Click **"New app"**
3. Chọn repository vừa tạo
4. Main file path: `app.py`
5. Click **"Deploy"**

Sau 2-5 phút, bạn sẽ nhận được link dạng:
```
https://your-app-name.streamlit.app
```

## ✨ Tính Năng

- ✅ Xác thực bằng mật khẩu
- ✅ Tính toán Kỳ Môn theo thời gian thực
- ✅ Hiển thị 9 cung với thông tin chi tiết
- ✅ 1059 chủ đề với Dụng Thần cụ thể
- ✅ Mai Hoa 64 Quẻ
- ✅ Lục Hào Kinh Dịch
- ✅ Tìm kiếm chủ đề nhanh
- ✅ Giao diện responsive (PC, Mobile, Tablet)
- ✅ Chạy 24/7 trên cloud

## 📱 Truy Cập

Sau khi deploy, bạn có thể truy cập từ:
- 💻 Máy tính (bất kỳ trình duyệt nào)
- 📱 Điện thoại (4G, WiFi)
- 🌍 Bất kỳ đâu trên thế giới

## 🔧 Cập Nhật Code

Sau khi deploy, nếu muốn cập nhật:

```bash
# Sửa code trong app.py hoặc các file khác

# Commit và push
git add .
git commit -m "Update features"
git push

# Streamlit Cloud sẽ tự động deploy lại sau 1-2 phút
```

## 📞 Liên Hệ

**Tác giả:** Vũ Việt Cường

**Mật khẩu ứng dụng:** `1987`

---

© 2026 - Kỳ Môn Độn Giáp Web Application
