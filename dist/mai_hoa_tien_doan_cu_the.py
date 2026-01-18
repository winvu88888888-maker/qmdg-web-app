# -*- coding: utf-8 -*-
"""
MAI HOA DỊCH SỐ - TƯỢNG SỐ TIÊN ĐOÁN CỤ THỂ
Chú trọng: Số lượng, Số tiền, Trai/Gái, Già/Trẻ, Vật gì
"""

from mai_hoa_dich_so import BAT_QUAI, LUC_THAP_TU_QUAI

# Bát Quái Tượng Số - Hệ thống tiên đoán cụ thể
BAT_QUAI_TUONG_SO_CHI_TIET = {
    "Càn": {
        "so_luong": "1, 4, 6, 9 (số lẻ, số lớn)",
        "so_tien": "Lớn, nhiều, giá trị cao (hàng triệu, hàng tỷ)",
        "gioi_tinh": "Nam, đàn ông, con trai",
        "tuoi_tac": "Già, trung niên (45-70 tuổi), người lớn tuổi",
        "ngoai_hinh": "Cao lớn, vạm vỡ, khỏe mạnh, da trắng/vàng",
        "tinh_cach": "Cứng rắn, quyết đoán, có quyền lực, nghiêm khắc",
        "nghe_nghiep": "Lãnh đạo, giám đốc, quan chức, chủ doanh nghiệp",
        "vat_the": "Kim loại quý (vàng, bạc), đồ trang sức, xe hơi cao cấp, nhà lớn",
        "dong_vat": "Ngựa, sư tử, rồng, chim ưng",
        "mau_sac": "Trắng, vàng kim, bạc",
        "huong": "Tây Bắc",
        "thoi_gian": "Mùa Thu (Tháng 9-11), giờ Tuất-Hợi (19h-23h)"
    },
    
    "Khôn": {
        "so_luong": "2, 5, 8, 10 (số chẵn, số nhiều)",
        "so_tien": "Trung bình, tích lũy từ từ, ổn định",
        "gioi_tinh": "Nữ, đàn bà, mẹ, vợ",
        "tuoi_tac": "Già, cao tuổi (60+ tuổi), bà lão",
        "ngoai_hinh": "Thấp, mập, da ngăm đen, hiền lành",
        "tinh_cach": "Nhu hòa, chịu đựng, khiêm tốn, hiền lành",
        "nghe_nghiep": "Nông dân, công nhân, người làm ruộng, nội trợ",
        "vat_the": "Đất đai, ruộng vườn, vải vóc, lương thực, gạo",
        "dong_vat": "Bò, trâu, dê, gà mái",
        "mau_sac": "Vàng, nâu, đen",
        "huong": "Tây Nam",
        "thoi_gian": "Mùa Hạ cuối (Tháng 6), giờ Mùi-Thân (13h-17h)"
    },
    
    "Chấn": {
        "so_luong": "3, 4, 8 (số động, thay đổi)",
        "so_tien": "Tăng nhanh, biến động lớn, đột biến",
        "gioi_tinh": "Nam, con trai cả, thanh niên",
        "tuoi_tac": "Trẻ, thanh niên (20-35 tuổi)",
        "ngoai_hinh": "Cao, gầy, năng động, da ngăm",
        "tinh_cach": "Nóng nảy, năng động, quyết đoán, thích thay đổi",
        "nghe_nghiep": "Vận động viên, quân nhân, lái xe, nhạc sĩ",
        "vat_the": "Cây cối, tre trúc, nhạc cụ, điện thoại, máy móc động",
        "dong_vat": "Rồng, rắn, chim sẻ",
        "mau_sac": "Xanh lá đậm, xanh lục",
        "huong": "Đông",
        "thoi_gian": "Mùa Xuân (Tháng 2-4), giờ Mão (5h-7h)"
    },
    
    "Tốn": {
        "so_luong": "3, 4, 5 (số nhỏ, linh hoạt)",
        "so_tien": "Nhỏ nhưng nhiều lần, lợi nhuận từ thương mại",
        "gioi_tinh": "Nữ, con gái cả, phụ nữ trung niên",
        "tuoi_tac": "Trung niên (30-45 tuổi)",
        "ngoai_hinh": "Cao, mảnh khảnh, tóc dài, da trắng",
        "tinh_cach": "Khiêm tốn, linh hoạt, khéo léo, hay suy nghĩ",
        "nghe_nghiep": "Thương nhân, giáo viên, tư vấn, môi giới",
        "vat_the": "Gió, hương thơm, dây thừng, hàng hóa, quạt",
        "dong_vat": "Gà, chim, rắn",
        "mau_sac": "Xanh lá nhạt, xanh lục nhạt",
        "huong": "Đông Nam",
        "thoi_gian": "Mùa Xuân cuối (Tháng 4-5), giờ Thìn-Tỵ (7h-11h)"
    },
    
    "Khảm": {
        "so_luong": "1, 6 (số ít, số âm)",
        "so_tien": "Ít, khó khăn, hoặc rất nhiều (nước chảy)",
        "gioi_tinh": "Nam, con trai giữa, thanh niên",
        "tuoi_tac": "Trung niên (25-40 tuổi)",
        "ngoai_hinh": "Trung bình, da đen, mắt sâu",
        "tinh_cach": "Thông minh, khôn ngoan, bí ẩn, khó đoán",
        "nghe_nghiep": "Người làm việc với nước, ngư dân, thợ lặn, trinh thám",
        "vat_the": "Nước, rượu, mực, dầu, chất lỏng",
        "dong_vat": "Heo, chuột, cá, rùa",
        "mau_sac": "Đen, xanh đen, xanh dương đậm",
        "huong": "Bắc",
        "thoi_gian": "Mùa Đông (Tháng 11-1), giờ Tý (23h-1h)"
    },
    
    "Ly": {
        "so_luong": "2, 3, 7, 9 (số lẻ, số sáng)",
        "so_tien": "Trung bình đến cao, thu nhập từ văn hóa/nghệ thuật",
        "gioi_tinh": "Nữ, con gái giữa, thiếu nữ",
        "tuoi_tac": "Trẻ, thanh niên (15-30 tuổi)",
        "ngoai_hinh": "Đẹp, rực rỡ, mắt to, da trắng hồng",
        "tinh_cach": "Sáng sủa, thông minh, nóng nảy, văn minh",
        "nghe_nghiep": "Văn nghệ sĩ, giáo viên, nhà văn, họa sĩ",
        "vat_the": "Lửa, đèn, sách vở, văn thư, điện tử",
        "dong_vat": "Chim phượng, rùa, cua, chim hót",
        "mau_sac": "Đỏ, tím, cam",
        "huong": "Nam",
        "thoi_gian": "Mùa Hè (Tháng 5-7), giờ Ngọ (11h-13h)"
    },
    
    "Cấn": {
        "so_luong": "5, 7, 10 (số dừng, số cuối)",
        "so_tien": "Ít, tích lũy chậm, giữ được của",
        "gioi_tinh": "Nam, con trai út, thiếu niên",
        "tuoi_tac": "Trẻ, thiếu niên (10-20 tuổi)",
        "ngoai_hinh": "Thấp, chắc nịch, da vàng",
        "tinh_cach": "Bảo thủ, cố chấp, trung thực, giữ gìn",
        "nghe_nghiep": "Người giữ của, bảo vệ, kho bạc, nhà sư",
        "vat_the": "Núi, đá, nhà cửa, kho tàng, tường",
        "dong_vat": "Chó, chuột, hổ",
        "mau_sac": "Vàng, nâu, xám",
        "huong": "Đông Bắc",
        "thoi_gian": "Mùa Xuân đầu (Tháng 1-2), giờ Dần-Mão (3h-7h)"
    },
    
    "Đoài": {
        "so_luong": "2, 4, 9 (số vui, số nói)",
        "so_tien": "Trung bình, thu nhập từ giao tiếp/bán hàng",
        "gioi_tinh": "Nữ, con gái út, thiếu nữ",
        "tuoi_tac": "Trẻ, thiếu nữ (12-25 tuổi)",
        "ngoai_hinh": "Xinh đẹp, vui vẻ, miệng đẹp, da trắng",
        "tinh_cach": "Vui vẻ, hòa đồng, hay nói, thuyết phục",
        "nghe_nghiep": "Ca sĩ, diễn viên, MC, nhân viên bán hàng",
        "vat_the": "Trạch, ao, miệng, lời nói, kim loại nhỏ",
        "dong_vat": "Dê, cá, chim hót",
        "mau_sac": "Trắng, bạc",
        "huong": "Tây",
        "thoi_gian": "Mùa Thu (Tháng 8-9), giờ Dậu (17h-19h)"
    }
}


def tien_doan_cu_the_mai_hoa(ket_qua_qua, chu_de="Tổng Quát"):
    """
    Tiên đoán cụ thể từ Mai Hoa: Số lượng, Số tiền, Trai/Gái, Già/Trẻ, Vật gì
    
    Args:
        ket_qua_qua: Kết quả từ tinh_qua_theo_thoi_gian()
        chu_de: Chủ đề cần tiên đoán
    
    Returns:
        Dict chứa các tiên đoán cụ thể
    """
    
    qua_thuong = ket_qua_qua['qua_thuong']
    qua_ha = ket_qua_qua['qua_ha']
    ban_qua = ket_qua_qua['ban_qua']
    qua_bien = ket_qua_qua['qua_bien']
    hao_dong = ket_qua_qua['hao_dong']
    
    # Lấy thông tin tượng số
    thuong_tuong = BAT_QUAI_TUONG_SO_CHI_TIET.get(qua_thuong['ten'], {})
    ha_tuong = BAT_QUAI_TUONG_SO_CHI_TIET.get(qua_ha['ten'], {})
    
    tien_doan = {
        "so_luong": "",
        "so_tien": "",
        "gioi_tinh": "",
        "tuoi_tac": "",
        "ngoai_hinh": "",
        "tinh_cach": "",
        "nghe_nghiep": "",
        "vat_the": "",
        "thoi_gian": ""
    }
    
    # TIÊN ĐOÁN SỐ LƯỢNG
    so_thuong = thuong_tuong.get("so_luong", "")
    so_ha = ha_tuong.get("so_luong", "")
    tien_doan["so_luong"] = f"""
📊 SỐ LƯỢNG:
• Thượng Quái ({qua_thuong['ten']}): {so_thuong}
• Hạ Quái ({qua_ha['ten']}): {so_ha}
• Hào Động: Hào {hao_dong} → Số {hao_dong} có ý nghĩa đặc biệt
• Tổng hợp: Nếu hỏi số lượng, có thể là {so_thuong.split(',')[0].strip()} hoặc {so_ha.split(',')[0].strip()}
"""
    
    # TIÊN ĐOÁN SỐ TIỀN
    tien_thuong = thuong_tuong.get("so_tien", "")
    tien_ha = ha_tuong.get("so_tien", "")
    tien_doan["so_tien"] = f"""
💰 SỐ TIỀN:
• Thượng Quái ({qua_thuong['ten']}): {tien_thuong}
• Hạ Quái ({qua_ha['ten']}): {tien_ha}
• Xu hướng: Từ '{ban_qua['ten']}' → '{qua_bien['ten']}'
  - Nếu Quẻ Biến tốt hơn: Tiền sẽ tăng
  - Nếu Quẻ Biến xấu hơn: Tiền sẽ giảm
"""
    
    # TIÊN ĐOÁN GIỚI TÍNH & TUỔI TÁC
    gioi_thuong = thuong_tuong.get("gioi_tinh", "")
    gioi_ha = ha_tuong.get("gioi_tinh", "")
    tuoi_thuong = thuong_tuong.get("tuoi_tac", "")
    tuoi_ha = ha_tuong.get("tuoi_tac", "")
    
    tien_doan["gioi_tinh"] = f"""
👤 GIỚI TÍNH:
• Thượng Quái ({qua_thuong['ten']}): {gioi_thuong}
• Hạ Quái ({qua_ha['ten']}): {gioi_ha}
• Kết luận: Nếu hỏi về người, có thể là {gioi_thuong.split(',')[0].strip()}
"""
    
    tien_doan["tuoi_tac"] = f"""
👴👵 TUỔI TÁC:
• Thượng Quái ({qua_thuong['ten']}): {tuoi_thuong}
• Hạ Quái ({qua_ha['ten']}): {tuoi_ha}
• Kết luận: Người này khoảng {tuoi_thuong.split('(')[0].strip()}
"""
    
    # TIÊN ĐOÁN NGOẠI HÌNH & TÍNH CÁCH
    hinh_thuong = thuong_tuong.get("ngoai_hinh", "")
    hinh_ha = ha_tuong.get("ngoai_hinh", "")
    cach_thuong = thuong_tuong.get("tinh_cach", "")
    cach_ha = ha_tuong.get("tinh_cach", "")
    
    tien_doan["ngoai_hinh"] = f"""
🧍 NGOẠI HÌNH:
• Thượng Quái ({qua_thuong['ten']}): {hinh_thuong}
• Hạ Quái ({qua_ha['ten']}): {hinh_ha}
• Tổng hợp: {hinh_thuong.split(',')[0].strip()}, {hinh_ha.split(',')[1].strip() if ',' in hinh_ha else hinh_ha}
"""
    
    tien_doan["tinh_cach"] = f"""
💭 TÍNH CÁCH:
• Thượng Quái ({qua_thuong['ten']}): {cach_thuong}
• Hạ Quái ({qua_ha['ten']}): {cach_ha}
• Tổng hợp: Bề ngoài {cach_thuong.split(',')[0].strip()}, bên trong {cach_ha.split(',')[0].strip()}
"""
    
    # TIÊN ĐOÁN NGHỀ NGHIỆP & VẬT THỂ
    nghe_thuong = thuong_tuong.get("nghe_nghiep", "")
    nghe_ha = ha_tuong.get("nghe_nghiep", "")
    vat_thuong = thuong_tuong.get("vat_the", "")
    vat_ha = ha_tuong.get("vat_the", "")
    
    tien_doan["nghe_nghiep"] = f"""
💼 NGHỀ NGHIỆP:
• Thượng Quái ({qua_thuong['ten']}): {nghe_thuong}
• Hạ Quái ({qua_ha['ten']}): {nghe_ha}
• Kết luận: Có thể làm nghề {nghe_thuong.split(',')[0].strip()} hoặc {nghe_ha.split(',')[0].strip()}
"""
    
    tien_doan["vat_the"] = f"""
📦 VẬT THỂ (Nếu hỏi về đồ vật):
• Thượng Quái ({qua_thuong['ten']}): {vat_thuong}
• Hạ Quái ({qua_ha['ten']}): {vat_ha}
• Kết luận: Có thể là {vat_thuong.split(',')[0].strip()} hoặc {vat_ha.split(',')[0].strip()}
"""
    
    # TIÊN ĐOÁN THỜI GIAN
    tg_thuong = thuong_tuong.get("thoi_gian", "")
    tg_ha = ha_tuong.get("thoi_gian", "")
    
    # Tính số ngày/tháng dựa vào Hào Động và Bát Quái
    so_ngay = ""
    so_thang = ""
    so_nam = ""
    
    # Dựa vào Hào Động
    if hao_dong == 1:
        so_ngay = "1-3 ngày"
        so_thang = "Tháng 1 hoặc tháng đầu"
    elif hao_dong == 2:
        so_ngay = "2-7 ngày"
        so_thang = "Tháng 2 hoặc đầu quý"
    elif hao_dong == 3:
        so_ngay = "3-10 ngày"
        so_thang = "Tháng 3 hoặc giữa quý"
    elif hao_dong == 4:
        so_ngay = "1-2 tuần"
        so_thang = "Tháng 4 hoặc cuối quý"
    elif hao_dong == 5:
        so_ngay = "2-4 tuần"
        so_thang = "Tháng 5 hoặc giữa năm"
    else:  # hao_dong == 6
        so_ngay = "1-3 tháng"
        so_thang = "Tháng 6 hoặc cuối năm"
    
    # Dựa vào số của Thượng Quái và Hạ Quái
    so_thuong_num = qua_thuong['ten']
    so_ha_num = qua_ha['ten']
    
    # Map tên quẻ sang số
    qua_so_map = {
        "Càn": 1, "Đoài": 2, "Ly": 3, "Chấn": 4,
        "Tốn": 5, "Khảm": 6, "Cấn": 7, "Khôn": 8
    }
    
    so_thuong_val = qua_so_map.get(so_thuong_num, 1)
    so_ha_val = qua_so_map.get(so_ha_num, 1)
    
    # Tính số cụ thể
    so_cu_the = (so_thuong_val + so_ha_val + hao_dong) % 10
    if so_cu_the == 0:
        so_cu_the = 10
    
    tien_doan["thoi_gian"] = f"""
⏰ THỜI GIAN ỨNG NGHIỆM CỤ THỂ:

📅 THEO MÙA & GIỜ:
• Thượng Quái ({qua_thuong['ten']}): {tg_thuong}
• Hạ Quái ({qua_ha['ten']}): {tg_ha}

📊 THEO HÀO ĐỘNG (Hào {hao_dong}):
• Ngắn hạn: {so_ngay}
• Trung hạn: {so_thang}
• Dài hạn: {hao_dong} tháng hoặc {hao_dong} năm

🔢 SỐ CỤ THỂ:
• Số ngày: {so_cu_the} ngày, {so_thuong_val} ngày, hoặc {so_ha_val} ngày
• Số tháng: Tháng {so_thuong_val}, Tháng {so_ha_val}, hoặc Tháng {hao_dong}
• Số năm: Năm có chữ số {so_cu_the} (VD: 202{so_cu_the}, 203{so_cu_the})

📌 DỰ ĐOÁN CHÍNH XÁC NHẤT:
• Nếu hỏi sự việc gần: Khoảng {so_ngay}
• Nếu hỏi sự việc xa: Khoảng {hao_dong} tháng
• Thời điểm tốt nhất: {tg_thuong.split(',')[0].strip() if ',' in tg_thuong else tg_thuong}

💡 LƯU Ý:
- Thời gian có thể sớm hơn nếu có quý nhân giúp đỡ
- Thời gian có thể chậm hơn nếu gặp trở ngại
- Xem Quẻ Biến để biết xu hướng thay đổi
"""
    
    return tien_doan


# Test
if __name__ == "__main__":
    print("=== TEST TIÊN ĐOÁN CỤ THỂ MAI HOA ===\n")
    
    from datetime import datetime
    from mai_hoa_dich_so import tinh_qua_theo_thoi_gian
    
    now = datetime.now()
    ket_qua = tinh_qua_theo_thoi_gian(now.year, now.month, now.day, now.hour)
    
    tien_doan = tien_doan_cu_the_mai_hoa(ket_qua, "Kinh Doanh")
    
    print("📊 TIÊN ĐOÁN CỤ THỂ:")
    for key, value in tien_doan.items():
        print(value)
        print()
    
    print("\n✅ Test hoàn thành!")
