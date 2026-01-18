# -*- coding: utf-8 -*-
"""
TÍCH HỢP DỤNG THẦN VÀO KẾT QUẢ
Phân tích kết quả dựa trên Dụng Thần của từng chủ đề
Đưa ra lời khuyên và phương án cụ thể
"""

from dung_than_chi_tiet_200_chu_de import lay_dung_than_chi_tiet

def phan_tich_ky_mon_theo_dung_than(chu_de, cung_data):
    """
    Phân tích kết quả Kỳ Môn dựa trên Dụng Thần
    
    Args:
        chu_de: Chủ đề đang hỏi
        cung_data: Dictionary chứa thông tin các cung
        
    Returns:
        String chứa phân tích chi tiết
    """
    dung_than_info = lay_dung_than_chi_tiet(chu_de)
    km_info = dung_than_info['ky_mon']
    
    result = []
    result.append("="*80)
    result.append(f"📊 PHÂN TÍCH KỲ MÔN - CHỦ ĐỀ: {chu_de}")
    result.append("="*80)
    result.append("")
    
    result.append(f"🎯 MỤC TIÊU: {dung_than_info['muc_tieu']}")
    result.append("")
    
    result.append(f"🔮 DỤNG THẦN KỲ MÔN: {km_info['dung_than']}")
    result.append(f"   {km_info['giai_thich']}")
    result.append("")
    
    # Tìm Dụng Thần trong bàn
    result.append("📍 VỊ TRÍ DỤNG THẦN TRÊN BÀN:")
    # TODO: Tìm cung chứa Dụng Thần
    result.append("   (Đang phân tích...)")
    result.append("")
    
    # Phân tích vượng suy
    result.append("⚖️ PHÂN TÍCH VƯỢNG SUY:")
    result.append("   (Dựa vào mùa và Ngũ Hành)")
    result.append("")
    
    # Kết luận
    result.append("✅ KẾT LUẬN:")
    result.append("   • Dụng Thần vượng → Tốt, thuận lợi")
    result.append("   • Dụng Thần suy → Khó khăn, cần chờ")
    result.append("")
    
    # Lời khuyên
    result.append("💡 LỜI KHUYÊN:")
    result.append(f"   {km_info['cach_xem']}")
    result.append("")
    
    # Phương án
    result.append("🎯 PHƯƠNG ÁN:")
    result.append("   • Nếu tốt: Hành động ngay, tận dụng thời cơ")
    result.append("   • Nếu xấu: Chờ đợi, chuẩn bị kỹ hơn")
    result.append("")
    
    result.append("="*80)
    
    return "\n".join(result)


def phan_tich_mai_hoa_theo_dung_than(chu_de, qua_data):
    """
    Phân tích kết quả Mai Hoa dựa trên Dụng Thần
    
    Args:
        chu_de: Chủ đề đang hỏi
        qua_data: Dictionary chứa thông tin quẻ
        
    Returns:
        String chứa phân tích chi tiết
    """
    dung_than_info = lay_dung_than_chi_tiet(chu_de)
    mh_info = dung_than_info['mai_hoa']
    
    result = []
    result.append("="*80)
    result.append(f"📊 PHÂN TÍCH MAI HOA - CHỦ ĐỀ: {chu_de}")
    result.append("="*80)
    result.append("")
    
    result.append(f"🎯 MỤC TIÊU: {dung_than_info['muc_tieu']}")
    result.append("")
    
    result.append(f"📖 DỤNG THẦN MAI HOA: {mh_info['dung_than']}")
    result.append(f"   {mh_info['giai_thich']}")
    result.append("")
    
    # Phân tích quẻ
    result.append("🔍 PHÂN TÍCH QUẺ:")
    if qua_data:
        result.append(f"   • Bản Quẻ: {qua_data.get('ban_qua', 'N/A')}")
        result.append(f"   • Quẻ Biến: {qua_data.get('qua_bien', 'N/A')}")
        result.append(f"   • Hào Động: {qua_data.get('hao_dong', 'N/A')}")
    result.append("")
    
    # Phân tích Ngũ Hành
    result.append("⚖️ PHÂN TÍCH NGŨ HÀNH:")
    result.append(f"   • Ngũ Hành cần xem: {mh_info.get('ngu_hanh', 'N/A')}")
    result.append("   (Dựa vào mùa để xét vượng suy)")
    result.append("")
    
    # Kết luận
    result.append("✅ KẾT LUẬN:")
    result.append("   • Quẻ tốt + Ngũ Hành vượng → Thành công")
    result.append("   • Quẻ xấu + Ngũ Hành suy → Khó khăn")
    result.append("")
    
    # Lời khuyên
    result.append("💡 LỜI KHUYÊN:")
    result.append(f"   {mh_info['cach_xem']}")
    result.append("")
    
    # Phương án
    result.append("🎯 PHƯƠNG ÁN:")
    result.append("   • Quẻ Biến tốt hơn: Tình hình sẽ cải thiện")
    result.append("   • Quẻ Biến xấu hơn: Cần cẩn trọng, có thể xấu đi")
    result.append("")
    
    result.append("="*80)
    
    return "\n".join(result)


def phan_tich_luc_hao_theo_dung_than(chu_de, luc_hao_data):
    """
    Phân tích kết quả Lục Hào dựa trên Dụng Thần
    
    Args:
        chu_de: Chủ đề đang hỏi
        luc_hao_data: Dictionary chứa thông tin 3 quẻ
        
    Returns:
        String chứa phân tích chi tiết
    """
    dung_than_info = lay_dung_than_chi_tiet(chu_de)
    lh_info = dung_than_info['luc_hao']
    
    result = []
    result.append("="*80)
    result.append(f"📊 PHÂN TÍCH LỤC HÀO - CHỦ ĐỀ: {chu_de}")
    result.append("="*80)
    result.append("")
    
    result.append(f"🎯 MỤC TIÊU: {dung_than_info['muc_tieu']}")
    result.append("")
    
    result.append(f"☯️ DỤNG THẦN LỤC HÀO: {lh_info['dung_than']}")
    result.append(f"   {lh_info['giai_thich']}")
    result.append("")
    
    # Phân tích 3 quẻ
    result.append("🔍 PHÂN TÍCH 3 QUẺ:")
    if luc_hao_data:
        result.append(f"   • Quẻ Chính: {luc_hao_data.get('qua_chinh', 'N/A')}")
        result.append(f"   • Quẻ Hỗ: {luc_hao_data.get('qua_ho', 'N/A')}")
        result.append(f"   • Quẻ Biến: {luc_hao_data.get('qua_bien', 'N/A')}")
    result.append("")
    
    # Phân tích Dụng Thần
    result.append("⚖️ PHÂN TÍCH DỤNG THẦN:")
    result.append("   • Tìm hào mang Dụng Thần")
    result.append("   • Xem Vượng hay Suy (theo ngày tháng)")
    result.append("   • Xem Động hay Tĩnh")
    result.append("")
    
    # Kết luận
    result.append("✅ KẾT LUẬN:")
    result.append("   • Dụng Thần vượng + động → Nhanh, tốt")
    result.append("   • Dụng Thần suy + tĩnh → Chậm, khó")
    result.append("")
    
    # Lời khuyên
    result.append("💡 LỜI KHUYÊN:")
    result.append(f"   {lh_info['cach_xem']}")
    result.append("")
    
    # Phương án
    result.append("🎯 PHƯƠNG ÁN:")
    result.append("   • Dụng Thần tốt: Tiến hành theo kế hoạch")
    result.append("   • Dụng Thần xấu: Cần điều chỉnh, chờ thời")
    result.append("")
    
    result.append("="*80)
    
    return "\n".join(result)


# Test
if __name__ == "__main__":
    print(phan_tich_ky_mon_theo_dung_than("Mua Nhà", {}))
    print("\n\n")
    print(phan_tich_mai_hoa_theo_dung_than("Kinh Doanh", {}))
    print("\n\n")
    print(phan_tich_luc_hao_theo_dung_than("Hôn Nhân", {}))
