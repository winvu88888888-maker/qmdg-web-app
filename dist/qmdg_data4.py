import json
import os
from datetime import datetime

# --- CẤU HÌNH FILE DỮ LIỆU TÙY CHỈNH ---
CUSTOM_DATA_FILE = 'custom_data.json'

def load_custom_data():
    """Tải dữ liệu tùy chỉnh từ file JSON, nếu không có thì trả về cấu trúc rỗng."""
    if os.path.exists(CUSTOM_DATA_FILE):
        try:
            with open(CUSTOM_DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            # Nếu file bị lỗi định dạng hoặc không đọc được
            return {"TRUCTU_TRANH": {}}
    return {"TRUCTU_TRANH": {}}

def save_custom_data(data):
    """Lưu dữ liệu tùy chỉnh vào file JSON."""
    try:
        with open(CUSTOM_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except IOError:
        return False

# ======================================================================
# PHẦN 1: DỮ LIỆU CỐ ĐỊNH KY MÔN
# ======================================================================

# Cấu trúc 9 cung
CUNG_NGU_HANH = {
    1: "Thủy", 2: "Thổ", 3: "Mộc", 4: "Mộc", 5: "Thổ",
    6: "Kim", 7: "Kim", 8: "Thổ", 9: "Hỏa"
}

QUAI_TUONG = {
    1: "Khảm", 2: "Khôn", 3: "Chấn", 4: "Tốn", 5: "Trung Cung",
    6: "Càn", 7: "Đoài", 8: "Cấn", 9: "Ly"
}

# Dữ liệu Bát Môn Cố Định (Tra cứu tên gọi hiển thị)
BAT_MON_CO_DINH_DISPLAY = {
    "Khai": "Khai Môn", "Hưu": "Hưu Môn", "Sinh": "Sinh Môn", 
    "Thương": "Thương Môn", "Đỗ": "Đỗ Môn", "Cảnh": "Cảnh Môn", 
    "Tử": "Tử Môn", "Kinh": "Kinh Môn"
}

# Vị trí Bát Môn Cố Định theo Cung (không dùng cung 5)
BAT_MON_CO_DINH_CUNG = {
    1: "Hưu", 2: "Tử", 3: "Thương", 4: "Đỗ", 6: "Kinh", 7: "Khai", 8: "Sinh", 9: "Cảnh"
}

# Địa Chi Giờ
CAN_CHI_Gio = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

# DỮ LIỆU CHÍNH
KY_MON_DATA = {
    "DU_LIEU_DUNG_THAN_PHU_TRO": {
        "CUU_TINH": {
            "Thiên Bồng": {"Hành": "Thủy", "Tính_Chất": "Tướng quân, thích hợp trộm cướp, binh đao."},
            "Thiên Nhuế": {"Hành": "Thổ", "Tính_Chất": "Y dược, giáo dục, bất lợi xuất hành."},
            "Thiên Xung": {"Hành": "Mộc", "Tính_Chất": "Quân sự, cạnh tranh, động tĩnh."},
            "Thiên Phụ": {"Hành": "Mộc", "Tính_Chất": "Văn chương, học thuật, ẩn tàng."},
            "Thiên Cầm": {"Hành": "Thổ", "Tính_Chất": "Lãnh đạo, trung tâm, điều hòa."},
            "Thiên Tâm": {"Hành": "Kim", "Tính_Chất": "Mưu lược, y học, thần bí."},
            "Thiên Trụ": {"Hành": "Kim", "Tính_Chất": "Võ thuật, ẩn náu, gây rối."},
            "Thiên Nhậm": {"Hành": "Thổ", "Tính_Chất": "Điền sản, tài lộc, chậm chạp."},
            "Thiên Anh": {"Hành": "Hỏa", "Tính_Chất": "Văn minh, danh vọng, hỏa hoạn."}
        },
        "BAT_MON": {
            "Khai Môn": {"Cát_Hung": "Đại Cát", "Luận_Đoán": "Thích hợp khai trương, nhậm chức, xuất hành."},
            "Hưu Môn": {"Cát_Hung": "Cát", "Luận_Đoán": "Thích hợp tĩnh dưỡng, nghỉ ngơi, gặp quý nhân."},
            "Sinh Môn": {"Cát_Hung": "Đại Cát", "Luận_Đoán": "Thích hợp cầu tài, sinh sản, kinh doanh."},
            "Thương Môn": {"Cát_Hung": "Hung", "Luận_Đoán": "Thích hợp săn bắt, đòi nợ, kiện cáo (bất lợi)."},
            "Đỗ Môn": {"Cát_Hung": "Bình", "Luận_Đoán": "Thích hợp ẩn náu, phòng thủ, kỹ thuật."},
            "Cảnh Môn": {"Cát_Hung": "Bình", "Luận_Đoán": "Thích hợp văn thư, thi cử, yến tiệc."},
            "Tử Môn": {"Cát_Hung": "Đại Hung", "Luận_Đoán": "Bất lợi mọi việc, chỉ thích hợp mai táng, săn bắn."},
            "Kinh Môn": {"Cát_Hung": "Hung", "Luận_Đoán": "Thích hợp kiện tụng, tranh cãi, báo động."}
        },
        "BAT_THAN": {
            "Trực Phù": {"Tính_Chất": "Quý nhân tối cao, thần che chở, cát lợi."},
            "Đằng Xà": {"Tính_Chất": "Dây dưa, thần quỷ, biến hóa khôn lường."},
            "Thái Âm": {"Tính_Chất": "Ẩn tàng, mưu kế, giúp đỡ kín đáo."},
            "Lục Hợp": {"Tính_Chất": "Hợp tác, hôn nhân, hòa hợp, công bằng."},
            "Bạch Hổ": {"Tính_Chất": "Binh khí, tai ương, hình phạt, uy vũ."},
            "Huyền Vũ": {"Tính_Chất": "Trộm cắp, lừa dối, ám muội."},
            "Cửu Địa": {"Tính_Chất": "Tĩnh, chậm chạp, có lợi ẩn náu."},
            "Cửu Thiên": {"Tính_Chất": "Động, cao xa, có lợi xuất chinh, hành động."}
        }
    },
    
    "CAN_CHI_LUAN_GIAI": {
        "Giáp": {"Hành": "Mộc", "Tính_Chất": "Nguyên soái, chỉ huy, ẩn tàng."},
        "Ất": {"Hành": "Mộc", "Tính_Chất": "Nữ nhân, thần y, thảo dược, cong."},
        "Bính": {"Hành": "Hỏa", "Tính_Chất": "Văn thư, ánh sáng, đột ngột, tai họa."},
        "Đinh": {"Hành": "Hỏa", "Tính_Chất": "Lửa nhỏ, thần tài, văn thư, bí mật."},
        "Mậu": {"Hành": "Thổ", "Tính_Chất": "Tiền vốn, tài sản, người trung thực."},
        "Kỷ": {"Hành": "Thổ", "Tính_Chất": "Đất thấp, dâm dục, bệnh tật, ẩn giấu."},
        "Canh": {"Hành": "Kim", "Tính_Chất": "Đối thủ, trở ngại, đường xá, hình pháp."},
        "Tân": {"Hành": "Kim", "Tính_Chất": "Tội lỗi, sai lầm, kim khí nhỏ."},
        "Nhâm": {"Hành": "Thủy", "Tính_Chất": "Sông nước, trộm cắp, phạm nhân."},
        "Quý": {"Hành": "Thủy", "Tính_Chất": "Thiên võng, tù nhân, mưa gió."}
    },
    
    # Cách cục cố định (Dữ liệu tùy chỉnh sẽ được ghi đè/bổ sung tại đây)
    "TRUCTU_TRANH": {
        # Ất (Thiên)
        "ẤtẤt": {"Tên_Cách_Cục": "Nhật Kỳ Phục Vịnh", "Cát_Hung": "Bình/Hung", "Luận_Giải": "Trì trệ, rối rắm, cần kiên nhẫn."},
        "ẤtBính": {"Tên_Cách_Cục": "Kỳ Nghi Hợp Môn", "Cát_Hung": "Đại Cát", "Luận_Giải": "Tài lộc lớn, tốt cho đầu tư, kết hôn."},
        "ẤtĐinh": {"Tên_Cách_Cục": "Kỳ Nghi Tương Tùy", "Cát_Hung": "Cát", "Luận_Giải": "Hôn nhân tốt, kiện tụng hòa giải."},
        "ẤtMậu": {"Tên_Cách_Cục": "Cầm Tác", "Cát_Hung": "Cát", "Luận_Giải": "Được tài lộc từ người quý, đắc lợi lớn."},
        "ẤtKỷ": {"Tên_Cách_Cục": "Nhật Kỳ Nhập Vọng", "Cát_Hung": "Hung", "Luận_Giải": "Công việc rối rắm, gặp khó khăn."},
        "ẤtCanh": {"Tên_Cách_Cục": "Nhật Kỳ Bách Cách", "Cát_Hung": "Đại Hung", "Luận_Giải": "Mất người, mất tiền, gặp tai họa, đại hung."},
        "ẤtTân": {"Tên_Cách_Cục": "Thanh Long Triết Túc", "Cát_Hung": "Đại Hung", "Luận_Giải": "Bị thương tật chân tay, tài lộc bị mất."},
        "ẤtNhâm": {"Tên_Cách_Cục": "Nhật Kỳ Nhập Địa", "Cát_Hung": "Đại Hung", "Luận_Giải": "Thuyền chìm gặp sóng gió, mọi việc thất bại."},
        "ẤtQuý": {"Tên_Cách_Cục": "Hoa Cái Mão Mệnh", "Cát_Hung": "Cát", "Luận_Giải": "Vận may đến, công danh tốt."},
        # Bính (Thiên)
        "BínhẤt": {"Tên_Cách_Cục": "Hỏa Mộc Tương Sinh", "Cát_Hung": "Cát", "Luận_Giải": "Được quý nhân giúp đỡ, có người cầu hôn."},
        "BínhBính": {"Tên_Cách_Cục": "Tuế Tinh Phục Vịnh", "Cát_Hung": "Bình/Hung", "Luận_Giải": "Trì trệ, nhiều lời đồn, kiện tụng bất lợi."},
        "BínhĐinh": {"Tên_Cách_Cục": "Tinh Kỳ Nhập Tọa", "Cát_Hung": "Cát", "Luận_Giải": "Tốt cho văn chương, khoa cử, thi cử."},
        "BínhMậu": {"Tên_Cách_Cục": "Thanh Long Hồi Đầu", "Cát_Hung": "Đại Cát", "Luận_Giải": "Tiền của đến dồn dập, đầu tư phát đạt, cực kỳ tốt."},
        "BínhKỷ": {"Tên_Cách_Cục": "Hỏa Thổ Tương Sinh", "Cát_Hung": "Cát", "Luận_Giải": "Gặp quý nhân, mọi việc hanh thông."},
        "BínhCanh": {"Tên_Cách_Cục": "Oai Hùng Hỏa Tinh", "Cát_Hung": "Đại Hung", "Luận_Giải": "Kiện tụng thua kiện, tai nạn, tổn hại tài sản."},
        "BínhTân": {"Tên_Cách_Cục": "Hình Cách", "Cát_Hung": "Hung", "Luận_Giải": "Dễ bị phạm tội, kiện cáo, mọi việc không thông."},
        "BínhNhâm": {"Tên_Cách_Cục": "Tuế Tinh Nhập Thiên", "Cát_Hung": "Đại Hung", "Luận_Giải": "Cẩn thận tai họa sông nước, mất của."},
        "BínhQuý": {"Tên_Cách_Cục": "Hoa Cái", "Cát_Hung": "Hung", "Luận_Giải": "Dễ gặp thị phi, kiện tụng bất lợi."},
        # Đinh (Thiên)
        "ĐinhẤt": {"Tên_Cách_Cục": "Nhân Hợp", "Cát_Hung": "Cát", "Luận_Giải": "Tình cảm hòa hợp, hợp tác tốt, hôn nhân thành công."},
        "ĐinhBính": {"Tên_Cách_Cục": "Tinh Kỳ Vọng Trợ", "Cát_Hung": "Cát", "Luận_Giải": "Tốt cho văn thư, giấy tờ, thi cử."},
        "ĐinhĐinh": {"Tên_Cách_Cục": "Tinh Kỳ Phục Vịnh", "Cát_Hung": "Bình/Cát", "Luận_Giải": "Có lợi cho văn chương, thi cử, việc khác trì trệ."},
        "ĐinhMậu": {"Tên_Cách_Cục": "Thanh Long Chuyển Quang", "Cát_Hung": "Đại Cát", "Luận_Giải": "Tốt cho mọi việc, đặc biệt văn chương, thi cử, người đi xa."},
        "ĐinhKỷ": {"Tên_Cách_Cục": "Âm Cung", "Cát_Hung": "Đại Hung", "Luận_Giải": "Bị lừa gạt, mất của, kiện tụng thua kiện."},
        "ĐinhCanh": {"Tên_Cách_Cục": "Hỏa Kim Hình Cách", "Cát_Hung": "Hung", "Luận_Giải": "Xấu cho kiện tụng, đề phòng tiểu nhân."},
        "ĐinhTân": {"Tên_Cách_Cục": "Chu Tước Nhập Ngục", "Cát_Hung": "Đại Hung", "Luận_Giải": "Bị nhốt, kiện tụng bất lợi."},
        "ĐinhNhâm": {"Tên_Cách_Cục": "Nguyệt Hợp", "Cát_Hung": "Hung", "Luận_Giải": "Xấu cho kiện tụng, có nguy cơ phạm tội."},
        "ĐinhQuý": {"Tên_Cách_Cục": "Đằng Xà Giao", "Cát_Hung": "Hung", "Luận_Giải": "Cẩn thận lời nói, thị phi, kiện tụng."},
        # Mậu (Thiên)
        "MậuẤt": {"Tên_Cách_Cục": "Cầm Trác", "Cát_Hung": "Cát", "Luận_Giải": "Được người quý nhân phù trợ, dễ kiếm tiền."},
        "MậuBính": {"Tên_Cách_Cục": "Thanh Long Hồi Đầu", "Cát_Hung": "Đại Cát", "Luận_Giải": "Cực tốt, tiền của dồi dào, mọi sự hanh thông."},
        "MậuĐinh": {"Tên_Cách_Cục": "Thanh Long Chuyển Quang", "Cát_Hung": "Đại Cát", "Luận_Giải": "Tốt cho mọi việc, đặc biệt văn chương, thi cử."},
        "MậuMậu": {"Tên_Cách_Cục": "Phục Vịnh", "Cát_Hung": "Bình/Hung", "Luận_Giải": "Trì trệ, cần nhiều vốn, chậm lợi nhuận."},
        "MậuKỷ": {"Tên_Cách_Cục": "Thanh Long Nhập Thổ", "Cát_Hung": "Đại Hung", "Luận_Giải": "Hung tàn, dễ bị kiện tụng, khó khăn chồng chất."},
        "MậuCanh": {"Tên_Cách_Cục": "Trực Phù Phanh Cách", "Cát_Hung": "Đại Hung", "Luận_Giải": "Mất hết tiền tài, bị thương, cực xấu."},
        "MậuTân": {"Tên_Cách_Cục": "Thanh Long Hiến Giáp", "Cát_Hung": "Hung", "Luận_Giải": "Xấu cho kiện tụng, tranh chấp tài sản."},
        "MậuNhâm": {"Tên_Cách_Cục": "Thanh Long Đào Tẩu", "Cát_Hung": "Đại Hung", "Luận_Giải": "Xấu cho kiện tụng, tài sản bị mất mát, dễ bị cướp."},
        "MậuQuý": {"Tên_Cách_Cục": "Thanh Long Cấu Hợp", "Cát_Hung": "Hung", "Luận_Giải": "Hôn nhân, tình duyên xấu, dễ có quan hệ bất chính."},
        # Kỷ (Thiên)
        "KỷẤt": {"Tên_Cách_Cục": "Địa Hình Mộ Khắc", "Cát_Hung": "Hung", "Luận_Giải": "Xấu, dễ bị kiện cáo, cẩn thận người nhà."},
        "KỷBính": {"Tên_Cách_Cục": "Địa Hỏa Mộc Sinh", "Cát_Hung": "Cát", "Luận_Giải": "Tài lộc dồi dào, công việc phát triển."},
        "KỷĐinh": {"Tên_Cách_Cục": "Địa Tinh", "Cát_Hung": "Cát", "Luận_Giải": "Văn chương, thi cử tốt."},
        "KỷMậu": {"Tên_Cách_Cục": "Khuyển Nhập Địa Võng", "Cát_Hung": "Hung", "Luận_Giải": "Công việc khó khăn, bị lừa gạt, trộm cắp."},
        "KỷKỷ": {"Tên_Cách_Cục": "Địa Hộ Phục Vịnh", "Cát_Hung": "Bình/Hung", "Luận_Giải": "Công việc trì trệ, không thể tiến hành, nên nằm im."},
        "KỷCanh": {"Tên_Cách_Cục": "Hình Cách", "Cát_Hung": "Đại Hung", "Luận_Giải": "Xấu, dễ bị kiện cáo, phạt tù."},
        "KỷTân": {"Tên_Cách_Cục": "Hình Khắc", "Cát_Hung": "Hung", "Luận_Giải": "Cẩn thận kiện tụng, bị nhốt, mắc bệnh."},
        "KỷNhâm": {"Tên_Cách_Cục": "Địa Lưới", "Cát_Hung": "Hung", "Luận_Giải": "Đi lại không tốt, không nên ra ngoài, dễ mất của."},
        "KỷQuý": {"Tên_Cách_Cục": "Địa Võng", "Cát_Hung": "Hung", "Luận_Giải": "Xấu cho làm ăn, kiện tụng thất bại."},
        # Canh (Thiên)
        "CanhẤt": {"Tên_Cách_Cục": "Canh Cách", "Cát_Hung": "Đại Hung", "Luận_Giải": "Kiện tụng, thất bại, đề phòng tiểu nhân."},
        "CanhBính": {"Tên_Cách_Cục": "Canh Hỏa Tương Xung", "Cát_Hung": "Đại Hung", "Luận_Giải": "Dễ bị trộm cướp, lửa tai họa."},
        "CanhĐinh": {"Tên_Cách_Cục": "Hỏa Kim Tương Hình", "Cát_Hung": "Hung", "Luận_Giải": "Có người đến gây sự, kiện tụng không xong."},
        "CanhMậu": {"Tên_Cách_Cục": "Thiên Cách", "Cát_Hung": "Đại Hung", "Luận_Giải": "Rất xấu, tài sản bị mất, bị phạt."},
        "CanhKỷ": {"Tên_Cách_Cục": "Hình Cách", "Cát_Hung": "Hung", "Luận_Giải": "Kiện tụng, dễ bị phạt, cẩn thận tai nạn."},
        "CanhCanh": {"Tên_Cách_Cục": "Thái Bạch Phục Vịnh", "Cát_Hung": "Đại Hung", "Luận_Giải": "Chiến tranh, tai họa, không thể tiến hành, nên tránh."},
        "CanhTân": {"Tên_Cách_Cục": "Bạch Hổ Xung Khắc", "Cát_Hung": "Đại Hung", "Luận_Giải": "Tai nạn giao thông, gặp tiểu nhân, bị phạt."},
        "CanhNhâm": {"Tên_Cách_Cục": "Bạch Hổ Xâm Đại", "Cát_Hung": "Đại Hung", "Luận_Giải": "Cẩn thận tai họa sông nước, kiện tụng tù tội."},
        "CanhQuý": {"Tên_Cách_Cục": "Bàng Quỹ", "Cát_Hung": "Đại Hung", "Luận_Giải": "Tù tội, bệnh nặng, không thể thoát."},
        # Tân (Thiên)
        "TânẤt": {"Tên_Cách_Cục": "Thanh Long Triết Túc", "Cát_Hung": "Đại Hung", "Luận_Giải": "Tàn tật, mất của, bệnh tật tái phát."},
        "TânBính": {"Tên_Cách_Cục": "Hợp Hình", "Cát_Hung": "Hung", "Luận_Giải": "Kiện tụng thua kiện, tai nạn, mất của."},
        "TânĐinh": {"Tên_Cách_Cục": "Chu Tước Nhập Ngục", "Cát_Hung": "Đại Hung", "Luận_Giải": "Bị nhốt, phạt tù."},
        "TânMậu": {"Tên_Cách_Cục": "Thanh Long Hiến Giáp", "Cát_Hung": "Hung", "Luận_Giải": "Kiện tụng bất lợi, cẩn thận trộm cướp."},
        "TânKỷ": {"Tên_Cách_Cục": "Hình Khắc", "Cát_Hung": "Hung", "Luận_Giải": "Dễ bị kiện cáo, cẩn thận mất của."},
        "TânCanh": {"Tên_Cách_Cục": "Bạch Hổ Xung Khắc", "Cát_Hung": "Đại Hung", "Luận_Giải": "Mất tiền, tai nạn."},
        "TânTân": {"Tên_Cách_Cục": "Thiên Đình Phục Vịnh", "Cát_Hung": "Bình/Hung", "Luận_Giải": "Kiện tụng bất lợi, việc chậm tiến."},
        "TânNhâm": {"Tên_Cách_Cục": "Thiên Lao Khổ", "Cát_Hung": "Đại Hung", "Luận_Giải": "Bị nhốt, kiện tụng không xong."},
        "TânQuý": {"Tên_Cách_Cục": "Thiên Đình Cấu Hợp", "Cát_Hung": "Hung", "Luận_Giải": "Kiện tụng liên miên, bệnh tật kéo dài."},
        # Nhâm (Thiên)
        "NhâmẤt": {"Tên_Cách_Cục": "Xà Yêu Triền Thân", "Cát_Hung": "Hung", "Luận_Giải": "Có thị phi, lừa gạt, hôn nhân xấu."},
        "NhâmBính": {"Tên_Cách_Cục": "Xà Thủy Vọng Giang", "Cát_Hung": "Đại Hung", "Luận_Giải": "Gặp tai họa sông nước, kiện tụng bất lợi."},
        "NhâmĐinh": {"Tên_Cách_Cục": "Thủy Hỏa Tương Sát", "Cát_Hung": "Hung", "Luận_Giải": "Kiện tụng, tranh chấp, dễ phạm tội."},
        "NhâmMậu": {"Tên_Cách_Cục": "Thanh Long Đào Tẩu", "Cát_Hung": "Đại Hung", "Luận_Giải": "Kiện tụng thua, mất của, bỏ trốn."},
        "NhâmKỷ": {"Tên_Cách_Cục": "Địa Lưới", "Cát_Hung": "Hung", "Luận_Giải": "Xấu cho đi lại, dễ bị nhốt, mất của."},
        "NhâmCanh": {"Tên_Cách_Cục": "Đại Bạch Hổ", "Cát_Hung": "Đại Hung", "Luận_Giải": "Bệnh tật nặng, dễ chết, cẩn thận tai nạn."},
        "NhâmTân": {"Tên_Cách_Cục": "Thiên Lao Khổ", "Cát_Hung": "Đại Hung", "Luận_Giải": "Tù tội, bệnh tật khó chữa."},
        "NhâmNhâm": {"Tên_Cách_Cục": "Thiên Phạt Phục Vịnh", "Cát_Hung": "Đại Hung", "Luận_Giải": "Tai họa, kiện tụng kéo dài, không nên hành động."},
        "NhâmQuý": {"Tên_Cách_Cục": "Thuyền Chìm", "Cát_Hung": "Đại Hung", "Luận_Giải": "Mất của, tai họa lớn, kiện tụng thua."},
        # Quý (Thiên)
        "QuýẤt": {"Tên_Cách_Cục": "Hoa Cái Mão Mệnh", "Cát_Hung": "Cát", "Luận_Giải": "Tốt cho công danh, có quý nhân phù trợ."},
        "QuýBính": {"Tên_Cách_Cục": "Hoa Cái", "Cát_Hung": "Hung", "Luận_Giải": "Dễ gặp thị phi, kiện tụng."},
        "QuýĐinh": {"Tên_Cách_Cục": "Đằng Xà Giao", "Cát_Hung": "Hung", "Luận_Giải": "Bị lừa gạt, gặp thị phi, kiện tụng."},
        "QuýMậu": {"Tên_Cách_Cục": "Thanh Long Cấu Hợp", "Cát_Hung": "Hung", "Luận_Giải": "Xấu cho hôn nhân, tình cảm, dễ có quan hệ bất chính."},
        "QuýKỷ": {"Tên_Cách_Cục": "Địa Võng", "Cát_Hung": "Hung", "Luận_Giải": "Xấu cho đi lại, dễ bị nhốt."},
        "QuýCanh": {"Tên_Cách_Cục": "Bàng Quỹ", "Cát_Hung": "Đại Hung", "Luận_Giải": "Tù tội, bệnh tật nặng, không thể thoát."},
        "QuýTân": {"Tên_Cách_Cục": "Thiên Đình Cấu Hợp", "Cát_Hung": "Hung", "Luận_Giải": "Kiện tụng, tranh chấp kéo dài, bệnh tật khó chữa."},
        "QuýNhâm": {"Tên_Cách_Cục": "Thiên Võng", "Cát_Hung": "Đại Hung", "Luận_Giải": "Tai họa, mất của, kiện tụng thua."},
        "QuýQuý": {"Tên_Cách_Cục": "Thiên Võng Phục Vịnh", "Cát_Hung": "Đại Hung", "Luận_Giải": "Tù tội, tai họa liên tiếp, không nên hành động."}
    },
    
    "TOPIC_INTERPRETATIONS": {
        "Xem Nhà (Dương Trạch)": {
            "Dụng_Thần": ["Sinh Môn", "Trực Phù", "Cửu Địa", "Can Ngày", "Can Giờ"],
            "Luận_Giải_Gợi_Ý": "Sinh Môn là nhà, Trực Phù là chủ. Sinh Môn sinh Trực Phù là nhà tốt. Trực Phù khắc Sinh Môn là chủ khắc nhà (tốt). Sinh Môn khắc Trực Phù là nhà khắc chủ (xấu)."
        },
        "Xem Hạn (Vận Hạn)": {
            "Dụng_Thần": ["Can Ngày", "Can Tuổi", "Trực Phù", "Cửa Sinh", "Cửa Tử"],
            "Luận_Giải_Gợi_Ý": "Xem Can Ngày (mệnh chủ) gặp Cửa gì, Sao gì. Gặp Cửa Tử, Cửa Kinh là xấu. Gặp Cửa Sinh, Cửa Khai là tốt."
        },
        "Xem Xe Cộ": {
            "Dụng_Thần": ["Cảnh Môn", "Thương Môn", "Can Giờ"],
            "Luận_Giải_Gợi_Ý": "Cảnh Môn là xe, Thương Môn là hư hại/tai nạn. Nếu Cảnh Môn gặp Hung cách (Bạch Hổ, Huyền Vũ) thì xe dễ hỏng hoặc bị lừa."
        },
        "Xem Mua Bán (Kinh Doanh)": {
            "Dụng_Thần": ["Can Ngày", "Can Giờ", "Sinh Môn", "Mậu"],
            "Luận_Giải_Gợi_Ý": "Can Ngày là người mua, Can Giờ là người bán. Sinh Môn là lợi nhuận, Mậu là vốn. Sinh Môn sinh Can Ngày là có lợi."
        },
        "Xem Tình Duyên (Hôn Nhân)": {
            "Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Cửa Hưu"],
            "Luận_Giải_Gợi_Ý": "Lục Hợp là mai mối/tình cảm chung. Ất là nữ, Canh là nam. Ất Canh tương sinh là tốt. Lục Hợp sinh cả hai là đại cát."
        },
        "Xem Bệnh Tật": {
            "Dụng_Thần": ["Thiên Nhuế", "Cửa Tử", "Can Ngày", "Bệnh Nhân (Can Tuổi)"],
            "Luận_Giải_Gợi_Ý": "Thiên Nhuế là bệnh, Cửa Tử là chết chóc. Thiên Tâm/Ất Kỳ là bác sĩ/thuốc. Thiên Tâm khắc Thiên Nhuế là bệnh chữa được."
        },
        "Xem Mất Của": {
            "Dụng_Thần": ["Huyền Vũ", "Can Giờ", "Can Ngày"],
            "Luận_Giải_Gợi_Ý": "Huyền Vũ là kẻ trộm. Huyền Vũ khắc Can Ngày là khó tìm. Can Ngày khắc Huyền Vũ là bắt được trộm."
        },
        "Xem Công Danh (Sự Nghiệp)": {
            "Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"],
            "Luận_Giải_Gợi_Ý": "Khai Môn là công việc/chức vụ. Khai Môn sinh Can Ngày là thăng tiến. Khai Môn khắc Can Ngày là áp lực/bị sa thải."
        },
        "Xem Thi Cử": {
            "Dụng_Thần": ["Cảnh Môn", "Đinh Kỳ", "Thiên Phụ"],
            "Luận_Giải_Gợi_Ý": "Cảnh Môn là bài thi, Đinh Kỳ là điểm số, Thiên Phụ là giám thị. Đinh/Cảnh sinh Can Ngày là đỗ đạt."
        },
        "Xem Xuất Hành": {
            "Dụng_Thần": ["Khai Môn", "Cảnh Môn", "Can Ngày"],
            "Luận_Giải_Gợi_Ý": "Khai Môn là hướng đi. Khai Môn sinh Can Ngày là đi thuận lợi. Gặp Cửa Kinh/Thương là dễ bị cản trở."
        },
        "Luận về chiêm nghiệm Chủ - Khách": {"Dụng_Thần": ["Can Ngày (Khách)", "Can Giờ (Chủ)", "Trực Phù", "Trực Sử"], "Luận_Giải_Gợi_Ý": "Chủ (Tĩnh/Sau) lợi khi Can Giờ vượng, sinh Trực Phù. Khách (Động/Trước) lợi khi Can Ngày vượng, sinh Trực Sử."},
        "Kỳ Môn Xem Việc": {"Dụng_Thần": ["Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Can Ngày khắc Can Giờ là việc dễ thành. Can Giờ khắc Can Ngày là việc khó, trắc trở."},
        "Xem Việc Nhập Ngũ": {"Dụng_Thần": ["Trực Phù", "Thương Môn"], "Luận_Giải_Gợi_Ý": "Thương Môn vượng tướng, không bị khắc là tốt. Trực Phù sinh Thương Môn là đường binh nghiệp thuận lợi."},
        "Xem Việc Đánh Chiếm Thành Trì": {"Dụng_Thần": ["Trực Phù", "Canh"], "Luận_Giải_Gợi_Ý": "Cần Cửu Thiên, Thương Môn vượng. Trực Phù (Tướng) khắc Canh (Địch) là thắng."},
        "Xem Việc Giữ Thành": {"Dụng_Thần": ["Trực Phù", "Cửa Đỗ"], "Luận_Giải_Gợi_Ý": "Cần Cửu Địa, Đỗ Môn vượng tướng để ẩn tàng, phòng thủ vững chắc."},
        "Xem Về Đạo Tặc": {"Dụng_Thần": ["Huyền Vũ", "Thiên Bồng"], "Luận_Giải_Gợi_Ý": "Huyền Vũ, Thiên Bồng vượng là trộm cướp mạnh. Nếu bị khắc là dễ bắt."},
        "Xem Giặc Ở Biên Giới": {"Dụng_Thần": ["Canh", "Huyền Vũ"], "Luận_Giải_Gợi_Ý": "Canh kim vượng là giặc mạnh, đang đến gần. Sao Thiên Xung, Thiên Bồng chỉ hướng giặc."},
        "Xem Thắng Bại Chủ Khách": {"Dụng_Thần": ["Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Can Ngày khắc Can Giờ: Khách thắng. Can Giờ khắc Can Ngày: Chủ thắng. Tương sinh là hòa."},
        "Địch Ta": {"Dụng_Thần": ["Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Ta khắc địch là ta thắng. Địch khắc ta là địch thắng. Cần xem thêm vượng suy của Can."},
        "Xem Về Tin Tức Nơi Xa": {"Dụng_Thần": ["Cửa Cảnh", "Đinh Kỳ"], "Luận_Giải_Gợi_Ý": "Cửa Cảnh sinh Can Ngày là tin thật. Gặp Hung cách/Huyền Vũ là tin giả."},
        "Xem Về Cát Hung Kế Hoạch Lớn": {"Dụng_Thần": ["Trực Phù", "Khai Môn"], "Luận_Giải_Gợi_Ý": "Trực Phù sinh Can Ngày là đại cát. Khai Môn vượng tướng là thành công."},
        "Xem Nhận Văn Kiện Trả Lời": {"Dụng_Thần": ["Cửa Cảnh", "Đinh Kỳ"], "Luận_Giải_Gợi_Ý": "Cửa Cảnh, Đinh Kỳ sinh Can Ngày là có tin hồi âm tốt."},
        "Xem Quan Mới Nhập Chức Tốt Xấu": {"Dụng_Thần": ["Khai Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Khai Môn sinh Can Ngày, được Niên Can sinh là quan lộc bền vững."},
        "Xem Quan Sai Phái Thong Thả/Gấp": {"Dụng_Thần": ["Trực Phù"], "Luận_Giải_Gợi_Ý": "Trực Phù vượng là đi nhanh, Hưu/Tù là chậm."},
        "Xem Di Dời Mồ Mả/Nhà Cửa": {"Dụng_Thần": ["Cửa Sinh", "Cửa Tử"], "Luận_Giải_Gợi_Ý": "Cửa Tử (Mộ)/Sinh (Nhà) sinh Can Ngày là tốt. Không Vong, Phản Ngâm là xấu."},
        "Xem Thăng Chức": {"Dụng_Thần": ["Khai Môn", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Khai Môn sinh Can Ngày, lại được Cửu Tinh vượng sinh là thăng chức nhanh."},
        "Xem Yết Kiến": {"Dụng_Thần": ["Cửa Hưu", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Trực Phù sinh Can Ngày là được gặp và giúp đỡ. Khắc là bị từ chối."},
        "Xem Lùng Bắt Trộm Cướp": {"Dụng_Thần": ["Huyền Vũ", "Thương Môn"], "Luận_Giải_Gợi_Ý": "Huyền Vũ khắc Can Ngày là mất. Can Ngày khắc Huyền Vũ là bắt được."},
        "Xem Vay Mượn": {"Dụng_Thần": ["Cửa Sinh", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Trực Phù (Chủ nợ) sinh Can Ngày (Người vay) là vay được."},
        "Xem Cầu Tài": {"Dụng_Thần": ["Cửa Sinh", "Mậu"], "Luận_Giải_Gợi_Ý": "Sinh Môn sinh Can Ngày, Mậu vượng là đại lợi. Sinh khắc Mậu là có lời."},
        "Xem Người Bên Ngoài Yên Không": {"Dụng_Thần": ["Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Can Ngày (Người ở nhà) sinh Can Giờ (Người ngoài) là bình yên."},
        "Xem Thời Tiết": {"Dụng_Thần": ["Thiên Trụ", "Thiên Anh"], "Luận_Giải_Gợi_Ý": "Thiên Trụ/Nhâm Quý chủ mưa. Thiên Anh/Bính Đinh chủ nắng. Thiên Bồng mưa to."},
        "Xem Đi Xa Định Ngày Về": {"Dụng_Thần": ["Can Ngày", "Mã Tinh"], "Luận_Giải_Gợi_Ý": "Can Ngày khắc Can Giờ/Mã Tinh động là về được."},
        "Người Đi Xa Xem Ở Nhà Yên Không": {"Dụng_Thần": ["Can Ngày", "Cửa Sinh"], "Luận_Giải_Gợi_Ý": "Can Ngày sinh Cửa Sinh (Nhà) là bình an."},
        "Xem Cầu Người": {"Dụng_Thần": ["Trực Phù", "Cửa Hưu"], "Luận_Giải_Gợi_Ý": "Trực Phù, Cửa Hưu sinh Can Ngày là được giúp đỡ."},
        "Xem Đơn Kiện": {"Dụng_Thần": ["Cửa Cảnh", "Đinh Kỳ"], "Luận_Giải_Gợi_Ý": "Cửa Cảnh, Đinh Kỳ vượng tướng, sinh Can Ngày là đơn từ thuận lợi."},
        "Xem Ngủ Mơ Cát Hung": {"Dụng_Thần": ["Đằng Xà", "Môn Cảnh"], "Luận_Giải_Gợi_Ý": "Đằng Xà lâm Huyền Vũ, Cửa Tử là ác mộng. Lâm Cát Môn là điềm lành."},
        "Xem Chim Chóc Kêu": {"Dụng_Thần": ["Cửa Cảnh"], "Luận_Giải_Gợi_Ý": "Cửa Cảnh, Đằng Xà vượng là có điềm lạ, cần đề phòng."},
        "Xem Yêu Quái Phương Nào": {"Dụng_Thần": ["Đằng Xà"], "Luận_Giải_Gợi_Ý": "Cung có Đằng Xà là phương có điềm lạ/yêu quái."},
        "Xem Tránh Nạn Phương Nào": {"Dụng_Thần": ["Cửa Đỗ", "Cửu Địa"], "Luận_Giải_Gợi_Ý": "Phương có Cửa Đỗ, Cửu Địa là nơi ẩn nấp an toàn nhất."},
        "Xem Nên Sai Khiến Người Nào": {"Dụng_Thần": ["Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Can Ngày khắc Can Giờ là sai khiến được người đó."},
        "Xem Nghỉ Việc": {"Dụng_Thần": ["Khai Môn"], "Luận_Giải_Gợi_Ý": "Khai Môn khắc Can Ngày/Mệnh là nên nghỉ. Khai Môn sinh là tốt, nên giữ."},
        "Xem Xin Việc": {"Dụng_Thần": ["Khai Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Khai Môn sinh Can Ngày, Niên mệnh là được việc. Khắc là trượt."},
        "Xem Mở Quán": {"Dụng_Thần": ["Cửa Sinh", "Khai Môn"], "Luận_Giải_Gợi_Ý": "Khai Môn, Cửa Sinh đồng sinh Can Ngày là đại lợi. Tỵ Hòa cũng tốt."},
        "Xem Thăm Hỏi Người": {"Dụng_Thần": ["Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Can Ngày (khách) sinh Can Giờ (chủ) là dễ gặp, được tiếp đón."},
        "Xem Người Đến Thăm": {"Dụng_Thần": ["Can Giờ", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Can Giờ sinh Can Ngày là khách mang lợi đến. Khắc là khách gây phiền."},
        "Xem Tin Tức Thực Hư": {"Dụng_Thần": ["Cửa Cảnh", "Chu Tước"], "Luận_Giải_Gợi_Ý": "Cửa Cảnh sinh Can Ngày là thật. Gặp Huyền Vũ/Đằng Xà là giả/bị lừa."},
        "Xem Đi Xa (Thủy/Bộ/Hàng Không)": {"Dụng_Thần": ["Khai Môn", "Cảnh Môn", "Cửa Hưu"], "Luận_Giải_Gợi_Ý": "Bộ xem Khai Môn. Thủy xem Hưu Môn. Không xem Cảnh Môn. Vượng Tướng là tốt."},
        "Xem Tội Nặng Nhẹ": {"Dụng_Thần": ["Tân", "Nhâm"], "Luận_Giải_Gợi_Ý": "Tân là tội nhân. Nhâm là thiên lao. Tân gặp Mậu là tội nhẹ/tha."},
        "Xem Cầm Tù": {"Dụng_Thần": ["Nhâm", "Tân"], "Luận_Giải_Gợi_Ý": "Nhâm vượng là tù lâu. Nhâm gặp Không Vong là sớm ra."},
        "Xem Kiện Tụng": {"Dụng_Thần": ["Cửa Kinh", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Cửa Kinh là luật sư. Trực Phù khắc Canh là thắng."},
        "Xem Có Bị Trách Phạt": {"Dụng_Thần": ["Trực Phù", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Trực Phù sinh Can Ngày là được tha. Khắc là bị phạt."},
        "Xem Xét Xử Kiện Tụng": {"Dụng_Thần": ["Cửa Kinh", "Thiên Tâm"], "Luận_Giải_Gợi_Ý": "Cửa Kinh, Thiên Tâm công bằng. Canh sinh Trực Phù là hòa giải."},
        "Xem Thưa Kiện": {"Dụng_Thần": ["Cửa Kinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Cửa Kinh sinh Can Ngày là thuận lợi."},
        "Xem Hỏi Bệnh": {"Dụng_Thần": ["Thiên Nhuế", "Cửa Tử"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế là bệnh. Tử Môn là chết. Sinh Môn khắc Thiên Nhuế là sống."},
        "Xem Mời Thầy Thuốc": {"Dụng_Thần": ["Thiên Tâm", "Ất"], "Luận_Giải_Gợi_Ý": "Thiên Tâm/Ất sinh Can Ngày là thuốc tốt/thầy giỏi."},
        "Xem Là Chứng Bệnh Gì": {"Dụng_Thần": ["Thiên Nhuế"], "Luận_Giải_Gợi_Ý": "Căn cứ ngũ hành Thiên Nhuế và cung nó đóng."},
        "Xem Cát Hung Bệnh Tình": {"Dụng_Thần": ["Thiên Nhuế", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Bệnh tinh khắc Mệnh là hung. Mệnh khắc Bệnh tinh là cát."},
        "Xác Định Người Lấy Trộm": {"Dụng_Thần": ["Huyền Vũ", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Huyền Vũ dương tinh là nam, âm tinh là nữ."},
        "Xem Việc Mời Khách": {"Dụng_Thần": ["Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Can Giờ sinh Can Ngày là khách đến, chủ được lợi."},
        "Xem Mộ Phần": {"Dụng_Thần": ["Cửa Tử", "Cửu Địa"], "Luận_Giải_Gợi_Ý": "Tử Môn sinh Can Ngày là tốt. Khắc là xấu."},
        "Xem Phương Nhậm Chức": {"Dụng_Thần": ["Khai Môn"], "Luận_Giải_Gợi_Ý": "Khai Môn ở phương nào thì nhậm chức phương đó tốt."},
        "Xem Đoán Người Đi Xa Về": {"Dụng_Thần": ["Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Can Ngày sinh Can Giờ: Chưa về. Khắc là sắp về."},
        "Xem Đòi Tiền": {"Dụng_Thần": ["Thương Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thương Môn/Trực Phù khắc Can Giờ là đòi được."},
        "Xem Yết Kiến Quý Nhân": {"Dụng_Thần": ["Cửa Hưu", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Trực Phù sinh Can Ngày là gặp thuận lợi."},
        "Xem Sinh Trai Gái": {"Dụng_Thần": ["Thiên Cầm"], "Luận_Giải_Gợi_Ý": "Thiên Cầm/Thiên Nhuế + Dương tinh là trai, Âm tinh là gái."},
        "Xem Bao Giờ Có Con": {"Dụng_Thần": ["Thiên Nhuế", "Cửa Sinh"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế, Cửa Sinh vượng. Cung Thai nhi không bị khắc."},
        "Xem Mua Hàng": {"Dụng_Thần": ["Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Can Ngày sinh Mậu là mua được hàng tốt."},
        "Xem Bán Hàng": {"Dụng_Thần": ["Can Giờ", "Mậu"], "Luận_Giải_Gợi_Ý": "Can Giờ sinh Mậu là bán đắt hàng."},
        "Xem Đầu Tư Kinh Doanh": {"Dụng_Thần": ["Cửa Sinh", "Mậu"], "Luận_Giải_Gợi_Ý": "Cửa Sinh sinh Can Ngày, Mậu vượng là đại lợi."},
        "Xem Mua Nhà/Đất": {"Dụng_Thần": ["Cửa Sinh", "Cửa Tử"], "Luận_Giải_Gợi_Ý": "Cửa Sinh sinh Can Ngày là mua được nhà tốt."},
        "Xem Bán Nhà/Đất": {"Dụng_Thần": ["Cửa Sinh", "Cửa Tử"], "Luận_Giải_Gợi_Ý": "Cửa Sinh sinh Can Ngày là bán được giá."},
        "Xem Sống Thọ": {"Dụng_Thần": ["Thiên Xung", "Cửa Sinh"], "Luận_Giải_Gợi_Ý": "Thiên Xung vượng, Cửa Sinh sinh Can Ngày là thọ. Khắc là yểu."},
        "Xem Vận Mệnh": {"Dụng_Thần": ["Can Ngày", "Cửa Sinh"], "Luận_Giải_Gợi_Ý": "Phân tích tổng hợp Bát Môn, Cửu Tinh, Bát Thần tại cung Mệnh (Can Ngày)."},
        "Xem Trú Ẩn": {"Dụng_Thần": ["Cửa Đỗ", "Cửu Địa"], "Luận_Giải_Gợi_Ý": "Dưới Cửa Đỗ, Cửu Địa là nơi ẩn nấp an toàn nhất."}
    }
}


# ======================================================================
# PHẦN 2: LOGIC TÍNH TOÁN CƠ BẢN (CHÍNH XÁC THEO QMDG)
# ======================================================================

def tinh_dia_chi_gio(gio_hien_tai):
    """Tìm Địa Chi Giờ dựa trên giờ hiện tại."""
    # Tý (23h-1h) -> Hợi (21h-23h)
    index = int((gio_hien_tai + 1) / 2) % 12
    return CAN_CHI_Gio[index]

def an_bai_luc_nghi(cuc, is_duong_don):
    """
    An bài Lục Nghi (Địa Bàn) dựa vào Cục và Âm/Dương Độn.
    Thứ tự: Mậu, Kỷ, Canh, Tân, Nhâm, Quý, Đinh, Bính, Ất.
    Dương Độn: Thuận (1->9). Âm Độn: Nghịch (9->1).
    Args:
        cuc (int): Số cục (1-9).
        is_duong_don (bool): True = Dương Độn, False = Âm Độn.
    Returns:
        dict: {cung_so: 'Can'}
    """
    # Lục nghi tam kỳ thứ tự: Mậu Kỷ Canh Tân Nhâm Quý Đinh Bính Ất
    LUC_NGHI_ORDER = ["Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý", "Đinh", "Bính", "Ất"]
    dia_ban = {}
    
    current_pos = cuc
    
    for nghi in LUC_NGHI_ORDER:
        dia_ban[current_pos] = nghi
        if is_duong_don:
            current_pos += 1
            if current_pos > 9: current_pos = 1
        else:
            current_pos -= 1
            if current_pos < 1: current_pos = 9
            
    return dia_ban

def tinh_ngu_hanh_sinh_khac(hanh1, hanh2):
    """Tính Ngũ Hành Sinh Khắc."""
    if hanh1 == 'N/A' or hanh2 == 'N/A': return "N/A"
    if hanh1 == hanh2: return "Bình Hòa"
    
    rules = {
        ("Kim", "Thủy"): "Sinh", ("Thủy", "Mộc"): "Sinh", ("Mộc", "Hỏa"): "Sinh",
        ("Hỏa", "Thổ"): "Sinh", ("Thổ", "Kim"): "Sinh",
        
        ("Kim", "Mộc"): "Khắc", ("Mộc", "Thổ"): "Khắc", ("Thổ", "Thủy"): "Khắc",
        ("Thủy", "Hỏa"): "Khắc", ("Hỏa", "Kim"): "Khắc"
    }
    
    result = rules.get((hanh1, hanh2))
    if result == "Sinh": return f"{hanh1} Sinh {hanh2} (Cát)"
    if result == "Khắc": return f"{hanh1} Khắc {hanh2} (Hung)"
    
    result_nguoc = rules.get((hanh2, hanh1))
    if result_nguoc == "Sinh": return f"{hanh1} Bị {hanh2} Sinh (Tiểu Cát)" 
    if result_nguoc == "Khắc": return f"{hanh1} Bị {hanh2} Khắc (Đại Hung)" 
    
    return "Bình Hòa"


def kiem_tra_cau_truc_tranh(can_thien_ban, dia_can):
    """Kiểm tra các cặp Can Thiên/Can Địa có nằm trong TRUCTU_TRANH không."""
    ket_qua = {}
    
    # Chuẩn bị Can Thiên Bàn đầy đủ (thêm Mậu vào cung 5 nếu chưa có)
    can_thien_ban_full = can_thien_ban.copy()
    if 5 not in can_thien_ban_full or can_thien_ban_full[5] == 'N/A':
        can_thien_ban_full[5] = "Mậu" 
        
    tranh_data_all = KY_MON_DATA["TRUCTU_TRANH"] 

    for cung_so in range(1, 10):
        can_thien = can_thien_ban_full.get(cung_so, 'N/A')
        can_dia = dia_can.get(cung_so, 'N/A')
        
        if can_thien and can_dia and can_thien not in ["Giáp", "N/A"] and can_dia not in ["Giáp", "N/A"]:
            # Key: Can Thiên + Can Địa (ví dụ: ẤtBính)
            key = can_thien.strip() + can_dia.strip()
            
            result = tranh_data_all.get(key, {})
            
            if result:
                ket_qua[cung_so] = result
            else:
                ket_qua[cung_so] = {"Tên_Cách_Cục": "Không có", "Cát_Hung": "Bình", "Luận_Giải": "Không có cách cục đặc biệt được lưu."}
                
        else:
            ket_qua[cung_so] = {"Tên_Cách_Cục": "Không có", "Cát_Hung": "Bình", "Luận_Giải": "Không có cách cục đặc biệt được lưu."}

    return ket_qua


def tinh_khong_vong(can_gio, dia_chi_gio):
    """Tính Khổng Vong dựa vào Can Giờ và Chi Giờ."""
    if not can_gio: return []
    CAN_LIST = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    CHI_LIST = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    
    try:
        idx_can = CAN_LIST.index(can_gio)
        idx_chi = CHI_LIST.index(dia_chi_gio)
        
        # Tìm Tuần Không (Khoảng cách từ Chi đến Can)
        diff = idx_chi - idx_can
        if diff < 0: diff += 12
        
        # Tuần Thủ tại: (Chi - Can) % 12? Không, Tuần Thủ là Giáp tại vị trí đó
        # Tuần Không là 2 chi tiếp theo sau khi kết thúc 10 can
        # Ví dụ: Giáp Tý (0,0) -> Tuần Không là Tuất Hợi (10, 11)
        # Công thức: Tìm chi của Quý. Chi sau Quý là Tuần Không.
        # Chi Quý = (idx_chi + (9 - idx_can)) % 12
        idx_chi_quy = (idx_chi + (9 - idx_can)) % 12
        
        kv1_idx = (idx_chi_quy + 1) % 12
        kv2_idx = (idx_chi_quy + 2) % 12
        
        kv1 = CHI_LIST[kv1_idx]
        kv2 = CHI_LIST[kv2_idx]
        
        # Ánh xạ Chi sang Cung
        CHI_CUNG_MAP = {
            "Tý": 1, "Sửu": 8, "Dần": 8, "Mão": 3, "Thìn": 4, "Tị": 4,
            "Ngọ": 9, "Mùi": 2, "Thân": 2, "Dậu": 7, "Tuất": 6, "Hợi": 6
        }
        
        return list(set([CHI_CUNG_MAP[kv1], CHI_CUNG_MAP[kv2]]))
        
    except ValueError:
        return []


def tinh_dich_ma(dia_chi_gio):
    """Tính Dịch Mã thực tế."""
    # Thân Tý Thìn -> Dần (Cung 8)
    # Dần Ngọ Tuất -> Thân (Cung 2)
    # Tị Dậu Sửu -> Hợi (Cung 6)
    # Hợi Mão Mùi -> Tị (Cung 4)
    if dia_chi_gio in ["Thân", "Tý", "Thìn"]: return 8
    if dia_chi_gio in ["Dần", "Ngọ", "Tuất"]: return 2
    if dia_chi_gio in ["Tị", "Dậu", "Sửu"]: return 6
    if dia_chi_gio in ["Hợi", "Mão", "Mùi"]: return 4
    return None


def lap_ban_qmdg(cuc, truc_phu_star, truc_su_door, can_gio, chi_gio, is_duong_don):
    """
    Lập bàn QMDG đầy đủ theo quy luật chuyển động.
    """
    # 1. Định nghĩa vị trí Cố Định (Gốc)
    # Cửu Tinh Gốc (Địa Bàn)
    SAO_GOC = {
        1: "Thiên Bồng", 2: "Thiên Nhuế", 3: "Thiên Xung", 4: "Thiên Phụ",
        5: "Thiên Cầm", 6: "Thiên Tâm", 7: "Thiên Trụ", 8: "Thiên Nhậm", 9: "Thiên Anh"
    }
    # Bát Môn Gốc
    MON_GOC = {
        1: "Hưu", 2: "Tử", 3: "Thương", 4: "Đỗ", 
        6: "Khai", 7: "Kinh", 8: "Sinh", 9: "Cảnh"
    }
    
    # 2. Lập Địa Bàn (Lục Nghi)
    dia_ban = an_bai_luc_nghi(cuc, is_duong_don)
    
    # 3. Tìm vị trí hiện tại của Trực Phù (Star) và Trực Sử (Door) trên Địa Bàn
    # Trực Phù và Trực Sử đã được xác định tên ở ngoài, giờ tìm vị trí gốc của chúng
    # Để biết chúng "mang" Can nào đi đâu.
    
    # Tìm cung gốc của Sao Trực Phù
    cung_goc_truc_phu = 0
    for c, s in SAO_GOC.items():
        if s == truc_phu_star:
            cung_goc_truc_phu = c
            break
            
    # Tìm cung gốc của Môn Trực Sử
    cung_goc_truc_su = 0
    for c, m in MON_GOC.items():
        if m == truc_su_door:
            cung_goc_truc_su = c
            break
    if cung_goc_truc_su == 0 and truc_su_door == "Tử": cung_goc_truc_su = 2 # Fallback cho Tử
    
    # 4. Xác định Cung Đích của Trực Phù (Thiên Bàn)
    # Trực Phù bay đến cung có Can Giờ trên Địa Bàn.
    target_stem = can_gio
    if target_stem == "Giáp":
        # Tìm Tuần Thủ dựa trên Chi Giờ (Vì Can là Giáp)
        # Giáp Tý -> Mậu, Giáp Tuất -> Kỷ ...
        # Mapping Chi -> Tuần Thủ (chỉ đúng khi Can là Giáp)
        # Tý(0)->Mậu, Tuất(10)->Kỷ, Thân(8)->Canh, Ngọ(6)->Tân, Thìn(4)->Nhâm, Dần(2)->Quý
        map_giap = {"Tý": "Mậu", "Tuất": "Kỷ", "Thân": "Canh", "Ngọ": "Tân", "Thìn": "Nhâm", "Dần": "Quý"}
        target_stem = map_giap.get(chi_gio, "Mậu")
    
    cung_dich_truc_phu = 0
    for c, can in dia_ban.items():
        if can == target_stem:
            cung_dich_truc_phu = c
            break
            
    if cung_dich_truc_phu == 0:
        # Fallback nếu không tìm thấy
        cung_dich_truc_phu = cung_goc_truc_phu

    # 5. Xoay Thiên Bàn (Chuyển Sao và Can Thiên)
    # Tính độ lệch (Offset)
    # Logic xoay vòng: 1->8->3->4->9->2->7->6 (Vòng Cửu Cung Lạc Thư)
    QUEUE_CUNG = [1, 8, 3, 4, 9, 2, 7, 6]
    
    try:
        idx_src = QUEUE_CUNG.index(cung_goc_truc_phu)
        idx_dst = QUEUE_CUNG.index(cung_dich_truc_phu)
        offset_sao = idx_dst - idx_src
    except ValueError:
        # Cung 5 (Trung Cung)? Thiên Cầm (5) thường đi theo Thiên Nhuế (2)
        if cung_goc_truc_phu == 5:
            # Thiên Cầm ký ở cung 2
            try:
                idx_src = QUEUE_CUNG.index(2)
                idx_dst = QUEUE_CUNG.index(cung_dich_truc_phu)
                offset_sao = idx_dst - idx_src
            except: offset_sao = 0
        else:
            offset_sao = 0

    thien_ban = {}
    can_thien_ban = {}
    
    # Sao và Can gốc di chuyển cùng nhau
    for c_goc in SAO_GOC:
        sao = SAO_GOC[c_goc]
        can_goc = dia_ban.get(c_goc, "N/A") # Can Thiên lấy từ Địa Bàn gốc tại vị trí sao đứng
        
        # Cung 5 (Thiên Cầm) đi cùng Cung 2 (Thiên Nhuế)
        target_c_goc = c_goc
        if c_goc == 5: target_c_goc = 2
            
        try:
            current_idx = QUEUE_CUNG.index(target_c_goc)
            new_idx = (current_idx + offset_sao) % 8
            cung_moi = QUEUE_CUNG[new_idx]
            
            # Lưu Thiên Bàn
            if c_goc == 5: # Thiên Cầm
                 # Nếu cung mới đã có sao (từ Nhuế), ghép thêm hoặc ghi đè?
                 # Thường Thiên Cầm hiển thị cùng Thiên Nhuế.
                 # Ở đây ta lưu riêng, App cần xử lý hiển thị nếu muốn ghép.
                 # Nhưng cấu trúc dict key=cung_so, nên sẽ bị ghi đè.
                 # Giải pháp: App hiển thị Nhuế, Cầm là phụ.
                 pass 
            else:
                thien_ban[cung_moi] = sao
                can_thien_ban[cung_moi] = can_goc
                
        except ValueError: pass
        
    # Xử lý Thiên Cầm đặc biệt: Luôn đi kèm Thiên Nhuế
    # Tìm cung mới của Thiên Nhuế
    for c, s in thien_ban.items():
        if s == "Thiên Nhuế":
            # Gán thêm Thiên Cầm hoặc đánh dấu?
            # Để đơn giản, ta không lưu key riêng cho Cầm ở các cung khác 5,
            # Mà mặc định Cầm đi theo Nhuế trong hiển thị (App lo).
            # Ở đây ta trả về Cầm ở vị trí của Nhuế để tham khảo
            pass

    # 6. Xoay Nhân Bàn (Chuyển Môn)
    # Trực Sử (Lead Door) di chuyển theo số giờ (Chi Giờ)
    # Nguyên tắc: Từ Cung của Phù Đầu (Leader), đếm thuận/nghịch theo Dương/Âm Độn
    # cho đến Chi Giờ hiện tại.
    # Mỗi giờ (1 canh) đi 1 cung.
    # Thứ tự cung đi: 1, 2, 3, 4, 5, 6, 7, 8, 9 (Theo Lạc Thư số)
    # Nếu gặp 5 thì chuyển sang 2 (Khôn).
    
    # a. Tìm chênh lệch giờ (Chi Giờ - Chi Leader)
    # Leader Stem (Mậu/Kỷ...) ẩn Giáp. 
    # Ta biết cung của Leader (cung_tuan_thu -> cung_goc_truc_su)
    # Nhưng ta cần biết Chi của Leader.
    # Leader là Giáp Tý, Giáp Tuất...?
    # Trong hàm calculate_qmdg_params có tính luc_nghi_tuan_thu (Mậu..). 
    # Nhưng ở đây ta chỉ có can_gio, chi_gio.
    # Ta cần tính lại Tuần Thủ của giờ hiện tại để biết Chi khởi đầu.
    # Ví dụ: Giờ Bính Dần.
    # Dần (2) - Bính (2) = 0 -> Giáp Tý (0). Chi Leader = Tý.
    # Khoảng cách = Dần - Tý = 2.
    
    # Tính lại Chi Leader
    CAN_LIST = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    CHI_LIST = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    
    try:
        idx_can = CAN_LIST.index(can_gio)
        idx_chi = CHI_LIST.index(chi_gio)
        diff_val = (idx_chi - idx_can) % 12 # Chi - Can
        # Leader start at this diff. 
        # Ví dụ: Bính(2) Dần(2) -> Diff=0 (Tý). Leader là Giáp Tý.
        # Bính(2) Thân(8). 8-2=6 (Ngọ). Leader là Giáp Ngọ.
        idx_chi_leader = diff_val
        
        # Số bước di chuyển = Chi Giờ - Chi Leader
        steps = (idx_chi - idx_chi_leader) % 12
    except ValueError: 
        steps = 0
        
    # b. Di chuyển từ Cung Leader (cung_tuan_thu)
    # Thay vì từ Cung Gốc của Môn (2), ta phải đi từ vị trí thực tế của Leader (5).
    # Ví dụ: Leader Mậu tại 5. Môn là Tử (2). Ta bắt đầu đi từ 5.
    
    current_cung = cung_goc_truc_phu
    
    for _ in range(steps):
        if is_duong_don:
            current_cung += 1
            if current_cung > 9: current_cung = 1
        else:
            current_cung -= 1
            if current_cung < 1: current_cung = 9
            
    # Sau khi chạy hết steps, ta có cung đích
    if current_cung == 5: current_cung = 2
    cung_dich_truc_su = current_cung
    
    # Tính offset Môn (Xoay Nhân Bàn)
    # Môn ở Cung Đích phải là Trực Sử (Môn Gốc)
    try:
        idx_src_mon = QUEUE_CUNG.index(cung_goc_truc_su)
        idx_dst_mon = QUEUE_CUNG.index(cung_dich_truc_su)
        
        # Môn đi thuận hay nghịch?
        # QMDG đa số phái: Môn xoay thuận chiều kim đồng hồ trên vòng tròn cung.
        offset_mon = idx_dst_mon - idx_src_mon
    except ValueError: offset_mon = 0
    
    nhan_ban = {}
    for c_goc in MON_GOC:
        mon = MON_GOC[c_goc]
        if c_goc == 5: continue # Không có Môn ở 5
        
        try:
            current_idx = QUEUE_CUNG.index(c_goc)
            new_idx = (current_idx + offset_mon) % 8
            cung_moi = QUEUE_CUNG[new_idx]
            nhan_ban[cung_moi] = mon
        except: pass
        
    # 7. An Thần Bàn (Bát Thần)
    # Trực Phù (Thần) đi theo Trực Phù (Sao) -> Tức là về cung_dich_truc_phu
    THAN_ORDER = ["Trực Phù", "Đằng Xà", "Thái Âm", "Lục Hợp", "Bạch Hổ", "Huyền Vũ", "Cửu Địa", "Cửu Thiên"]
    
    than_ban = {}
    try:
        start_idx_cung = QUEUE_CUNG.index(cung_dich_truc_phu)
        
        for i, than in enumerate(THAN_ORDER):
            if is_duong_don:
                # Dương Độn: Thần đi Thuận
                cung_idx = (start_idx_cung + i) % 8
            else:
                # Âm Độn: Thần đi Nghịch
                cung_idx = (start_idx_cung - i) % 8
                
            cung_than = QUEUE_CUNG[cung_idx]
            than_ban[cung_than] = than
            
    except ValueError: pass

    # Trả về kết quả
    return thien_ban, can_thien_ban, nhan_ban, than_ban, cung_dich_truc_phu


def lap_ban_qmdg_thủ_công(sao_cung_1, cua_cung_1, can_thien_cung_1, than_cung_1):
    """
    Lập bàn QMDG thủ công (giữ nguyên logic cũ).
    """
    SAO_LIST = list(KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["CUU_TINH"].keys())
    MON_LIST = list(BAT_MON_CO_DINH_DISPLAY.keys())
    THAN_LIST = list(KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_THAN"].keys())
    CAN_LIST_NON_GIAP = [c for c in KY_MON_DATA["CAN_CHI_LUAN_GIAI"].keys() if c != "Giáp"]
    
    CUNG_AN_BAI = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    
    try: sao_cung_1_index = SAO_LIST.index(sao_cung_1)
    except ValueError: sao_cung_1_index = 0
    
    try: can_cung_1_index = CAN_LIST_NON_GIAP.index(can_thien_cung_1)
    except ValueError: can_cung_1_index = 0
    
    try: cua_cung_1_index = MON_LIST.index(cua_cung_1)
    except ValueError: cua_cung_1_index = 0
        
    try: than_cung_1_index = THAN_LIST.index(than_cung_1)
    except ValueError: than_cung_1_index = 0
        
    thien_ban = {}; can_thien_ban = {}; nhan_ban = {}; than_ban = {}
    
    sao_counter = 0; can_counter = 0; mon_counter = 0; than_counter = 0
    
    for cung_so in CUNG_AN_BAI:
        if cung_so != 5:
            thien_ban[cung_so] = SAO_LIST[(sao_cung_1_index + sao_counter) % len(SAO_LIST)]
            can_thien_ban[cung_so] = CAN_LIST_NON_GIAP[(can_cung_1_index + can_counter) % len(CAN_LIST_NON_GIAP)]
            nhan_ban[cung_so] = MON_LIST[(cua_cung_1_index + mon_counter) % len(MON_LIST)]
            than_ban[cung_so] = THAN_LIST[(than_cung_1_index + than_counter) % len(THAN_LIST)]
            sao_counter += 1; can_counter += 1; mon_counter += 1; than_counter += 1
        else:
            thien_ban[5] = "Thiên Cầm"; can_thien_ban[5] = "Mậu"

    dia_can = an_bai_luc_nghi(1, True) # Mặc định
    truc_phu_cung_so = 1

    return thien_ban, can_thien_ban, nhan_ban, than_ban, truc_phu_cung_so, dia_can

# Tải dữ liệu tùy chỉnh khi khởi động
KY_MON_DATA_CUSTOM = load_custom_data()
if KY_MON_DATA_CUSTOM and "TRUCTU_TRANH" in KY_MON_DATA_CUSTOM:
    KY_MON_DATA["TRUCTU_TRANH"].update(KY_MON_DATA_CUSTOM["TRUCTU_TRANH"])

TOPIC_INTERPRETATIONS = KY_MON_DATA.get("TOPIC_INTERPRETATIONS", {})
