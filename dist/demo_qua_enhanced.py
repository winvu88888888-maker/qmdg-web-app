# -*- coding: utf-8 -*-
"""
DEMO - Hiển thị Quẻ Mai Hoa và Lục Hào với Gạch Âm Dương TO, RÕ NÉT
"""

from datetime import datetime

print("="*150)
print("🔮 DEMO HIỂN THỊ QUẺ MAI HOA VÀ LỤC HÀO VỚI GẠCH ÂM DƯƠNG TO, RÕ NÉT 🔮")
print("="*150)
print()

# ============================================================================
# PHẦN 1: MAI HOA DỊCH SỐ
# ============================================================================
print("📖 PHẦN 1: MAI HOA DỊCH SỐ - 64 QUẺ KINH DỊCH")
print("-"*150)
print()

from mai_hoa_dich_so import tinh_qua_theo_thoi_gian, giai_qua, BAT_QUAI

# Tính quẻ theo thời gian hiện tại
now = datetime.now()
ket_qua = tinh_qua_theo_thoi_gian(now.year, now.month, now.day, now.hour)

ban_qua = ket_qua['ban_qua']
qua_bien = ket_qua['qua_bien']
hao_dong = ket_qua['hao_dong']
qua_thuong = ket_qua['qua_thuong']
qua_ha = ket_qua['qua_ha']

print(f"⏰ Thời gian: {now.strftime('%H:%M - %d/%m/%Y')}")
print(f"📊 Bản Quẻ: {ban_qua['ten']} {ban_qua['unicode']} ({qua_thuong['unicode']}{qua_ha['unicode']})")
print(f"🔄 Quẻ Biến: {qua_bien['ten']} {qua_bien['unicode']}")
print(f"⚡ Hào Động: Hào thứ {hao_dong}")
print()

# Giải quẻ
giai_thich = giai_qua(ket_qua, "Tổng Quát")
print(giai_thich)
print()

# Hiển thị quẻ với gạch âm dương TO
try:
    from ve_qua_am_duong_enhanced import tao_hien_thi_qua_chi_tiet_to
    
    # Tìm số quẻ từ tên
    qua_thuong_so = None
    qua_ha_so = None
    for so, info in BAT_QUAI.items():
        if info['ten'] == qua_thuong['ten']:
            qua_thuong_so = so
        if info['ten'] == qua_ha['ten']:
            qua_ha_so = so
    
    if qua_thuong_so is not None and qua_ha_so is not None:
        chinh_quai_visual = {
            'thuong_quai': qua_thuong_so - 1,
            'ha_quai': qua_ha_so - 1,
            'dong_hao': [hao_dong],
            'quai_info': ban_qua,
            'bat_quai_thuong': qua_thuong,
            'bat_quai_ha': qua_ha
        }
        
        print("="*150)
        print("📊 HÌNH TƯỢNG QUẺ VỚI GẠCH ÂM DƯƠNG TO, RÕ NÉT")
        print("="*150)
        visual_qua = tao_hien_thi_qua_chi_tiet_to(chinh_quai_visual, now.month)
        print(visual_qua)
except Exception as e:
    print(f"(Không thể hiển thị visualization: {str(e)})")

print()
print()

# ============================================================================
# PHẦN 2: LỤC HÀO KINH DỊCH
# ============================================================================
print("☯️ PHẦN 2: LỤC HÀO KINH DỊCH - 3 QUẺ (CHÍNH - HỖ - BIẾN)")
print("-"*150)
print()

from luc_hao_kinh_dich import lap_qua_luc_hao

# Tính quẻ Lục Hào
ket_qua_luc_hao = lap_qua_luc_hao(now.year, now.month, now.day, now.hour, "Kinh Doanh")

print(ket_qua_luc_hao['giai_thich'])

print()
print("="*150)
print("✅ DEMO HOÀN THÀNH!")
print("="*150)
