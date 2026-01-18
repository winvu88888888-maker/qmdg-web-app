# -*- coding: utf-8 -*-
"""
DATABASE TƯƠNG TÁC ĐA TẦNG
Chứa ma trận tương tác giữa các yếu tố trong Kỳ Môn Độn Giáp
"""

# ============================================================================
# PHẦN 1: LỤC THÂN (SIX RELATIVES) - MAPPING
# ============================================================================

LUC_THAN_MAPPING = {
    "Bản thân": {
        "type": "Tỷ Kiếp",
        "quan_he_ngu_hanh": "cung_hanh",  # Cùng hành
        "icon": "🧑",
        "mau_sac": "#4CAF50",
        "mo_ta": "Chính mình, sức mạnh bản thân"
    },
    "Anh chị em": {
        "type": "Tỷ Kiếp",
        "quan_he_ngu_hanh": "cung_hanh",
        "icon": "👨‍👩‍👧",
        "mau_sac": "#4CAF50",
        "mo_ta": "Anh em ruột thịt, bạn bè đồng hành"
    },
    "Bố mẹ": {
        "type": "Phụ Mẫu",
        "quan_he_ngu_hanh": "sinh_ta",  # Hành sinh ta
        "icon": "👴👵",
        "mau_sac": "#2196F3",
        "mo_ta": "Cha mẹ, bề trên, quý nhân phù trợ"
    },
    "Con cái": {
        "type": "Tử Tôn",
        "quan_he_ngu_hanh": "ta_sinh",  # Ta sinh hành
        "icon": "👶",
        "mau_sac": "#FF9800",
        "mo_ta": "Con cái, học trò, người dưới quyền"
    },
    "Người ngoài (Quan)": {
        "type": "Quan Quỷ",
        "quan_he_ngu_hanh": "khac_ta",  # Hành khắc ta
        "icon": "🤝",
        "mau_sac": "#F44336",
        "mo_ta": "Quan phủ, đối thủ, áp lực từ bên ngoài"
    },
    "Người ngoài (Tài)": {
        "type": "Thê Tài",
        "quan_he_ngu_hanh": "ta_khac",  # Ta khắc hành
        "icon": "💰",
        "mau_sac": "#9C27B0",
        "mo_ta": "Tài lộc, vợ chồng, tài sản kiểm soát được"
    }
}

# ============================================================================
# PHẦN 1.5: LIÊN KẾT LỤC THÂN VỚI CHỦ ĐỀ (LOGIC TỰ ĐỘNG)
# ============================================================================

LUC_THAN_THEO_CHU_DE = {
    # Con cái
    "Con cái": ["Con cái", "Con", "Học hành", "Thi cử", "Du học", "Giáo dục"],
    
    # Bố mẹ
    "Bố mẹ": ["Bố mẹ", "Cha mẹ", "Phụ mẫu", "Ông bà", "Tổ tiên", "Hiếu đạo"],
    
    # Anh chị em
    "Anh chị em": ["Anh chị em", "Anh em", "Bạn bè", "Đồng nghiệp", "Đối tác", "Hợp tác"],
    
    # Người ngoài (Quan)
    "Người ngoài (Quan)": ["Kiện tụng", "Quan phủ", "Chính quyền", "Pháp luật", "Đối thủ", "Cạnh tranh", "Kẻ thù"],
    
    # Người ngoài (Tài)
    "Người ngoài (Tài)": ["Kinh doanh", "Đầu tư", "Tài chính", "Tiền bạc", "Mua bán", "Giao dịch", "Khách hàng"],
    
    # Bản thân (mặc định)
    "Bản thân": ["Sức khỏe", "Vận mệnh", "Tổng quát", "Bản thân", "Cá nhân", "Tâm lý", "Tinh thần"]
}

# Hàm tự động chọn đối tượng dựa trên chủ đề
def goi_y_doi_tuong_theo_chu_de(chu_de):
    """
    Gợi ý đối tượng phù hợp dựa trên chủ đề
    
    Args:
        chu_de: Tên chủ đề
    
    Returns:
        str: Tên đối tượng gợi ý (VD: "Con cái", "Bản thân")
    """
    chu_de_lower = chu_de.lower()
    
    # Duyệt qua từng loại đối tượng
    for doi_tuong, keywords in LUC_THAN_THEO_CHU_DE.items():
        for keyword in keywords:
            if keyword.lower() in chu_de_lower:
                return doi_tuong
    
    # Mặc định
    return "Bản thân"


# ============================================================================
# PHẦN 2: MA TRẬN SINH KHẮC CHI TIẾT (25 TỔ HỢP)
# ============================================================================

SINH_KHAC_MATRIX = {
    # Mộc
    ("Mộc", "Mộc"): {
        "quan_he": "Tỷ Kiếp",
        "loai": "cung_hanh",
        "diem": 70,
        "y_nghia": "Ngang hàng, cạnh tranh, chia sẻ nguồn lực",
        "loi_khuyen": "Hợp tác tốt hơn cạnh tranh"
    },
    ("Mộc", "Hỏa"): {
        "quan_he": "Tử Tôn",
        "loai": "ta_sinh",
        "diem": 85,
        "y_nghia": "Ta sinh, tốn sức nhưng có lợi, phát triển tốt",
        "loi_khuyen": "Đầu tư vào con cái/dự án sẽ thành công"
    },
    ("Mộc", "Thổ"): {
        "quan_he": "Thê Tài",
        "loai": "ta_khac",
        "diem": 80,
        "y_nghia": "Ta khắc, có lợi về tài, kiểm soát được",
        "loi_khuyen": "Thời điểm tốt để kiếm tiền, đầu tư"
    },
    ("Mộc", "Kim"): {
        "quan_he": "Quan Quỷ",
        "loai": "khac_ta",
        "diem": 40,
        "y_nghia": "Khắc ta, áp lực lớn, gặp khó khăn",
        "loi_khuyen": "Cẩn thận với đối thủ, quan phủ"
    },
    ("Mộc", "Thủy"): {
        "quan_he": "Phụ Mẫu",
        "loai": "sinh_ta",
        "diem": 90,
        "y_nghia": "Sinh ta, được hỗ trợ, quý nhân phù trợ",
        "loi_khuyen": "Nhờ vả bề trên, cha mẹ sẽ được giúp đỡ"
    },
    
    # Hỏa
    ("Hỏa", "Mộc"): {
        "quan_he": "Phụ Mẫu",
        "loai": "sinh_ta",
        "diem": 90,
        "y_nghia": "Sinh ta, được nuôi dưỡng, hỗ trợ mạnh",
        "loi_khuyen": "Dựa vào nguồn lực sẵn có"
    },
    ("Hỏa", "Hỏa"): {
        "quan_he": "Tỷ Kiếp",
        "loai": "cung_hanh",
        "diem": 70,
        "y_nghia": "Ngang hàng, cạnh tranh gay gắt",
        "loi_khuyen": "Tránh xung đột nội bộ"
    },
    ("Hỏa", "Thổ"): {
        "quan_he": "Tử Tôn",
        "loai": "ta_sinh",
        "diem": 85,
        "y_nghia": "Ta sinh, tạo ra kết quả tốt",
        "loi_khuyen": "Đầu tư sẽ sinh lời"
    },
    ("Hỏa", "Kim"): {
        "quan_he": "Thê Tài",
        "loai": "ta_khac",
        "diem": 80,
        "y_nghia": "Ta khắc, thu về tài lộc",
        "loi_khuyen": "Thời điểm tốt để gặt hái"
    },
    ("Hỏa", "Thủy"): {
        "quan_he": "Quan Quỷ",
        "loai": "khac_ta",
        "diem": 35,
        "y_nghia": "Khắc ta mạnh, bị dập tắt, thất bại",
        "loi_khuyen": "Tránh đối đầu trực tiếp"
    },
    
    # Thổ
    ("Thổ", "Mộc"): {
        "quan_he": "Quan Quỷ",
        "loai": "khac_ta",
        "diem": 40,
        "y_nghia": "Khắc ta, bị xâm lấn, mất quyền lợi",
        "loi_khuyen": "Bảo vệ lợi ích của mình"
    },
    ("Thổ", "Hỏa"): {
        "quan_he": "Phụ Mẫu",
        "loai": "sinh_ta",
        "diem": 90,
        "y_nghia": "Sinh ta, được tiếp sức, phát triển",
        "loi_khuyen": "Nhận sự giúp đỡ từ quý nhân"
    },
    ("Thổ", "Thổ"): {
        "quan_he": "Tỷ Kiếp",
        "loai": "cung_hanh",
        "diem": 70,
        "y_nghia": "Ngang hàng, ổn định nhưng ít biến động",
        "loi_khuyen": "Hợp tác để tăng sức mạnh"
    },
    ("Thổ", "Kim"): {
        "quan_he": "Tử Tôn",
        "loai": "ta_sinh",
        "diem": 85,
        "y_nghia": "Ta sinh, nuôi dưỡng thành công",
        "loi_khuyen": "Đầu tư dài hạn sẽ tốt"
    },
    ("Thổ", "Thủy"): {
        "quan_he": "Thê Tài",
        "loai": "ta_khac",
        "diem": 75,
        "y_nghia": "Ta khắc, kiểm soát tài lộc nhưng khó khăn",
        "loi_khuyen": "Cần nỗ lực để giữ tài"
    },
    
    # Kim
    ("Kim", "Mộc"): {
        "quan_he": "Thê Tài",
        "loai": "ta_khac",
        "diem": 80,
        "y_nghia": "Ta khắc, thu về lợi nhuận lớn",
        "loi_khuyen": "Thời điểm vàng để kiếm tiền"
    },
    ("Kim", "Hỏa"): {
        "quan_he": "Quan Quỷ",
        "loai": "khac_ta",
        "diem": 35,
        "y_nghia": "Khắc ta, bị nung chảy, tổn thất",
        "loi_khuyen": "Tránh rủi ro, bảo toàn vốn"
    },
    ("Kim", "Thổ"): {
        "quan_he": "Phụ Mẫu",
        "loai": "sinh_ta",
        "diem": 90,
        "y_nghia": "Sinh ta, được nuôi dưỡng, tăng trưởng",
        "loi_khuyen": "Dựa vào nền tảng vững chắc"
    },
    ("Kim", "Kim"): {
        "quan_he": "Tỷ Kiếp",
        "loai": "cung_hanh",
        "diem": 70,
        "y_nghia": "Ngang hàng, cạnh tranh quyết liệt",
        "loi_khuyen": "Liên minh thay vì đối đầu"
    },
    ("Kim", "Thủy"): {
        "quan_he": "Tử Tôn",
        "loai": "ta_sinh",
        "diem": 85,
        "y_nghia": "Ta sinh, tạo ra giá trị mới",
        "loi_khuyen": "Đầu tư vào sáng tạo"
    },
    
    # Thủy
    ("Thủy", "Mộc"): {
        "quan_he": "Tử Tôn",
        "loai": "ta_sinh",
        "diem": 85,
        "y_nghia": "Ta sinh, nuôi dưỡng phát triển",
        "loi_khuyen": "Hỗ trợ người khác sẽ được đền đáp"
    },
    ("Thủy", "Hỏa"): {
        "quan_he": "Thê Tài",
        "loai": "ta_khac",
        "diem": 75,
        "y_nghia": "Ta khắc, kiểm soát nhưng tốn năng lượng",
        "loi_khuyen": "Cân bằng giữa kiểm soát và linh hoạt"
    },
    ("Thủy", "Thổ"): {
        "quan_he": "Quan Quỷ",
        "loai": "khac_ta",
        "diem": 40,
        "y_nghia": "Khắc ta, bị ngăn chặn, khó lưu thông",
        "loi_khuyen": "Tìm đường vòng, tránh đối đầu"
    },
    ("Thủy", "Kim"): {
        "quan_he": "Phụ Mẫu",
        "loai": "sinh_ta",
        "diem": 90,
        "y_nghia": "Sinh ta, nguồn lực dồi dào",
        "loi_khuyen": "Tận dụng cơ hội tốt"
    },
    ("Thủy", "Thủy"): {
        "quan_he": "Tỷ Kiếp",
        "loai": "cung_hanh",
        "diem": 70,
        "y_nghia": "Ngang hàng, hòa hợp nhưng thiếu động lực",
        "loi_khuyen": "Cần thêm sự thúc đẩy từ bên ngoài"
    }
}

# ============================================================================
# PHẦN 3: MA TRẬN TƯƠNG TÁC SAO-MÔN (CỬU TINH x BÁT MÔN)
# ============================================================================

TUONG_TAC_SAO_MON = {
    # Thiên Phụ (Tài lộc)
    ("Thiên Phụ", "Sinh"): {"diem": 95, "y_nghia": "Cực kỳ tốt, tài lộc dồi dào, sinh sôi nảy nở"},
    ("Thiên Phụ", "Khai"): {"diem": 88, "y_nghia": "Mở rộng kinh doanh, cơ hội tài chính tốt"},
    ("Thiên Phụ", "Tử"): {"diem": 30, "y_nghia": "Tài lộc bị đóng băng, khó khăn tài chính"},
    ("Thiên Phụ", "Thương"): {"diem": 55, "y_nghia": "Tài lộc có nhưng tranh chấp, kiện tụng"},
    ("Thiên Phụ", "Cảnh"): {"diem": 75, "y_nghia": "Tài lộc ổn định, cảnh quan tốt"},
    ("Thiên Phụ", "Du"): {"diem": 65, "y_nghia": "Tài lộc lưu động, không ổn định"},
    ("Thiên Phụ", "Kinh"): {"diem": 45, "y_nghia": "Tài lộc bị sốc, biến động mạnh"},
    ("Thiên Phụ", "Tử (Tử Môn)"): {"diem": 30, "y_nghia": "Tài lộc bế tắc, nguy hiểm"},
    
    # Thiên Tâm (Trí tuệ)
    ("Thiên Tâm", "Sinh"): {"diem": 90, "y_nghia": "Trí tuệ sáng tạo, ý tưởng mới nảy sinh"},
    ("Thiên Tâm", "Khai"): {"diem": 92, "y_nghia": "Mở mang trí tuệ, học hỏi tốt"},
    ("Thiên Tâm", "Tử"): {"diem": 40, "y_nghia": "Tư duy bị hạn chế, khó suy nghĩ"},
    ("Thiên Tâm", "Thương"): {"diem": 60, "y_nghia": "Tranh luận, biện bác tốt"},
    ("Thiên Tâm", "Cảnh"): {"diem": 85, "y_nghia": "Tư duy rõ ràng, sáng suốt"},
    ("Thiên Tâm", "Du"): {"diem": 70, "y_nghia": "Tư duy linh hoạt, thích ứng"},
    ("Thiên Tâm", "Kinh"): {"diem": 50, "y_nghia": "Tư duy bất ổn, lo lắng"},
    ("Thiên Tâm", "Tử (Tử Môn)"): {"diem": 35, "y_nghia": "Tư duy tiêu cực, nguy hiểm"},
    
    # Thiên Nhuế (Bệnh tật, tình duyên)
    ("Thiên Nhuế", "Sinh"): {"diem": 65, "y_nghia": "Bệnh nhẹ, tình duyên phát triển chậm"},
    ("Thiên Nhuế", "Khai"): {"diem": 70, "y_nghia": "Mở lòng, tình cảm dễ bộc lộ"},
    ("Thiên Nhuế", "Tử"): {"diem": 25, "y_nghia": "Bệnh nặng, tình duyên bế tắc"},
    ("Thiên Nhuế", "Thương"): {"diem": 40, "y_nghia": "Tình duyên tranh cãi, bệnh tật kéo dài"},
    ("Thiên Nhuế", "Cảnh"): {"diem": 75, "y_nghia": "Tình duyên đẹp, sức khỏe ổn"},
    ("Thiên Nhuế", "Du"): {"diem": 55, "y_nghia": "Tình duyên lưu động, không ổn định"},
    ("Thiên Nhuế", "Kinh"): {"diem": 35, "y_nghia": "Sốc về tình cảm, bệnh đột ngột"},
    ("Thiên Nhuế", "Tử (Tử Môn)"): {"diem": 20, "y_nghia": "Tình duyên tan vỡ, bệnh nguy hiểm"},
    
    # Thiên Anh (Quân sự, tranh đấu)
    ("Thiên Anh", "Sinh"): {"diem": 85, "y_nghia": "Sức mạnh tăng trưởng, chiến thắng"},
    ("Thiên Anh", "Khai"): {"diem": 90, "y_nghia": "Mở màn tốt, khởi đầu thuận lợi"},
    ("Thiên Anh", "Tử"): {"diem": 35, "y_nghia": "Bế tắc, không thể tiến công"},
    ("Thiên Anh", "Thương"): {"diem": 80, "y_nghia": "Chiến đấu quyết liệt, thắng lợi"},
    ("Thiên Anh", "Cảnh"): {"diem": 70, "y_nghia": "Uy thế, danh vọng"},
    ("Thiên Anh", "Du"): {"diem": 65, "y_nghia": "Linh hoạt trong chiến thuật"},
    ("Thiên Anh", "Kinh"): {"diem": 75, "y_nghia": "Tấn công bất ngờ hiệu quả"},
    ("Thiên Anh", "Tử (Tử Môn)"): {"diem": 40, "y_nghia": "Nguy hiểm, có thể thất bại"},
}

# ============================================================================
# PHẦN 4: QUY TẮC CHỌN DỤNG THẦN THEO CHỦ ĐỀ
# ============================================================================

QUY_TAC_CHON_DUNG_THAN = {
    "Kinh Doanh": {
        "dung_than_chinh": "Thiên Phụ",
        "dung_than_phu": ["Thiên Tâm", "Thiên Anh"],
        "cung_uu_tien": ["Cấn 8", "Khôn 2"],
        "ngu_hanh_tot": ["Kim", "Thổ"],
        "trong_so": 1.0
    },
    "Đầu Tư": {
        "dung_than_chinh": "Thiên Phụ",
        "dung_than_phu": ["Thiên Tâm"],
        "cung_uu_tien": ["Cấn 8", "Đoài 7"],
        "ngu_hanh_tot": ["Kim", "Thủy"],
        "trong_so": 1.0
    },
    "Hôn Nhân": {
        "dung_than_chinh": "Thiên Nhuế",
        "dung_than_phu": ["Thiên Phụ"],
        "cung_uu_tien": ["Khảm 1", "Ly 9"],
        "ngu_hanh_tot": ["Hỏa", "Thủy"],
        "trong_so": 1.0
    },
    "Sức Khỏe": {
        "dung_than_chinh": "Thiên Anh",
        "dung_than_phu": ["Thiên Nhuế"],
        "cung_uu_tien": ["Chấn 3", "Tốn 4"],
        "ngu_hanh_tot": ["Mộc", "Hỏa"],
        "trong_so": 1.0
    },
    "Học Tập": {
        "dung_than_chinh": "Thiên Tâm",
        "dung_than_phu": ["Thiên Phụ"],
        "cung_uu_tien": ["Tốn 4", "Ly 9"],
        "ngu_hanh_tot": ["Mộc", "Hỏa"],
        "trong_so": 1.0
    },
    "Công Danh": {
        "dung_than_chinh": "Thiên Anh",
        "dung_than_phu": ["Thiên Tâm", "Thiên Phụ"],
        "cung_uu_tien": ["Ly 9", "Khảm 1"],
        "ngu_hanh_tot": ["Hỏa", "Kim"],
        "trong_so": 1.0
    }
}

# ============================================================================
# PHẦN 5: ẢNH HƯỞNG THỜI GIAN (MÙA, THÁNG, GIỜ)
# ============================================================================

ANH_HUONG_MUA = {
    "Xuân": {
        "Mộc": 1.3,  # Vượng
        "Hỏa": 1.1,  # Tướng
        "Thổ": 0.9,  # Tử
        "Kim": 0.7,  # Tù
        "Thủy": 1.0  # Hưu
    },
    "Hạ": {
        "Mộc": 1.0,
        "Hỏa": 1.3,
        "Thổ": 1.1,
        "Kim": 0.8,
        "Thủy": 0.7
    },
    "Thu": {
        "Mộc": 0.7,
        "Hỏa": 0.8,
        "Thổ": 1.0,
        "Kim": 1.3,
        "Thủy": 1.1
    },
    "Đông": {
        "Mộc": 1.1,
        "Hỏa": 0.7,
        "Thổ": 0.8,
        "Kim": 1.0,
        "Thủy": 1.3
    }
}

# Trọng số phân tích
TRONG_SO_PHAN_TICH = {
    "trong_cung": 0.50,      # 50% - Tương tác trong cung
    "giua_cac_cung": 0.35,   # 35% - Tương tác giữa các cung
    "thoi_gian": 0.15        # 15% - Yếu tố thời gian
}

# Trọng số yếu tố trong cung
TRONG_SO_YEU_TO = {
    "dung_than": 0.40,  # 40%
    "mon": 0.25,        # 25%
    "sao": 0.20,        # 20%
    "than": 0.10,       # 10%
    "ngu_hanh": 0.05    # 5%
}
