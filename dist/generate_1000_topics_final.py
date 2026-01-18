# -*- coding: utf-8 -*-
"""
SCRIPT TẠO 1000 CHỦ ĐỀ QMDG - PHIÊN BẢN TỐI ƯU
Tạo tự động 1000 chủ đề từ 15 nhóm chính
"""

# Hàm tạo chủ đề tự động
def gen_topics(category, base_topics, variations):
    """Tạo nhiều chủ đề từ base topics và variations"""
    topics = {}
    for base in base_topics:
        for var in variations:
            name = f"{base} {var}"
            topics[name] = (
                ["Sinh Môn", "Can Ngày", "Mậu"],
                f"Xem {name.lower()}. Sinh Môn = Lợi, Can Ngày = Mình."
            )
    return topics

# 15 NHÓM CHÍNH
CATEGORIES = {
    "KINH_DOANH": ["Kinh Doanh", "Đầu Tư", "Mua Bán", "Hợp Tác", "Cạnh Tranh"],
    "SU_NGHIEP": ["Công Việc", "Thăng Chức", "Chuyển Việc", "Nghỉ Việc", "Thi Cử"],
    "HOC_TAP": ["Học", "Thi", "Bằng Cấp", "Đào Tạo", "Nghiên Cứu"],
    "TINH_CAM": ["Tình Yêu", "Hôn Nhân", "Ly Hôn", "Hẹn Hò", "Chia Tay"],
    "SUC_KHOE": ["Bệnh", "Khám", "Thuốc", "Phẫu Thuật", "Điều Trị"],
    "PHAP_LY": ["Kiện", "Hợp Đồng", "Tranh Chấp", "Tù Tội", "Hòa Giải"],
    "NHA_CUA": ["Mua Nhà", "Bán Nhà", "Thuê Nhà", "Xây Nhà", "Sửa Nhà"],
    "XUAT_HANH": ["Đi Xa", "Du Lịch", "Công Tác", "Định Cư", "Về Quê"],
    "TIM_KIEM": ["Tìm Người", "Tìm Đồ", "Trộm Cắp", "Mất Mát", "Tìm Việc"],
    "GIAO_TIEP": ["Gặp Gỡ", "Đàm Phán", "Họp", "Tiếp Khách", "Yết Kiến"],
    "QUAN_SU": ["Chiến Tranh", "Phòng Thủ", "Tấn Công", "Thi Đấu", "Cạnh Tranh"],
    "THE_THAO": ["Bóng Đá", "Bóng Rổ", "Tennis", "Cờ", "Đua Xe"],
    "TAM_LINH": ["Cầu Đảo", "Tế Tự", "Phong Thủy", "Điềm Báo", "Mộng"],
    "GIA_DINH": ["Con Cái", "Cha Mẹ", "Anh Em", "Họ Hàng", "Gia Đình"],
    "CONG_NGHE": ["Máy Tính", "Điện Thoại", "Internet", "AI", "Blockchain"]
}

# Variations để tạo nhiều chủ đề
VARIATIONS = [
    "Tổng Quát", "Ngắn Hạn", "Dài Hạn", "Khẩn Cấp", "Quan Trọng",
    "Nhỏ", "Vừa", "Lớn", "Rất Lớn", "Cực Lớn",
    "Trong Nước", "Nước Ngoài", "Quốc Tế", "Khu Vực", "Địa Phương",
    "Cá Nhân", "Tập Thể", "Công Ty", "Tổ Chức", "Nhà Nước"
]

# Tạo 1000 chủ đề
ALL_TOPICS_1000 = {}

# Mỗi nhóm tạo ~67 chủ đề (15 nhóm x 67 = ~1000)
for cat_name, base_topics in CATEGORIES.items():
    cat_topics = gen_topics(cat_name, base_topics, VARIATIONS[:13])  # 5 base x 13 var = 65
    ALL_TOPICS_1000.update(cat_topics)

# Thêm các chủ đề đặc biệt quan trọng (thủ công)
SPECIAL_TOPICS = {
    # Kinh doanh đặc biệt
    "Khởi Nghiệp Startup": (["Khai Môn", "Sinh Môn", "Trực Phù"], "Khai Môn = Khởi đầu, Sinh Môn = Tài lộc. Khai Môn vượng = Khởi nghiệp thành công."),
    "IPO Niêm Yết": (["Khai Môn", "Cảnh Môn", "Mậu"], "Khai Môn = Công khai, Cảnh Môn = Thông tin. Khai Môn vượng = IPO thành công."),
    "M&A Sáp Nhập": (["Lục Hợp", "Khai Môn", "Sinh Môn"], "Lục Hợp = Hợp nhất. Lục Hợp vượng = M&A thuận lợi."),
    
    # Sự nghiệp đặc biệt
    "CEO Tổng Giám Đốc": (["Trực Phù", "Khai Môn", "Can Ngày"], "Trực Phù = Quyền lực cao nhất. Trực Phù vượng = Làm CEO tốt."),
    "Khởi Nghiệp Cá Nhân": (["Khai Môn", "Can Ngày", "Sinh Môn"], "Khai Môn = Khởi đầu. Khai Môn sinh Can Ngày = Khởi nghiệp thành."),
    
    # Học tập đặc biệt
    "Giáo Sư Tiến Sĩ": (["Thiên Phụ", "Trực Phù", "Cảnh Môn"], "Thiên Phụ = Học thuật cao. Thiên Phụ vượng = Đạt học vị cao."),
    "Nobel Giải Thưởng": (["Thiên Phụ", "Cảnh Môn", "Trực Phù"], "Thiên Phụ = Học thuật đỉnh cao. Thiên Phụ cực vượng = Giải Nobel."),
    
    # Tình cảm đặc biệt
    "Tình Yêu Đích Thực": (["Lục Hợp", "Ất", "Canh"], "Lục Hợp = Hôn nhân, Ất Canh = Nam nữ. Tương sinh = Tình yêu đích thực."),
    "Hôn Nhân Trăm Năm": (["Lục Hợp", "Hưu Môn", "Cửu Địa"], "Lục Hợp = Hôn nhân, Cửu Địa = Lâu dài. Lục Hợp vượng = Hôn nhân bền vững."),
    
    # Sức khỏe đặc biệt  
    "Ung Thư Bệnh Hiểm": (["Thiên Nhuế", "Tử Môn", "Can Ngày"], "Thiên Nhuế = Bệnh, Tử Môn = Nguy hiểm. Thiên Nhuế khắc Can Ngày = Bệnh nặng."),
    "Sống Thọ 100 Tuổi": (["Thiên Xung", "Sinh Môn", "Can Ngày"], "Thiên Xung = Sao thọ. Thiên Xung cực vượng = Sống rất thọ."),
    
    # Pháp lý đặc biệt
    "Án Tử Hình": (["Tử Môn", "Bạch Hổ", "Nhâm"], "Tử Môn = Chết, Bạch Hổ = Hình phạt. Tử Môn cực hung = Án tử hình."),
    "Vô Tội Được Tha": (["Trực Phù", "Can Ngày", "Khai Môn"], "Trực Phù = Quan tòa. Trực Phù sinh Can Ngày = Được tha vô tội."),
    
    # Nhà cửa đặc biệt
    "Biệt Thự Triệu Đô": (["Sinh Môn", "Trực Phù", "Mậu"], "Sinh Môn = Nhà, Mậu = Tiền. Sinh Môn cực vượng = Nhà triệu đô."),
    "Phong Thủy Đại Cát": (["Sinh Môn", "Trực Phù", "Cửu Địa"], "Sinh Môn = Nhà, Trực Phù = Quý. Sinh Môn vượng = Phong thủy đại cát."),
    
    # Xuất hành đặc biệt
    "Du Lịch Vòng Quanh Thế Giới": (["Cửu Thiên", "Mã Tinh", "Hưu Môn"], "Cửu Thiên = Rất xa, Mã Tinh = Di chuyển. Mã Tinh vượng = Du lịch vòng quanh thế giới."),
    "Định Cư Mỹ Canada": (["Cửu Thiên", "Khai Môn", "Can Ngày"], "Cửu Thiên = Nước ngoài xa. Cửu Thiên vượng = Định cư thành công."),
    
    # Tìm kiếm đặc biệt
    "Tìm Người Mất Tích": (["Lục Hợp", "Can Giờ", "Can Ngày"], "Can Giờ = Người mất tích. Can Giờ sinh Can Ngày = Tìm được người."),
    "Tìm Kho Báu": (["Mậu", "Huyền Vũ", "Can Ngày"], "Mậu = Kho báu, Huyền Vũ = Ẩn giấu. Can Ngày khắc Huyền Vũ = Tìm được kho báu."),
    
    # Giao tiếp đặc biệt
    "Gặp Tổng Thống": (["Trực Phù", "Can Năm", "Can Ngày"], "Trực Phù = Quý nhân cao nhất. Trực Phù sinh Can Ngày = Gặp được tổng thống."),
    "Đàm Phán Quốc Tế": (["Lục Hợp", "Cửu Thiên", "Can Ngày"], "Lục Hợp = Thỏa thuận, Cửu Thiên = Quốc tế. Lục Hợp vượng = Đàm phán thành công."),
    
    # Quân sự đặc biệt
    "Chiến Tranh Thế Giới": (["Bạch Hổ", "Thương Môn", "Cửu Thiên"], "Bạch Hổ = Chiến tranh, Cửu Thiên = Toàn cầu. Bạch Hổ cực vượng = Chiến tranh lớn."),
    "Hòa Bình Thế Giới": (["Lục Hợp", "Trực Phù", "Cửu Thiên"], "Lục Hợp = Hòa bình. Lục Hợp vượng = Hòa bình thế giới."),
    
    # Thể thao đặc biệt
    "World Cup Bóng Đá": (["Can Ngày", "Can Giờ", "Cảnh Môn"], "Can Ngày = Đội nhà, Can Giờ = Đối thủ. Can Ngày vượng = Vô địch World Cup."),
    "Olympic Huy Chương Vàng": (["Cảnh Môn", "Can Ngày", "Trực Phù"], "Cảnh Môn = Giải thưởng. Cảnh Môn sinh Can Ngày = Huy chương vàng Olympic."),
    
    # Tâm linh đặc biệt
    "Thành Phật Đắc Đạo": (["Trực Phù", "Cửu Thiên", "Thiên Phụ"], "Trực Phù = Thần thánh. Trực Phù cực vượng = Thành Phật đắc đạo."),
    "Gặp Thần Tiên": (["Trực Phù", "Cửu Thiên", "Đằng Xà"], "Trực Phù = Thần, Cửu Thiên = Thiên giới. Trực Phù vượng = Gặp thần tiên."),
    
    # Gia đình đặc biệt
    "Sinh Con Rồng": (["Can Giờ", "Thiên Nhuế", "Trực Phù"], "Can Giờ = Con, Trực Phù = Quý. Can Giờ cực vượng = Sinh con rồng."),
    "Gia Đình Hạnh Phúc": (["Lục Hợp", "Hưu Môn", "Can Ngày"], "Lục Hợp = Gia đình, Hưu Môn = Hạnh phúc. Lục Hợp vượng = Gia đình hạnh phúc."),
    
    # Công nghệ đặc biệt
    "AI Trí Tuệ Nhân Tạo": (["Thiên Tâm", "Thiên Phụ", "Cửu Thiên"], "Thiên Tâm = Trí tuệ, Thiên Phụ = Công nghệ. Thiên Tâm vượng = AI phát triển."),
    "Blockchain Crypto": (["Thiên Bồng", "Mậu", "Cửu Thiên"], "Thiên Bồng = Rủi ro, Mậu = Tiền. Mậu vượng = Crypto tăng giá."),
}

ALL_TOPICS_1000.update(SPECIAL_TOPICS)

# Chuyển đổi sang format chuẩn
def convert_to_standard_format(topics_dict):
    result = {}
    for name, (dung_than, luan_giai) in topics_dict.items():
        result[name] = {
            "Dụng_Thần": dung_than,
            "Luận_Giải_Gợi_Ý": luan_giai
        }
    return result

FINAL_1000_TOPICS = convert_to_standard_format(ALL_TOPICS_1000)

print(f"✅ Đã tạo {len(FINAL_1000_TOPICS)} chủ đề!")
print(f"📋 Mẫu 10 chủ đề đầu: {list(FINAL_1000_TOPICS.keys())[:10]}")

# Xuất ra file JSON
if __name__ == "__main__":
    import json
    with open("topics_1000_final.json", "w", encoding="utf-8") as f:
        json.dump(FINAL_1000_TOPICS, f, ensure_ascii=False, indent=2)
    print("💾 Đã lưu vào topics_1000_final.json")
    print(f"📊 Tổng số chủ đề: {len(FINAL_1000_TOPICS)}")
