# -*- coding: utf-8 -*-
"""
VẼ QUẺ BẰNG GẠCH ÂM DƯƠNG - PHIÊN BẢN NÂNG CẤP
Hiển thị quẻ với gạch âm dương TO, RÕ NÉT và thông tin chi tiết từng hào
"""

def xac_dinh_hao_am_duong(thuong_quai, ha_quai):
    """
    Xác định 6 hào âm/dương từ Thượng Quái và Hạ Quái
    
    Args:
        thuong_quai: số quẻ trên (0-7)
        ha_quai: số quẻ dưới (0-7)
    
    Returns:
        list: [hào 1, hào 2, hào 3, hào 4, hào 5, hào 6]
              1 = Dương (━━━), 0 = Âm (━ ━)
    """
    # Bảng chuyển đổi số quẻ sang 3 hào
    qua_to_hao = {
        0: [0, 0, 0],  # Khôn
        1: [0, 0, 1],  # Chấn
        2: [0, 1, 0],  # Khảm
        3: [0, 1, 1],  # Đoài
        4: [1, 0, 0],  # Cấn
        5: [1, 0, 1],  # Ly
        6: [1, 1, 0],  # Tốn
        7: [1, 1, 1]   # Càn
    }
    
    # Hạ Quái (hào 1, 2, 3) + Thượng Quái (hào 4, 5, 6)
    hao_ha = qua_to_hao.get(ha_quai, [0, 0, 0])
    hao_thuong = qua_to_hao.get(thuong_quai, [0, 0, 0])
    
    return hao_ha + hao_thuong


def ve_hao_to(hao_type, width=28):
    """
    Vẽ một hào âm hoặc dương với kích thước vừa phải, rõ ràng
    
    Args:
        hao_type: 1 = Dương, 0 = Âm
        width: độ rộng của gạch (mặc định 28 cho kích thước vừa)
    
    Returns:
        str: Gạch âm hoặc dương
    """
    if hao_type == 1:  # Dương - Vạch liền
        return "█" * width
    else:  # Âm - Vạch đứt
        half = width // 2 - 2
        return "█" * half + "    " + "█" * half


def tao_hien_thi_qua_chi_tiet_to(chinh_quai, thang):
    """
    Tạo hiển thị quẻ với gạch âm dương rõ ràng và thông tin chi tiết
    Kích thước vừa phải để phù hợp với giao diện, tập trung vào diễn giải
    
    Args:
        chinh_quai: dict quẻ chính
        thang: tháng để xác định Vượng Suy
    
    Returns:
        str: Chuỗi hiển thị quẻ
    """
    from luc_hao_kinh_dich import (
        DIA_CHI_NGU_HANH, LUC_THAN, LUC_THAN as LUC_THAN_DICT,
        TUAN_KHONG, DICH_MA, xac_dinh_vuong_suy
    )
    
    # Lấy thông tin quẻ
    thuong = chinh_quai['thuong_quai']
    ha = chinh_quai['ha_quai']
    dong_hao = chinh_quai['dong_hao'][0]
    
    # Xác định 6 hào âm/dương
    hao_list = xac_dinh_hao_am_duong(thuong, ha)
    
    # Thông tin cho 6 hào
    luc_than_6_hao = ["Phụ Mẫu", "Huynh Đệ", "Tử Tôn", "Thê Tài", "Quan Quỷ", "Phụ Mẫu"]
    luc_than_6_hao_list = ["Thanh Long", "Chu Tước", "Câu Trần", "Đằng Xà", "Bạch Hổ", "Huyền Vũ"]
    dia_chi_6_hao = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị"]
    tuan_khong_list = TUAN_KHONG.get("Giáp Tý", [])
    
    # Tạo hiển thị
    ket_qua = []
    ket_qua.append("")
    ket_qua.append("╔" + "═" * 95 + "╗")
    ket_qua.append("║" + f" QUẺ {chinh_quai['quai_info']['ten']} {chinh_quai['quai_info']['unicode']} ".center(95) + "║")
    ket_qua.append("╠" + "═" * 95 + "╣")
    
    # Hiển thị từ hào 6 xuống hào 1 (từ trên xuống dưới)
    for i in range(5, -1, -1):
        hao_so = i + 1
        hao_am_duong = hao_list[i]
        
        # Thông tin hào
        luc_than = luc_than_6_hao[i]
        luc_than_item = luc_than_6_hao_list[i]
        dia_chi = dia_chi_6_hao[i]
        ngu_hanh = DIA_CHI_NGU_HANH.get(dia_chi, "")
        vuong_suy = xac_dinh_vuong_suy(ngu_hanh, thang)
        
        # Các đánh dấu đặc biệt
        dong_mark = "⚡ĐỘNG" if hao_so == dong_hao else "     "
        tuan_khong_mark = "🈳Tuần Không" if dia_chi in tuan_khong_list else "          "
        dich_ma_mark = "🐎Dịch Mã" if dia_chi in DICH_MA else "        "
        
        # Icon Vượng Suy
        vuong_suy_icon = {
            "Vượng": "💪", "Tướng": "👍", "Hưu": "😐", 
            "Tù": "😔", "Tử": "💀"
        }.get(vuong_suy, "  ")
        
        # Vẽ gạch vừa phải
        gach = ve_hao_to(hao_am_duong, 28)
        
        # Thông tin chi tiết
        thong_tin = f"{luc_than:9} │ {luc_than_item:9} │ {dia_chi}({ngu_hanh:3}){vuong_suy_icon}{vuong_suy:5}"
        
        # Dòng hiển thị
        dong = f"║ H{hao_so} {dong_mark} {tuan_khong_mark} {dich_ma_mark} │ {gach} │ {thong_tin:42} ║"
        ket_qua.append(dong)
        
        if i > 0:
            ket_qua.append("║" + " " * 95 + "║")
    
    ket_qua.append("╚" + "═" * 95 + "╝")
    ket_qua.append("")
    
    # Chú thích
    ket_qua.append("📌 CHÚ THÍCH:")
    ket_qua.append("   ████████████████████████████ = Hào DƯƠNG (Cứng, Mạnh)")
    ket_qua.append("   ████████████    ████████████ = Hào ÂM (Mềm, Yếu)")
    ket_qua.append("   ⚡ Động | 🈳 Tuần Không | 🐎 Dịch Mã | 💪 Vượng > 👍 Tướng > 😐 Hưu > 😔 Tù > 💀 Tử")
    
    return "\n".join(ket_qua)


def tao_hien_thi_3_qua_to(chinh_quai, ho_quai, bien_quai, thang):
    """
    Tạo hiển thị 3 quẻ: Chính, Hỗ, Biến (kích thước vừa phải)
    
    Args:
        chinh_quai, ho_quai, bien_quai: dict quẻ
        thang: tháng
    
    Returns:
        str: Chuỗi hiển thị 3 quẻ
    """
    ket_qua = []
    
    ket_qua.append("╔" + "═" * 95 + "╗")
    ket_qua.append("║" + " 3 QUẺ: CHÍNH - HỖ - BIẾN ".center(95) + "║")
    ket_qua.append("╚" + "═" * 95 + "╝")
    ket_qua.append("")
    
    # Lấy hào của 3 quẻ
    chinh_hao = xac_dinh_hao_am_duong(chinh_quai['thuong_quai'], chinh_quai['ha_quai'])
    ho_hao = xac_dinh_hao_am_duong(ho_quai['thuong_quai'], ho_quai['ha_quai'])
    bien_hao = xac_dinh_hao_am_duong(bien_quai['thuong_quai'], bien_quai['ha_quai'])
    
    dong_hao = chinh_quai['dong_hao'][0]
    
    # Hiển thị từ hào 6 xuống hào 1
    for i in range(5, -1, -1):
        hao_so = i + 1
        dong_mark = "⚡" if hao_so == dong_hao else " "
        
        # Vẽ 3 gạch vừa
        gach_chinh = ve_hao_to(chinh_hao[i], 20)
        gach_ho = ve_hao_to(ho_hao[i], 20)
        gach_bien = ve_hao_to(bien_hao[i], 20)
        
        dong = f"  H{hao_so}{dong_mark} │ {gach_chinh} │ {gach_ho} │ {gach_bien} │"
        ket_qua.append(dong)
    
    ket_qua.append("")
    ket_qua.append(f"     │ {'CHÍNH':^20} │ {'HỖ':^20} │ {'BIẾN':^20} │")
    ket_qua.append(f"     │ {chinh_quai['quai_info']['ten']:^20} │ {ho_quai['quai_info']['ten']:^20} │ {bien_quai['quai_info']['ten']:^20} │")
    
    return "\n".join(ket_qua)


# Test
if __name__ == "__main__":
    print("=== TEST VẼ QUẺ BẰNG GẠCH ÂM DƯƠNG TO, RÕ NÉT ===\n")
    
    # Giả lập quẻ Phong Hỏa Gia Nhân
    chinh_quai = {
        'thuong_quai': 6,  # Tốn (Phong)
        'ha_quai': 5,      # Ly (Hỏa)
        'dong_hao': [3],
        'quai_info': {'ten': 'Phong Hỏa Gia Nhân', 'unicode': '䷤'}
    }
    
    ho_quai = {
        'thuong_quai': 2,  # Khảm
        'ha_quai': 1,      # Chấn
        'quai_info': {'ten': 'Thủy Lôi Truân', 'unicode': '䷂'}
    }
    
    bien_quai = {
        'thuong_quai': 6,  # Tốn
        'ha_quai': 6,      # Tốn
        'quai_info': {'ten': 'Tốn Vi Phong', 'unicode': '䷸'}
    }
    
    # Test hiển thị quẻ chi tiết
    print(tao_hien_thi_qua_chi_tiet_to(chinh_quai, 1))
    
    print("\n" + "="*150 + "\n")
    
    # Test hiển thị 3 quẻ
    print(tao_hien_thi_3_qua_to(chinh_quai, ho_quai, bien_quai, 1))
    
    print("\n✅ Test hoàn thành!")
