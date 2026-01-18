import datetime
import math

# --- HẰNG SỐ CƠ BẢN ---
CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

# 24 Tiết Khí (Ước lượng ngày bắt đầu)
TIET_KHI = [
    "Tiểu Hàn", "Đại Hàn", "Lập Xuân", "Vũ Thủy", "Kinh Trập", "Xuân Phân",
    "Thanh Minh", "Cốc Vũ", "Lập Hạ", "Tiểu Mãn", "Mang Chủng", "Hạ Chí",
    "Tiểu Thử", "Đại Thử", "Lập Thu", "Xử Thử", "Bạch Lộ", "Thu Phân",
    "Hàn Lộ", "Sương Giáng", "Lập Đông", "Tiểu Tuyết", "Đại Tuyết", "Đông Chí"
]

# Bảng tra Cục (Tiết Khí -> [Thượng Nguyên, Trung Nguyên, Hạ Nguyên])
# Dương Độn: Đông Chí -> Mang Chủng
# Âm Độn: Hạ Chí -> Đại Tuyết
BANG_CUC = {
    "Đông Chí": [1, 7, 4], "Tiểu Hàn": [2, 8, 5], "Đại Hàn": [3, 9, 6],
    "Lập Xuân": [8, 5, 2], "Vũ Thủy": [9, 6, 3], "Kinh Trập": [1, 7, 4],
    "Xuân Phân": [3, 9, 6], "Thanh Minh": [4, 1, 7], "Cốc Vũ": [5, 2, 8],
    "Lập Hạ": [4, 1, 7], "Tiểu Mãn": [5, 2, 8], "Mang Chủng": [6, 3, 9],
    "Hạ Chí": [9, 3, 6], "Tiểu Thử": [8, 2, 5], "Đại Thử": [7, 1, 4],
    "Lập Thu": [2, 5, 8], "Xử Thử": [1, 4, 7], "Bạch Lộ": [9, 3, 6],
    "Thu Phân": [7, 1, 4], "Hàn Lộ": [6, 9, 3], "Sương Giáng": [5, 8, 2],
    "Lập Đông": [6, 9, 3], "Tiểu Tuyết": [5, 8, 2], "Đại Tuyết": [4, 7, 1]
}

# Cửu Tinh (Thứ tự trên địa bàn cố định để tìm Trực Phù)
# 1:Bồng, 2:Nhuế, 3:Xung, 4:Phụ, 5:Cầm, 6:Tâm, 7:Trụ, 8:Nhậm, 9:Anh
THU_TU_SAO_DIA_BAN = {
    1: "Thiên Bồng", 2: "Thiên Nhuế", 3: "Thiên Xung", 4: "Thiên Phụ",
    5: "Thiên Cầm", 6: "Thiên Tâm", 7: "Thiên Trụ", 8: "Thiên Nhậm", 9: "Thiên Anh"
}

# Bát Môn (Thứ tự trên địa bàn cố định để tìm Trực Sử)
# 1:Hưu, 2:Tử, 3:Thương, 4:Đỗ, 5:Trung(Gửi 2), 6:Khai, 7:Kinh, 8:Sinh, 9:Cảnh
THU_TU_MON_DIA_BAN = {
    1: "Hưu", 2: "Tử", 3: "Thương", 4: "Đỗ", 
    6: "Khai", 7: "Kinh", 8: "Sinh", 9: "Cảnh"
}

def get_can_chi_ngay(dt):
    """Tính Can Chi Ngày. Chuyển ngày tại 23:00 theo quy tắc truyền thống."""
    # Quy tắc: Sau 23:00 (Giờ Tý) tính là ngày mới
    effective_dt = dt
    if dt.hour >= 23:
        effective_dt = dt + datetime.timedelta(days=1)
        
    # Mốc: 1/1/1900 là ngày Giáp Tuất (Can 0, Chi 10)
    base_date = datetime.datetime(1900, 1, 1)
    days_diff = (effective_dt.date() - base_date.date()).days
    
    can_index = (0 + days_diff) % 10
    chi_index = (10 + days_diff) % 12
    
    return CAN[can_index], CHI[chi_index]

def get_can_chi_gio(dt, can_ngay):
    """Tính Can Chi Giờ."""
    # Chi Giờ
    gio = dt.hour
    chi_index = int((gio + 1) / 2) % 12
    chi_gio = CHI[chi_index]
    
    # Can Giờ (Dựa vào Can Ngày - Ngũ Hổ Độn/Ngũ Thử Độn)
    # Giáp/Kỷ -> Giáp Tý
    # Ất/Canh -> Bính Tý
    # Bính/Tân -> Mậu Tý
    # Đinh/Nhâm -> Canh Tý
    # Mậu/Quý -> Nhâm Tý
    
    can_ngay_index = CAN.index(can_ngay)
    start_can_index = (can_ngay_index % 5) * 2
    can_gio_index = (start_can_index + chi_index) % 10
    
    return CAN[can_gio_index], CHI[chi_index]

def get_tiet_khi(dt):
    """Xác định Tiết Khí (Ước lượng)."""
    # Đây là ước lượng đơn giản, thực tế cần thuật toán thiên văn chính xác hơn
    # Tuy nhiên với mục đích ứng dụng cơ bản, ta dùng ngày cố định trong tháng
    day = dt.day
    month = dt.month
    
    # Dữ liệu ngày bắt đầu tiết khí (xấp xỉ)
    tiet_khi_dates = [
        (1, 5, "Tiểu Hàn"), (1, 20, "Đại Hàn"),
        (2, 4, "Lập Xuân"), (2, 19, "Vũ Thủy"),
        (3, 5, "Kinh Trập"), (3, 20, "Xuân Phân"),
        (4, 4, "Thanh Minh"), (4, 20, "Cốc Vũ"),
        (5, 5, "Lập Hạ"), (5, 21, "Tiểu Mãn"),
        (6, 5, "Mang Chủng"), (6, 21, "Hạ Chí"),
        (7, 7, "Tiểu Thử"), (7, 22, "Đại Thử"),
        (8, 7, "Lập Thu"), (8, 23, "Xử Thử"),
        (9, 7, "Bạch Lộ"), (9, 23, "Thu Phân"),
        (10, 8, "Hàn Lộ"), (10, 23, "Sương Giáng"),
        (11, 7, "Lập Đông"), (11, 22, "Tiểu Tuyết"),
        (12, 7, "Đại Tuyết"), (12, 21, "Đông Chí")
    ]
    
    current_tiet = "Đông Chí" # Mặc định cuối năm trước
    for m, d, name in tiet_khi_dates:
        if month > m or (month == m and day >= d):
            current_tiet = name
        else:
            break
            
    return current_tiet

def get_can_chi_nam(dt):
    """Tính Can Chi Năm (Thay đổi tại Lập Xuân)."""
    year = dt.year
    # Nếu trước Lập Xuân (thường là ngày 4/2), tính theo năm trước
    if dt.month < 2 or (dt.month == 2 and dt.day < 4):
        year -= 1
        
    can_idx = (year - 4) % 10
    chi_idx = (year - 4) % 12
    return CAN[can_idx], CHI[chi_idx]

def get_can_chi_thang(dt, can_nam):
    """Tính Can Chi Tháng dựa trên Tiết Khí."""
    tiet = get_tiet_khi(dt)
    
    # Map Tiết Khí sang Chi Tháng (Dần=2, Mão=3, ...)
    tiet_to_chi = {
        "Lập Xuân": 2, "Vũ Thủy": 2,
        "Kinh Trập": 3, "Xuân Phân": 3,
        "Thanh Minh": 4, "Cốc Vũ": 4,
        "Lập Hạ": 5, "Tiểu Mãn": 5,
        "Mang Chủng": 6, "Hạ Chí": 6,
        "Tiểu Thử": 7, "Đại Thử": 7,
        "Lập Thu": 8, "Xử Thử": 8,
        "Bạch Lộ": 9, "Thu Phân": 9,
        "Hàn Lộ": 10, "Sương Giáng": 10,
        "Lập Đông": 11, "Tiểu Tuyết": 11,
        "Đại Tuyết": 0, "Đông Chí": 0,
        "Tiểu Hàn": 1, "Đại Hàn": 1
    }
    
    chi_idx = tiet_to_chi.get(tiet, 2)
    
    # Can Tháng dựa vào Can Năm ÂM LỊCH (Đã điều chỉnh tại Lập Xuân)
    # Quy tắc: Theo truyền thống, tháng 1 dương lich (trước Lập Xuân) đi theo Can Năm cũ
    # Ất (Năm âm lịch hiện tại) -> Giáp Tý, Ất Sửu... -> Jan 10 là tháng Mậu Tý
    can_nam_idx = CAN.index(can_nam)
    start_can_idx = (can_nam_idx % 5) * 2 + 2 
    
    # Khoangan cach tu thang Dan (idx 2) den thang hien tai
    can_idx = (start_can_idx + (chi_idx - 2) % 12) % 10
    
    return CAN[can_idx], CHI[chi_idx]

def get_nguyen(can_ngay, chi_ngay):
    """Xác định Tam Nguyên (Thượng, Trung, Hạ) dựa vào Can Chi Ngày."""
    # Quy tắc:
    # Giáp Tý, Giáp Ngọ, Kỷ Mão, Kỷ Dậu -> Thượng Nguyên
    # Giáp Dần, Giáp Thân, Kỷ Tị, Kỷ Hợi -> Trung Nguyên
    # Giáp Thìn, Giáp Tuất, Kỷ Sửu, Kỷ Mùi -> Hạ Nguyên
    # Cách tính nhanh: (Chi - Can) % 12 ... 
    # Đơn giản nhất: Tra bảng Lục Thập Hoa Giáp chia 3 nhóm 5 ngày (1 Phù Đầu quản 15 ngày?? Không, 1 Nguyên 5 ngày)
    
    # Tìm Phù Đầu (Ngày Giáp/Kỷ gần nhất)
    # Nguyên lý: Tam Nguyên dựa trên Phù Đầu. 
    # Mỗi Cục có 3 Nguyên. 
    # Phù đầu Giáp/Kỷ Tý,Ngọ,Mão,Dậu -> Thượng Nguyên
    # Phù đầu Giáp/Kỷ Dần,Thân,Tị,Hợi -> Trung Nguyên
    # Phù đầu Giáp/Kỷ Thìn,Tuất,Sửu,Mùi -> Hạ Nguyên
    
    can_idx = CAN.index(can_ngay)
    chi_idx = CHI.index(chi_ngay)
    
    # Khoảng cách đến Giáp/Kỷ gần nhất (Giáp=0, Kỷ=5)
    if can_idx < 5:
        offset = can_idx
        phu_dau_can = "Giáp"
    else:
        offset = can_idx - 5
        phu_dau_can = "Kỷ"
        
    # Chi của Phù Đầu
    phu_dau_chi_idx = (chi_idx - offset) % 12
    phu_dau_chi = CHI[phu_dau_chi_idx]
    
    pair = phu_dau_can + " " + phu_dau_chi
    
    thuong_nguyen = ["Giáp Tý", "Giáp Ngọ", "Kỷ Mão", "Kỷ Dậu"]
    trung_nguyen = ["Giáp Dần", "Giáp Thân", "Kỷ Tị", "Kỷ Hợi"]
    ha_nguyen = ["Giáp Thìn", "Giáp Tuất", "Kỷ Sửu", "Kỷ Mùi"]
    
    if pair in thuong_nguyen: return 0 # Index trong mảng [Thượng, Trung, Hạ]
    if pair in trung_nguyen: return 1
    if pair in ha_nguyen: return 2
    
    return 0 # Fallback

def calculate_qmdg_params(dt):
    """Tính toán toàn bộ thông số QMDG cho thời điểm dt."""
    
    # 1. Can Chi Năm/Tháng/Ngày/Giờ
    can_nam, chi_nam = get_can_chi_nam(dt)
    can_ngay, chi_ngay = get_can_chi_ngay(dt)
    can_thang, chi_thang = get_can_chi_thang(dt, can_nam)
    can_gio, chi_gio = get_can_chi_gio(dt, can_ngay)
    
    # 2. Tiết Khí & Nguyên
    tiet_khi = get_tiet_khi(dt)
    nguyen_idx = get_nguyen(can_ngay, chi_ngay)
    
    # 3. Cục
    cuc_list = BANG_CUC.get(tiet_khi, [1, 1, 1])
    cuc_so = cuc_list[nguyen_idx]
    
    # Xác định Âm/Dương Độn
    # Dương: Đông Chí -> Mang Chủng
    duong_don_tiets = [
        "Đông Chí", "Tiểu Hàn", "Đại Hàn", "Lập Xuân", "Vũ Thủy", "Kinh Trập",
        "Xuân Phân", "Thanh Minh", "Cốc Vũ", "Lập Hạ", "Tiểu Mãn", "Mang Chủng"
    ]
    is_duong_don = tiet_khi in duong_don_tiets
    
    # 3.5 Điều chỉnh dt cho các tính toán tiếp theo nếu là giờ Tý đêm
    calc_dt = dt
    if dt.hour >= 23:
        calc_dt = dt + datetime.timedelta(days=1)
    
    # 4. Tìm Tuần Thủ (Của Giờ)
    # Tuần Thủ là Can Giáp của tuần đó (Giáp Tý, Giáp Tuất, ...)
    # Can Giờ - Chi Giờ
    can_gio_idx = CAN.index(can_gio)
    chi_gio_idx = CHI.index(chi_gio)
    diff = (can_gio_idx - chi_gio_idx) % 12
    if diff < 0: diff += 12
    
    # Mapping diff -> Tuần Thủ (Lục Nghi tương ứng)
    # 0 (Tý-Tý=0): Giáp Tý (Mậu)
    # 10 (Tuất-Giáp=-2->10): Giáp Tuất (Kỷ)
    # 8 (Thân-Giáp=-4->8): Giáp Thân (Canh)
    # 6 (Ngọ-Giáp=-6->6): Giáp Ngọ (Tân)
    # 4 (Thìn-Giáp=-8->4): Giáp Thìn (Nhâm)
    # 2 (Dần-Giáp=-10->2): Giáp Dần (Quý)
    
    tuan_thu_map = {
        0: "Mậu", 2: "Kỷ", 4: "Canh", 6: "Tân", 8: "Nhâm", 10: "Quý"
    }
    luc_nghi_tuan_thu = tuan_thu_map.get(diff, "Mậu")
    
    # 5. Tìm Trực Phù & Trực Sử
    # a. Tìm cung của Tuần Thủ trên Địa Bàn (Địa Bàn an theo Cục)
    # Địa bàn: Mậu, Kỷ, Canh, Tân, Nhâm, Quý, Đinh, Bính, Ất (Dương)
    
    # An Lục Nghi theo Cục (Địa Bàn)
    # Dương Độn: Mậu khởi tại Cung Cục, đi thuận (1-9)
    # Âm Độn: Mậu khởi tại Cung Cục, đi nghịch (9-1)
    
    # Thứ tự Lục Nghi: Mậu, Kỷ, Canh, Tân, Nhâm, Quý, Đinh, Bính, Ất
    LUC_NGHI_ORDER = ["Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý", "Đinh", "Bính", "Ất"]
    
    dia_ban = {}
    curr = cuc_so
    for nghi in LUC_NGHI_ORDER:
        dia_ban[curr] = nghi
        if is_duong_don:
            curr += 1
            if curr > 9: curr = 1
        else:
            curr -= 1
            if curr < 1: curr = 9
            
    # Tìm cung của Tuần Thủ
    cung_tuan_thu = 0
    for c, nghi in dia_ban.items():
        if nghi == luc_nghi_tuan_thu:
            cung_tuan_thu = c
            break
            
    # Trực Phù là Sao tại cung Tuần Thủ (Địa Bàn gốc)
    # Trực Sử là Môn tại cung Tuần Thủ (Địa Bàn gốc)
    truc_phu = THU_TU_SAO_DIA_BAN.get(cung_tuan_thu, "Thiên Cầm") # Nếu 5 thì là Thiên Cầm
    
    # Xử lý Trực Sử (Nếu cung 5 thì gửi cung 2 - Tử Môn)
    cung_mon = cung_tuan_thu
    if cung_mon == 5: cung_mon = 2
    truc_su_raw = THU_TU_MON_DIA_BAN.get(cung_mon, "Tử")
    truc_su = truc_su_raw # Dạng "Hưu", "Sinh"
    
    return {
        "cuc": cuc_so,
        "truc_phu": truc_phu,
        "truc_su": truc_su,
        "can_nam": can_nam,
        "chi_nam": chi_nam,
        "can_thang": can_thang,
        "chi_thang": chi_thang,
        "can_ngay": can_ngay,
        "chi_ngay": chi_ngay,
        "can_gio": can_gio,
        "chi_gio": chi_gio,
        "tiet_khi": tiet_khi,
        "is_duong_don": is_duong_don
    }
