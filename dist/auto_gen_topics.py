# -*- coding: utf-8 -*-
"""
SCRIPT TỰ ĐỘNG TẠO 200 CHỦ ĐỀ DỤNG THẦN
Tự động sinh ra database đầy đủ dựa trên template
"""

# Template cho các chủ đề
TOPIC_TEMPLATES = {
    # NHÓM 1: KINH DOANH & TÀI CHÍNH
    "Cầu Tài Lộc": {
        "ky_mon": ("Sinh Môn + Trực Phù + Mậu", "Sinh Môn = Tài lộc. Trực Phù = Quý nhân. Mậu = Tiền", "Sinh Môn + Trực Phù sinh Can Ngày = Được tài", 70),
        "mai_hoa": ("Quẻ Càn/Đoài - KIM", "Càn/Đoài = Tiền bạc", "Kim vượng = Có tài", 60),
        "luc_hao": ("Hào Thê Tài", "Thê Tài = Tiền bạc", "Thê Tài vượng = Được tài", 65)
    },
    "Mở Rộng Kinh Doanh": {
        "ky_mon": ("Khai Môn + Sinh Môn + Can Ngày", "Khai Môn = Mở rộng. Sinh Môn = Lợi nhuận", "Khai Môn sinh Can Ngày = Mở rộng thành công", 70),
        "mai_hoa": ("Quẻ Chấn - MỘC", "Chấn = Phát triển", "Chấn vượng = Mở rộng tốt", 60),
        "luc_hao": ("Hào Tử Tôn", "Tử Tôn = Phát triển", "Tử Tôn vượng = Mở rộng thuận", 65)
    },
    
    # NHÓM 2: SỰ NGHIỆP & CÔNG DANH
    "Chuyển Công Tác": {
        "ky_mon": ("Khai Môn + Mã Tinh + Can Ngày", "Khai Môn = Công việc mới. Mã Tinh = Di chuyển", "Khai Môn sinh Can Ngày = Chuyển tốt", 70),
        "mai_hoa": ("Quẻ Chấn - MỘC", "Chấn = Chuyển động", "Chấn vượng = Chuyển thuận", 60),
        "luc_hao": ("Hào Quan Quỷ", "Quan Quỷ = Công việc", "Quan Quỷ sinh Thế = Chuyển tốt", 65)
    },
    
    # ... Thêm template cho tất cả 200 chủ đề
}

def tao_chu_de(ten, template):
    """Tạo 1 chủ đề từ template"""
    ky_mon_data, mai_hoa_data, luc_hao_data = template["ky_mon"], template["mai_hoa"], template["luc_hao"]
    
    return {
        "muc_tieu": f"Xem {ten.lower()} như thế nào",
        "ky_mon": {
            "dung_than": ky_mon_data[0],
            "giai_thich": ky_mon_data[1],
            "cach_xem": ky_mon_data[2],
            "trong_so": ky_mon_data[3],
            "vi_du": f"{ky_mon_data[0].split('+')[0].strip()} vượng = {ten} tốt"
        },
        "mai_hoa": {
            "dung_than": mai_hoa_data[0],
            "giai_thich": mai_hoa_data[1],
            "cach_xem": mai_hoa_data[2],
            "trong_so": mai_hoa_data[3],
            "vi_du": f"{mai_hoa_data[2]}"
        },
        "luc_hao": {
            "dung_than": luc_hao_data[0],
            "giai_thich": luc_hao_data[1],
            "cach_xem": luc_hao_data[2],
            "trong_so": luc_hao_data[3],
            "vi_du": f"{luc_hao_data[2]}"
        }
    }

# Tạo tất cả chủ đề
ALL_TOPICS = {}
for ten, template in TOPIC_TEMPLATES.items():
    ALL_TOPICS[ten] = tao_chu_de(ten, template)

print(f"Đã tạo {len(ALL_TOPICS)} chủ đề")
