# -*- coding: utf-8 -*-
"""
LỤC HÀO KINH DỊCH THEO CHỦ ĐỀ
Sử dụng 200+ chủ đề từ Kỳ Môn làm căn cứ để giải thích Lục Hào chính xác hơn
"""

from luc_hao_kinh_dich import lap_qua_luc_hao, BAT_QUAI, LUC_THAP_TU_QUAI
from qmdg_data import TOPIC_INTERPRETATIONS

def giai_luc_hao_theo_chu_de_cu_the(ket_qua_luc_hao, chu_de):
    """
    Giải quẻ Lục Hào dựa trên chủ đề cụ thể từ 200+ chủ đề Kỳ Môn
    
    Args:
        ket_qua_luc_hao: Kết quả từ lap_qua_luc_hao()
        chu_de: Chủ đề cụ thể (từ TOPIC_INTERPRETATIONS)
    
    Returns:
        String giải thích chi tiết theo chủ đề
    """
    
    chinh_quai = ket_qua_luc_hao['chinh_quai']
    ho_quai = ket_qua_luc_hao['ho_quai']
    bien_quai = ket_qua_luc_hao['bien_quai']
    
    # Lấy thông tin chủ đề từ Kỳ Môn
    chu_de_info = TOPIC_INTERPRETATIONS.get(chu_de, {})
    
    giai_thich = []
    giai_thich.append("="*95)
    giai_thich.append(f"☯️ LỤC HÀO KINH DỊCH - PHÂN TÍCH CHỦ ĐỀ: {chu_de.upper()}")
    giai_thich.append("="*95)
    giai_thich.append("")
    
    # PHẦN 1: THÔNG TIN 3 QUẺ
    giai_thich.append("🔷 THÔNG TIN 3 QUẺ:")
    giai_thich.append(f"   • Chính Quái: {chinh_quai['quai_info']['ten']} - Tình hình hiện tại")
    giai_thich.append(f"   • Hỗ Quái: {ho_quai['quai_info']['ten']} - Yếu tố nội tại, hỗ trợ")
    giai_thich.append(f"   • Biến Quái: {bien_quai['quai_info']['ten']} - Kết quả tương lai")
    giai_thich.append("")
    
    # PHẦN 2: PHÂN TÍCH THEO CHỦ ĐỀ KỲ MÔN
    if chu_de_info:
        giai_thich.append(f"📚 PHÂN TÍCH DựA TRÊN CHỦ ĐỀ '{chu_de}':")
        giai_thich.append("")
        
        # Dụng Thần từ Kỳ Môn
        if "Dụng_Thần" in chu_de_info:
            dung_than = chu_de_info["Dụng_Thần"]
            giai_thich.append(f"   🎯 Dụng Thần (Yếu tố cần xem): {', '.join(dung_than)}")
            giai_thich.append("")
            
            # Liên kết Dụng Thần với Lục Thân trong quẻ
            giai_thich.append("   🔗 LIÊN KẾT DỤNG THẦN VỚI LỤC THÂN:")
            
            # Phân tích từng Dụng Thần
            for dt in dung_than:
                if dt == "Thê Tài":
                    giai_thich.append("   • Thê Tài (Tiền bạc, Vợ):")
                    giai_thich.append("     - Xem hào nào mang Thê Tài")
                    giai_thich.append("     - Vượng/Suy quyết định kết quả về tài lộc")
                    giai_thich.append("     - Động = có biến động về tiền bạc")
                
                elif dt == "Quan Quỷ":
                    giai_thich.append("   • Quan Quỷ (Chồng, Quyền lực, Áp lực):")
                    giai_thich.append("     - Xem hào nào mang Quan Quỷ")
                    giai_thich.append("     - Vượng = áp lực lớn hoặc quyền lực cao")
                    giai_thich.append("     - Động = có thay đổi về địa vị/bệnh tật")
                
                elif dt == "Phụ Mẫu":
                    giai_thich.append("   • Phụ Mẫu (Cha mẹ, Văn thư, Nhà cửa):")
                    giai_thich.append("     - Xem hào nào mang Phụ Mẫu")
                    giai_thich.append("     - Vượng = giấy tờ thuận lợi, có nhà")
                    giai_thich.append("     - Động = có thay đổi về văn thư/nhà cửa")
                
                elif dt == "Huynh Đệ":
                    giai_thich.append("   • Huynh Đệ (Anh em, Bạn bè, Cạnh tranh):")
                    giai_thich.append("     - Xem hào nào mang Huynh Đệ")
                    giai_thich.append("     - Vượng = nhiều đối thủ/bạn bè")
                    giai_thich.append("     - Động = có tranh chấp/hợp tác")
                
                elif dt == "Tử Tôn":
                    giai_thich.append("   • Tử Tôn (Con cái, Sản phẩm, Vui vẻ):")
                    giai_thich.append("     - Xem hào nào mang Tử Tôn")
                    giai_thich.append("     - Vượng = con cái khỏe/hàng bán chạy")
                    giai_thich.append("     - Động = có tin vui về con cái/sản phẩm")
            
            giai_thich.append("")
    
    # PHẦN 3: DỰ ĐOÁN SỰ VIỆC CỤ THỂ THEO 3 QUẺ
    giai_thich.append(f"🎯 DỰ ĐOÁN SỰ VIỆC CỤ THỂ CHO '{chu_de}':")
    giai_thich.append("")
    
    # Dựa vào Chính Quái
    giai_thich.append(f"   📊 HIỆN TẠI (Chính Quái - {chinh_quai['quai_info']['ten']}):")
    
    if chu_de in ["Kinh Doanh", "Công Việc"]:
        giai_thich.append("   💼 Tình hình kinh doanh:")
        giai_thich.append("   • Xem Thê Tài (tiền bạc) vượng hay suy")
        giai_thich.append("   • Xem Tử Tôn (sản phẩm) có động không")
        giai_thich.append("   • Xem Huynh Đệ (cạnh tranh) mạnh yếu thế nào")
        
        # Phân tích cụ thể
        if "Cát" in chinh_quai['quai_info'].get('y_nghia', ''):
            giai_thich.append("   → Kinh doanh thuận lợi, có lợi nhuận")
        else:
            giai_thich.append("   → Cần cẩn trọng, có thể gặp khó khăn")
    
    elif chu_de in ["Hôn Nhân", "Tình Cảm"]:
        giai_thich.append("   💑 Tình hình tình cảm:")
        giai_thich.append("   • Nam xem Thê Tài (vợ), Nữ xem Quan Quỷ (chồng)")
        giai_thich.append("   • Xem Phụ Mẫu (cha mẹ hai bên) có cản trở không")
        giai_thich.append("   • Xem Huynh Đệ (người thứ ba) có xuất hiện không")
        
        if "hòa" in chinh_quai['quai_info'].get('y_nghia', '').lower():
            giai_thich.append("   → Quan hệ hòa thuận, có thể tiến triển")
        else:
            giai_thich.append("   → Cần thời gian, có trở ngại")
    
    elif chu_de in ["Sức Khỏe", "Bệnh Tật"]:
        giai_thich.append("   🏥 Tình hình sức khỏe:")
        giai_thich.append("   • Xem Quan Quỷ (bệnh tật) vượng hay suy")
        giai_thich.append("   • Xem Tử Tôn (thuốc men) có giúp được không")
        giai_thich.append("   • Xem Phụ Mẫu (bác sĩ, bệnh viện)")
        
        if "Cát" in chinh_quai['quai_info'].get('y_nghia', ''):
            giai_thich.append("   → Sức khỏe tốt, bệnh sẽ khỏi")
        else:
            giai_thich.append("   → Cần chữa trị, theo dõi sát")
    
    giai_thich.append("")
    
    # Dựa vào Hỗ Quái
    giai_thich.append(f"   🔄 NỘI TẠI (Hỗ Quái - {ho_quai['quai_info']['ten']}):")
    giai_thich.append("   • Yếu tố bên trong, tiềm năng")
    giai_thich.append("   • Điều kiện sẵn có, nền tảng")
    giai_thich.append("   • Hỗ trợ hoặc cản trở từ bên trong")
    giai_thich.append("")
    
    # Dựa vào Biến Quái
    giai_thich.append(f"   🎯 TƯƠNG LAI (Biến Quái - {bien_quai['quai_info']['ten']}):")
    
    if chu_de in ["Kinh Doanh", "Công Việc"]:
        giai_thich.append("   💼 Kết quả kinh doanh:")
        if "Cát" in bien_quai['quai_info'].get('y_nghia', ''):
            giai_thich.append("   • Sẽ thành công, có lợi nhuận")
            giai_thich.append("   • Hợp đồng được ký kết")
            giai_thich.append("   • Khách hàng hài lòng")
        else:
            giai_thich.append("   • Cần thêm thời gian")
            giai_thich.append("   • Có thể gặp trở ngại")
            giai_thich.append("   • Nên chuẩn bị phương án B")
    
    elif chu_de in ["Hôn Nhân", "Tình Cảm"]:
        giai_thich.append("   💑 Kết quả tình cảm:")
        if "hòa" in bien_quai['quai_info'].get('y_nghia', '').lower():
            giai_thich.append("   • Sẽ kết hôn/hạnh phúc")
            giai_thich.append("   • Gia đình ủng hộ")
            giai_thich.append("   • Quan hệ bền vững")
        else:
            giai_thich.append("   • Cần kiên nhẫn")
            giai_thich.append("   • Có thể chia tay")
            giai_thich.append("   • Nên suy nghĩ kỹ")
    
    giai_thich.append("")
    
    # PHẦN 4: THỜI GIAN ỨNG NGHIỆM
    giai_thich.append("   ⏰ THỜI GIAN ỨNG NGHIỆM:")
    giai_thich.append("   • Xem Hào Động để xác định thời gian")
    giai_thich.append("   • Xem Ngũ Hành của quẻ để biết nhanh/chậm")
    giai_thich.append("   • Xem Lục Thần để biết cát/hung khi nào")
    giai_thich.append("")
    
    # PHẦN 5: LỜI KHUYÊN
    giai_thich.append("💡 LỜI KHUYÊN HÀNH ĐỘNG:")
    giai_thich.append("")
    giai_thich.append("   ✓ NÊN:")
    giai_thich.append("   • Chú ý Dụng Thần - Yếu tố quan trọng nhất")
    giai_thich.append("   • Theo dõi Hào Động - Thời điểm biến hóa")
    giai_thich.append("   • Xem 3 quẻ kết hợp - Toàn cảnh sự việc")
    giai_thich.append("")
    giai_thich.append("   ✗ TRÁNH:")
    giai_thich.append("   • Chỉ xem 1 quẻ mà bỏ qua 2 quẻ kia")
    giai_thich.append("   • Bỏ qua Dụng Thần")
    giai_thich.append("   • Không xem Vượng Suy")
    giai_thich.append("")
    giai_thich.append("="*95)
    
    return "\n".join(giai_thich)


# Test
if __name__ == "__main__":
    print("=== TEST LỤC HÀO THEO CHỦ ĐỀ ===\n")
    
    from datetime import datetime
    
    # Lập quẻ
    now = datetime.now()
    ket_qua = lap_qua_luc_hao(now.year, now.month, now.day, now.hour, "Kinh Doanh")
    
    # Giải theo chủ đề
    giai_thich = giai_luc_hao_theo_chu_de_cu_the(ket_qua, "Kinh Doanh")
    print(giai_thich)
    
    print("\n✅ Test hoàn thành!")
