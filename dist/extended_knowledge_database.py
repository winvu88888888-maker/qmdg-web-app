# -*- coding: utf-8 -*-
"""
DATABASE TRI THỨC MỞ RỘNG - 9 PHƯƠNG PHÁP DỰ ĐOÁN
Bổ sung thêm 5 phương pháp nổi tiếng
"""

# ============================================================================
# PHẦN 6: LỤC NHÂM THẦN KHÓA (六壬神课)
# ============================================================================

LUC_NHAM_THAN_KHOA = {
    "NGUYEN_TAC_CO_BAN": {
        "Vị Trí": "Đứng đầu Tam Thức (Thái Ất, Lục Nhâm, Kỳ Môn)",
        "Tên Gọi": "Thần Khóa - Khóa thần thánh",
        "Độ Chính Xác": "Cao nhất trong các phương pháp - 90-95%",
        "Đặc Điểm": "Phức tạp nhất, toàn diện nhất"
    },
    
    "HAI_LOAI": {
        "Đại Lục Nhâm": {
            "Phương Pháp": "Tam truyền (sơ, trung, mạt) + Tứ khóa",
            "Phạm Vi": "Tài vận, sức khỏe, hôn nhân, sự nghiệp, kiện tụng, gia đình",
            "Độ Chính Xác": "95% cho sự kiện cụ thể",
            "Đặc Điểm": "Rất phức tạp, cần học lâu năm"
        },
        "Tiểu Lục Nhâm": {
            "Phương Pháp": "Lục thần (Đại An, Lưu Niên, Tốc Hỷ, Xích Khẩu, Tiểu Cát, Không Vong)",
            "Phạm Vi": "Dự đoán cát hung nhanh",
            "Độ Chính Xác": "75-80%",
            "Đặc Điểm": "Đơn giản, dễ học"
        }
    },
    
    "UNG_DUNG": {
        "Tài Vận": "Dự đoán thời điểm phát tài, nguồn tài",
        "Sức Khỏe": "Chẩn đoán bệnh, thời gian khỏi",
        "Hôn Nhân": "Thời điểm gặp người, tính cách người ấy",
        "Sự Nghiệp": "Thăng tiến, chuyển việc",
        "Kiện Tụng": "Thắng/thua, thời gian kết thúc",
        "Gia Đình": "Quan hệ gia đình, con cái"
    },
    
    "UU_DIEM": {
        "Toàn Diện": "Phân tích mọi khía cạnh cuộc sống",
        "Chi Tiết": "Đưa ra thông tin cụ thể, không mơ hồ",
        "Chính Xác": "Độ chính xác cao nhất",
        "Thời Gian": "Xác định chính xác thời điểm ứng nghiệm"
    }
}

# ============================================================================
# PHẦN 7: HUYỀN KHÔNG PHI TINH (玄空飞星)
# ============================================================================

HUYEN_KHONG_PHI_TINH = {
    "NGUYEN_TAC_CO_BAN": {
        "Bản Chất": "Phong thủy dựa trên thiên văn học",
        "Cửu Tinh": "9 ngôi sao bay qua 9 cung",
        "Thời Gian": "Vận 20 năm, năm, tháng, ngày, giờ",
        "Không Gian": "Hướng nhà, vị trí phòng"
    },
    
    "CUU_TINH_CHI_TIET": {
        "Nhất Bạch": {
            "Tên": "Đào Hoa Tinh",
            "Chủ": "Hôn nhân, nhân duyên, tình duyên",
            "Cát/Hung": "Cát",
            "Màu": "Trắng",
            "Hành": "Thủy"
        },
        "Nhị Hắc": {
            "Tên": "Bệnh Tinh",
            "Chủ": "Bệnh tật, sức khỏe",
            "Cát/Hung": "Hung",
            "Màu": "Đen",
            "Hành": "Thổ"
        },
        "Tam Bích": {
            "Tên": "Thị Phi Tinh",
            "Chủ": "Tranh chấp, kiện tụng, cãi vã",
            "Cát/Hung": "Hung",
            "Màu": "Xanh lá",
            "Hành": "Mộc"
        },
        "Tứ Lục": {
            "Tên": "Văn Xương Tinh",
            "Chủ": "Học hành, thi cử, văn chương",
            "Cát/Hung": "Cát",
            "Màu": "Xanh lục",
            "Hành": "Mộc"
        },
        "Ngũ Hoàng": {
            "Tên": "Đại Hung Tinh",
            "Chủ": "Tai nạn, họa lớn",
            "Cát/Hung": "Đại Hung",
            "Màu": "Vàng",
            "Hành": "Thổ"
        },
        "Lục Bạch": {
            "Tên": "Vũ Khúc Tinh",
            "Chủ": "Tài vận, quan lộc, quyền lực",
            "Cát/Hung": "Đại Cát",
            "Màu": "Trắng",
            "Hành": "Kim"
        },
        "Thất Xích": {
            "Tên": "Phá Quân Tinh",
            "Chủ": "Hao tán tài sản, mất mát",
            "Cát/Hung": "Hung",
            "Màu": "Đỏ",
            "Hành": "Kim"
        },
        "Bát Bạch": {
            "Tên": "Tả Phù Tinh",
            "Chủ": "Giàu sang, phú quý, tài lộc",
            "Cát/Hung": "Đại Cát",
            "Màu": "Trắng",
            "Hành": "Thổ"
        },
        "Cửu Tử": {
            "Tên": "Hữu Bật Tinh",
            "Chủ": "Cơ hội tình cảm, hỷ sự",
            "Cát/Hung": "Cát",
            "Màu": "Tím",
            "Hành": "Hỏa"
        }
    },
    
    "UNG_DUNG": {
        "Dự Đoán Vận Hạn": "Theo năm, tháng, ngày",
        "Thiết Kế Nhà": "Chọn hướng, bố trí phòng",
        "Chọn Ngày": "Khai trương, động thổ, cưới hỏi",
        "Hóa Giải": "Hóa giải sao hung"
    },
    
    "DO_CHINH_XAC": {
        "Dự Đoán Vận": "85-90%",
        "Phong Thủy": "90-95%",
        "Thời Gian": "80-85%"
    }
}

# ============================================================================
# PHẦN 8: BÁT TỰ TỨ TRỤ (八字四柱 - BAZI)
# ============================================================================

BAT_TU_TU_TRU = {
    "NGUYEN_TAC_CO_BAN": {
        "Bốn Trụ": "Năm, Tháng, Ngày, Giờ sinh",
        "Tám Chữ": "Mỗi trụ có 2 chữ (Can + Chi)",
        "Ngũ Hành": "Phân tích cân bằng 5 hành",
        "Dụng Thần": "Tìm yếu tố cần bổ sung"
    },
    
    "DO_CHINH_XAC": {
        "Tính Cách": "90-95%",
        "Sự Nghiệp": "80-85%",
        "Hôn Nhân": "75-80%",
        "Tài Vận": "70-75%",
        "Sức Khỏe": "75-80%",
        "Tuổi Thọ": "60-70% (xu hướng)"
    },
    
    "PHAN_TICH": {
        "Cường Nhược": "Phân tích mạnh yếu của Nhật Can",
        "Hỷ Kỵ": "Xác định hành nào tốt, hành nào xấu",
        "Đại Vận": "Mỗi 10 năm đổi 1 vận",
        "Lưu Niên": "Vận hạn từng năm",
        "Lưu Nguyệt": "Vận hạn từng tháng"
    },
    
    "UNG_DUNG": {
        "Phân Tích Tính Cách": "Rất chính xác",
        "Chọn Nghề": "Dựa vào Dụng Thần",
        "Chọn Ngày Cưới": "Hợp Bát Tự 2 người",
        "Đặt Tên": "Bổ sung Ngũ Hành thiếu",
        "Dự Đoán Vận": "Theo Đại Vận, Lưu Niên"
    },
    
    "BAC_THAY_NOI_TIENG": {
        "Sean Chan": "Singapore - Chuyên BaZi + Qi Men",
        "Joey Yap": "Malaysia - Tác giả nhiều sách",
        "Master Kevin Foong": "20 năm kinh nghiệm",
        "Master Edwaard Liu": "Singapore - Tích hợp tâm linh"
    }
}

# ============================================================================
# PHẦN 9: THIẾT BẢN THẦN SỐ (铁板神数)
# ============================================================================

THIET_BAN_THAN_SO = {
    "NGUYEN_TAC_CO_BAN": {
        "Số Câu": "12,000 câu thơ dự đoán",
        "Phương Pháp": "Tính toán vũ trụ học từ ngày giờ sinh",
        "Tên Gọi": "Tấm sắt - Số phận cố định",
        "Độ Khó": "Khó nhất trong các phương pháp"
    },
    
    "DO_CHINH_XAC": {
        "Quá Khứ": "90-95% (rất chính xác)",
        "Quan Hệ Gia Đình": "85-90%",
        "Tương Lai": "70-75% (mơ hồ hơn)",
        "Sự Kiện Cụ Thể": "80-85%"
    },
    
    "YEU_CAU": {
        "Thời Gian Sinh": "Phải chính xác đến phút",
        "Kỹ Năng": "Người luận đoán phải giỏi",
        "Kinh Nghiệm": "Cần nhiều năm tu luyện"
    },
    
    "UU_DIEM": {
        "Chi Tiết": "Dự đoán rất cụ thể",
        "Toàn Diện": "Bao quát cả đời người",
        "Độc Đáo": "Mỗi người có câu thơ riêng"
    },
    
    "HAN_CHE": {
        "Khó Học": "Rất khó, ít người thành thạo",
        "Cần Thời Gian": "Phải biết chính xác giờ sinh",
        "Tương Lai Mơ Hồ": "Không cụ thể bằng quá khứ"
    }
}

# ============================================================================
# PHẦN 10: MAI HOA DỊCH SỐ (梅花易数)
# ============================================================================

MAI_HOA_DICH_SO = {
    "NGUYEN_TAC_CO_BAN": {
        "Người Sáng Lập": "Thiệu Ung (Shao Yong) - Nhà triết học Tống",
        "Phương Pháp": "Lập quẻ từ thời gian, âm thanh, vật thể",
        "Đặc Điểm": "Linh hoạt, nhanh, trực giác",
        "Độ Chính Xác": "78% cho sự kiện đột xuất"
    },
    
    "CACH_LAP_QUAI": {
        "Từ Thời Gian": "Năm + Tháng + Ngày + Giờ",
        "Từ Âm Thanh": "Số lần tiếng động",
        "Từ Vật Thể": "Số lượng vật quan sát",
        "Từ Phương Hướng": "8 hướng = 8 quẻ",
        "Từ Số Bất Kỳ": "Người hỏi chọn số"
    },
    
    "THANH_TICH": {
        "Thiệu Ung": {
            "Sự Kiện": "Dự đoán cô gái bị thương khi hái mận",
            "Phương Pháp": "Quan sát chim sẻ",
            "Kết Quả": "Chính xác 100%"
        },
        "Nghiên Cứu 2025": {
            "Độ Chính Xác": "78% cho sự kiện đột xuất",
            "Phương Pháp": "Nghiên cứu khoa học"
        }
    },
    
    "UU_DIEM": {
        "Nhanh": "Lập quẻ và luận đoán nhanh",
        "Linh Hoạt": "Dùng bất kỳ yếu tố nào",
        "Trực Giác": "Phát huy tâm linh",
        "Đơn Giản": "Dễ học hơn các phương pháp khác"
    },
    
    "UNG_DUNG": {
        "Sự Kiện Đột Xuất": "Rất chính xác",
        "Quyết Định Nhanh": "Có/Không làm việc gì",
        "Tìm Đồ Vật": "Mất đồ, tìm người",
        "Dự Đoán Ngắn Hạn": "Trong ngày, trong tuần"
    }
}

# ============================================================================
# PHẦN 11: CÔNG THỨC TÍCH HỢP 9 PHƯƠNG PHÁP
# ============================================================================

CONG_THUC_9_PHUONG_PHAP = {
    "PHAN_CHIA_TRONG_SO": {
        "Kỳ Môn Độn Giáp": "20% - Hiện tại, sự kiện cụ thể",
        "Lục Nhâm Thần Khóa": "20% - Chi tiết, toàn diện",
        "Bát Tự Tứ Trụ (BaZi)": "15% - Tính cách, bản chất",
        "Bốc Dịch (I-Ching)": "10% - Biến đổi, xu hướng",
        "Tử Vi Đẩu Số": "10% - Vận mệnh dài hạn",
        "Huyền Không Phi Tinh": "10% - Phong thủy, thời gian",
        "Thái Ất Thần Kinh": "5% - Chiến lược quốc gia",
        "Thiết Bản Thần Số": "5% - Quá khứ, gia đình",
        "Mai Hoa Dịch Số": "5% - Sự kiện đột xuất"
    },
    
    "QUY_TAC_SU_DUNG": {
        "Sự Kiện Hiện Tại": "Kỳ Môn (40%) + Lục Nhâm (30%) + Mai Hoa (30%)",
        "Tính Cách Con Người": "BaZi (50%) + Tử Vi (30%) + Kỳ Môn (20%)",
        "Vận Mệnh Dài Hạn": "Tử Vi (40%) + Thái Ất (30%) + BaZi (30%)",
        "Phong Thủy Nhà Cửa": "Huyền Không (60%) + Kỳ Môn (40%)",
        "Quá Khứ Gia Đình": "Thiết Bản (50%) + BaZi (30%) + Tử Vi (20%)",
        "Sự Kiện Đột Xuất": "Mai Hoa (50%) + Kỳ Môn (30%) + Lục Nhâm (20%)"
    },
    
    "DO_TIN_CAY_TONG_HOP": {
        "9/9 phương pháp cùng hướng": "99% (gần như chắc chắn)",
        "7-8/9 phương pháp cùng hướng": "95% (rất chắc chắn)",
        "5-6/9 phương pháp cùng hướng": "85% (chắc chắn)",
        "3-4/9 phương pháp cùng hướng": "70% (khá chắc)",
        "Dưới 3/9": "Dưới 50% (không nên dự đoán)"
    },
    
    "PHUONG_PHAP_PHAN_TICH": {
        "Bước 1": "Thu thập thông tin đầy đủ (ngày giờ sinh, câu hỏi)",
        "Bước 2": "Áp dụng 9 phương pháp song song",
        "Bước 3": "Tính điểm từng phương pháp",
        "Bước 4": "Tổng hợp theo trọng số",
        "Bước 5": "Kiểm tra độ đồng thuận",
        "Bước 6": "Đưa ra kết luận chi tiết",
        "Bước 7": "Xác định thời gian ứng nghiệm",
        "Bước 8": "Đưa ra hành động cụ thể"
    }
}

# Export
__all__ = [
    'LUC_NHAM_THAN_KHOA',
    'HUYEN_KHONG_PHI_TINH',
    'BAT_TU_TU_TRU',
    'THIET_BAN_THAN_SO',
    'MAI_HOA_DICH_SO',
    'CONG_THUC_9_PHUONG_PHAP'
]
