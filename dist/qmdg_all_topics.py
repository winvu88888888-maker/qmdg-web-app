# -*- coding: utf-8 -*-
"""
DANH SÁCH ĐẦY ĐỦ TẤT CẢ CÁC CHỦ ĐỀ KỲ MÔN ĐỘN GIÁP
Tổng hợp từ nhiều nguồn: Việt Nam, Trung Quốc, quốc tế
"""

# TẤT CẢ CÁC CHỦ ĐỀ LUẬN ĐOÁN (100+ chủ đề)
ALL_QMDG_TOPICS = {
    # === NHÓM 1: KINH DOANH & TÀI CHÍNH ===
    "Kinh Doanh Tổng Quát": {"category": "Business", "priority": "high"},
    "Khai Trương Cửa Hàng": {"category": "Business", "priority": "high"},
    "Ký Kết Hợp Đồng": {"category": "Business", "priority": "high"},
    "Đàm Phán Thương Mại": {"category": "Business", "priority": "high"},
    "Mua Bán Hàng Hóa": {"category": "Business", "priority": "medium"},
    "Đầu Tư Chứng Khoán": {"category": "Finance", "priority": "high"},
    "Đầu Tư Bất Động Sản": {"category": "Finance", "priority": "high"},
    "Vay Mượn Tiền Bạc": {"category": "Finance", "priority": "medium"},
    "Đòi Nợ Thu Hồi": {"category": "Finance", "priority": "medium"},
    "Cầu Tài Lộc": {"category": "Finance", "priority": "high"},
    "Mở Rộng Kinh Doanh": {"category": "Business", "priority": "high"},
    "Hợp Tác Đối Tác": {"category": "Business", "priority": "high"},
    "Cạnh Tranh Thị Trường": {"category": "Business", "priority": "medium"},
    "Phá Sản Rủi Ro": {"category": "Finance", "priority": "high"},
    
    # === NHÓM 2: SỰ NGHIỆP & CÔNG DANH ===
    "Xin Việc Làm": {"category": "Career", "priority": "high"},
    "Thăng Chức Thăng Tiến": {"category": "Career", "priority": "high"},
    "Chuyển Công Tác": {"category": "Career", "priority": "medium"},
    "Nghỉ Việc Từ Chức": {"category": "Career", "priority": "medium"},
    "Thi Công Chức": {"category": "Career", "priority": "high"},
    "Nhậm Chức Mới": {"category": "Career", "priority": "high"},
    "Quan Hệ Đồng Nghiệp": {"category": "Career", "priority": "low"},
    "Quan Hệ Sếp Cấp Trên": {"category": "Career", "priority": "medium"},
    "Tạo Lập Sự Nghiệp": {"category": "Career", "priority": "high"},
    "Công Danh Danh Vọng": {"category": "Career", "priority": "medium"},
    
    # === NHÓM 3: HỌC TẬP & THI CỬ ===
    "Thi Đại Học": {"category": "Education", "priority": "high"},
    "Thi Tốt Nghiệp": {"category": "Education", "priority": "high"},
    "Thi Chứng Chỉ": {"category": "Education", "priority": "medium"},
    "Học Bổng Du Học": {"category": "Education", "priority": "high"},
    "Kết Quả Học Tập": {"category": "Education", "priority": "medium"},
    "Thi Nâng Bậc": {"category": "Education", "priority": "medium"},
    
    # === NHÓM 4: TÌNH CẢM & HÔN NHÂN ===
    "Tình Duyên Hôn Nhân": {"category": "Relationship", "priority": "high"},
    "Hẹn Hò Tán Tỉnh": {"category": "Relationship", "priority": "medium"},
    "Cầu Hôn Đính Hôn": {"category": "Relationship", "priority": "high"},
    "Lễ Cưới": {"category": "Relationship", "priority": "high"},
    "Ly Hôn Chia Tay": {"category": "Relationship", "priority": "high"},
    "Ngoại Tình Thứ Ba": {"category": "Relationship", "priority": "medium"},
    "Hòa Hợp Vợ Chồng": {"category": "Relationship", "priority": "medium"},
    "Tái Hôn": {"category": "Relationship", "priority": "medium"},
    "Tìm Bạn Đời": {"category": "Relationship", "priority": "high"},
    
    # === NHÓM 5: SỨC KHỎE & BỆNH TẬT ===
    "Bệnh Tật Chữa Trị": {"category": "Health", "priority": "high"},
    "Phẫu Thuật": {"category": "Health", "priority": "high"},
    "Khám Bệnh": {"category": "Health", "priority": "medium"},
    "Mua Thuốc": {"category": "Health", "priority": "low"},
    "Tìm Thầy Thuốc": {"category": "Health", "priority": "medium"},
    "Bệnh Mãn Tính": {"category": "Health", "priority": "high"},
    "Tai Nạn Thương Tích": {"category": "Health", "priority": "high"},
    "Sinh Con": {"category": "Health", "priority": "high"},
    "Thai Nhi": {"category": "Health", "priority": "high"},
    "Tuổi Thọ": {"category": "Health", "priority": "medium"},
    
    # === NHÓM 6: PHÁP LÝ & KIỆN TỤNG ===
    "Kiện Tụng": {"category": "Legal", "priority": "high"},
    "Hòa Giải": {"category": "Legal", "priority": "medium"},
    "Tranh Chấp Đất Đai": {"category": "Legal", "priority": "high"},
    "Tranh Chấp Tài Sản": {"category": "Legal", "priority": "high"},
    "Tội Phạm Hình Sự": {"category": "Legal", "priority": "high"},
    "Tù Tội": {"category": "Legal", "priority": "high"},
    "Án Mạng": {"category": "Legal", "priority": "high"},
    "Kháng Cáo": {"category": "Legal", "priority": "medium"},
    
    # === NHÓM 7: NHÀ CỬA & PHONG THỦY ===
    "Mua Nhà Đất": {"category": "Property", "priority": "high"},
    "Bán Nhà Đất": {"category": "Property", "priority": "high"},
    "Xây Dựng Nhà": {"category": "Property", "priority": "high"},
    "Sửa Chữa Nhà": {"category": "Property", "priority": "medium"},
    "Chuyển Nhà": {"category": "Property", "priority": "high"},
    "Phong Thủy Nhà Ở": {"category": "FengShui", "priority": "high"},
    "Phong Thủy Văn Phòng": {"category": "FengShui", "priority": "high"},
    "Phong Thủy Mộ Phần": {"category": "FengShui", "priority": "high"},
    "Động Thổ": {"category": "Property", "priority": "high"},
    "Khai Trương Văn Phòng": {"category": "Business", "priority": "high"},
    
    # === NHÓM 8: XUẤT HÀNH & DI CHUYỂN ===
    "Xuất Hành Xa": {"category": "Travel", "priority": "high"},
    "Đi Công Tác": {"category": "Travel", "priority": "medium"},
    "Du Lịch": {"category": "Travel", "priority": "low"},
    "Định Cư Nước Ngoài": {"category": "Travel", "priority": "high"},
    "Về Quê": {"category": "Travel", "priority": "low"},
    "Phương Hướng Xuất Hành": {"category": "Travel", "priority": "medium"},
    "Thời Gian Xuất Hành": {"category": "Travel", "priority": "medium"},
    
    # === NHÓM 9: TÌM KIẾM & MẤT MÁT ===
    "Tìm Người Thất Lạc": {"category": "Search", "priority": "high"},
    "Tìm Đồ Vật Mất": {"category": "Search", "priority": "medium"},
    "Trộm Cắp": {"category": "Search", "priority": "high"},
    "Mất Cắp Tài Sản": {"category": "Search", "priority": "high"},
    "Bắt Trộm": {"category": "Search", "priority": "medium"},
    "Tìm Thú Cưng": {"category": "Search", "priority": "low"},
    
    # === NHÓM 10: GIAO TIẾP & QUAN HỆ ===
    "Gặp Quý Nhân": {"category": "Social", "priority": "high"},
    "Yết Kiến Lãnh Đạo": {"category": "Social", "priority": "high"},
    "Gặp Khách Hàng": {"category": "Social", "priority": "medium"},
    "Tiếp Khách": {"category": "Social", "priority": "low"},
    "Mời Khách": {"category": "Social", "priority": "low"},
    "Hội Họp": {"category": "Social", "priority": "medium"},
    "Đàm Phán": {"category": "Social", "priority": "high"},
    
    # === NHÓM 11: QUÂN SỰ & CẠNH TRANH ===
    "Chiến Tranh": {"category": "Military", "priority": "high"},
    "Phòng Thủ": {"category": "Military", "priority": "high"},
    "Tấn Công": {"category": "Military", "priority": "high"},
    "Thi Đấu Thể Thao": {"category": "Competition", "priority": "medium"},
    "Thi Đấu Cờ": {"category": "Competition", "priority": "low"},
    "Cuộc Thi": {"category": "Competition", "priority": "medium"},
    
    # === NHÓM 12: THỂ THAO & BÓNG ĐÁ ===
    "Trận Đấu Bóng Đá": {"category": "Sports", "priority": "high"},
    "Tỉ Số Trận Đấu": {"category": "Sports", "priority": "high"},
    "Đua Ngựa Đua Xe": {"category": "Sports", "priority": "medium"},
    
    # === NHÓM 12: KHÁC ===
    "Thời Tiết": {"category": "Weather", "priority": "low"},
    "Thiên Tai": {"category": "Disaster", "priority": "high"},
    "Mộng Chiêm": {"category": "Dream", "priority": "low"},
    "Điềm Báo": {"category": "Omen", "priority": "low"},
    "Vận Mệnh Năm": {"category": "Destiny", "priority": "high"},
    "Vận Mệnh Tháng": {"category": "Destiny", "priority": "medium"},
    "Vận Mệnh Ngày": {"category": "Destiny", "priority": "low"},
    "Chọn Ngày Tốt": {"category": "DateSelection", "priority": "high"},
    "Trồng Trọt": {"category": "Agriculture", "priority": "low"},
    "Chăn Nuôi": {"category": "Agriculture", "priority": "low"},
    "Câu Cá": {"category": "Recreation", "priority": "low"},
    "Săn Bắn": {"category": "Recreation", "priority": "low"},
    
    # === NHÓM 13: TÂM LINH & HUYỀN BÍ ===
    "Ma quỷ": {"category": "Mystical", "priority": "high"},
    "Thần thánh": {"category": "Mystical", "priority": "high"},
    "Cầu Đảo Tế Tự": {"category": "Mystical", "priority": "medium"},
    "Điềm Báo Tâm Linh": {"category": "Mystical", "priority": "medium"},
}

# Tổng số chủ đề
TOTAL_TOPICS = len(ALL_QMDG_TOPICS)
print(f"Tổng số chủ đề: {TOTAL_TOPICS}")
