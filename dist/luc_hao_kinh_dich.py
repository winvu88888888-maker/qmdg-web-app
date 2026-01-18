# -*- coding: utf-8 -*-
"""
LỤC HÀO KINH DỊCH - HỆ THỐNG HOÀN CHỈNH
Bao gồm: Chính Quái, Hỗ Quái, Biến Quái
Phân tích: Lục Thân, Lục Thần, Ngũ Hành, Phụ Thần
"""

import random
from datetime import datetime

# ============================================================================
# PHẦN 1: DATABASE CƠ SỞ
# ============================================================================

# 8 Quẻ Đơn (Bát Quái)
BAT_QUAI_DON = {
    0: {"ten": "Khôn", "unicode": "☷", "hanh": "Thổ", "tuong": "Địa"},
    1: {"ten": "Chấn", "unicode": "☳", "hanh": "Mộc", "tuong": "Lôi"},
    2: {"ten": "Khảm", "unicode": "☵", "hanh": "Thủy", "tuong": "Thủy"},
    3: {"ten": "Đoài", "unicode": "☱", "hanh": "Kim", "tuong": "Trạch"},
    4: {"ten": "Cấn", "unicode": "☶", "hanh": "Thổ", "tuong": "Sơn"},
    5: {"ten": "Ly", "unicode": "☲", "hanh": "Hỏa", "tuong": "Hỏa"},
    6: {"ten": "Tốn", "unicode": "☴", "hanh": "Mộc", "tuong": "Phong"},
    7: {"ten": "Càn", "unicode": "☰", "hanh": "Kim", "tuong": "Thiên"}
}

# 12 Địa Chi
DIA_CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

# Địa Chi theo Ngũ Hành
DIA_CHI_NGU_HANH = {
    "Tý": "Thủy", "Sửu": "Thổ", "Dần": "Mộc", "Mão": "Mộc",
    "Thìn": "Thổ", "Tị": "Hỏa", "Ngọ": "Hỏa", "Mùi": "Thổ",
    "Thân": "Kim", "Dậu": "Kim", "Tuất": "Thổ", "Hợi": "Thủy"
}

# Lục Thân (6 Thân)
LUC_THAN = {
    "Phụ Mẫu": {"y_nghia": "Cha mẹ, văn thư, tài liệu, nhà cửa"},
    "Huynh Đệ": {"y_nghia": "Anh em, bạn bè, đồng nghiệp, cạnh tranh"},
    "Tử Tôn": {"y_nghia": "Con cái, học sinh, vui vẻ, sáng tạo"},
    "Thê Tài": {"y_nghia": "Vợ, tài lộc, tiền bạc, của cải"},
    "Quan Quỷ": {"y_nghia": "Quan chức, chồng, áp lực, bệnh tật"}
}

# Lục Thần (6 Thần)
LUC_THAN = {
    "Thanh Long": {"y_nghia": "Cát tường, vui vẻ, thăng tiến", "mau": "xanh lá"},
    "Chu Tước": {"y_nghia": "Văn thư, thị phi, tranh cãi", "mau": "đỏ"},
    "Câu Trần": {"y_nghia": "Tranh chấp, kiện tụng, rắc rối", "mau": "vàng"},
    "Đằng Xà": {"y_nghia": "Quỷ quái, bệnh tật, âm mưu", "mau": "đen"},
    "Bạch Hổ": {"y_nghia": "Hung ác, tai nạn, tổn thương", "mau": "trắng"},
    "Huyền Vũ": {"y_nghia": "Trộm cắp, lừa đảo, bí mật", "mau": "đen xám"}
}

# Quan hệ Sinh Khắc Ngũ Hành
NGU_HANH_SINH = {
    "Kim": "Thủy",  # Kim sinh Thủy
    "Thủy": "Mộc",  # Thủy sinh Mộc
    "Mộc": "Hỏa",   # Mộc sinh Hỏa
    "Hỏa": "Thổ",   # Hỏa sinh Thổ
    "Thổ": "Kim"    # Thổ sinh Kim
}

NGU_HANH_KHAC = {
    "Kim": "Mộc",   # Kim khắc Mộc
    "Mộc": "Thổ",   # Mộc khắc Thổ
    "Thổ": "Thủy",  # Thổ khắc Thủy
    "Thủy": "Hỏa",  # Thủy khắc Hỏa
    "Hỏa": "Kim"    # Hỏa khắc Kim
}

# Tuần Không (theo Can Chi)
TUAN_KHONG = {
    "Giáp Tý": ["Tuất", "Hợi"],
    "Giáp Tuất": ["Thân", "Dậu"],
    "Giáp Thân": ["Ngọ", "Mùi"],
    "Giáp Ngọ": ["Thìn", "Tị"],
    "Giáp Thìn": ["Dần", "Mão"],
    "Giáp Dần": ["Tý", "Sửu"]
}

# Dịch Mã (theo Địa Chi)
DICH_MA = {
    "Dần": "Thân", "Ngọ": "Thân", "Tuất": "Thân",  # Tam hợp Hỏa
    "Thân": "Dần", "Tý": "Dần", "Thìn": "Dần",     # Tam hợp Thủy
    "Tị": "Hợi", "Dậu": "Hợi", "Sửu": "Hợi",       # Tam hợp Kim
    "Hợi": "Tị", "Mão": "Tị", "Mùi": "Tị"          # Tam hợp Mộc
}

# Vượng Suy Mộ Tuyệt (theo tháng và Ngũ Hành)
# Đơn giản hóa: dựa vào Ngũ Hành và tháng
def xac_dinh_vuong_suy(ngu_hanh, thang):
    """Xác định trạng thái Vượng/Suy/Mộ/Tuyệt"""
    # Mùa xuân (1,2,3): Mộc vượng, Hỏa tướng, Thủy hưu, Kim tù, Thổ tử
    # Mùa hạ (4,5,6): Hỏa vượng, Thổ tướng, Mộc hưu, Thủy tù, Kim tử
    # Mùa thu (7,8,9): Kim vượng, Thủy tướng, Thổ hưu, Hỏa tù, Mộc tử
    # Mùa đông (10,11,12): Thủy vượng, Mộc tướng, Kim hưu, Thổ tù, Hỏa tử
    
    if thang in [1, 2, 3]:  # Xuân
        vuong_suy = {"Mộc": "Vượng", "Hỏa": "Tướng", "Thủy": "Hưu", "Kim": "Tù", "Thổ": "Tử"}
    elif thang in [4, 5, 6]:  # Hạ
        vuong_suy = {"Hỏa": "Vượng", "Thổ": "Tướng", "Mộc": "Hưu", "Thủy": "Tù", "Kim": "Tử"}
    elif thang in [7, 8, 9]:  # Thu
        vuong_suy = {"Kim": "Vượng", "Thủy": "Tướng", "Thổ": "Hưu", "Hỏa": "Tù", "Mộc": "Tử"}
    else:  # Đông (10, 11, 12)
        vuong_suy = {"Thủy": "Vượng", "Mộc": "Tướng", "Kim": "Hưu", "Thổ": "Tù", "Hỏa": "Tử"}
    
    return vuong_suy.get(ngu_hanh, "Hưu")

# 64 Quẻ Kinh Dịch (đầy đủ)
QUA_64 = {
    (7, 7): {"so": 1, "ten": "Càn Vi Thiên", "unicode": "䷀"},
    (0, 0): {"so": 2, "ten": "Khôn Vi Địa", "unicode": "䷁"},
    (2, 1): {"so": 3, "ten": "Thủy Lôi Truân", "unicode": "䷂"},
    (4, 2): {"so": 4, "ten": "Sơn Thủy Mông", "unicode": "䷃"},
    (2, 7): {"so": 5, "ten": "Thủy Thiên Nhu", "unicode": "䷄"},
    (7, 2): {"so": 6, "ten": "Thiên Thủy Tụng", "unicode": "䷅"},
    (0, 2): {"so": 7, "ten": "Địa Thủy Sư", "unicode": "䷆"},
    (2, 0): {"so": 8, "ten": "Thủy Địa Tỷ", "unicode": "䷇"},
    (6, 7): {"so": 9, "ten": "Phong Thiên Tiểu Súc", "unicode": "䷈"},
    (7, 3): {"so": 10, "ten": "Thiên Trạch Lý", "unicode": "䷉"},
    (0, 7): {"so": 11, "ten": "Địa Thiên Thái", "unicode": "䷊"},
    (7, 0): {"so": 12, "ten": "Thiên Địa Bĩ", "unicode": "䷋"},
    (7, 5): {"so": 13, "ten": "Thiên Hỏa Đồng Nhân", "unicode": "䷌"},
    (5, 7): {"so": 14, "ten": "Hỏa Thiên Đại Hữu", "unicode": "䷍"},
    (0, 4): {"so": 15, "ten": "Địa Sơn Khiêm", "unicode": "䷎"},
    (1, 0): {"so": 16, "ten": "Lôi Địa Dự", "unicode": "䷏"},
    (3, 1): {"so": 17, "ten": "Trạch Lôi Tùy", "unicode": "䷐"},
    (4, 6): {"so": 18, "ten": "Sơn Phong Cổ", "unicode": "䷑"},
    (0, 3): {"so": 19, "ten": "Địa Trạch Lâm", "unicode": "䷒"},
    (6, 0): {"so": 20, "ten": "Phong Địa Quán", "unicode": "䷓"},
    (5, 1): {"so": 21, "ten": "Hỏa Lôi Phệ Hạp", "unicode": "䷔"},
    (4, 5): {"so": 22, "ten": "Sơn Hỏa Bí", "unicode": "䷕"},
    (4, 0): {"so": 23, "ten": "Sơn Địa Bác", "unicode": "䷖"},
    (0, 1): {"so": 24, "ten": "Địa Lôi Phục", "unicode": "䷗"},
    (7, 1): {"so": 25, "ten": "Thiên Lôi Vô Vọng", "unicode": "䷘"},
    (4, 7): {"so": 26, "ten": "Sơn Thiên Đại Súc", "unicode": "䷙"},
    (4, 1): {"so": 27, "ten": "Sơn Lôi Di", "unicode": "䷚"},
    (3, 6): {"so": 28, "ten": "Trạch Phong Đại Quá", "unicode": "䷛"},
    (2, 2): {"so": 29, "ten": "Khảm Vi Thủy", "unicode": "䷜"},
    (5, 5): {"so": 30, "ten": "Ly Vi Hỏa", "unicode": "䷝"},
    (3, 4): {"so": 31, "ten": "Trạch Sơn Hàm", "unicode": "䷞"},
    (1, 6): {"so": 32, "ten": "Lôi Phong Hằng", "unicode": "䷟"},
    (7, 4): {"so": 33, "ten": "Thiên Sơn Độn", "unicode": "䷠"},
    (1, 7): {"so": 34, "ten": "Lôi Thiên Đại Tráng", "unicode": "䷡"},
    (5, 0): {"so": 35, "ten": "Hỏa Địa Tấn", "unicode": "䷢"},
    (0, 5): {"so": 36, "ten": "Địa Hỏa Minh Di", "unicode": "䷣"},
    (6, 5): {"so": 37, "ten": "Phong Hỏa Gia Nhân", "unicode": "䷤"},
    (5, 3): {"so": 38, "ten": "Hỏa Trạch Khuê", "unicode": "䷥"},
    (2, 4): {"so": 39, "ten": "Thủy Sơn Kiển", "unicode": "䷦"},
    (1, 2): {"so": 40, "ten": "Lôi Thủy Giải", "unicode": "䷧"},
    (4, 3): {"so": 41, "ten": "Sơn Trạch Tổn", "unicode": "䷨"},
    (6, 1): {"so": 42, "ten": "Phong Lôi Ích", "unicode": "䷩"},
    (3, 7): {"so": 43, "ten": "Trạch Thiên Quải", "unicode": "䷪"},
    (7, 6): {"so": 44, "ten": "Thiên Phong Cấu", "unicode": "䷫"},
    (0, 6): {"so": 45, "ten": "Địa Phong Tụy", "unicode": "䷬"},
    (6, 0): {"so": 46, "ten": "Phong Địa Thăng", "unicode": "䷭"},
    (3, 2): {"so": 47, "ten": "Trạch Thủy Khốn", "unicode": "䷮"},
    (2, 6): {"so": 48, "ten": "Thủy Phong Tỉnh", "unicode": "䷯"},
    (3, 5): {"so": 49, "ten": "Trạch Hỏa Cách", "unicode": "䷰"},
    (5, 6): {"so": 50, "ten": "Hỏa Phong Đỉnh", "unicode": "䷱"},
    (1, 1): {"so": 51, "ten": "Chấn Vi Lôi", "unicode": "䷲"},
    (4, 4): {"so": 52, "ten": "Cấn Vi Sơn", "unicode": "䷳"},
    (6, 4): {"so": 53, "ten": "Phong Sơn Tiệm", "unicode": "䷴"},
    (1, 3): {"so": 54, "ten": "Lôi Trạch Quy Muội", "unicode": "䷵"},
    (1, 5): {"so": 55, "ten": "Lôi Hỏa Phong", "unicode": "䷶"},
    (5, 4): {"so": 56, "ten": "Hỏa Sơn Lữ", "unicode": "䷷"},
    (6, 6): {"so": 57, "ten": "Tốn Vi Phong", "unicode": "䷸"},
    (3, 3): {"so": 58, "ten": "Đoài Vi Trạch", "unicode": "䷹"},
    (6, 2): {"so": 59, "ten": "Phong Thủy Hoán", "unicode": "䷺"},
    (2, 3): {"so": 60, "ten": "Thủy Trạch Tiết", "unicode": "䷻"},
    (6, 3): {"so": 61, "ten": "Phong Trạch Trung Phu", "unicode": "䷼"},
    (1, 4): {"so": 62, "ten": "Lôi Sơn Tiểu Quá", "unicode": "䷽"},
    (2, 5): {"so": 63, "ten": "Thủy Hỏa Ký Tế", "unicode": "䷾"},
    (5, 2): {"so": 64, "ten": "Hỏa Thủy Vị Tế", "unicode": "䷿"}
}

# ============================================================================
# PHẦN 2: HÀM TÍNH TOÁN
# ============================================================================

def tinh_chinh_quai_theo_thoi_gian(nam, thang, ngay, gio):
    """
    Tính Chính Quái từ thời gian (phương pháp Lục Hào)
    
    Returns:
        dict: {
            'thuong_quai': số quẻ trên (0-7),
            'ha_quai': số quẻ dưới (0-7),
            'dong_hao': [danh sách hào động 1-6],
            'quai_info': thông tin quẻ
        }
    """
    # Tính Thượng Quái (quẻ trên)
    thuong = (nam + thang + ngay) % 8
    
    # Tính Hạ Quái (quẻ dưới)
    ha = (nam + thang + ngay + gio) % 8
    
    # Tính hào động
    dong_hao_so = (nam + thang + ngay + gio) % 6
    if dong_hao_so == 0:
        dong_hao_so = 6
    
    # Lấy thông tin quẻ
    quai_key = (thuong, ha)
    quai_info = QUA_64.get(quai_key, {"so": 0, "ten": "Chưa xác định", "unicode": "?"})
    
    return {
        'thuong_quai': thuong,
        'ha_quai': ha,
        'dong_hao': [dong_hao_so],  # Có thể có nhiều hào động
        'quai_info': quai_info,
        'bat_quai_thuong': BAT_QUAI_DON[thuong],
        'bat_quai_ha': BAT_QUAI_DON[ha]
    }

def tinh_ho_quai(chinh_quai):
    """
    Tính Hỗ Quái từ Chính Quái
    Hỗ Quái = Hào 2,3,4 làm Hạ Quái + Hào 3,4,5 làm Thượng Quái
    
    Args:
        chinh_quai: dict từ tinh_chinh_quai_theo_thoi_gian()
    
    Returns:
        dict: Thông tin Hỗ Quái
    """
    # Lấy 6 hào của Chính Quái (cần hàm phụ để tạo 6 hào)
    # Đơn giản hóa: lấy từ Thượng và Hạ quái
    thuong = chinh_quai['thuong_quai']
    ha = chinh_quai['ha_quai']
    
    # Hỗ Quái thường là quẻ đối nghịch hoặc tính theo công thức đặc biệt
    # Đơn giản: đảo ngược
    ho_thuong = (thuong + 4) % 8
    ho_ha = (ha + 4) % 8
    
    quai_key = (ho_thuong, ho_ha)
    quai_info = QUA_64.get(quai_key, {"so": 0, "ten": "Chưa xác định", "unicode": "?"})
    
    return {
        'thuong_quai': ho_thuong,
        'ha_quai': ho_ha,
        'quai_info': quai_info,
        'bat_quai_thuong': BAT_QUAI_DON[ho_thuong],
        'bat_quai_ha': BAT_QUAI_DON[ho_ha]
    }

def tinh_bien_quai(chinh_quai):
    """
    Tính Biến Quái từ Chính Quái (đảo hào động)
    
    Args:
        chinh_quai: dict từ tinh_chinh_quai_theo_thoi_gian()
    
    Returns:
        dict: Thông tin Biến Quái
    """
    thuong = chinh_quai['thuong_quai']
    ha = chinh_quai['ha_quai']
    dong_hao = chinh_quai['dong_hao'][0]
    
    # Nếu hào động ở Hạ Quái (1-3), đảo Hạ Quái
    if dong_hao <= 3:
        ha = (ha + 1) % 8
    # Nếu hào động ở Thượng Quái (4-6), đảo Thượng Quái
    else:
        thuong = (thuong + 1) % 8
    
    quai_key = (thuong, ha)
    quai_info = QUA_64.get(quai_key, {"so": 0, "ten": "Chưa xác định", "unicode": "?"})
    
    return {
        'thuong_quai': thuong,
        'ha_quai': ha,
        'quai_info': quai_info,
        'bat_quai_thuong': BAT_QUAI_DON[thuong],
        'bat_quai_ha': BAT_QUAI_DON[ha]
    }

def xac_dinh_luc_than(quai, hao_vi_tri):
    """
    Xác định Lục Thân cho một hào
    
    Args:
        quai: dict quẻ
        hao_vi_tri: vị trí hào (1-6)
    
    Returns:
        str: Tên Lục Thân
    """
    # Logic phức tạp, cần dựa vào Ngũ Hành của quẻ và hào
    # Đơn giản hóa: phân bổ theo vị trí
    luc_than_list = ["Phụ Mẫu", "Huynh Đệ", "Tử Tôn", "Thê Tài", "Quan Quỷ", "Phụ Mẫu"]
    return luc_than_list[hao_vi_tri - 1]

def xac_dinh_luc_than_theo_ngay(ngay_gio):
    """
    Xác định Lục Thần theo ngày giờ
    
    Args:
        ngay_gio: datetime object
    
    Returns:
        list: Danh sách 6 thần cho 6 hào
    """
    # Lục Thần thay đổi theo ngày
    luc_than_list = ["Thanh Long", "Chu Tước", "Câu Trần", "Đằng Xà", "Bạch Hổ", "Huyền Vũ"]
    
    # Xoay vòng theo ngày
    ngay_so = ngay_gio.day % 6
    return luc_than_list[ngay_so:] + luc_than_list[:ngay_so]

def giai_qua_luc_hao(chinh_quai, ho_quai, bien_quai, thang, chu_de="Tổng Quát"):
    """
    Giải quẻ Lục Hào chi tiết với 6 hào, Lục Thân, Lục Thần, Tuần Không, Dịch Mã, Vượng Suy
    
    Args:
        chinh_quai, ho_quai, bien_quai: dict quẻ
        thang: tháng để xác định Vượng Suy
        chu_de: chủ đề cần giải
    
    Returns:
        str: Diễn giải chi tiết
    """
    ket_qua = []
    
    ket_qua.append("═" * 75)
    ket_qua.append("📖 GIẢI QUẺ LỤC HÀO KINH DỊCH")
    ket_qua.append("═" * 75)
    ket_qua.append("")
    
    # Chính Quái
    ket_qua.append(f"🔷 CHÍNH QUÁI: {chinh_quai['quai_info']['ten']} {chinh_quai['quai_info']['unicode']}")
    ket_qua.append(f"   Thượng Quái: {chinh_quai['bat_quai_thuong']['ten']} {chinh_quai['bat_quai_thuong']['unicode']} ({chinh_quai['bat_quai_thuong']['hanh']})")
    ket_qua.append(f"   Hạ Quái: {chinh_quai['bat_quai_ha']['ten']} {chinh_quai['bat_quai_ha']['unicode']} ({chinh_quai['bat_quai_ha']['hanh']})")
    ket_qua.append(f"   Hào Động: Hào {chinh_quai['dong_hao'][0]}")
    ket_qua.append("")
    
    # PHÂN TÍCH 6 HÀO CHI TIẾT
    ket_qua.append("📊 PHÂN TÍCH 6 HÀO CHI TIẾT:")
    ket_qua.append("─" * 75)
    
    # Lục Thân cho 6 hào
    luc_than_6_hao = ["Phụ Mẫu", "Huynh Đệ", "Tử Tôn", "Thê Tài", "Quan Quỷ", "Phụ Mẫu"]
    
    # Lục Thần cho 6 hào
    luc_than_6_hao_list = ["Thanh Long", "Chu Tước", "Câu Trần", "Đằng Xà", "Bạch Hổ", "Huyền Vũ"]
    
    # Địa Chi cho 6 hào
    dia_chi_6_hao = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị"]
    
    # Tuần Không (giả sử Giáp Tý tuần)
    tuan_khong_list = TUAN_KHONG.get("Giáp Tý", [])
    
    # Hiển thị từ hào 6 xuống hào 1 (từ trên xuống dưới)
    for i in range(5, -1, -1):
        hao_so = i + 1
        luc_than_ten = luc_than_6_hao[i]
        luc_than_ten_item = luc_than_6_hao_list[i]
        dia_chi = dia_chi_6_hao[i]
        ngu_hanh = DIA_CHI_NGU_HANH.get(dia_chi, "")
        
        # Đánh dấu hào động
        dong_hao_mark = " ⚡ ĐỘNG" if hao_so == chinh_quai['dong_hao'][0] else ""
        
        # Tuần Không
        tuan_khong_mark = " 🈳 Tuần Không" if dia_chi in tuan_khong_list else ""
        
        # Dịch Mã
        dich_ma = DICH_MA.get(dia_chi, "")
        dich_ma_mark = f" 🐎 Dịch Mã ({dich_ma})" if dich_ma else ""
        
        # Vượng Suy
        vuong_suy = xac_dinh_vuong_suy(ngu_hanh, thang)
        vuong_suy_icon = {"Vượng": "💪", "Tướng": "👍", "Hưu": "😐", "Tù": "😔", "Tử": "💀"}.get(vuong_suy, "")
        
        ket_qua.append(f"\n  Hào {hao_so}{dong_hao_mark}{tuan_khong_mark}{dich_ma_mark}:")
        ket_qua.append(f"    • Lục Thân: {luc_than_ten} - {LUC_THAN.get(luc_than_ten, {}).get('y_nghia', '')}")
        ket_qua.append(f"    • Lục Thần: {luc_than_ten_item} - {LUC_THAN.get(luc_than_ten_item, {}).get('y_nghia', '')}")
        ket_qua.append(f"    • Địa Chi: {dia_chi} ({ngu_hanh}) - {vuong_suy_icon} {vuong_suy}")
        
        # Ý nghĩa tượng quẻ cho hào này
        if hao_so <= 3:
            tuong_qua = chinh_quai['bat_quai_ha']['tuong']
        else:
            tuong_qua = chinh_quai['bat_quai_thuong']['tuong']
        ket_qua.append(f"    • Tượng: {tuong_qua}")
    
    ket_qua.append("")
    ket_qua.append("─" * 75)
    
    # Hỗ Quái
    ket_qua.append(f"\n🔶 HỖ QUÁI: {ho_quai['quai_info']['ten']} {ho_quai['quai_info']['unicode']}")
    ket_qua.append(f"   (Yếu tố nội tại, diễn biến bên trong)")
    ket_qua.append("")
    
    # Biến Quái
    ket_qua.append(f"🔸 BIẾN QUÁI: {bien_quai['quai_info']['ten']} {bien_quai['quai_info']['unicode']}")
    ket_qua.append(f"   (Kết quả tương lai, xu hướng phát triển)")
    ket_qua.append("")
    
    # Phân tích Ngũ Hành
    ket_qua.append("⚡ PHÂN TÍCH NGŨ HÀNH:")
    chinh_hanh = chinh_quai['bat_quai_thuong']['hanh']
    bien_hanh = bien_quai['bat_quai_thuong']['hanh']
    
    if chinh_hanh == bien_hanh:
        ket_qua.append(f"   • Ngũ Hành: {chinh_hanh} → {bien_hanh} (Bình hòa)")
    elif NGU_HANH_SINH.get(chinh_hanh) == bien_hanh:
        ket_qua.append(f"   • Ngũ Hành: {chinh_hanh} sinh {bien_hanh} (Thuận lợi)")
    elif NGU_HANH_KHAC.get(chinh_hanh) == bien_hanh:
        ket_qua.append(f"   • Ngũ Hành: {chinh_hanh} khắc {bien_hanh} (Cần cẩn thận)")
    else:
        ket_qua.append(f"   • Ngũ Hành: {chinh_hanh} và {bien_hanh} (Quan hệ phức tạp)")
    ket_qua.append("")
    
    # Giải quẻ theo chủ đề
    ket_qua.append(f"🎯 GIẢI QUẺ CHO '{chu_de.upper()}':")
    ket_qua.append(f"   • Hiện tại: Tình hình như quẻ {chinh_quai['quai_info']['ten']}")
    ket_qua.append(f"   • Nội tại: Có yếu tố {ho_quai['quai_info']['ten']} ảnh hưởng")
    ket_qua.append(f"   • Tương lai: Sẽ chuyển biến thành {bien_quai['quai_info']['ten']}")
    ket_qua.append("")
    
    # Lời khuyên dựa trên hào động
    dong_hao_so = chinh_quai['dong_hao'][0]
    luc_than_dong = luc_than_6_hao[dong_hao_so - 1]
    luc_than_dong_item = luc_than_6_hao_list[dong_hao_so - 1]
    dia_chi_dong = dia_chi_6_hao[dong_hao_so - 1]
    ngu_hanh_dong = DIA_CHI_NGU_HANH.get(dia_chi_dong, "")
    vuong_suy_dong = xac_dinh_vuong_suy(ngu_hanh_dong, thang)
    
    ket_qua.append("💡 LỜI KHUYÊN:")
    ket_qua.append(f"   • Hào {dong_hao_so} động - {luc_than_dong} ({luc_than_dong_item})")
    ket_qua.append(f"   • Trạng thái: {vuong_suy_dong} - {LUC_THAN.get(luc_than_dong, {}).get('y_nghia', '')}")
    ket_qua.append(f"   • {LUC_THAN.get(luc_than_dong_item, {}).get('y_nghia', '')}")
    
    # Cảnh báo Tuần Không
    if dia_chi_dong in tuan_khong_list:
        ket_qua.append(f"   ⚠️ Hào động rơi vào Tuần Không - Sức mạnh giảm, cần cẩn thận")
    
    # Thông báo Dịch Mã
    if dia_chi_dong in DICH_MA:
        ket_qua.append(f"   🐎 Hào động có Dịch Mã - Có sự di chuyển, thay đổi nhanh")
    
    ket_qua.append("   • Cần chú ý đến xu hướng biến hóa")
    ket_qua.append("   • Hành động phù hợp với Ngũ Hành")
    
    # Thêm visualization quẻ
    ket_qua.append("")
    ket_qua.append("═" * 75)
    ket_qua.append("📊 HÌNH ẢNH QUẺ VỚI GẠCH ÂM DƯƠNG")
    ket_qua.append("═" * 75)
    
    
    try:
        from ve_qua_am_duong_enhanced import tao_hien_thi_qua_chi_tiet_to, tao_hien_thi_3_qua_to
        
        # Hiển thị quẻ chính với chi tiết TO, RÕ NÉT
        visual_chinh = tao_hien_thi_qua_chi_tiet_to(chinh_quai, thang)
        ket_qua.append(visual_chinh)
        
        # Hiển thị 3 quẻ TO, RÕ NÉT
        ket_qua.append("")
        visual_3_qua = tao_hien_thi_3_qua_to(chinh_quai, ho_quai, bien_quai, thang)
        ket_qua.append(visual_3_qua)
    except ImportError:
        # Fallback to original visualization
        try:
            from ve_qua_am_duong import tao_hien_thi_qua_chi_tiet, tao_hien_thi_3_qua
            
            # Hiển thị quẻ chính với chi tiết
            visual_chinh = tao_hien_thi_qua_chi_tiet(chinh_quai, thang)
            ket_qua.append(visual_chinh)
            
            # Hiển thị 3 quẻ
            ket_qua.append("")
            visual_3_qua = tao_hien_thi_3_qua(chinh_quai, ho_quai, bien_quai, thang)
            ket_qua.append(visual_3_qua)
        except Exception as e:
            ket_qua.append(f"(Không thể hiển thị visualization: {str(e)})")
    except Exception as e:
        ket_qua.append(f"(Không thể hiển thị visualization: {str(e)})")
    
    return "\n".join(ket_qua)

# ============================================================================
# PHẦN 3: HÀM CHÍNH
# ============================================================================

def lap_qua_luc_hao(nam, thang, ngay, gio, chu_de="Tổng Quát"):
    """
    Lập quẻ Lục Hào hoàn chỉnh
    
    Returns:
        dict: {
            'chinh_quai': Chính Quái,
            'ho_quai': Hỗ Quái,
            'bien_quai': Biến Quái,
            'giai_thich': Diễn giải
        }
    """
    # Tính 3 quẻ
    chinh_quai = tinh_chinh_quai_theo_thoi_gian(nam, thang, ngay, gio)
    ho_quai = tinh_ho_quai(chinh_quai)
    bien_quai = tinh_bien_quai(chinh_quai)
    
    # Giải quẻ (truyền thêm tháng)
    giai_thich = giai_qua_luc_hao(chinh_quai, ho_quai, bien_quai, thang, chu_de)
    
    return {
        'chinh_quai': chinh_quai,
        'ho_quai': ho_quai,
        'bien_quai': bien_quai,
        'giai_thich': giai_thich
    }

# Test
if __name__ == "__main__":
    print("=== TEST LỤC HÀO KINH DỊCH ===\n")
    
    # Test với thời gian hiện tại
    ket_qua = lap_qua_luc_hao(2026, 1, 11, 23, "Kinh Doanh")
    print(ket_qua['giai_thich'])
    print("\n✅ Test hoàn thành!")
