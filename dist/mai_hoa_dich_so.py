# -*- coding: utf-8 -*-
"""
MAI HOA DỊCH SỐ - 64 QUẺ KINH DỊCH - PHIÊN BẢN NÂNG CẤP
Tính toán và giải quẻ chi tiết, sâu sắc theo phương pháp Mai Hoa Dịch Số
"""

import random
from datetime import datetime

# 8 Quẻ Cơ Bản (Bát Quái)
BAT_QUAI = {
    1: {"ten": "Càn", "ten_han": "乾", "unicode": "☰", "hanh": "Kim", "tuong": "Trời"},
    2: {"ten": "Đoài", "ten_han": "兌", "unicode": "☱", "hanh": "Kim", "tuong": "Trạch"},
    3: {"ten": "Ly", "ten_han": "離", "unicode": "☲", "hanh": "Hỏa", "tuong": "Hỏa"},
    4: {"ten": "Chấn", "ten_han": "震", "unicode": "☳", "hanh": "Mộc", "tuong": "Lôi"},
    5: {"ten": "Tốn", "ten_han": "巽", "unicode": "☴", "hanh": "Mộc", "tuong": "Phong"},
    6: {"ten": "Khảm", "ten_han": "坎", "unicode": "☵", "hanh": "Thủy", "tuong": "Thủy"},
    7: {"ten": "Cấn", "ten_han": "艮", "unicode": "☶", "hanh": "Thổ", "tuong": "Sơn"},
    8: {"ten": "Khôn", "ten_han": "坤", "unicode": "☷", "hanh": "Thổ", "tuong": "Địa"}
}

# 64 Quẻ Kinh Dịch (Lục Thập Tứ Quái)
# Format: (Quẻ Thượng, Quẻ Hạ): {thông tin quẻ}
LUC_THAP_TU_QUAI = {
    (1, 1): {"so": 1, "ten": "Càn Vi Thiên", "unicode": "䷀", "y_nghia": "Cát đại, vạn sự hanh thông, quý nhân phù trợ"},
    (1, 2): {"so": 43, "ten": "Trạch Thiên Quải", "unicode": "䷪", "y_nghia": "Quyết đoán, loại bỏ tiểu nhân, cương quyết tiến lên"},
    (1, 3): {"so": 13, "ten": "Thiên Hỏa Đồng Nhân", "unicode": "䷌", "y_nghia": "Đồng tâm hiệp lực, hợp tác thành công"},
    (1, 4): {"so": 25, "ten": "Thiên Lôi Vô Vọng", "unicode": "䷘", "y_nghia": "Chân thành, không vọng động, thuận theo tự nhiên"},
    (1, 5): {"so": 44, "ten": "Thiên Phong Cấu", "unicode": "䷫", "y_nghia": "Gặp gỡ, cơ hội bất ngờ, cẩn thận cám dỗ"},
    (1, 6): {"so": 6, "ten": "Thiên Thủy Tụng", "unicode": "䷅", "y_nghia": "Tranh tụng, kiện cáo, nên hòa giải"},
    (1, 7): {"so": 33, "ten": "Thiên Sơn Độn", "unicode": "䷠", "y_nghia": "Ẩn náu, tránh xa, bảo toàn thực lực"},
    (1, 8): {"so": 12, "ten": "Thiên Địa Bĩ", "unicode": "䷋", "y_nghia": "Bế tắc, khó khăn, nên kiên nhẫn chờ đợi"},
    
    (2, 1): {"so": 10, "ten": "Thiên Trạch Lý", "unicode": "䷉", "y_nghia": "Đi đúng đường, cẩn thận hành động"},
    (2, 2): {"so": 58, "ten": "Đoài Vi Trạch", "unicode": "䷹", "y_nghia": "Vui vẻ, hòa thuận, giao tiếp tốt"},
    (2, 3): {"so": 38, "ten": "Hỏa Trạch Khuê", "unicode": "䷥", "y_nghia": "Mâu thuẫn, bất hòa, cần hòa giải"},
    (2, 4): {"so": 54, "ten": "Lôi Trạch Quy Muội", "unicode": "䷵", "y_nghia": "Hôn nhân, kết hợp, cần thận trọng"},
    (2, 5): {"so": 61, "ten": "Phong Trạch Trung Phu", "unicode": "䷼", "y_nghia": "Trung thực, tin cậy, thành công"},
    (2, 6): {"so": 47, "ten": "Trạch Thủy Khốn", "unicode": "䷮", "y_nghia": "Khốn khó, thiếu thốn, cần kiên trì"},
    (2, 7): {"so": 31, "ten": "Trạch Sơn Hàm", "unicode": "䷞", "y_nghia": "Cảm ứng, tương tác, tình cảm"},
    (2, 8): {"so": 45, "ten": "Trạch Địa Tụy", "unicode": "䷬", "y_nghia": "Tụ họp, đoàn kết, hội họp"},
    
    (3, 1): {"so": 14, "ten": "Hỏa Thiên Đại Hữu", "unicode": "䷍", "y_nghia": "Phú quý, thịnh vượng, đại cát"},
    (3, 2): {"so": 49, "ten": "Trạch Hỏa Cách", "unicode": "䷰", "y_nghia": "Cải cách, thay đổi, đổi mới"},
    (3, 3): {"so": 30, "ten": "Ly Vi Hỏa", "unicode": "䷝", "y_nghia": "Sáng sủa, văn minh, rực rỡ"},
    (3, 4): {"so": 55, "ten": "Lôi Hỏa Phong", "unicode": "䷶", "y_nghia": "Phong phú, thịnh đạt, đỉnh cao"},
    (3, 5): {"so": 37, "ten": "Phong Hỏa Gia Nhân", "unicode": "䷤", "y_nghia": "Gia đạo, hòa thuận, gia đình"},
    (3, 6): {"so": 63, "ten": "Thủy Hỏa Ký Tế", "unicode": "䷾", "y_nghia": "Đã thành, hoàn tất, cẩn thận duy trì"},
    (3, 7): {"so": 22, "ten": "Sơn Hỏa Bí", "unicode": "䷕", "y_nghia": "Trang trí, văn chương, hình thức"},
    (3, 8): {"so": 36, "ten": "Địa Hỏa Minh Di", "unicode": "䷣", "y_nghia": "Tổn thương, khó khăn, ẩn nhẫn"},
    
    (4, 1): {"so": 34, "ten": "Lôi Thiên Đại Tráng", "unicode": "䷡", "y_nghia": "Cường tráng, mạnh mẽ, tiến lên"},
    (4, 2): {"so": 17, "ten": "Trạch Lôi Tùy", "unicode": "䷐", "y_nghia": "Theo đuổi, tuân theo, linh hoạt"},
    (4, 3): {"so": 21, "ten": "Hỏa Lôi Phệ Hạp", "unicode": "䷔", "y_nghia": "Cắn đứt, quyết đoán, xử lý"},
    (4, 4): {"so": 51, "ten": "Chấn Vi Lôi", "unicode": "䷲", "y_nghia": "Chấn động, kinh hoàng, cảnh giác"},
    (4, 5): {"so": 42, "ten": "Phong Lôi Ích", "unicode": "䷩", "y_nghia": "Lợi ích, tăng thêm, có lợi"},
    (4, 6): {"so": 3, "ten": "Thủy Lôi Truân", "unicode": "䷂", "y_nghia": "Khó khăn ban đầu, cần kiên trì"},
    (4, 7): {"so": 27, "ten": "Sơn Lôi Di", "unicode": "䷚", "y_nghia": "Nuôi dưỡng, chăm sóc, ăn uống"},
    (4, 8): {"so": 24, "ten": "Địa Lôi Phục", "unicode": "䷗", "y_nghia": "Phục hồi, trở lại, chu kỳ"},
    
    (5, 1): {"so": 9, "ten": "Phong Thiên Tiểu Súc", "unicode": "䷈", "y_nghia": "Tích lũy nhỏ, chờ đợi, chuẩn bị"},
    (5, 2): {"so": 28, "ten": "Trạch Phong Đại Quá", "unicode": "䷛", "y_nghia": "Quá mức, vượt quá, cần cân bằng"},
    (5, 3): {"so": 50, "ten": "Hỏa Phong Đỉnh", "unicode": "䷱", "y_nghia": "Đỉnh cao, thành tựu, ổn định"},
    (5, 4): {"so": 32, "ten": "Lôi Phong Hằng", "unicode": "䷟", "y_nghia": "Bền vững, lâu dài, kiên trì"},
    (5, 5): {"so": 57, "ten": "Tốn Vi Phong", "unicode": "䷸", "y_nghia": "Khiêm tốn, thuận theo, linh hoạt"},
    (5, 6): {"so": 48, "ten": "Thủy Phong Tỉnh", "unicode": "䷯", "y_nghia": "Giếng nước, nguồn lực, ổn định"},
    (5, 7): {"so": 18, "ten": "Sơn Phong Cổ", "unicode": "䷑", "y_nghia": "Sửa chữa, cải thiện, trị liệu"},
    (5, 8): {"so": 46, "ten": "Địa Phong Thăng", "unicode": "䷭", "y_nghia": "Thăng tiến, lên cao, phát triển"},
    
    (6, 1): {"so": 5, "ten": "Thủy Thiên Nhu", "unicode": "䷄", "y_nghia": "Chờ đợi, kiên nhẫn, thời cơ"},
    (6, 2): {"so": 60, "ten": "Trạch Thủy Tiết", "unicode": "䷻", "y_nghia": "Tiết chế, điều độ, giới hạn"},
    (6, 3): {"so": 64, "ten": "Hỏa Thủy Vị Tế", "unicode": "䷿", "y_nghia": "Chưa hoàn thành, cẩn thận tiếp tục"},
    (6, 4): {"so": 40, "ten": "Lôi Thủy Giải", "unicode": "䷧", "y_nghia": "Giải thoát, tháo gỡ, vượt qua"},
    (6, 5): {"so": 59, "ten": "Phong Thủy Hoán", "unicode": "䷺", "y_nghia": "Tan rã, phân tán, cần đoàn kết"},
    (6, 6): {"so": 29, "ten": "Khảm Vi Thủy", "unicode": "䷜", "y_nghia": "Hiểm trở, khó khăn, cẩn thận"},
    (6, 7): {"so": 4, "ten": "Sơn Thủy Mông", "unicode": "䷃", "y_nghia": "Mông muội, học hỏi, giáo dục"},
    (6, 8): {"so": 7, "ten": "Địa Thủy Sư", "unicode": "䷆", "y_nghia": "Quân đội, tổ chức, kỷ luật"},
    
    (7, 1): {"so": 26, "ten": "Sơn Thiên Đại Súc", "unicode": "䷙", "y_nghia": "Tích lũy lớn, dự trữ, chuẩn bị"},
    (7, 2): {"so": 41, "ten": "Trạch Sơn Tổn", "unicode": "䷨", "y_nghia": "Tổn thất, giảm bớt, hy sinh"},
    (7, 3): {"so": 56, "ten": "Hỏa Sơn Lữ", "unicode": "䷷", "y_nghia": "Du lịch, xa xứ, không ổn định"},
    (7, 4): {"so": 62, "ten": "Lôi Sơn Tiểu Quá", "unicode": "䷽", "y_nghia": "Nhỏ quá, vượt nhẹ, cẩn thận"},
    (7, 5): {"so": 53, "ten": "Phong Sơn Tiệm", "unicode": "䷴", "y_nghia": "Tiến dần, từ từ, bền bỉ"},
    (7, 6): {"so": 39, "ten": "Thủy Sơn Kiển", "unicode": "䷦", "y_nghia": "Khập khiễng, khó khăn, cần giúp đỡ"},
    (7, 7): {"so": 52, "ten": "Cấn Vi Sơn", "unicode": "䷳", "y_nghia": "Dừng lại, nghỉ ngơi, suy nghĩ"},
    (7, 8): {"so": 15, "ten": "Địa Sơn Khiêm", "unicode": "䷎", "y_nghia": "Khiêm tốn, hạ mình, đại cát"},
    
    (8, 1): {"so": 11, "ten": "Địa Thiên Thái", "unicode": "䷊", "y_nghia": "Thông thái, hanh thông, đại cát"},
    (8, 2): {"so": 19, "ten": "Địa Trạch Lâm", "unicode": "䷒", "y_nghia": "Đến gần, giám sát, quản lý"},
    (8, 3): {"so": 35, "ten": "Hỏa Địa Tấn", "unicode": "䷢", "y_nghia": "Tiến lên, thăng tiến, phát triển"},
    (8, 4): {"so": 16, "ten": "Lôi Địa Dự", "unicode": "䷏", "y_nghia": "Vui vẻ, hưởng thụ, âm nhạc"},
    (8, 5): {"so": 20, "ten": "Phong Địa Quán", "unicode": "䷓", "y_nghia": "Quan sát, xem xét, học hỏi"},
    (8, 6): {"so": 8, "ten": "Thủy Địa Tỷ", "unicode": "䷇", "y_nghia": "Thân mật, hợp tác, đoàn kết"},
    (8, 7): {"so": 23, "ten": "Sơn Địa Bác", "unicode": "䷖", "y_nghia": "Bóc lột, suy thoái, cẩn thận"},
    (8, 8): {"so": 2, "ten": "Khôn Vi Địa", "unicode": "䷁", "y_nghia": "Thuận theo, nhu hòa, chịu đựng"}
}

def tinh_qua_theo_thoi_gian(nam, thang, ngay, gio):
    """
    Tính quẻ theo phương pháp Mai Hoa Dịch Số
    
    Args:
        nam, thang, ngay, gio: Thời gian âm lịch hoặc dương lịch
    
    Returns:
        Dict chứa thông tin quẻ
    """
    # Tính Quẻ Thượng
    so_thuong = (nam + thang + ngay) % 8
    if so_thuong == 0:
        so_thuong = 8
    
    # Tính Quẻ Hạ
    so_ha = (nam + thang + ngay + gio) % 8
    if so_ha == 0:
        so_ha = 8
    
    # Tính Hào Động
    hao_dong = (nam + thang + ngay + gio) % 6
    if hao_dong == 0:
        hao_dong = 6
    
    # Lấy thông tin Bản Quẻ
    ban_qua = LUC_THAP_TU_QUAI.get((so_thuong, so_ha), {})
    
    # Tính Quẻ Biến (đảo hào động)
    if hao_dong >= 4:
        so_thuong_bien = (so_thuong % 8) + 1 if so_thuong < 8 else 1
        qua_bien = LUC_THAP_TU_QUAI.get((so_thuong_bien, so_ha), {})
    else:
        so_ha_bien = (so_ha % 8) + 1 if so_ha < 8 else 1
        qua_bien = LUC_THAP_TU_QUAI.get((so_thuong, so_ha_bien), {})
    
    return {
        "qua_thuong": BAT_QUAI[so_thuong],
        "qua_ha": BAT_QUAI[so_ha],
        "ban_qua": ban_qua,
        "qua_bien": qua_bien,
        "hao_dong": hao_dong,
        "thoi_gian": f"{gio}h {ngay}/{thang}/{nam}"
    }

def tinh_qua_ngau_nhien():
    """
    Tính quẻ ngẫu nhiên theo Mai Hoa Dịch Số
    
    Returns:
        Dict chứa thông tin quẻ
    """
    so_thuong = random.randint(1, 8)
    so_ha = random.randint(1, 8)
    hao_dong = random.randint(1, 6)
    
    ban_qua = LUC_THAP_TU_QUAI.get((so_thuong, so_ha), {})
    
    if hao_dong >= 4:
        so_thuong_bien = (so_thuong % 8) + 1 if so_thuong < 8 else 1
        qua_bien = LUC_THAP_TU_QUAI.get((so_thuong_bien, so_ha), {})
    else:
        so_ha_bien = (so_ha % 8) + 1 if so_ha < 8 else 1
        qua_bien = LUC_THAP_TU_QUAI.get((so_thuong, so_ha_bien), {})
    
    return {
        "qua_thuong": BAT_QUAI[so_thuong],
        "qua_ha": BAT_QUAI[so_ha],
        "ban_qua": ban_qua,
        "qua_bien": qua_bien,
        "hao_dong": hao_dong,
        "thoi_gian": "Ngẫu nhiên"
    }

def giai_qua(ket_qua_qua, chu_de="Tổng Quát"):
    """
    Giải quẻ CHI TIẾT, SÂU SẮC với phân tích đa chiều
    
    Args:
        ket_qua_qua: Dict từ tinh_qua_theo_thoi_gian() hoặc tinh_qua_ngau_nhien()
        chu_de: Chủ đề cần giải
    
    Returns:
        String giải quẻ chi tiết
    """
    ban_qua = ket_qua_qua["ban_qua"]
    qua_bien = ket_qua_qua["qua_bien"]
    hao_dong = ket_qua_qua["hao_dong"]
    qua_thuong = ket_qua_qua["qua_thuong"]
    qua_ha = ket_qua_qua["qua_ha"]
    
    giai_thich = []
    giai_thich.append("═" * 95)
    giai_thich.append("📖 DIỄN GIẢI CHI TIẾT MAI HOA DỊCH SỐ")
    giai_thich.append("═" * 95)
    giai_thich.append("")
    
    # PHẦN 1: THÔNG TIN QUẺ CƠ BẢN
    giai_thich.append("🔷 THÔNG TIN QUẺ:")
    giai_thich.append(f"   • Bản Quẻ: {ban_qua['ten']} {ban_qua['unicode']}")
    giai_thich.append(f"   • Thượng Quái: {qua_thuong['ten']} {qua_thuong['unicode']} ({qua_thuong['hanh']}) - Tượng: {qua_thuong['tuong']}")
    giai_thich.append(f"   • Hạ Quái: {qua_ha['ten']} {qua_ha['unicode']} ({qua_ha['hanh']}) - Tượng: {qua_ha['tuong']}")
    giai_thich.append(f"   • Hào Động: Hào thứ {hao_dong}")
    giai_thich.append(f"   • Quẻ Biến: {qua_bien['ten']} {qua_bien['unicode']}")
    giai_thich.append("")
    
    # PHẦN 2: Ý NGHĨA BẢN QUẺ
    giai_thich.append("📊 Ý NGHĨA BẢN QUẺ (Tình Hình Hiện Tại):")
    giai_thich.append(f"   {ban_qua['y_nghia']}")
    giai_thich.append("")
    giai_thich.append("   🔍 Phân Tích Sâu:")
    
    # Phân tích theo Ngũ Hành
    hanh_thuong = qua_thuong['hanh']
    hanh_ha = qua_ha['hanh']
    
    if hanh_thuong == hanh_ha:
        giai_thich.append(f"   • Ngũ Hành: {hanh_thuong} - {hanh_ha} (Đồng hành, thuần khiết, ổn định)")
    elif (hanh_thuong == "Kim" and hanh_ha == "Thủy") or \
         (hanh_thuong == "Thủy" and hanh_ha == "Mộc") or \
         (hanh_thuong == "Mộc" and hanh_ha == "Hỏa") or \
         (hanh_thuong == "Hỏa" and hanh_ha == "Thổ") or \
         (hanh_thuong == "Thổ" and hanh_ha == "Kim"):
        giai_thich.append(f"   • Ngũ Hành: {hanh_thuong} sinh {hanh_ha} (Thuận lợi, được hỗ trợ)")
    elif (hanh_ha == "Kim" and hanh_thuong == "Thủy") or \
         (hanh_ha == "Thủy" and hanh_thuong == "Mộc") or \
         (hanh_ha == "Mộc" and hanh_thuong == "Hỏa") or \
         (hanh_ha == "Hỏa" and hanh_thuong == "Thổ") or \
         (hanh_ha == "Thổ" and hanh_thuong == "Kim"):
        giai_thich.append(f"   • Ngũ Hành: {hanh_ha} sinh {hanh_thuong} (Có tiềm năng, cần nỗ lực)")
    else:
        giai_thich.append(f"   • Ngũ Hành: {hanh_thuong} - {hanh_ha} (Khắc chế, cần cẩn trọng)")
    
    # Phân tích Tượng
    giai_thich.append(f"   • Tượng Trưng: {qua_thuong['tuong']} (trên) - {qua_ha['tuong']} (dưới)")
    giai_thich.append("")
    
    # PHẦN 3: HÀO ĐỘNG
    giai_thich.append(f"⚡ PHÂN TÍCH HÀO ĐỘNG (Hào {hao_dong}):")
    
    # Vị trí hào động
    if hao_dong <= 3:
        vi_tri = "Hạ Quái (Nội quái)"
        y_nghia_vi_tri = "Ảnh hưởng đến nội tại, bản thân, khởi đầu"
    else:
        vi_tri = "Thượng Quái (Ngoại quái)"
        y_nghia_vi_tri = "Ảnh hưởng đến bên ngoài, môi trường, kết quả"
    
    giai_thich.append(f"   • Vị trí: {vi_tri} - {y_nghia_vi_tri}")
    
    # Ý nghĩa theo vị trí cụ thể
    hao_y_nghia = {
        1: "Khởi đầu, nền tảng - Cần thận trọng, xây dựng cơ sở vững chắc",
        2: "Phát triển, tiến bộ - Thời điểm thuận lợi để hành động",
        3: "Chuyển tiếp, biến đổi - Giai đoạn quan trọng, cần quyết đoán",
        4: "Mở rộng, giao tiếp - Tập trung vào quan hệ bên ngoài",
        5: "Đỉnh cao, quyền lực - Thời điểm quan trọng nhất, cần khôn ngoan",
        6: "Kết thúc, hoàn thành - Chuẩn bị cho chu kỳ mới"
    }
    
    giai_thich.append(f"   • Ý nghĩa: {hao_y_nghia[hao_dong]}")
    giai_thich.append("")
    
    # PHẦN 4: QUẺ BIẾN
    giai_thich.append("🔄 QUẺ BIẾN (Xu Hướng Phát Triển):")
    giai_thich.append(f"   {qua_bien['y_nghia']}")
    giai_thich.append("")
    giai_thich.append("   📈 Diễn Biến:")
    giai_thich.append(f"   • Từ '{ban_qua['ten']}' → '{qua_bien['ten']}'")
    
    if ban_qua['so'] == qua_bien['so']:
        giai_thich.append("   • Tình hình ổn định, ít biến động")
    else:
        giai_thich.append("   • Sẽ có sự thay đổi rõ rệt, cần chuẩn bị")
    
    giai_thich.append("")
    
    # PHẦN 5: GIẢI QUẺ THEO CHỦ ĐỀ
    giai_thich.append(f"🎯 DIỄN GIẢI CHO '{chu_de.upper()}':")
    giai_thich.append("")
    
    if chu_de in ["Kinh Doanh", "Công Việc", "Sự Nghiệp"]:
        giai_thich.append("   💼 Về Kinh Doanh/Công Việc:")
        giai_thich.append(f"   • Hiện tại: {ban_qua['y_nghia']}")
        giai_thich.append(f"   • Xu hướng: {qua_bien['y_nghia']}")
        giai_thich.append(f"   • Điểm chú ý: Hào {hao_dong} động - {hao_y_nghia[hao_dong]}")
        giai_thich.append("   • Lời khuyên: Nắm bắt thời cơ, hành động đúng lúc, chú ý biến hóa")
    elif chu_de in ["Hôn Nhân", "Tình Cảm", "Gia Đình"]:
        giai_thich.append("   💑 Về Hôn Nhân/Tình Cảm:")
        giai_thich.append(f"   • Tình hình: {ban_qua['y_nghia']}")
        giai_thich.append(f"   • Phát triển: {qua_bien['y_nghia']}")
        giai_thich.append(f"   • Yếu tố quan trọng: {hao_y_nghia[hao_dong]}")
        giai_thich.append("   • Lời khuyên: Chân thành, kiên nhẫn, thấu hiểu lẫn nhau")
    elif chu_de in ["Sức Khỏe", "Bệnh Tật"]:
        giai_thich.append("   🏥 Về Sức Khỏe:")
        giai_thich.append(f"   • Tình trạng: {ban_qua['y_nghia']}")
        giai_thich.append(f"   • Diễn biến: {qua_bien['y_nghia']}")
        giai_thich.append("   • Lời khuyên: Chăm sóc sức khỏe, nghỉ ngơi hợp lý")
    elif chu_de in ["Tài Lộc", "Tài Chính", "Đầu Tư"]:
        giai_thich.append("   💰 Về Tài Lộc/Tài Chính:")
        giai_thich.append(f"   • Hiện tại: {ban_qua['y_nghia']}")
        giai_thich.append(f"   • Triển vọng: {qua_bien['y_nghia']}")
        giai_thich.append("   • Lời khuyên: Thận trọng trong đầu tư, quản lý hợp lý")
    else:  # Tổng Quát
        giai_thich.append("   🌟 Tổng Quát:")
        giai_thich.append(f"   • Tình hình hiện tại: {ban_qua['y_nghia']}")
        giai_thich.append(f"   • Xu hướng tương lai: {qua_bien['y_nghia']}")
        giai_thich.append(f"   • Yếu tố biến đổi: Hào {hao_dong} - {hao_y_nghia[hao_dong]}")
        giai_thich.append("   • Lời khuyên: Thuận theo tự nhiên, linh hoạt ứng biến")
    
    giai_thich.append("")
    
    # PHẦN 6: LỜI KHUYÊN TỔNG HỢP
    giai_thich.append("💡 LỜI KHUYÊN TỔNG HỢP:")
    giai_thich.append("   ✓ Nên làm:")
    giai_thich.append("     - Nắm bắt thời cơ khi hào động xuất hiện")
    giai_thich.append("     - Chuẩn bị cho sự thay đổi từ Bản Quẻ sang Quẻ Biến")
    giai_thich.append("     - Hành động phù hợp với Ngũ Hành và Tượng của quẻ")
    giai_thich.append("")
    giai_thich.append("   ✗ Tránh:")
    giai_thich.append("     - Hành động vội vàng, thiếu cân nhắc")
    giai_thich.append("     - Bỏ qua các dấu hiệu cảnh báo")
    giai_thich.append("     - Đi ngược lại xu hướng tự nhiên")
    giai_thich.append("")
    giai_thich.append("═" * 95)
    
    # PHẦN 6: TIÊN ĐOÁN CỤ THỂ (SỐ LƯỢNG, SỐ TIỀN, TRAI/GÁI, GIÀ/TRẺ, VẬT GÌ)
    giai_thich.append("="*95)
    giai_thich.append("🔮 TIÊN ĐOÁN CỤ THỂ (TƯỢNG SỐ)")
    giai_thich.append("="*95)
    giai_thich.append("")
    
    # Import module tiên đoán cụ thể
    try:
        from mai_hoa_tien_doan_cu_the import tien_doan_cu_the_mai_hoa
        tien_doan = tien_doan_cu_the_mai_hoa(ket_qua_qua, chu_de)
        
        # Hiển thị các tiên đoán
        giai_thich.append(tien_doan["so_luong"])
        giai_thich.append(tien_doan["so_tien"])
        giai_thich.append(tien_doan["gioi_tinh"])
        giai_thich.append(tien_doan["tuoi_tac"])
        giai_thich.append(tien_doan["ngoai_hinh"])
        giai_thich.append(tien_doan["tinh_cach"])
        giai_thich.append(tien_doan["nghe_nghiep"])
        giai_thich.append(tien_doan["vat_the"])
        giai_thich.append(tien_doan["thoi_gian"])
    except Exception as e:
        giai_thich.append("⚠️ Chưa có module tiên đoán cụ thể")
        giai_thich.append(f"   (Lỗi: {e})")
    
    giai_thich.append("")
    giai_thich.append("="*95)
    
    return "\n".join(giai_thich)

# Test
if __name__ == "__main__":
    print("=== TEST MAI HOA DỊCH SỐ ===\n")
    
    # Test theo thời gian
    print("1. Test theo thời gian (2026/1/11 22:00):")
    ket_qua = tinh_qua_theo_thoi_gian(2026, 1, 11, 22)
    print(giai_qua(ket_qua, "Kinh Doanh"))
    print("\n" + "="*50 + "\n")
    
    # Test ngẫu nhiên
    print("2. Test ngẫu nhiên:")
    ket_qua_random = tinh_qua_ngau_nhien()
    print(giai_qua(ket_qua_random, "Hôn Nhân"))
    print("\n✅ Tests hoàn thành!")
