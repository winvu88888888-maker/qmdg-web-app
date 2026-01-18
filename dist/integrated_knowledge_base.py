# -*- coding: utf-8 -*-
"""
MODULE TỔNG HỢP TRI THỨC - TÍCH HỢP TẤT CẢ DỮ LIỆU
Kết hợp dữ liệu từ Excel, JSON và các module hiện có
"""

import json
import os

# Load dữ liệu từ các file JSON
def load_json_data(filename):
    """Load dữ liệu từ file JSON"""
    try:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Không thể load {filename}: {e}")
        return {}

# Load tất cả dữ liệu
EXCEL_DATA = load_json_data('qmdg_excel_full.json')
ADVANCED_DATA = load_json_data('qmdg_advanced_knowledge.json')

# Mapping Cung -> Quẻ
CUNG_TO_QUA = {
    1: "CÀN",    # Càn Cung
    2: "KHÔN",   # Khôn Cung
    3: "CHẤN",   # Chấn Cung
    4: "TỐN",    # Tốn Cung
    6: "CÀN",    # Càn Cung (trung tâm thường dùng Càn)
    7: "ĐOÀI",   # Đoài Cung
    8: "CẤN",    # Cấn Cung
    9: "LY"      # Ly Cung
}

def get_qua_info(cung_so):
    """
    Lấy thông tin chi tiết về Quẻ tương ứng với Cung
    
    Args:
        cung_so: Số cung (1-9)
    
    Returns:
        Dict chứa thông tin đầy đủ về Quẻ
    """
    qua_name = CUNG_TO_QUA.get(cung_so, "CÀN")
    qua_data = EXCEL_DATA.get("GUA_ATTRIBUTES", {}).get(qua_name, {})
    
    return {
        "ten": qua_name,
        "khai_niem": qua_data.get("KHÁI NIỆM", ""),
        "tinh_tinh": qua_data.get("TÍNH TÌNH", ""),
        "hinh_thai": qua_data.get("HÌNH THÁI", ""),
        "thien_thoi": qua_data.get("THIÊN THỜI", ""),
        "dia_ly": qua_data.get("ĐỊA LÝ", ""),
        "nhan_vat": qua_data.get("NHÂN VẬT", ""),
        "dong_vat": qua_data.get("ĐỘNG VẬT", ""),
        "thuc_vat": qua_data.get("THỰC VẬT", ""),
        "do_an": qua_data.get("ĐỒ ĂN", ""),
        "tinh_vat": qua_data.get("TĨNH VẬT", ""),
        "nhan_the": qua_data.get("NHÂN THỂ", ""),
        "tat_benh": qua_data.get("TẬT BỆNH", ""),
        "thoi_gian": qua_data.get("THỜI GIAN", ""),
        "sac_thai": qua_data.get("SĂC THÁI", ""),
        "xep_hang": qua_data.get("XẾP HẠNG", "")
    }

def get_can_info(can_name):
    """
    Lấy thông tin chi tiết về Can
    
    Args:
        can_name: Tên Can (Giáp, Ất, Bính, v.v.)
    
    Returns:
        Dict chứa thông tin đầy đủ về Can
    """
    can_data = EXCEL_DATA.get("GUA_ATTRIBUTES", {}).get(can_name.upper(), {})
    
    # Nếu không có trong Excel, lấy từ Advanced Data
    if not can_data:
        profiling = ADVANCED_DATA.get("STEM_PROFILING", {}).get(can_name, "")
        return {
            "ten": can_name,
            "profiling": profiling,
            "khai_niem": "",
            "tinh_tinh": "",
            "hinh_thai": ""
        }
    
    return {
        "ten": can_name,
        "khai_niem": can_data.get("KHÁI NIỆM", ""),
        "tinh_tinh": can_data.get("TÍNH TÌNH", ""),
        "hinh_thai": can_data.get("HÌNH THÁI", ""),
        "thien_thoi": can_data.get("THIÊN THỜI", ""),
        "dia_ly": can_data.get("ĐỊA LÝ", ""),
        "nhan_vat": can_data.get("NHÂN VẬT", ""),
        "dong_vat": can_data.get("ĐỘNG VẬT", ""),
        "thuc_vat": can_data.get("THỰC VẬT", ""),
        "do_an": can_data.get("ĐỒ ĂN", ""),
        "tinh_vat": can_data.get("TĨNH VẬT", ""),
        "nhan_the": can_data.get("NHÂN THỂ", ""),
        "tat_benh": can_data.get("TẬT BỆNH", ""),
        "thoi_gian": can_data.get("THỜI GIAN", ""),
        "sac_thai": can_data.get("SĂC THÁI", "")
    }

def get_chi_info(chi_name):
    """
    Lấy thông tin chi tiết về Chi
    
    Args:
        chi_name: Tên Chi (Tí, Sửu, Dần, v.v.)
    
    Returns:
        Dict chứa thông tin đầy đủ về Chi
    """
    chi_data = EXCEL_DATA.get("GUA_ATTRIBUTES", {}).get(chi_name.upper(), {})
    
    return {
        "ten": chi_name,
        "khai_niem": chi_data.get("KHÁI NIỆM", ""),
        "tinh_tinh": chi_data.get("TÍNH TÌNH", ""),
        "hinh_thai": chi_data.get("HÌNH THÁI", ""),
        "thien_thoi": chi_data.get("THIÊN THỜI", ""),
        "dia_ly": chi_data.get("ĐỊA LÝ", ""),
        "nhan_vat": chi_data.get("NHÂN VẬT", ""),
        "dong_vat": chi_data.get("ĐỘNG VẬT", ""),
        "thuc_vat": chi_data.get("THỰC VẬT", ""),
        "do_an": chi_data.get("ĐỒ ĂN", ""),
        "tinh_vat": chi_data.get("TĨNH VẬT", ""),
        "nhan_the": chi_data.get("NHÂN THỂ", ""),
        "tat_benh": chi_data.get("TẬT BỆNH", ""),
        "thoi_gian": chi_data.get("THỜI GIAN", ""),
        "sac_thai": chi_data.get("SĂC THÁI", "")
    }

def get_sao_info(sao_name):
    """
    Lấy thông tin chi tiết về Sao (Cửu Tinh)
    
    Args:
        sao_name: Tên Sao (Thiên Bồng, Thiên Nhậm, v.v.)
    
    Returns:
        Dict chứa thông tin đầy đủ về Sao
    """
    # Chuẩn hóa tên (bỏ "Thiên" nếu có)
    sao_key = sao_name.replace("Thiên ", "THIÊN ")
    
    sao_data = EXCEL_DATA.get("GUA_ATTRIBUTES", {}).get(sao_key, {})
    
    # Nếu không có, thử tìm trong Advanced Data
    if not sao_data:
        advanced_sao = ADVANCED_DATA.get("STARS_ICONIC", {}).get(sao_name, {})
        if advanced_sao:
            return {
                "ten": sao_name,
                "hanh": advanced_sao.get("Hành", ""),
                "tinh_chat": advanced_sao.get("Tính_Chất", ""),
                "nhan_vat": advanced_sao.get("Nhân_Vật", ""),
                "than_the": advanced_sao.get("Thân_Thể", ""),
                "dia_ly": advanced_sao.get("Địa_Lý", ""),
                "dong_vat": advanced_sao.get("Động_Vật", ""),
                "am_ban_tuong": advanced_sao.get("Âm_Bàn_Tượng", "")
            }
    
    return {
        "ten": sao_name,
        "khai_niem": sao_data.get("KHÁI NIỆM", ""),
        "tinh_tinh": sao_data.get("TÍNH TÌNH", ""),
        "hinh_thai": sao_data.get("HÌNH THÁI", ""),
        "thien_thoi": sao_data.get("THIÊN THỜI", ""),
        "dia_ly": sao_data.get("ĐỊA LÝ", ""),
        "nhan_vat": sao_data.get("NHÂN VẬT", ""),
        "dong_vat": sao_data.get("ĐỘNG VẬT", ""),
        "thuc_vat": sao_data.get("THỰC VẬT", ""),
        "do_an": sao_data.get("ĐỒ ĂN", ""),
        "tinh_vat": sao_data.get("TĨNH VẬT", ""),
        "nhan_the": sao_data.get("NHÂN THỂ", ""),
        "tat_benh": sao_data.get("TẬT BỆNH", ""),
        "thoi_gian": sao_data.get("THỜI GIAN", ""),
        "sac_thai": sao_data.get("SĂC THÁI", "")
    }

def get_mon_info(mon_name):
    """
    Lấy thông tin chi tiết về Môn (Bát Môn)
    
    Args:
        mon_name: Tên Môn (Hưu, Sinh, Thương, v.v.)
    
    Returns:
        Dict chứa thông tin đầy đủ về Môn
    """
    # Chuẩn hóa tên
    mon_key = mon_name.upper() + " MÔN"
    
    mon_data = EXCEL_DATA.get("GUA_ATTRIBUTES", {}).get(mon_key, {})
    
    # Nếu không có, thử tìm trong Advanced Data
    if not mon_data:
        advanced_mon = ADVANCED_DATA.get("DOORS_ICONIC", {}).get(mon_name + " Môn", {})
        if advanced_mon:
            return {
                "ten": mon_name,
                "tinh_chat": advanced_mon.get("Tính_Chất", ""),
                "am_ban_tuong": advanced_mon.get("Âm_Bàn_Tượng", "")
            }
    
    return {
        "ten": mon_name,
        "khai_niem": mon_data.get("KHÁI NIỆM", ""),
        "tinh_tinh": mon_data.get("TÍNH TÌNH", ""),
        "hinh_thai": mon_data.get("HÌNH THÁI", ""),
        "thien_thoi": mon_data.get("THIÊN THỜI", ""),
        "dia_ly": mon_data.get("ĐỊA LÝ", ""),
        "nhan_vat": mon_data.get("NHÂN VẬT", ""),
        "dong_vat": mon_data.get("ĐỘNG VẬT", ""),
        "thuc_vat": mon_data.get("THỰC VẬT", ""),
        "do_an": mon_data.get("ĐỒ ĂN", ""),
        "tinh_vat": mon_data.get("TĨNH VẬT", ""),
        "nhan_the": mon_data.get("NHÂN THỂ", ""),
        "tat_benh": mon_data.get("TẬT BỆNH", ""),
        "thoi_gian": mon_data.get("THỜI GIAN", ""),
        "sac_thai": mon_data.get("SĂC THÁI", "")
    }

def get_comprehensive_palace_info(palace_dict):
    """
    Lấy thông tin tổng hợp đầy đủ cho một Cung
    
    Args:
        palace_dict: Dict chứa thông tin cung (so, sao, cua, than, can_thien, can_dia, hanh)
    
    Returns:
        Dict chứa thông tin tổng hợp từ tất cả các nguồn
    """
    result = {
        "qua": get_qua_info(palace_dict['so']),
        "sao": get_sao_info(palace_dict['sao']),
        "mon": get_mon_info(palace_dict['cua']),
        "can_thien": get_can_info(palace_dict['can_thien']),
        "can_dia": get_can_info(palace_dict['can_dia'])
    }
    
    return result

def format_info_for_display(info_dict, category):
    """
    Format thông tin để hiển thị đẹp
    
    Args:
        info_dict: Dict chứa thông tin
        category: Loại thông tin (qua, sao, mon, can)
    
    Returns:
        String formatted để hiển thị
    """
    lines = []
    
    if category == "qua":
        if info_dict.get("khai_niem"):
            lines.append(f"  📖 Khái niệm: {info_dict['khai_niem'][:200]}...")
        if info_dict.get("tinh_tinh"):
            lines.append(f"  👤 Tính tình: {info_dict['tinh_tinh']}")
        if info_dict.get("nhan_vat"):
            lines.append(f"  🧑 Nhân vật: {info_dict['nhan_vat'][:150]}...")
        if info_dict.get("dia_ly"):
            lines.append(f"  🗺️ Địa lý: {info_dict['dia_ly'][:150]}...")
    
    elif category == "sao":
        if info_dict.get("khai_niem"):
            lines.append(f"  ⭐ Khái niệm: {info_dict['khai_niem'][:200]}...")
        if info_dict.get("tinh_tinh"):
            lines.append(f"  💫 Tính tình: {info_dict['tinh_tinh']}")
        if info_dict.get("nhan_vat"):
            lines.append(f"  👥 Nhân vật: {info_dict['nhan_vat'][:150]}...")
    
    elif category == "mon":
        if info_dict.get("khai_niem"):
            lines.append(f"  🚪 Khái niệm: {info_dict['khai_niem'][:200]}...")
        if info_dict.get("dia_ly"):
            lines.append(f"  📍 Địa lý: {info_dict['dia_ly'][:150]}...")
    
    elif category == "can":
        if info_dict.get("khai_niem"):
            lines.append(f"  📜 Khái niệm: {info_dict['khai_niem'][:200]}...")
        if info_dict.get("profiling"):
            lines.append(f"  🔍 Profiling: {info_dict['profiling']}")
    
    return "\n".join(lines) if lines else "  (Chưa có dữ liệu chi tiết)"

# Test function
if __name__ == "__main__":
    print("=== TEST INTEGRATED KNOWLEDGE BASE ===\n")
    
    # Test Quẻ
    print("1. Test Quẻ (Cung 1 - Càn):")
    qua_info = get_qua_info(1)
    print(f"Tên: {qua_info['ten']}")
    print(f"Khái niệm: {qua_info['khai_niem'][:100]}...")
    print()
    
    # Test Sao
    print("2. Test Sao (Thiên Bồng):")
    sao_info = get_sao_info("Thiên Bồng")
    print(f"Tên: {sao_info['ten']}")
    print(f"Khái niệm: {sao_info['khai_niem'][:100]}...")
    print()
    
    # Test Môn
    print("3. Test Môn (Hưu):")
    mon_info = get_mon_info("Hưu")
    print(f"Tên: {mon_info['ten']}")
    print(f"Khái niệm: {mon_info['khai_niem'][:100]}...")
    print()
    
    # Test Can
    print("4. Test Can (Mậu):")
    can_info = get_can_info("Mậu")
    print(f"Tên: {can_info['ten']}")
    print(f"Khái niệm: {can_info['khai_niem'][:100]}...")
    print()
    
    print("\n✅ Tất cả tests hoàn thành!")
