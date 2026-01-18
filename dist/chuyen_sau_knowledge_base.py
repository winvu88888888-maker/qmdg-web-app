# -*- coding: utf-8 -*-
"""
KNOWLEDGE BASE - TÍCH HỢP DỮ LIỆU TỪ CÁC TÀI LIỆU CHUYÊN SÂU
Bao gồm: Lục Hào Kinh Dịch, Mai Hoa Dịch Số từ các sách chuyên môn

Nguồn tham khảo:
- Lục Hào Bảo Điển
- Lục Hào Thực Chiến
- Lục Hào Xử Cát Tị Hung Hóa Giải Bí Truyền
- Mai Hoa Dịch Số - Thiệu Khang Tiết
- Tuyển Tập Chu Dịch Với Dự Đoán Học
"""

# ============================================================================
# PHẦN 1: DỮ LIỆU LỤC HÀO KINH DỊCH CHUYÊN SÂU
# ============================================================================

# Giải thích chi tiết 64 quẻ theo Lục Hào
LUC_HAO_64_QUA_CHI_TIET = {
    1: {  # Càn Vi Thiên
        "ten": "Càn Vi Thiên",
        "unicode": "䷀",
        "tong_quan": "Quẻ thuần Dương, cát đại, vạn sự hanh thông. Tượng trưng cho sức mạnh, quyền lực, sáng tạo.",
        "kinh_doanh": "Rất tốt cho khởi nghiệp, mở rộng kinh doanh. Có quý nhân phù trợ, thành công lớn.",
        "hon_nhan": "Hôn nhân tốt đẹp, vợ chồng hòa thuận. Nam mạnh, nữ nhu, âm dương cân bằng.",
        "suc_khoe": "Sức khỏe tốt, tinh thần minh mẫn. Cần chú ý không quá lao lực.",
        "tai_loc": "Tài lộc hanh thông, thu nhập tăng. Đầu tư sinh lời.",
        "quan_tung": "Có lý, dễ thắng kiện. Nên hòa giải để tránh tốn kém.",
        "loi_khuyen": "Tiến lên mạnh mẽ nhưng cần khiêm tốn. Đừng quá cương quyết dẫn đến cô độc."
    },
    
    2: {  # Khôn Vi Địa
        "ten": "Khôn Vi Địa",
        "unicode": "䷁",
        "tong_quan": "Quẻ thuần Âm, nhu hòa, thuận theo. Tượng trưng cho đất mẹ, nuôi dưỡng, chịu đựng.",
        "kinh_doanh": "Nên hợp tác, làm việc nhóm. Tránh độc đoán, cần người dẫn dắt.",
        "hon_nhan": "Hôn nhân hòa thuận nếu biết nhường nhịn. Vợ hiền, chồng thương.",
        "suc_khoe": "Cần chăm sóc, nghỉ ngơi. Dễ mệt mỏi, stress.",
        "tai_loc": "Tài lộc ổn định nhưng không lớn. Tích lũy từ từ.",
        "quan_tung": "Nên nhượng bộ, hòa giải. Tránh tranh chấp kéo dài.",
        "loi_khuyen": "Thuận theo tự nhiên, kiên nhẫn chờ đợi. Sức mạnh nằm ở sự nhu hòa."
    },
    
    # ... Thêm 62 quẻ còn lại với thông tin chi tiết
}

# Lục Thân - Ý nghĩa chi tiết trong các tình huống
LUC_THAN_CHI_TIET = {
    "Phụ Mẫu": {
        "y_nghia_chung": "Cha mẹ, văn thư, tài liệu, nhà cửa, xe cộ, quần áo",
        "kinh_doanh": "Hợp đồng, giấy tờ, văn bản pháp lý. Phụ Mẫu vượng = giấy tờ thuận lợi",
        "hon_nhan": "Cha mẹ hai bên, người lớn tuổi. Phụ Mẫu động = cha mẹ can thiệp",
        "suc_khoe": "Đầu, ngực, hệ hô hấp. Phụ Mẫu khắc = bệnh về đầu óc",
        "tai_loc": "Bất động sản, nhà đất. Phụ Mẫu vượng = có nhà có xe",
        "hoc_tap": "Học vấn, bằng cấp. Phụ Mẫu vượng = thi cử tốt",
        "vuong": "Giấy tờ thuận lợi, học tập tốt, có nhà có xe",
        "suy": "Giấy tờ khó khăn, học tập kém, thiếu chỗ ở"
    },
    
    "Huynh Đệ": {
        "y_nghia_chung": "Anh em, bạn bè, đồng nghiệp, đối thủ cạnh tranh",
        "kinh_doanh": "Đối tác, đồng nghiệp, cạnh tranh. Huynh Đệ động = có tranh chấp",
        "hon_nhan": "Người thứ ba, tình địch. Huynh Đệ vượng = dễ có người thứ ba",
        "suc_khoe": "Tứ chi, cơ bắp. Huynh Đệ khắc = chấn thương tay chân",
        "tai_loc": "Tiêu hao, mất mát. Huynh Đệ vượng = tiền bạc thất thoát",
        "quan_tung": "Đối thủ, kẻ thù. Huynh Đệ vượng = đối phương mạnh",
        "vuong": "Bạn bè nhiều, được giúp đỡ, nhưng dễ tiêu hao tiền bạc",
        "suy": "Ít bạn bè, cô đơn, nhưng giữ được tiền"
    },
    
    "Tử Tôn": {
        "y_nghia_chung": "Con cái, học sinh, vui vẻ, sáng tạo, giải trí",
        "kinh_doanh": "Sản phẩm, hàng hóa, khách hàng. Tử Tôn vượng = hàng bán chạy",
        "hon_nhan": "Con cái, sinh sản. Tử Tôn vượng = dễ có con",
        "suc_khoe": "Sinh dục, tiêu hóa. Tử Tôn khắc = bệnh tiêu hóa",
        "tai_loc": "Lợi nhuận, thu nhập. Tử Tôn vượng = kiếm tiền tốt",
        "hoc_tap": "Học sinh, đệ tử. Tử Tôn vượng = học trò giỏi",
        "vuong": "Con cái khỏe mạnh, kinh doanh sinh lời, vui vẻ",
        "suy": "Khó có con, kinh doanh ế ẩm, buồn bã"
    },
    
    "Thê Tài": {
        "y_nghia_chung": "Vợ (nam), tài lộc, tiền bạc, của cải",
        "kinh_doanh": "Vốn, tiền bạc, tài sản. Thê Tài vượng = vốn dồi dào",
        "hon_nhan": "Vợ (nam), chồng (nữ). Thê Tài vượng = hôn nhân tốt",
        "suc_khoe": "Lá lách, dạ dày. Thê Tài khắc = bệnh tiêu hóa",
        "tai_loc": "Tiền bạc, tài sản. Thê Tài vượng = giàu có",
        "quan_tung": "Tài sản tranh chấp. Thê Tài vượng = có lý về tài sản",
        "vuong": "Giàu có, vợ đẹp (nam), chồng giỏi (nữ)",
        "suy": "Nghèo khó, vợ yếu (nam), chồng kém (nữ)"
    },
    
    "Quan Quỷ": {
        "y_nghia_chung": "Quan chức, chồng (nữ), áp lực, bệnh tật, tai họa",
        "kinh_doanh": "Áp lực, trở ngại, thuế má. Quan Quỷ vượng = nhiều khó khăn",
        "hon_nhan": "Chồng (nữ), người yêu. Quan Quỷ vượng = chồng tốt (nữ)",
        "suc_khoe": "Bệnh tật, tai nạn. Quan Quỷ động = dễ ốm đau",
        "tai_loc": "Tổn thất, mất mát. Quan Quỷ vượng = tiền bị mất",
        "quan_tung": "Quan tòa, pháp luật. Quan Quỷ vượng = thua kiện",
        "vuong": "Có quyền lực (nam), chồng tốt (nữ), nhưng áp lực lớn",
        "suy": "Ít quyền lực, chồng yếu (nữ), nhưng ít bệnh tật"
    }
}

# Lục Thần - Ý nghĩa chi tiết
LUC_THAN_CHI_TIET = {
    "Thanh Long": {
        "y_nghia": "Cát tường, vui vẻ, thăng tiến, tài lộc, hỷ sự",
        "mau_sac": "Xanh lá",
        "huong": "Đông",
        "tinh_chat": "Dương, cát",
        "khi_vuong": "Hỷ sự liên tiếp, thăng quan tiến chức, tài lộc dồi dào",
        "khi_suy": "Vui vẻ nhưng không bền, hỷ sự nhỏ",
        "ung_dung": "Cầu tài, cầu quan, cầu hỷ sự đều tốt"
    },
    
    "Chu Tước": {
        "y_nghia": "Văn thư, thị phi, tranh cãi, tin tức, thông tin",
        "mau_sac": "Đỏ",
        "huong": "Nam",
        "tinh_chat": "Dương, nửa cát nửa hung",
        "khi_vuong": "Tin tức quan trọng, văn thư pháp lý, thi cử tốt",
        "khi_suy": "Tin đồn, thị phi, tranh cãi, kiện tụng",
        "ung_dung": "Cầu thi cử tốt, cầu tin tức cẩn thận thị phi"
    },
    
    "Câu Trần": {
        "y_nghia": "Tranh chấp, kiện tụng, rắc rối, trở ngại",
        "mau_sac": "Vàng",
        "huong": "Trung ương",
        "tinh_chat": "Âm, hung",
        "khi_vuong": "Kiện tụng kéo dài, tranh chấp gay gắt, rắc rối lớn",
        "khi_suy": "Rắc rối nhỏ, dễ giải quyết",
        "ung_dung": "Tránh tranh chấp, nên hòa giải"
    },
    
    "Đằng Xà": {
        "y_nghia": "Quỷ quái, bệnh tật, âm mưu, lừa đảo, bí mật",
        "mau_sac": "Đen",
        "huong": "Bắc",
        "tinh_chat": "Âm, hung",
        "khi_vuong": "Bệnh nặng, bị lừa đảo, âm mưu hại, ma quỷ",
        "khi_suy": "Bệnh nhẹ, cẩn thận là tránh được",
        "ung_dung": "Cẩn thận lừa đảo, chú ý sức khỏe, tránh chỗ tối"
    },
    
    "Bạch Hổ": {
        "y_nghia": "Hung ác, tai nạn, tổn thương, máu me, tang tóc",
        "mau_sac": "Trắng",
        "huong": "Tây",
        "tinh_chat": "Âm, đại hung",
        "khi_vuong": "Tai nạn nghiêm trọng, tổn thương, tang tóc, máu me",
        "khi_suy": "Tai nạn nhỏ, va chạm nhẹ",
        "ung_dung": "Cẩn thận tai nạn, tránh dao kéo, chú ý an toàn"
    },
    
    "Huyền Vũ": {
        "y_nghia": "Trộm cắp, lừa đảo, bí mật, âm thầm, mất mát",
        "mau_sac": "Đen xám",
        "huong": "Bắc",
        "tinh_chat": "Âm, hung",
        "khi_vuong": "Bị trộm cắp, lừa đảo lớn, mất mát nhiều, bí mật bị lộ",
        "khi_suy": "Mất mát nhỏ, cẩn thận là tránh được",
        "ung_dung": "Cẩn thận tài sản, tránh lừa đảo, giữ bí mật"
    }
}

# ============================================================================
# PHẦN 2: DỮ LIỆU MAI HOA DỊCH SỐ CHUYÊN SÂU
# ============================================================================

# Bát Quái - Tượng số chi tiết (theo Thiệu Khang Tiết)
BAT_QUAI_TUONG_SO_CHI_TIET = {
    "Càn": {
        "so": 1,
        "hanh": "Kim",
        "tuong_nguoi": "Cha, lãnh đạo, người cao tuổi, người quyền lực",
        "tuong_vat": "Vàng, bạc, kim loại quý, đồ trang sức",
        "tuong_than_the": "Đầu, xương, phổi, hệ hô hấp",
        "tuong_dong_vat": "Ngựa, sư tử, rồng",
        "tuong_thoi_tiet": "Nắng gắt, trời quang đãng",
        "tuong_phuong_vi": "Tây Bắc",
        "tuong_mau_sac": "Trắng, vàng kim",
        "tuong_so": "1, 6, 9",
        "tinh_chat": "Cứng rắn, mạnh mẽ, quyền uy, sáng tạo",
        "khi_vuong": "Thành công lớn, quyền lực, giàu có",
        "khi_suy": "Cô độc, cứng nhắc, áp lực lớn"
    },
    
    "Khôn": {
        "so": 8,
        "hanh": "Thổ",
        "tuong_nguoi": "Mẹ, người già, nông dân, người hiền lành",
        "tuong_vat": "Đất đai, ruộng vườn, vải vóc, lương thực",
        "tuong_than_the": "Bụng, lá lách, dạ dày, hệ tiêu hóa",
        "tuong_dong_vat": "Bò, trâu, dê",
        "tuong_thoi_tiet": "Mây mù, ẩm ướt",
        "tuong_phuong_vi": "Tây Nam",
        "tuong_mau_sac": "Vàng, nâu",
        "tuong_so": "2, 5, 8, 10",
        "tinh_chat": "Nhu hòa, chịu đựng, nuôi dưỡng, bao dung",
        "khi_vuong": "Ổn định, phát triển từ từ, được nhiều người giúp",
        "khi_suy": "Chậm chạp, bị áp đặt, thiếu quyết đoán"
    },
    
    "Chấn": {
        "so": 4,
        "hanh": "Mộc",
        "tuong_nguoi": "Con trai cả, người trẻ năng động",
        "tuong_vat": "Cây cối, tre trúc, nhạc cụ, điện thoại",
        "tuong_than_the": "Chân, gan, hệ thần kinh",
        "tuong_dong_vat": "Rồng, rắn",
        "tuong_thoi_tiet": "Sấm sét, mưa giông",
        "tuong_phuong_vi": "Đông",
        "tuong_mau_sac": "Xanh lá đậm",
        "tuong_so": "3, 4, 8",
        "tinh_chat": "Chuyển động, phát triển, năng động, đột biến",
        "khi_vuong": "Phát triển nhanh, thay đổi tốt, năng động",
        "khi_suy": "Bất ổn, thay đổi xấu, sợ hãi"
    },
    
    "Tốn": {
        "so": 5,
        "hanh": "Mộc",
        "tuong_nguoi": "Con gái cả, người khiêm tốn, thương nhân",
        "tuong_vat": "Gió, hương thơm, dây thừng, hàng hóa",
        "tuong_than_the": "Đùi, mông, hệ hô hấp",
        "tuong_dong_vat": "Gà, chim",
        "tuong_thoi_tiet": "Gió, mát mẻ",
        "tuong_phuong_vi": "Đông Nam",
        "tuong_mau_sac": "Xanh lá nhạt",
        "tuong_so": "3, 4, 5",
        "tinh_chat": "Linh hoạt, khiêm tốn, thấu hiểu, lan tỏa",
        "khi_vuong": "Kinh doanh tốt, giao tiếp tốt, linh hoạt",
        "khi_suy": "Do dự, thiếu quyết đoán, bị lợi dụng"
    },
    
    "Khảm": {
        "so": 6,
        "hanh": "Thủy",
        "tuong_nguoi": "Con trai giữa, người thông minh, người làm việc với nước",
        "tuong_vat": "Nước, rượu, mực, dầu",
        "tuong_than_the": "Tai, thận, hệ tiết niệu, máu",
        "tuong_dong_vat": "Heo, chuột, cá",
        "tuong_thoi_tiet": "Mưa, tuyết, lạnh",
        "tuong_phuong_vi": "Bắc",
        "tuong_mau_sac": "Đen, xanh đen",
        "tuong_so": "1, 6",
        "tinh_chat": "Hiểm trở, thông minh, khó khăn, lưu động",
        "khi_vuong": "Thông minh, linh hoạt, vượt qua khó khăn",
        "khi_suy": "Gặp hiểm nguy, khó khăn, bệnh tật"
    },
    
    "Ly": {
        "so": 3,
        "hanh": "Hỏa",
        "tuong_nguoi": "Con gái giữa, người đẹp, người văn hóa",
        "tuong_vat": "Lửa, đèn, sách vở, văn thư",
        "tuong_than_the": "Mắt, tim, hệ tuần hoàn",
        "tuong_dong_vat": "Chim phượng, rùa, cua",
        "tuong_thoi_tiet": "Nắng, nóng, khô",
        "tuong_phuong_vi": "Nam",
        "tuong_mau_sac": "Đỏ, tím",
        "tuong_so": "2, 3, 7, 9",
        "tinh_chat": "Sáng sủa, văn minh, rực rỡ, nóng nảy",
        "khi_vuong": "Thông minh, nổi tiếng, văn hóa cao",
        "khi_suy": "Nóng nảy, tranh cãi, bệnh tim mắt"
    },
    
    "Cấn": {
        "so": 7,
        "hanh": "Thổ",
        "tuong_nguoi": "Con trai út, người trẻ tuổi, người giữ của",
        "tuong_vat": "Núi, đá, nhà cửa, kho tàng",
        "tuong_than_the": "Tay, lưng, xương sống",
        "tuong_dong_vat": "Chó, chuột",
        "tuong_thoi_tiet": "Mây, sương mù",
        "tuong_phuong_vi": "Đông Bắc",
        "tuong_mau_sac": "Vàng, nâu",
        "tuong_so": "5, 7, 10",
        "tinh_chat": "Dừng lại, ổn định, giữ gìn, bảo thủ",
        "khi_vuong": "Ổn định, giữ được của, an toàn",
        "khi_suy": "Bế tắc, không tiến bộ, cứng nhắc"
    },
    
    "Đoài": {
        "so": 2,
        "hanh": "Kim",
        "tuong_nguoi": "Con gái út, người vui vẻ, ca sĩ, diễn viên",
        "tuong_vat": "Trạch, ao, miệng, lời nói",
        "tuong_than_the": "Miệng, lưỡi, răng, hệ hô hấp",
        "tuong_dong_vat": "Dê, cá",
        "tuong_thoi_tiet": "Mưa nhỏ, sương",
        "tuong_phuong_vi": "Tây",
        "tuong_mau_sac": "Trắng",
        "tuong_so": "2, 4, 9",
        "tinh_chat": "Vui vẻ, giao tiếp, hòa thuận, thuyết phục",
        "khi_vuong": "Vui vẻ, giao tiếp tốt, thành công trong đàm phán",
        "khi_suy": "Nói nhiều, thị phi, tranh cãi"
    }
}

# Hàm lấy thông tin chi tiết
def lay_thong_tin_luc_hao_qua(so_qua):
    """Lấy thông tin chi tiết về quẻ từ knowledge base"""
    return LUC_HAO_64_QUA_CHI_TIET.get(so_qua, {})

def lay_thong_tin_luc_than(ten_luc_than):
    """Lấy thông tin chi tiết về Lục Thân"""
    return LUC_THAN_CHI_TIET.get(ten_luc_than, {})

def lay_thong_tin_luc_than_item(ten_luc_than):
    """Lấy thông tin chi tiết về Lục Thần"""
    return LUC_THAN_CHI_TIET.get(ten_luc_than, {})

def lay_thong_tin_bat_quai_tuong_so(ten_qua):
    """Lấy thông tin chi tiết về Bát Quái tượng số"""
    return BAT_QUAI_TUONG_SO_CHI_TIET.get(ten_qua, {})

# Test
if __name__ == "__main__":
    print("=== TEST KNOWLEDGE BASE ===\n")
    
    # Test Lục Hào
    qua_1 = lay_thong_tin_luc_hao_qua(1)
    print(f"Quẻ 1 - {qua_1['ten']}:")
    print(f"  Kinh doanh: {qua_1['kinh_doanh']}")
    print(f"  Hôn nhân: {qua_1['hon_nhan']}")
    print()
    
    # Test Lục Thân
    phu_mau = lay_thong_tin_luc_than("Phụ Mẫu")
    print(f"Phụ Mẫu:")
    print(f"  Kinh doanh: {phu_mau['kinh_doanh']}")
    print(f"  Khi vượng: {phu_mau['vuong']}")
    print()
    
    # Test Bát Quái
    can = lay_thong_tin_bat_quai_tuong_so("Càn")
    print(f"Càn:")
    print(f"  Tượng người: {can['tuong_nguoi']}")
    print(f"  Tính chất: {can['tinh_chat']}")
    
    print("\n✅ Knowledge Base hoạt động tốt!")
