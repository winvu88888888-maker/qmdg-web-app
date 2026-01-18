# -*- coding: utf-8 -*-
"""
HỆ THỐNG PHÂN TÍCH CHI TIẾT CUNG - KỲ MÔN ĐỘN GIÁP
Phân tích từng yếu tố: Sao, Môn, Thần, Can, và mối quan hệ sinh khắc
"""

from qmdg_data import *

def phan_tich_chi_tiet_cung(cung_info):
    """
    Phân tích CỰC KỲ CHI TIẾT một cung
    
    Args:
        cung_info: dict chứa thông tin cung {so, ten, hanh, sao, cua, than, can_thien, can_dia}
    
    Returns:
        str: Phân tích chi tiết đầy đủ
    """
    phan_tich = ""
    
    # === 1. THÔNG TIN CƠ BẢN ===
    phan_tich += f"╔══════════════════════════════════════════════════════════════╗\n"
    phan_tich += f"║  CUNG {cung_info['so']} - {cung_info['ten']} ({cung_info['hanh']})  \n"
    phan_tich += f"╚══════════════════════════════════════════════════════════════╝\n\n"
    
    # === 2. PHÂN TÍCH SAO (CỬU TINH) ===
    sao = cung_info['sao']
    sao_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["CUU_TINH"].get(sao, {})
    sao_hanh = sao_data.get("Hành", "N/A")
    sao_tinh_chat = sao_data.get("Tính_Chất", "N/A")
    
    phan_tich += f"🌟 SAO (CỬU TINH): {sao}\n"
    phan_tich += f"   ├─ Ngũ Hành Sao: {sao_hanh}\n"
    phan_tich += f"   ├─ Tính Chất: {sao_tinh_chat}\n"
    
    # Phân tích sinh khắc Sao với Cung
    mqh_sao_cung = tinh_ngu_hanh_sinh_khac(sao_hanh, cung_info['hanh'])
    phan_tich += f"   └─ Sao vs Cung: {mqh_sao_cung}\n"
    
    if "Sinh" in mqh_sao_cung and sao_hanh in mqh_sao_cung.split()[0]:
        phan_tich += f"      → Sao sinh Cung = Tiêu hao năng lượng, sao yếu đi\n"
    elif "Sinh" in mqh_sao_cung:
        phan_tich += f"      → Cung sinh Sao = Sao được tăng cường, rất mạnh\n"
    elif "Khắc" in mqh_sao_cung and sao_hanh in mqh_sao_cung.split()[0]:
        phan_tich += f"      → Sao khắc Cung = Sao mạnh, cung yếu, bất lợi\n"
    elif "Khắc" in mqh_sao_cung:
        phan_tich += f"      → Cung khắc Sao = Sao bị áp chế, không phát huy\n"
    
    phan_tich += "\n"
    
    # === 3. PHÂN TÍCH MÔN (BÁT MÔN) ===
    cua = cung_info['cua']
    cua_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_MON"].get(cua + " Môn", {})
    cat_hung = cua_data.get("Cát_Hung", "Bình")
    luan_doan = cua_data.get("Luận_Đoán", "N/A")
    
    phan_tich += f"🚪 MÔN (BÁT MÔN): {cua} Môn\n"
    phan_tich += f"   ├─ Cát/Hung: {cat_hung}\n"
    phan_tich += f"   ├─ Luận Đoán: {luan_doan}\n"
    
    # Môn cố định
    mon_co_dinh = BAT_MON_CO_DINH_CUNG.get(cung_info['so'], "N/A")
    if mon_co_dinh != "N/A":
        phan_tich += f"   ├─ Môn Cố Định: {mon_co_dinh} Môn\n"
        if cua == mon_co_dinh:
            phan_tich += f"   │  → Môn Phục Vịnh (Môn chạy = Môn cố định) - Trì trệ\n"
    
    # Phân tích kết hợp Môn với Sao
    phan_tich += f"   └─ Kết Hợp Môn + Sao:\n"
    if cat_hung in ["Đại Cát", "Cát"] and sao in ["Thiên Anh", "Thiên Phụ", "Thiên Tâm"]:
        phan_tich += f"      → Cát Môn + Cát Sao = ĐẠI CÁT, rất thuận lợi\n"
    elif cat_hung in ["Hung", "Đại Hung"] and sao in ["Thiên Bồng", "Thiên Trụ"]:
        phan_tich += f"      → Hung Môn + Hung Sao = ĐẠI HUNG, rất bất lợi\n"
    elif cat_hung in ["Đại Cát", "Cát"] and sao in ["Thiên Bồng", "Thiên Trụ"]:
        phan_tich += f"      → Cát Môn nhưng Hung Sao = Bình, có trở ngại\n"
    elif cat_hung in ["Hung", "Đại Hung"] and sao in ["Thiên Anh", "Thiên Phụ"]:
        phan_tich += f"      → Hung Môn nhưng Cát Sao = Bình, có cơ hội\n"
    else:
        phan_tich += f"      → Kết hợp trung bình, cần xem thêm yếu tố khác\n"
    
    phan_tich += "\n"
    
    # === 4. PHÂN TÍCH THẦN (BÁT THẦN) ===
    than = cung_info['than']
    than_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_THAN"].get(than, {})
    than_tinh_chat = than_data.get("Tính_Chất", "N/A")
    
    phan_tich += f"👤 THẦN (BÁT THẦN): {than}\n"
    phan_tich += f"   ├─ Tính Chất: {than_tinh_chat}\n"
    
    # Đánh giá Thần
    if than in ["Trực Phù", "Lục Hợp", "Thái Âm", "Cửu Thiên"]:
        phan_tich += f"   └─ Đánh Giá: Cát Thần - Hỗ trợ tốt\n"
    elif than in ["Bạch Hổ", "Huyền Vũ", "Đằng Xà"]:
        phan_tich += f"   └─ Đánh Giá: Hung Thần - Gây trở ngại\n"
    else:
        phan_tich += f"   └─ Đánh Giá: Trung bình\n"
    
    phan_tich += "\n"
    
    # === 5. PHÂN TÍCH CAN THIÊN ===
    can_thien = cung_info['can_thien']
    can_thien_data = KY_MON_DATA["CAN_CHI_LUAN_GIAI"].get(can_thien, {})
    can_thien_hanh = can_thien_data.get("Hành", "N/A")
    can_thien_tinh_chat = can_thien_data.get("Tính_Chất", "N/A")
    
    phan_tich += f"☰ CAN THIÊN: {can_thien}\n"
    phan_tich += f"   ├─ Ngũ Hành: {can_thien_hanh}\n"
    phan_tich += f"   ├─ Tính Chất: {can_thien_tinh_chat}\n"
    
    # Sinh khắc Can Thiên với Cung
    mqh_can_thien_cung = tinh_ngu_hanh_sinh_khac(can_thien_hanh, cung_info['hanh'])
    phan_tich += f"   └─ Can Thiên vs Cung: {mqh_can_thien_cung}\n"
    
    phan_tich += "\n"
    
    # === 6. PHÂN TÍCH CAN ĐỊA ===
    can_dia = cung_info['can_dia']
    can_dia_data = KY_MON_DATA["CAN_CHI_LUAN_GIAI"].get(can_dia, {})
    can_dia_hanh = can_dia_data.get("Hành", "N/A")
    can_dia_tinh_chat = can_dia_data.get("Tính_Chất", "N/A")
    
    phan_tich += f"☷ CAN ĐỊA: {can_dia}\n"
    phan_tich += f"   ├─ Ngũ Hành: {can_dia_hanh}\n"
    phan_tich += f"   ├─ Tính Chất: {can_dia_tinh_chat}\n"
    
    # Sinh khắc Can Địa với Cung
    mqh_can_dia_cung = tinh_ngu_hanh_sinh_khac(can_dia_hanh, cung_info['hanh'])
    phan_tich += f"   └─ Can Địa vs Cung: {mqh_can_dia_cung}\n"
    
    phan_tich += "\n"
    
    # === 7. PHÂN TÍCH SINH KHẮC TỔNG HỢP ===
    phan_tich += "═══════════════════════════════════════════════════════════════\n"
    phan_tich += "🔄 SINH KHẮC TỔNG HỢP TRONG CUNG:\n\n"
    
    # Can Thiên vs Can Địa
    mqh_can = tinh_ngu_hanh_sinh_khac(can_thien_hanh, can_dia_hanh)
    phan_tich += f"   • Can Thiên vs Can Địa: {mqh_can}\n"
    if "Khắc" in mqh_can:
        phan_tich += f"     → Cách Cục Tranh (Thiên Địa Tranh) - Có mâu thuẫn nội tại\n"
    
    # Sao vs Can Thiên
    mqh_sao_can_thien = tinh_ngu_hanh_sinh_khac(sao_hanh, can_thien_hanh)
    phan_tich += f"   • Sao vs Can Thiên: {mqh_sao_can_thien}\n"
    
    # Sao vs Can Địa
    mqh_sao_can_dia = tinh_ngu_hanh_sinh_khac(sao_hanh, can_dia_hanh)
    phan_tich += f"   • Sao vs Can Địa: {mqh_sao_can_dia}\n"
    
    phan_tich += "\n"
    
    # === 8. KẾT LUẬN TỔNG QUAN CUNG ===
    phan_tich += "═══════════════════════════════════════════════════════════════\n"
    phan_tich += "📌 KẾT LUẬN TỔNG QUAN:\n\n"
    
    # Tính điểm tổng hợp
    diem = 50  # Điểm cơ bản
    
    # Điểm từ Môn
    if cat_hung == "Đại Cát":
        diem += 20
        phan_tich += f"   ✅ Môn {cua} Đại Cát (+20 điểm)\n"
    elif cat_hung == "Cát":
        diem += 10
        phan_tich += f"   ✅ Môn {cua} Cát (+10 điểm)\n"
    elif cat_hung == "Hung":
        diem -= 10
        phan_tich += f"   ❌ Môn {cua} Hung (-10 điểm)\n"
    elif cat_hung == "Đại Hung":
        diem -= 20
        phan_tich += f"   ❌ Môn {cua} Đại Hung (-20 điểm)\n"
    
    # Điểm từ Thần
    if than in ["Trực Phù", "Lục Hợp"]:
        diem += 15
        phan_tich += f"   ✅ Thần {than} rất tốt (+15 điểm)\n"
    elif than in ["Bạch Hổ", "Huyền Vũ"]:
        diem -= 15
        phan_tich += f"   ❌ Thần {than} rất xấu (-15 điểm)\n"
    
    # Điểm từ sinh khắc
    if "Sinh" in mqh_sao_cung and cung_info['hanh'] in mqh_sao_cung.split()[0]:
        diem += 10
        phan_tich += f"   ✅ Cung sinh Sao - Sao mạnh (+10 điểm)\n"
    elif "Khắc" in mqh_sao_cung and sao_hanh in mqh_sao_cung.split()[0]:
        diem -= 10
        phan_tich += f"   ❌ Sao khắc Cung - Bất hòa (-10 điểm)\n"
    
    diem = max(0, min(100, diem))
    phan_tich += f"\n   🎯 TỔNG ĐIỂM CUNG: {diem}/100\n"
    
    if diem >= 80:
        phan_tich += f"   → Đánh giá: CỰC KỲ THUẬN LỢI ⭐⭐⭐⭐⭐\n"
    elif diem >= 60:
        phan_tich += f"   → Đánh giá: THUẬN LỢI ⭐⭐⭐⭐\n"
    elif diem >= 40:
        phan_tich += f"   → Đánh giá: TRUNG BÌNH ⭐⭐⭐\n"
    elif diem >= 20:
        phan_tich += f"   → Đánh giá: BẤT LỢI ⭐⭐\n"
    else:
        phan_tich += f"   → Đánh giá: CỰC KỲ BẤT LỢI ⭐\n"
    
    phan_tich += "\n"
    
    return phan_tich, diem


def so_sanh_chi_tiet_chu_khach(chu_info, khach_info):
    """
    So sánh CỰC KỲ CHI TIẾT giữa Chủ và Khách
    
    Returns:
        str: Phân tích so sánh đầy đủ
    """
    so_sanh = ""
    
    so_sanh += "╔══════════════════════════════════════════════════════════════╗\n"
    so_sanh += "║          SO SÁNH CHI TIẾT CHỦ - KHÁCH                       ║\n"
    so_sanh += "╚══════════════════════════════════════════════════════════════╝\n\n"
    
    # Phân tích từng cung
    so_sanh += "【 PHÂN TÍCH CUNG CHỦ 】\n"
    phan_tich_chu, diem_chu = phan_tich_chi_tiet_cung(chu_info)
    so_sanh += phan_tich_chu
    
    so_sanh += "\n" + "="*65 + "\n\n"
    
    so_sanh += "【 PHÂN TÍCH CUNG KHÁCH 】\n"
    phan_tich_khach, diem_khach = phan_tich_chi_tiet_cung(khach_info)
    so_sanh += phan_tich_khach
    
    so_sanh += "\n" + "="*65 + "\n\n"
    
    # So sánh trực tiếp
    so_sanh += "【 SO SÁNH TRỰC TIẾP 】\n\n"
    
    # 1. So sánh Ngũ Hành Cung
    mqh_cung = tinh_ngu_hanh_sinh_khac(chu_info['hanh'], khach_info['hanh'])
    so_sanh += f"🔸 Ngũ Hành Cung:\n"
    so_sanh += f"   Chủ ({chu_info['hanh']}) vs Khách ({khach_info['hanh']})\n"
    so_sanh += f"   → {mqh_cung}\n\n"
    
    # 2. So sánh Sao
    chu_sao_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["CUU_TINH"].get(chu_info['sao'], {})
    khach_sao_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["CUU_TINH"].get(khach_info['sao'], {})
    
    mqh_sao = tinh_ngu_hanh_sinh_khac(chu_sao_data.get("Hành", "N/A"), 
                                       khach_sao_data.get("Hành", "N/A"))
    so_sanh += f"🔸 Sao (Cửu Tinh):\n"
    so_sanh += f"   Chủ: {chu_info['sao']} ({chu_sao_data.get('Hành', 'N/A')})\n"
    so_sanh += f"   Khách: {khach_info['sao']} ({khach_sao_data.get('Hành', 'N/A')})\n"
    so_sanh += f"   → {mqh_sao}\n\n"
    
    # 3. So sánh Môn
    chu_cua_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_MON"].get(chu_info['cua'] + " Môn", {})
    khach_cua_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_MON"].get(khach_info['cua'] + " Môn", {})
    
    so_sanh += f"🔸 Môn (Bát Môn):\n"
    so_sanh += f"   Chủ: {chu_info['cua']} ({chu_cua_data.get('Cát_Hung', 'N/A')})\n"
    so_sanh += f"   Khách: {khach_info['cua']} ({khach_cua_data.get('Cát_Hung', 'N/A')})\n"
    
    if chu_cua_data.get('Cát_Hung') == "Đại Cát" and khach_cua_data.get('Cát_Hung') in ["Hung", "Đại Hung"]:
        so_sanh += f"   → Chủ có lợi thế lớn về Môn\n\n"
    elif khach_cua_data.get('Cát_Hung') == "Đại Cát" and chu_cua_data.get('Cát_Hung') in ["Hung", "Đại Hung"]:
        so_sanh += f"   → Khách có lợi thế lớn về Môn\n\n"
    else:
        so_sanh += f"   → Ngang nhau hoặc chênh lệch nhỏ\n\n"
    
    # 4. So sánh Thần
    so_sanh += f"🔸 Thần (Bát Thần):\n"
    so_sanh += f"   Chủ: {chu_info['than']}\n"
    so_sanh += f"   Khách: {khach_info['than']}\n"
    
    chu_than_tot = chu_info['than'] in ["Trực Phù", "Lục Hợp", "Thái Âm", "Cửu Thiên"]
    khach_than_tot = khach_info['than'] in ["Trực Phù", "Lục Hợp", "Thái Âm", "Cửu Thiên"]
    
    if chu_than_tot and not khach_than_tot:
        so_sanh += f"   → Chủ có Thần tốt hơn\n\n"
    elif khach_than_tot and not chu_than_tot:
        so_sanh += f"   → Khách có Thần tốt hơn\n\n"
    else:
        so_sanh += f"   → Ngang nhau\n\n"
    
    # 5. Kết luận cuối cùng
    so_sanh += "="*65 + "\n"
    so_sanh += "🏆 KẾT LUẬN CUỐI CÙNG:\n\n"
    so_sanh += f"   Điểm Chủ: {diem_chu}/100\n"
    so_sanh += f"   Điểm Khách: {diem_khach}/100\n"
    so_sanh += f"   Chênh lệch: {abs(diem_chu - diem_khach)} điểm\n\n"
    
    if diem_chu > diem_khach + 20:
        so_sanh += f"   ✅ CHỦ CHIẾM ƯU THẾ TUYỆT ĐỐI\n"
    elif diem_chu > diem_khach + 10:
        so_sanh += f"   ✅ CHỦ CÓ LỢI THẾ RÕ RÀNG\n"
    elif diem_chu > diem_khach:
        so_sanh += f"   ✅ CHỦ HƠI CÓ LỢI THẾ\n"
    elif diem_khach > diem_chu + 20:
        so_sanh += f"   ❌ KHÁCH CHIẾM ƯU THẾ TUYỆT ĐỐI\n"
    elif diem_khach > diem_chu + 10:
        so_sanh += f"   ❌ KHÁCH CÓ LỢI THẾ RÕ RÀNG\n"
    elif diem_khach > diem_chu:
        so_sanh += f"   ❌ KHÁCH HƠI CÓ LỢI THẾ\n"
    else:
        so_sanh += f"   ⚖️ NGANG SỨC - CÂN BẰNG\n"
    
    return so_sanh, diem_chu, diem_khach
