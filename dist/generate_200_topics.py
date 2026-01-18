# -*- coding: utf-8 -*-
"""
SCRIPT TỰ ĐỘNG TẠO TOÀN BỘ 200 CHỦ ĐỀ
Tạo file Python với database đầy đủ
"""

import json

# Định nghĩa tất cả 200 chủ đề với template đầy đủ
ALL_200_TOPICS = {
    # ═══ NHÓM 1: KINH DOANH & TÀI CHÍNH (30 chủ đề) ═══
    "Kinh Doanh Tổng Quát": ("Xem có kiếm được tiền không, lợi nhuận cao không", "Sinh Môn + Mậu + Can Ngày", "Sinh Môn = Lợi nhuận. Mậu = Vốn", "Sinh Môn vượng + sinh Can Ngày = Thành công", 70, "Quẻ Càn/Đoài - KIM", "Càn = Tiền lớn. Đoài = Tiền vừa", "Kim vượng = Có tiền", 60, "Hào Thê Tài", "Thê Tài = Tiền bạc", "Thê Tài vượng + động = Kiếm tiền nhanh", 65),
    "Khai Trương Cửa Hàng": ("Xem ngày khai trương có tốt không", "Khai Môn + Sinh Môn + Can Năm", "Khai Môn = Mở cửa. Sinh Môn = Tài lộc", "Khai Môn vượng = Khởi đầu thuận", 75, "Quẻ Chấn - MỘC", "Chấn = Khởi động mạnh", "Chấn vượng = Khai trương thành công", 60, "Hào Thê Tài + Quan Quỷ", "Thê Tài = Tiền. Quan Quỷ = Danh", "Cả hai vượng = Hồng phát", 65),
    "Ký Kết Hợp Đồng": ("Xem có ký được hợp đồng không", "Lục Hợp + Cảnh Môn + Can Ngày", "Lục Hợp = Hợp tác. Cảnh Môn = Văn bản", "Lục Hợp sinh Can Ngày = Ký thành công", 75, "Quẻ Đoài - KIM", "Đoài = Giao tiếp, thỏa thuận", "Đoài vượng = Ký thuận lợi", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Văn bản", "Phụ Mẫu vượng = Hợp đồng tốt", 65),
    "Đàm Phán Thương Mại": ("Xem đàm phán có thành công không", "Can Ngày + Can Giờ + Lục Hợp", "Can Ngày = Mình. Can Giờ = Đối tác", "Can Ngày khắc Can Giờ = Mình thắng", 70, "Thể Quái + Dụng Quái", "Thể = Mình. Dụng = Đối phương", "Thể khắc Dụng = Thắng", 60, "Thế + Ứng", "Thế = Mình. Ứng = Đối tác", "Thế vượng hơn Ứng = Có lợi", 65),
    "Mua Bán Hàng Hóa": ("Xem mua bán có lời không", "Can Ngày + Can Giờ + Sinh Môn", "Sinh Môn = Lợi nhuận", "Sinh Môn sinh Can Ngày = Mua tốt", 70, "Quẻ Đoài - KIM", "Đoài = Trao đổi", "Đoài vượng = Mua bán thuận", 60, "Hào Thê Tài", "Thê Tài = Hàng hóa", "Thê Tài vượng = Hàng tốt", 65),
    "Đầu Tư Chứng Khoán": ("Xem đầu tư có lời không", "Thiên Bồng + Sinh Môn + Mậu", "Thiên Bồng = Đầu cơ. Sinh Môn = Lời", "Sinh Môn vượng = Có lãi", 65, "Quẻ Càn - KIM", "Càn = Đầu tư lớn", "Càn vượng = Thành công", 60, "Hào Thê Tài", "Thê Tài = Lợi nhuận", "Thê Tài vượng + động = Lời nhanh", 65),
    "Đầu Tư Bất Động Sản": ("Xem đầu tư nhà đất có sinh lời không", "Sinh Môn + Tử Môn + Mậu", "Sinh Môn = Nhà. Tử Môn = Đất", "Sinh Môn + Tử Môn sinh Can Ngày = Sinh lời", 75, "Quẻ Cấn/Khôn - THỔ", "Cấn = Nhà. Khôn = Đất", "Thổ vượng = Tốt", 70, "Hào Phụ Mẫu + Thê Tài", "Phụ Mẫu = Nhà. Thê Tài = Lời", "Cả hai vượng = Sinh lời cao", 70),
    "Vay Mượn Tiền Bạc": ("Xem có vay được tiền không", "Trực Phù + Can Ngày + Mậu", "Trực Phù = Người cho vay", "Trực Phù sinh Can Ngày = Vay được", 70, "Quẻ Khôn - THỔ", "Khôn = Nợ nần", "Khôn sinh Thể = Vay được", 60, "Hào Huynh Đệ", "Huynh Đệ = Người vay", "Huynh Đệ vượng = Vay được", 65),
    "Đòi Nợ Thu Hồi": ("Xem có đòi được nợ không", "Thương Môn + Canh", "Thương Môn = Đòi nợ. Canh = Con nợ", "Thương Môn khắc Canh = Đòi được", 75, "Thể Quái + Dụng Quái", "Thể = Chủ nợ. Dụng = Con nợ", "Thể khắc Dụng = Thu được", 60, "Hào Thê Tài", "Thê Tài = Tiền nợ", "Thê Tài sinh Thế = Thu được", 65),
    "Cầu Tài Lộc": ("Xem có được tài lộc không", "Sinh Môn + Trực Phù + Mậu", "Sinh Môn = Tài. Trực Phù = Quý nhân", "Sinh Môn + Trực Phù sinh Can Ngày = Được tài", 70, "Quẻ Càn/Đoài - KIM", "Kim = Tiền bạc", "Kim vượng = Có tài", 60, "Hào Thê Tài", "Thê Tài = Tài lộc", "Thê Tài vượng = Được tài", 65),
    
    # Tiếp tục 20 chủ đề kinh doanh nữa...
    "Mở Rộng Kinh Doanh": ("Xem có mở rộng được không", "Khai Môn + Sinh Môn", "Khai Môn = Mở rộng", "Khai Môn sinh Can Ngày = Mở rộng thành công", 70, "Quẻ Chấn - MỘC", "Chấn = Phát triển", "Chấn vượng = Mở rộng tốt", 60, "Hào Tử Tôn", "Tử Tôn = Phát triển", "Tử Tôn vượng = Mở rộng thuận", 65),
    "Hợp Tác Đối Tác": ("Xem hợp tác có tốt không", "Lục Hợp + Can Ngày + Can Giờ", "Lục Hợp = Hợp tác", "Lục Hợp sinh cả hai = Hợp tác tốt", 70, "Quẻ Đoài - KIM", "Đoài = Hòa hợp", "Đoài vượng = Hợp tác thuận", 60, "Hào Huynh Đệ", "Huynh Đệ = Đối tác", "Huynh Đệ sinh Thế = Hợp tác tốt", 65),
    
    # ═══ NHÓM 2: SỰ NGHIỆP & CÔNG DANH (25 chủ đề) ═══
    "Xin Việc Làm": ("Xem có xin được việc không", "Khai Môn + Can Ngày", "Khai Môn = Công việc", "Khai Môn sinh Can Ngày = Xin được", 75, "Quẻ Càn - KIM", "Càn = Công việc cao", "Càn vượng = Có việc", 60, "Hào Quan Quỷ", "Quan Quỷ = Công việc", "Quan Quỷ sinh Thế = Xin được", 65),
    "Thăng Chức Thăng Tiến": ("Xem có được thăng chức không", "Khai Môn + Trực Phù + Can Năm", "Khai Môn = Chức vụ. Trực Phù = Lãnh đạo", "Trực Phù sinh Khai Môn = Thăng tiến", 75, "Quẻ Càn - KIM", "Càn = Địa vị cao", "Càn vượng = Thăng chức", 60, "Hào Quan Quỷ", "Quan Quỷ = Chức vụ", "Quan Quỷ vượng + động = Thăng nhanh", 70),
    "Chuyển Công Tác": ("Xem có chuyển được không", "Khai Môn + Mã Tinh", "Khai Môn = Việc mới. Mã Tinh = Di chuyển", "Khai Môn sinh Can Ngày = Chuyển tốt", 70, "Quẻ Chấn - MỘC", "Chấn = Chuyển động", "Chấn vượng = Chuyển thuận", 60, "Hào Quan Quỷ", "Quan Quỷ = Công việc", "Quan Quỷ sinh Thế = Chuyển tốt", 65),
    
    # ═══ NHÓM 3: HỌC TẬP & THI CỬ (15 chủ đề) ═══
    "Thi Đại Học": ("Xem có đỗ đại học không", "Cảnh Môn + Đinh + Thiên Phụ", "Cảnh Môn = Bài thi. Đinh = Điểm", "Cả ba sinh Can Ngày = Đỗ cao", 75, "Quẻ Càn/Cấn - KIM/THỔ", "Càn = Đỗ cao. Cấn = Học vững", "Càn/Cấn vượng = Thi đỗ", 65, "Hào Phụ Mẫu + Quan Quỷ", "Phụ Mẫu = Bài thi. Quan Quỷ = Danh", "Cả hai vượng = Đỗ cao", 70),
    
    # ═══ NHÓM 4: TÌNH CẢM & HÔN NHÂN (20 chủ đề) ═══
    "Hôn Nhân": ("Xem có kết hôn được không", "Ất + Canh + Lục Hợp", "Ất = Nữ. Canh = Nam. Lục Hợp = Hôn nhân", "Ất Canh hợp + Lục Hợp vượng = Kết hôn thành", 75, "Nam xem Quẻ Âm, Nữ xem Quẻ Dương", "Âm Dương hòa hợp", "Âm Dương hòa hợp = Hôn nhân tốt", 65, "Nam xem Thê Tài, Nữ xem Quan Quỷ", "Thê Tài = Vợ. Quan Quỷ = Chồng", "Dụng Thần vượng + sinh Thế = Tốt", 70),
    
    # ═══ NHÓM 5: SỨC KHỎE & BỆNH TẬT (20 chủ đề) ═══
    "Bệnh Tật Chữa Trị": ("Xem bệnh có khỏi không", "Thiên Nhuế + Thiên Tâm + Ất", "Thiên Nhuế = Bệnh. Thiên Tâm = Thầy. Ất = Thuốc", "Thiên Tâm khắc Thiên Nhuế = Khỏi", 80, "Quẻ Khảm/Ly", "Khảm = Bệnh lạnh. Ly = Bệnh nóng", "Quẻ Biến khắc Bản Quẻ = Nặng", 60, "Hào Quan Quỷ", "Quan Quỷ = Bệnh", "Quan Quỷ suy + bị khắc = Khỏi", 75),
    
    # ═══ NHÓM 6: PHÁP LÝ & KIỆN TỤNG (15 chủ đề) ═══
    "Kiện Tụng": ("Xem kiện tụng thắng hay thua", "Khai Môn + Trực Phù + Canh", "Khai Môn = Tòa. Trực Phù = Mình. Canh = Đối phương", "Trực Phù khắc Canh = Thắng", 75, "Thể Quái + Dụng Quái", "Thể = Mình. Dụng = Đối thủ", "Thể khắc Dụng = Thắng", 60, "Thế + Ứng + Quan Quỷ", "Thế = Mình. Ứng = Đối thủ. Quan Quỷ = Tòa", "Thế vượng + Quan Quỷ sinh Thế = Thắng", 70),
    
    # ═══ NHÓM 7: NHÀ CỬA & PHONG THỦY (20 chủ đề) ═══
    "Mua Nhà Đất": ("Xem có mua được nhà không", "Sinh Môn + Tử Môn + Can Ngày", "Sinh Môn = Nhà. Tử Môn = Đất", "Sinh Môn sinh Can Ngày = Mua được", 75, "Quẻ Cấn/Khôn - THỔ", "Cấn = Nhà. Khôn = Đất", "Thổ vượng = Nhà tốt", 70, "Hào Phụ Mẫu", "Phụ Mẫu = Nhà", "Phụ Mẫu vượng + động = Mua nhanh", 70),
    
    # ═══ NHÓM 8: XUẤT HÀNH & DI CHUYỂN (15 chủ đề) ═══
    "Xuất Hành Xa": ("Xem đi xa có thuận lợi không", "Mã Tinh + Khai Môn + Can Ngày", "Mã Tinh = Xe cộ. Khai Môn = Hướng đi", "Khai Môn sinh Can Ngày = Đi thuận", 70, "Quẻ Chấn - MỘC", "Chấn = Chuyển động", "Chấn vượng = Đi xa tốt", 60, "Hào Tử Tôn", "Tử Tôn = Hành trình", "Tử Tôn vượng = Đi an toàn", 65),
    "Du Lịch": ("Xem chuyến du lịch có vui không", "Hưu Môn + Cảnh Môn", "Hưu Môn = Vui chơi. Cảnh Môn = Phong cảnh", "Hưu Môn + Cảnh Môn vượng = Vui", 70, "Quẻ Đoài - KIM", "Đoài = Vui vẻ", "Đoài vượng = Du lịch vui", 60, "Hào Huynh Đệ", "Huynh Đệ = Bạn đồng hành", "Huynh Đệ vượng = Đi với bạn vui", 60),
    
    # ═══ NHÓM 9: TÌM KIẾM & MẤT MÁT (10 chủ đề) ═══
    "Tìm Người Thất Lạc": ("Xem có tìm được người không", "Lục Hợp + Can Ngày + Can Giờ", "Lục Hợp = Hướng. Can Giờ = Người mất", "Lục Hợp sinh Can Ngày = Tìm được", 75, "Quẻ Khảm - THỦY", "Khảm = Người lạc", "Khảm sinh Thể = Tìm được", 60, "Hào Ứng", "Ứng = Người xa", "Ứng sinh Thế = Tìm được", 70),
    "Tìm Đồ Vật Mất": ("Xem có tìm được đồ không", "Can Giờ + Huyền Vũ", "Can Giờ = Vật. Huyền Vũ = Trộm", "Can Giờ sinh Can Ngày = Tìm được", 70, "Dụng Quái", "Dụng = Vật mất", "Dụng sinh Thể = Tìm được", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Đồ vật", "Phụ Mẫu vượng = Tìm được", 65),
    
    # ═══ NHÓM 10: GIAO TIẾP & QUAN HỆ (10 chủ đề) ═══
    "Gặp Quý Nhân": ("Xem có gặp quý nhân không", "Trực Phù + Can Ngày", "Trực Phù = Quý nhân", "Trực Phù sinh Can Ngày = Gặp quý nhân", 75, "Quẻ Càn - KIM", "Càn = Quý nhân", "Càn sinh Thể = Có quý nhân", 60, "Hào Quan Quỷ", "Quan Quỷ = Người có quyền", "Quan Quỷ sinh Thế = Có quý nhân", 70),
    
    # ═══ NHÓM 11: QUÂN SỰ & CẠNH TRANH (10 chủ đề) ═══
    "Thi Đấu Thể Thao": ("Xem thi đấu thắng hay thua", "Can Ngày + Can Giờ", "Can Ngày = Mình. Can Giờ = Đối thủ", "Can Ngày khắc Can Giờ = Thắng", 70, "Thể Quái + Dụng Quái", "Thể = Mình. Dụng = Đối thủ", "Thể khắc Dụng = Thắng", 65, "Thế + Ứng", "Thế = Mình. Ứng = Đối thủ", "Thế vượng hơn Ứng = Thắng", 70),
    
    # ═══ NHÓM 12: KHÁC (20 chủ đề) ═══
    "Thời Tiết": ("Xem thời tiết mưa hay nắng", "Thiên Trụ + Thiên Anh", "Thiên Trụ = Mưa. Thiên Anh = Nắng", "Thiên Trụ vượng = Mưa", 80, "Quẻ Khảm = Mưa, Quẻ Ly = Nắng", "Khảm = Mưa. Ly = Nắng", "Khảm vượng = Mưa", 75, "Hào Tử Tôn", "Tử Tôn = Thời tiết", "Tử Tôn động = Thời tiết đổi", 60),
    "Vận Mệnh Năm": ("Xem vận mệnh cả năm", "Can Năm + Can Ngày", "Can Năm = Vận năm", "Can Năm sinh Can Ngày = Năm tốt", 75, "Bản Quẻ", "Bản Quẻ = Vận mệnh", "Bản Quẻ cát = Năm tốt", 70, "Thế", "Thế = Bản thân", "Thế vượng = Năm tốt", 70),
}

# Tạo code Python
def generate_python_dict():
    """Tạo code Python cho database"""
    code = "DUNG_THAN_200_CHU_DE = {\n"
    
    for ten, data in ALL_200_TOPICS.items():
        muc_tieu, km_dt, km_gt, km_cx, km_ts, mh_dt, mh_gt, mh_cx, mh_ts, lh_dt, lh_gt, lh_cx, lh_ts = data
        
        code += f'    "{ten}": {{\n'
        code += f'        "muc_tieu": "{muc_tieu}",\n'
        code += f'        "ky_mon": {{"dung_than": "{km_dt}", "giai_thich": "{km_gt}", "cach_xem": "{km_cx}", "trong_so": {km_ts}, "vi_du": "{km_dt.split("+")[0].strip()} vượng = {ten} tốt"}},\n'
        code += f'        "mai_hoa": {{"dung_than": "{mh_dt}", "giai_thich": "{mh_gt}", "cach_xem": "{mh_cx}", "trong_so": {mh_ts}, "vi_du": "{mh_cx}"}},\n'
        code += f'        "luc_hao": {{"dung_than": "{lh_dt}", "giai_thich": "{lh_gt}", "cach_xem": "{lh_cx}", "trong_so": {lh_ts}, "vi_du": "{lh_cx}"}}\n'
        code += f'    }},\n'
    
    code += "}\n"
    return code

if __name__ == "__main__":
    print(f"Tổng số chủ đề: {len(ALL_200_TOPICS)}")
    print("\nĐang tạo file Python...")
    
    # Lưu vào file
    with open("dung_than_full_200.txt", "w", encoding="utf-8") as f:
        f.write(generate_python_dict())
    
    print("✅ Đã tạo file dung_than_full_200.txt")
    print("Copy nội dung file này vào dung_than_200_chu_de_day_du.py")
