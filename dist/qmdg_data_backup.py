import json
import os
from datetime import datetime

# --- CẤU HÌNH FILE DỮ LIỆU TÙY CHỈNH ---
CUSTOM_DATA_FILE = 'custom_data.json'
EXCEL_DATA_FILE = 'qmdg_excel_full.json'
ADVANCED_DATA_FILE = 'qmdg_advanced_knowledge.json'

def load_excel_data():
    """Tải dữ liệu đã trích xuất từ Excel và trộn vào KY_MON_DATA."""
    if os.path.exists(EXCEL_DATA_FILE):
        try:
            with open(EXCEL_DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def merge_excel_data(base_data):
    """Trộn dữ liệu Excel vào cấu trúc dữ liệu chính."""
    excel_data = load_excel_data()
    if not excel_data:
        return base_data
    
    # Trộn Stem Combos vào TRUCTU_TRANH
    stem_combos = excel_data.get("STEM_COMBOS", {})
    for key, content in stem_combos.items():
        if key not in base_data["TRUCTU_TRANH"]:
            base_data["TRUCTU_TRANH"][key] = {
                "Tên_Cách_Cục": "Tra cứu Excel",
                "Cát_Hung": "Tra cứu",
                "Luận_Giải": content
            }
        else:
            # Bổ sung thêm diễn giải từ Excel nếu đã có
            base_data["TRUCTU_TRANH"][key]["Luận_Giải"] += f"\n (Excel: {content})"
            
    base_data["ENRICHED_DATA"] = excel_data
    return base_data

def load_advanced_knowledge():
    """Tải dữ liệu nâng cao từ các nguồn PDF/Book."""
    if os.path.exists(ADVANCED_DATA_FILE):
        try:
            with open(ADVANCED_DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

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
    # Dữ liệu từ Excel sẽ được trộn vào đây nếu có
    "ENRICHED_DATA": load_excel_data(),
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
        "Kinh Doanh Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Vừa": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Lớn": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Đầu Tư Tổng Quát": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Ngắn Hạn": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Dài Hạn": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Khẩn Cấp": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Quan Trọng": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Nhỏ": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Vừa": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Lớn": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Rất Lớn": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Cực Lớn": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Trong Nước": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Nước Ngoài": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Quốc Tế": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Mua Bán Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Quốc Tế": {"Dụng_Thần": ["Lục Hợp", "Cửu Thiên", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Thỏa thuận, Cửu Thiên = Quốc tế. Lục Hợp vượng = Đàm phán thành công."},
        "Họp Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khởi Nghiệp Startup": {"Dụng_Thần": ["Khai Môn", "Sinh Môn", "Trực Phù", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Khai Môn = Khởi đầu mới, mở cửa kinh doanh. Sinh Môn = Nguồn tài lộc, lợi nhuận. Trực Phù = Quý nhân hỗ trợ, nhà đầu tư. Khai Môn vượng tướng + Sinh Môn sinh Can Ngày = Khởi nghiệp thành công, được quý nhân đầu tư. Nếu Khai Môn lâm Không Vong = Khó khăn ban đầu. Trực Phù sinh Can Ngày = Gặp nhà đầu tư tốt."},
        "IPO Niêm Yết": {"Dụng_Thần": ["Khai Môn", "Cảnh Môn", "Mậu"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công khai, Cảnh Môn = Thông tin. Khai Môn vượng = IPO thành công."},
        "M&A Sáp Nhập": {"Dụng_Thần": ["Lục Hợp", "Khai Môn", "Sinh Môn"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hợp nhất. Lục Hợp vượng = M&A thuận lợi."},
        "CEO Tổng Giám Đốc": {"Dụng_Thần": ["Trực Phù", "Khai Môn", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Trực Phù = Quyền lực cao nhất, vị trí CEO. Khai Môn = Công ty, tổ chức. Can Năm = Hội đồng quản trị. Can Ngày = Bản thân. Trực Phù lâm cung Can Ngày + Khai Môn vượng = Làm CEO thành công, lãnh đạo tốt. Can Năm sinh Can Ngày = Được hội đồng quản trị ủng hộ. Trực Phù khắc Can Ngày = Áp lực quyền lực lớn."},
        "Khởi Nghiệp Cá Nhân": {"Dụng_Thần": ["Khai Môn", "Can Ngày", "Sinh Môn"], "Luận_Giải_Gợi_Ý": "Khai Môn = Khởi đầu. Khai Môn sinh Can Ngày = Khởi nghiệp thành."},
        "Giáo Sư Tiến Sĩ": {"Dụng_Thần": ["Thiên Phụ", "Trực Phù", "Cảnh Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học thuật cao, nghiên cứu sâu. Trực Phù = Học vị cao nhất, danh vọng. Cảnh Môn = Công bố nghiên cứu, bài báo khoa học. Can Ngày = Bản thân. Thiên Phụ cực vượng + Trực Phù sinh Can Ngày = Đạt học vị Giáo Sư Tiến Sĩ. Cảnh Môn sinh Can Ngày = Công trình nghiên cứu được công nhận quốc tế."},
        "Nobel Giải Thưởng": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Trực Phù", "Cửu Thiên"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học thuật đỉnh cao. Cảnh Môn = Giải thưởng, vinh danh. Trực Phù = Ủy ban Nobel. Cửu Thiên = Tầm ảnh hưởng toàn cầu. Thiên Phụ cực vượng + Cảnh Môn + Trực Phù đồng sinh Can Ngày = Đạt giải Nobel. Cửu Thiên vượng = Nghiên cứu có tầm ảnh hưởng thế giới."},
        "Tình Yêu Đích Thực": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, Ất Canh = Nam nữ. Tương sinh = Tình yêu đích thực."},
        "Hôn Nhân Trăm Năm": {"Dụng_Thần": ["Lục Hợp", "Hưu Môn", "Cửu Địa"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, Cửu Địa = Lâu dài. Lục Hợp vượng = Hôn nhân bền vững."},
        "Ung Thư Bệnh Hiểm": {"Dụng_Thần": ["Thiên Nhuế", "Tử Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh, Tử Môn = Nguy hiểm. Thiên Nhuế khắc Can Ngày = Bệnh nặng."},
        "Sống Thọ 100 Tuổi": {"Dụng_Thần": ["Thiên Xung", "Sinh Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Xung = Sao thọ. Thiên Xung cực vượng = Sống rất thọ."},
        "Án Tử Hình": {"Dụng_Thần": ["Tử Môn", "Bạch Hổ", "Nhâm"], "Luận_Giải_Gợi_Ý": "Tử Môn = Chết, Bạch Hổ = Hình phạt. Tử Môn cực hung = Án tử hình."},
        "Vô Tội Được Tha": {"Dụng_Thần": ["Trực Phù", "Can Ngày", "Khai Môn"], "Luận_Giải_Gợi_Ý": "Trực Phù = Quan tòa. Trực Phù sinh Can Ngày = Được tha vô tội."},
        "Biệt Thự Triệu Đô": {"Dụng_Thần": ["Sinh Môn", "Trực Phù", "Mậu"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Nhà, Mậu = Tiền. Sinh Môn cực vượng = Nhà triệu đô."},
        "Phong Thủy Đại Cát": {"Dụng_Thần": ["Sinh Môn", "Trực Phù", "Cửu Địa"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Nhà, Trực Phù = Quý. Sinh Môn vượng = Phong thủy đại cát."},
        "Du Lịch Vòng Quanh Thế Giới": {"Dụng_Thần": ["Cửu Thiên", "Mã Tinh", "Hưu Môn"], "Luận_Giải_Gợi_Ý": "Cửu Thiên = Rất xa, Mã Tinh = Di chuyển. Mã Tinh vượng = Du lịch vòng quanh thế giới."},
        "Định Cư Mỹ Canada": {"Dụng_Thần": ["Cửu Thiên", "Khai Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Cửu Thiên = Nước ngoài xa. Cửu Thiên vượng = Định cư thành công."},
        "Tìm Người Mất Tích": {"Dụng_Thần": ["Lục Hợp", "Can Giờ", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Can Giờ = Người mất tích. Can Giờ sinh Can Ngày = Tìm được người."},
        "Tìm Kho Báu": {"Dụng_Thần": ["Mậu", "Huyền Vũ", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Mậu = Kho báu, Huyền Vũ = Ẩn giấu. Can Ngày khắc Huyền Vũ = Tìm được kho báu."},
        "Gặp Tổng Thống": {"Dụng_Thần": ["Trực Phù", "Can Năm", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Trực Phù = Quý nhân cao nhất. Trực Phù sinh Can Ngày = Gặp được tổng thống."},
        "Chiến Tranh Thế Giới": {"Dụng_Thần": ["Bạch Hổ", "Thương Môn", "Cửu Thiên"], "Luận_Giải_Gợi_Ý": "Bạch Hổ = Chiến tranh, Cửu Thiên = Toàn cầu. Bạch Hổ cực vượng = Chiến tranh lớn."},
        "Hòa Bình Thế Giới": {"Dụng_Thần": ["Lục Hợp", "Trực Phù", "Cửu Thiên"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hòa bình. Lục Hợp vượng = Hòa bình thế giới."},
        "World Cup Bóng Đá": {"Dụng_Thần": ["Can Ngày", "Can Giờ", "Cảnh Môn"], "Luận_Giải_Gợi_Ý": "Can Ngày = Đội nhà, Can Giờ = Đối thủ. Can Ngày vượng = Vô địch World Cup."},
        "Olympic Huy Chương Vàng": {"Dụng_Thần": ["Cảnh Môn", "Can Ngày", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Cảnh Môn = Giải thưởng. Cảnh Môn sinh Can Ngày = Huy chương vàng Olympic."},
        "Thành Phật Đắc Đạo": {"Dụng_Thần": ["Trực Phù", "Cửu Thiên", "Thiên Phụ"], "Luận_Giải_Gợi_Ý": "Trực Phù = Thần thánh. Trực Phù cực vượng = Thành Phật đắc đạo."},
        "Gặp Thần Tiên": {"Dụng_Thần": ["Trực Phù", "Cửu Thiên", "Đằng Xà"], "Luận_Giải_Gợi_Ý": "Trực Phù = Thần, Cửu Thiên = Thiên giới. Trực Phù vượng = Gặp thần tiên."},
        "Sinh Con Rồng": {"Dụng_Thần": ["Can Giờ", "Thiên Nhuế", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Can Giờ = Con, Trực Phù = Quý. Can Giờ cực vượng = Sinh con rồng."},
        "Gia Đình Hạnh Phúc": {"Dụng_Thần": ["Lục Hợp", "Hưu Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Gia đình, Hưu Môn = Hạnh phúc. Lục Hợp vượng = Gia đình hạnh phúc."},
        "AI Trí Tuệ Nhân Tạo": {"Dụng_Thần": ["Thiên Tâm", "Thiên Phụ", "Cửu Thiên"], "Luận_Giải_Gợi_Ý": "Thiên Tâm = Trí tuệ, Thiên Phụ = Công nghệ. Thiên Tâm vượng = AI phát triển."},
        "Blockchain Crypto": {"Dụng_Thần": ["Thiên Bồng", "Mậu", "Cửu Thiên"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro, Mậu = Tiền. Mậu vượng = Crypto tăng giá."},
        "IPO Niêm Yết Chứng Khoán": {"Dụng_Thần": ["Khai Môn", "Cảnh Môn", "Mậu", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công khai, niêm yết. Cảnh Môn = Thông tin công bố, báo chí. Mậu = Vốn hóa, giá trị cổ phiếu. Trực Phù = Ủy ban chứng khoán, cơ quan quản lý. Khai Môn + Cảnh Môn đồng vượng = IPO thành công vang dội. Mậu sinh Can Ngày = Giá cổ phiếu tăng mạnh sau niêm yết. Trực Phù sinh Can Ngày = Được phê duyệt nhanh."},
        "M&A Sáp Nhập Công Ty": {"Dụng_Thần": ["Lục Hợp", "Khai Môn", "Sinh Môn", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hợp nhất, sáp nhập. Khai Môn = Công ty mới sau sáp nhập. Sinh Môn = Hiệu quả tài chính sau M&A. Can Ngày = Công ty mua, Can Giờ = Công ty bị mua. Lục Hợp vượng + Can Ngày sinh Can Giờ = M&A thuận lợi, đôi bên cùng có lợi. Sinh Môn sinh Can Ngày = Sáp nhập tạo ra hiệu quả kinh tế cao."},
        "Giám Đốc Điều Hành COO": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Thiên Tâm", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Khai Môn = Hoạt động kinh doanh. Trực Phù = CEO, cấp trên. Thiên Tâm = Chiến lược vận hành. Can Ngày = Bản thân COO. Khai Môn sinh Can Ngày + Thiên Tâm vượng = Điều hành hiệu quả. Trực Phù sinh Can Ngày = Được CEO tin tưởng giao quyền."},
        "Kinh Doanh Khu Vực": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Kinh Doanh Địa Phương": {"Dụng_Thần": ["Sinh Môn", "Mậu", "Can Ngày", "Can Giờ"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Lợi nhuận, tài lộc. Mậu = Vốn kinh doanh. Can Ngày = Người kinh doanh. Can Giờ = Đối tác/Khách hàng. Sinh Môn sinh Can Ngày = Kinh doanh có lãi. Mậu vượng = Vốn dồi dào."},
        "Đầu Tư Khu Vực": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Đầu Tư Địa Phương": {"Dụng_Thần": ["Thiên Bồng", "Sinh Môn", "Mậu", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro đầu tư. Sinh Môn = Lợi nhuận. Mậu = Vốn đầu tư. Sinh Môn vượng + Thiên Bồng không khắc = Đầu tư sinh lời. Mậu bị khắc = Mất vốn."},
        "Sự Nghiệp Tổng Quát": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Ngắn Hạn": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Dài Hạn": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Khẩn Cấp": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Quan Trọng": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Nhỏ": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Vừa": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Lớn": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Rất Lớn": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Cực Lớn": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Trong Nước": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Nước Ngoài": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Quốc Tế": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Khu Vực": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Sự Nghiệp Địa Phương": {"Dụng_Thần": ["Khai Môn", "Trực Phù", "Can Ngày", "Can Năm"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công việc, chức vụ. Trực Phù = Cấp trên, lãnh đạo. Can Năm = Công ty, tổ chức. Khai Môn sinh Can Ngày = Thăng tiến. Trực Phù sinh Can Ngày = Được sếp ủng hộ."},
        "Học Tập Tổng Quát": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Ngắn Hạn": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Dài Hạn": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Khẩn Cấp": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Quan Trọng": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Nhỏ": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Vừa": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Lớn": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Rất Lớn": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Cực Lớn": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Trong Nước": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Nước Ngoài": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Quốc Tế": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Khu Vực": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Học Tập Địa Phương": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Đinh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học vấn, tri thức. Cảnh Môn = Kỳ thi, bài thi. Đinh = Điểm số. Thiên Phụ vượng + Cảnh Môn sinh Can Ngày = Thi đỗ cao. Đinh sinh Can Ngày = Điểm số tốt."},
        "Tình Cảm Tổng Quát": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Ngắn Hạn": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Dài Hạn": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Khẩn Cấp": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Quan Trọng": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Nhỏ": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Vừa": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Lớn": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Rất Lớn": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Cực Lớn": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Trong Nước": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Nước Ngoài": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Quốc Tế": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Khu Vực": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Tình Cảm Địa Phương": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, tình yêu. Ất = Nữ, Canh = Nam. Can Ngày = Bản thân. Lục Hợp vượng + Ất Canh tương sinh = Tình yêu hạnh phúc. Lục Hợp khắc = Chia tay."},
        "Sức Khỏe Tổng Quát": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Ngắn Hạn": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Dài Hạn": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Khẩn Cấp": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Quan Trọng": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Nhỏ": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Vừa": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Lớn": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Rất Lớn": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Cực Lớn": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Trong Nước": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Nước Ngoài": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Quốc Tế": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Khu Vực": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."},
        "Sức Khỏe Địa Phương": {"Dụng_Thần": ["Thiên Nhuế", "Thiên Tâm", "Ất", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ, y thuật. Ất = Thuốc men. Thiên Tâm khắc Thiên Nhuế = Chữa khỏi bệnh. Ất sinh Can Ngày = Thuốc hợp, điều trị hiệu quả."}
    }
        "Kinh Doanh Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kinh Doanh Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kinh doanh quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đầu Tư Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đầu tư quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Bán Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua bán quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Tác Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp tác quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cạnh Tranh Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cạnh tranh quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Việc Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công việc quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thăng Chức Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thăng chức quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chuyển Việc Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chuyển việc quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghỉ Việc Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghỉ việc quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cử Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cử quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Học Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem học quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bằng Cấp Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bằng cấp quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đào Tạo Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đào tạo quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Nghiên Cứu Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem nghiên cứu quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tình Yêu Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tình yêu quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hôn Nhân Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hôn nhân quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Ly Hôn Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ly hôn quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hẹn Hò Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hẹn hò quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chia Tay Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chia tay quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bệnh Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bệnh quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khám Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem khám quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuốc Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuốc quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phẫu Thuật Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phẫu thuật quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điều Trị Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điều trị quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Kiện Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem kiện quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hợp Đồng Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hợp đồng quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tranh Chấp Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tranh chấp quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tù Tội Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tù tội quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Hòa Giải Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem hòa giải quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mua Nhà Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mua nhà quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bán Nhà Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bán nhà quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thuê Nhà Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thuê nhà quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Xây Nhà Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem xây nhà quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Sửa Nhà Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem sửa nhà quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đi Xa Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đi xa quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Du Lịch Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem du lịch quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Công Tác Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem công tác quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Định Cư Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem định cư quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Về Quê Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem về quê quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Người Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm người quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Đồ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm đồ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Trộm Cắp Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem trộm cắp quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mất Mát Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mất mát quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tìm Việc Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tìm việc quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gặp Gỡ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gặp gỡ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đàm phán nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đàm Phán Quốc Tế": {"Dụng_Thần": ["Lục Hợp", "Cửu Thiên", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Thỏa thuận, Cửu Thiên = Quốc tế. Lục Hợp vượng = Đàm phán thành công."},
        "Họp Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họp Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họp quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tiếp Khách Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tiếp khách quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Yết Kiến Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem yết kiến quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Chiến Tranh Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem chiến tranh quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phòng Thủ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phòng thủ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tấn Công Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tấn công quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Thi Đấu Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem thi đấu quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Đá Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng đá quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Bóng Rổ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem bóng rổ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tennis Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tennis quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cờ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cờ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Đua Xe Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem đua xe quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cầu Đảo Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cầu đảo quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Tế Tự Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem tế tự quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Phong Thủy Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem phong thủy quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điềm Báo Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điềm báo quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Mộng Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem mộng quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Con Cái Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem con cái quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Cha Mẹ Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem cha mẹ quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Anh Em Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem anh em quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Họ Hàng Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem họ hàng quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Gia Đình Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem gia đình quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Máy Tính Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem máy tính quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Điện Thoại Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem điện thoại quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Internet Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem internet quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "AI Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem ai quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Tổng Quát": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain tổng quát. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Ngắn Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain ngắn hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Dài Hạn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain dài hạn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Khẩn Cấp": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain khẩn cấp. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Quan Trọng": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain quan trọng. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Nhỏ": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain nhỏ. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Vừa": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain vừa. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Rất Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain rất lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Cực Lớn": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain cực lớn. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Trong Nước": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain trong nước. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Nước Ngoài": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain nước ngoài. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Blockchain Quốc Tế": {"Dụng_Thần": ["Sinh Môn", "Can Ngày", "Mậu"], "Luận_Giải_Gợi_Ý": "Xem blockchain quốc tế. Sinh Môn = Lợi, Can Ngày = Mình."},
        "Khởi Nghiệp Startup": {"Dụng_Thần": ["Khai Môn", "Sinh Môn", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Khai Môn = Khởi đầu, Sinh Môn = Tài lộc. Khai Môn vượng = Khởi nghiệp thành công."},
        "IPO Niêm Yết": {"Dụng_Thần": ["Khai Môn", "Cảnh Môn", "Mậu"], "Luận_Giải_Gợi_Ý": "Khai Môn = Công khai, Cảnh Môn = Thông tin. Khai Môn vượng = IPO thành công."},
        "M&A Sáp Nhập": {"Dụng_Thần": ["Lục Hợp", "Khai Môn", "Sinh Môn"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hợp nhất. Lục Hợp vượng = M&A thuận lợi."},
        "CEO Tổng Giám Đốc": {"Dụng_Thần": ["Trực Phù", "Khai Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Trực Phù = Quyền lực cao nhất. Trực Phù vượng = Làm CEO tốt."},
        "Khởi Nghiệp Cá Nhân": {"Dụng_Thần": ["Khai Môn", "Can Ngày", "Sinh Môn"], "Luận_Giải_Gợi_Ý": "Khai Môn = Khởi đầu. Khai Môn sinh Can Ngày = Khởi nghiệp thành."},
        "Giáo Sư Tiến Sĩ": {"Dụng_Thần": ["Thiên Phụ", "Trực Phù", "Cảnh Môn"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học thuật cao. Thiên Phụ vượng = Đạt học vị cao."},
        "Nobel Giải Thưởng": {"Dụng_Thần": ["Thiên Phụ", "Cảnh Môn", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Thiên Phụ = Học thuật đỉnh cao. Thiên Phụ cực vượng = Giải Nobel."},
        "Tình Yêu Đích Thực": {"Dụng_Thần": ["Lục Hợp", "Ất", "Canh"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, Ất Canh = Nam nữ. Tương sinh = Tình yêu đích thực."},
        "Hôn Nhân Trăm Năm": {"Dụng_Thần": ["Lục Hợp", "Hưu Môn", "Cửu Địa"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hôn nhân, Cửu Địa = Lâu dài. Lục Hợp vượng = Hôn nhân bền vững."},
        "Ung Thư Bệnh Hiểm": {"Dụng_Thần": ["Thiên Nhuế", "Tử Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Nhuế = Bệnh, Tử Môn = Nguy hiểm. Thiên Nhuế khắc Can Ngày = Bệnh nặng."},
        "Sống Thọ 100 Tuổi": {"Dụng_Thần": ["Thiên Xung", "Sinh Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Thiên Xung = Sao thọ. Thiên Xung cực vượng = Sống rất thọ."},
        "Án Tử Hình": {"Dụng_Thần": ["Tử Môn", "Bạch Hổ", "Nhâm"], "Luận_Giải_Gợi_Ý": "Tử Môn = Chết, Bạch Hổ = Hình phạt. Tử Môn cực hung = Án tử hình."},
        "Vô Tội Được Tha": {"Dụng_Thần": ["Trực Phù", "Can Ngày", "Khai Môn"], "Luận_Giải_Gợi_Ý": "Trực Phù = Quan tòa. Trực Phù sinh Can Ngày = Được tha vô tội."},
        "Biệt Thự Triệu Đô": {"Dụng_Thần": ["Sinh Môn", "Trực Phù", "Mậu"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Nhà, Mậu = Tiền. Sinh Môn cực vượng = Nhà triệu đô."},
        "Phong Thủy Đại Cát": {"Dụng_Thần": ["Sinh Môn", "Trực Phù", "Cửu Địa"], "Luận_Giải_Gợi_Ý": "Sinh Môn = Nhà, Trực Phù = Quý. Sinh Môn vượng = Phong thủy đại cát."},
        "Du Lịch Vòng Quanh Thế Giới": {"Dụng_Thần": ["Cửu Thiên", "Mã Tinh", "Hưu Môn"], "Luận_Giải_Gợi_Ý": "Cửu Thiên = Rất xa, Mã Tinh = Di chuyển. Mã Tinh vượng = Du lịch vòng quanh thế giới."},
        "Định Cư Mỹ Canada": {"Dụng_Thần": ["Cửu Thiên", "Khai Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Cửu Thiên = Nước ngoài xa. Cửu Thiên vượng = Định cư thành công."},
        "Tìm Người Mất Tích": {"Dụng_Thần": ["Lục Hợp", "Can Giờ", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Can Giờ = Người mất tích. Can Giờ sinh Can Ngày = Tìm được người."},
        "Tìm Kho Báu": {"Dụng_Thần": ["Mậu", "Huyền Vũ", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Mậu = Kho báu, Huyền Vũ = Ẩn giấu. Can Ngày khắc Huyền Vũ = Tìm được kho báu."},
        "Gặp Tổng Thống": {"Dụng_Thần": ["Trực Phù", "Can Năm", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Trực Phù = Quý nhân cao nhất. Trực Phù sinh Can Ngày = Gặp được tổng thống."},
        "Chiến Tranh Thế Giới": {"Dụng_Thần": ["Bạch Hổ", "Thương Môn", "Cửu Thiên"], "Luận_Giải_Gợi_Ý": "Bạch Hổ = Chiến tranh, Cửu Thiên = Toàn cầu. Bạch Hổ cực vượng = Chiến tranh lớn."},
        "Hòa Bình Thế Giới": {"Dụng_Thần": ["Lục Hợp", "Trực Phù", "Cửu Thiên"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Hòa bình. Lục Hợp vượng = Hòa bình thế giới."},
        "World Cup Bóng Đá": {"Dụng_Thần": ["Can Ngày", "Can Giờ", "Cảnh Môn"], "Luận_Giải_Gợi_Ý": "Can Ngày = Đội nhà, Can Giờ = Đối thủ. Can Ngày vượng = Vô địch World Cup."},
        "Olympic Huy Chương Vàng": {"Dụng_Thần": ["Cảnh Môn", "Can Ngày", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Cảnh Môn = Giải thưởng. Cảnh Môn sinh Can Ngày = Huy chương vàng Olympic."},
        "Thành Phật Đắc Đạo": {"Dụng_Thần": ["Trực Phù", "Cửu Thiên", "Thiên Phụ"], "Luận_Giải_Gợi_Ý": "Trực Phù = Thần thánh. Trực Phù cực vượng = Thành Phật đắc đạo."},
        "Gặp Thần Tiên": {"Dụng_Thần": ["Trực Phù", "Cửu Thiên", "Đằng Xà"], "Luận_Giải_Gợi_Ý": "Trực Phù = Thần, Cửu Thiên = Thiên giới. Trực Phù vượng = Gặp thần tiên."},
        "Sinh Con Rồng": {"Dụng_Thần": ["Can Giờ", "Thiên Nhuế", "Trực Phù"], "Luận_Giải_Gợi_Ý": "Can Giờ = Con, Trực Phù = Quý. Can Giờ cực vượng = Sinh con rồng."},
        "Gia Đình Hạnh Phúc": {"Dụng_Thần": ["Lục Hợp", "Hưu Môn", "Can Ngày"], "Luận_Giải_Gợi_Ý": "Lục Hợp = Gia đình, Hưu Môn = Hạnh phúc. Lục Hợp vượng = Gia đình hạnh phúc."},
        "AI Trí Tuệ Nhân Tạo": {"Dụng_Thần": ["Thiên Tâm", "Thiên Phụ", "Cửu Thiên"], "Luận_Giải_Gợi_Ý": "Thiên Tâm = Trí tuệ, Thiên Phụ = Công nghệ. Thiên Tâm vượng = AI phát triển."},
        "Blockchain Crypto": {"Dụng_Thần": ["Thiên Bồng", "Mậu", "Cửu Thiên"], "Luận_Giải_Gợi_Ý": "Thiên Bồng = Rủi ro, Mậu = Tiền. Mậu vượng = Crypto tăng giá."}
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
        if s in truc_phu_star: # Sử dụng 'in' để khớp "Thiên Nhuế/Cầm"
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
                 # Thiên Cầm đi cùng Thiên Nhuế (2)
                 pass
            else:
                thien_ban[cung_moi] = sao
                can_thien_ban[cung_moi] = can_goc
                
                # Nếu cung này là nơi Thiên Nhuế đến, gán thêm Thiên Cầm
                if sao == "Thiên Nhuế":
                    # Tìm can của Thiên Cầm (từ cung gốc 5)
                    can_cam = dia_ban.get(5, "Mậu")
                    # Gán Thiên Cầm vào cùng cung
                    # Trong hiển thị, ta có thể dùng dấu / hoặc newline, 
                    # nhưng cấu trúc hiện tại là 1 string.
                    thien_ban[cung_moi] = "Thiên Nhuế/Cầm"
                    # Can thiên cũng có thể kép hoặc lấy của Nhuế? 
                    # Thường Cầm và Nhuế dùng chung Can Thiên của cung đích.
                
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

# NEW: Trộn dữ liệu từ Excel vào KY_MON_DATA
KY_MON_DATA = merge_excel_data(KY_MON_DATA)

# NEW: Trộn dữ liệu nâng cao (PDF Knowledge)
KY_MON_DATA["ADVANCED_KNOWLEDGE"] = load_advanced_knowledge()

TOPIC_INTERPRETATIONS = KY_MON_DATA.get("TOPIC_INTERPRETATIONS", {})
