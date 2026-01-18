# -*- coding: utf-8 -*-
"""
MAI HOA DỊCH SỐ THEO CHỦ ĐỀ
Sử dụng 200+ chủ đề từ Kỳ Môn làm căn cứ để giải thích Mai Hoa chính xác hơn
"""

from mai_hoa_dich_so import tinh_qua_theo_thoi_gian, tinh_qua_ngau_nhien, BAT_QUAI, LUC_THAP_TU_QUAI
from qmdg_data import TOPIC_INTERPRETATIONS

def giai_mai_hoa_theo_chu_de_cu_the(ket_qua_qua, chu_de):
    """
    Giải quẻ Mai Hoa dựa trên chủ đề cụ thể từ 200+ chủ đề Kỳ Môn
    
    Args:
        ket_qua_qua: Kết quả từ tinh_qua_theo_thoi_gian()
        chu_de: Chủ đề cụ thể (từ TOPIC_INTERPRETATIONS)
    
    Returns:
        String giải thích chi tiết theo chủ đề
    """
    
    ban_qua = ket_qua_qua["ban_qua"]
    qua_bien = ket_qua_qua["qua_bien"]
    hao_dong = ket_qua_qua["hao_dong"]
    qua_thuong = ket_qua_qua["qua_thuong"]
    qua_ha = ket_qua_qua["qua_ha"]
    
    # Lấy thông tin chủ đề từ Kỳ Môn
    chu_de_info = TOPIC_INTERPRETATIONS.get(chu_de, {})
    
    giai_thich = []
    giai_thich.append("="*95)
    giai_thich.append(f"📖 MAI HOA DỊCH SỐ - PHÂN TÍCH CHỦ ĐỀ: {chu_de.upper()}")
    giai_thich.append("="*95)
    giai_thich.append("")
    
    # PHẦN 1: THÔNG TIN QUẺ
    giai_thich.append("🔷 THÔNG TIN QUẺ:")
    giai_thich.append(f"   • Bản Quẻ: {ban_qua['ten']} {ban_qua['unicode']}")
    giai_thich.append(f"   • Thượng Quái: {qua_thuong['ten']} ({qua_thuong['hanh']}) - {qua_thuong['tuong']}")
    giai_thich.append(f"   • Hạ Quái: {qua_ha['ten']} ({qua_ha['hanh']}) - {qua_ha['tuong']}")
    giai_thich.append(f"   • Hào Động: Hào {hao_dong}")
    giai_thich.append(f"   • Quẻ Biến: {qua_bien['ten']} {qua_bien['unicode']}")
    giai_thich.append("")
    
    # PHẦN 2: PHÂN TÍCH THEO CHỦ ĐỀ KỲ MÔN
    if chu_de_info:
        giai_thich.append(f"📚 PHÂN TÍCH DựA TRÊN CHỦ ĐỀ '{chu_de}':")
        giai_thich.append("")
        
        # Dụng Thần từ Kỳ Môn
        if "Dụng_Thần" in chu_de_info:
            dung_than = chu_de_info["Dụng_Thần"]
            giai_thich.append(f"   🎯 Dụng Thần (Yếu tố quan trọng): {', '.join(dung_than)}")
            giai_thich.append("")
        
        # Phân tích Bát Quái theo Dụng Thần
        giai_thich.append("   🔍 PHÂN TÍCH BÁT QUÁI THEO DỤNG THẦN:")
        
        # Phân tích Thượng Quái
        giai_thich.append(f"   • Thượng Quái ({qua_thuong['ten']}):")
        giai_thich.append(f"     - Tượng: {qua_thuong['tuong']}")
        giai_thich.append(f"     - Ngũ Hành: {qua_thuong['hanh']}")
        
        # Liên kết với chủ đề
        if chu_de in ["Kinh Doanh", "Công Việc", "Sự Nghiệp"]:
            if qua_thuong['hanh'] == "Kim":
                giai_thich.append(f"     - Ý nghĩa: Kim tượng trưng cho tiền bạc, quyết đoán - Tốt cho kinh doanh")
            elif qua_thuong['hanh'] == "Mộc":
                giai_thich.append(f"     - Ý nghĩa: Mộc tượng trưng cho phát triển, mở rộng - Tốt cho khởi nghiệp")
            elif qua_thuong['hanh'] == "Thủy":
                giai_thich.append(f"     - Ý nghĩa: Thủy tượng trưng cho lưu thông, linh hoạt - Tốt cho thương mại")
            elif qua_thuong['hanh'] == "Hỏa":
                giai_thich.append(f"     - Ý nghĩa: Hỏa tượng trưng cho nổi tiếng, marketing - Tốt cho quảng cáo")
            else:
                giai_thich.append(f"     - Ý nghĩa: Thổ tượng trưng cho ổn định, tích lũy - Tốt cho đầu tư dài hạn")
        
        elif chu_de in ["Hôn Nhân", "Tình Cảm", "Gia Đình"]:
            if qua_thuong['ten'] == "Càn":
                giai_thich.append(f"     - Ý nghĩa: Càn (Trời) - Nam mạnh, chủ động, có trách nhiệm")
            elif qua_thuong['ten'] == "Khôn":
                giai_thich.append(f"     - Ý nghĩa: Khôn (Địa) - Nữ hiền, nhu hòa, chăm sóc")
            elif qua_thuong['ten'] == "Ly":
                giai_thich.append(f"     - Ý nghĩa: Ly (Hỏa) - Tình cảm nồng nhiệt, rực rỡ")
            elif qua_thuong['ten'] == "Khảm":
                giai_thich.append(f"     - Ý nghĩa: Khảm (Thủy) - Tình cảm sâu sắc nhưng có trở ngại")
        
        giai_thich.append("")
        
        # Phân tích Hạ Quái
        giai_thich.append(f"   • Hạ Quái ({qua_ha['ten']}):")
        giai_thich.append(f"     - Tượng: {qua_ha['tuong']}")
        giai_thich.append(f"     - Ngũ Hành: {qua_ha['hanh']}")
        giai_thich.append(f"     - Ý nghĩa: Nền tảng, khởi đầu của sự việc")
        giai_thich.append("")
    
    # PHẦN 3: DỰ ĐOÁN SỰ VIỆC CỤ THỂ
    giai_thich.append(f"🎯 DỰ ĐOÁN SỰ VIỆC CỤ THỂ CHO '{chu_de}':")
    giai_thich.append("")
    
    # Dựa trên Bản Quẻ và Quẻ Biến
    giai_thich.append(f"   📊 Tình hình hiện tại ({ban_qua['ten']}):")
    giai_thich.append(f"   {ban_qua['y_nghia']}")
    giai_thich.append("")
    
    # Dự đoán cụ thể theo chủ đề
    if chu_de in ["Kinh Doanh", "Công Việc"]:
        giai_thich.append("   💼 Sự việc sẽ xảy ra:")
        if "Cát" in ban_qua['y_nghia'] or "thành công" in ban_qua['y_nghia']:
            giai_thich.append("   • Hợp đồng sẽ được ký kết thuận lợi")
            giai_thich.append("   • Khách hàng/đối tác sẽ hợp tác")
            giai_thich.append("   • Doanh thu tăng trưởng tốt")
        else:
            giai_thich.append("   • Cần cẩn trọng trong đàm phán")
            giai_thich.append("   • Có thể gặp trở ngại về tài chính")
            giai_thich.append("   • Nên hoãn các quyết định lớn")
    
    elif chu_de in ["Hôn Nhân", "Tình Cảm"]:
        giai_thich.append("   💑 Sự việc sẽ xảy ra:")
        if "Cát" in ban_qua['y_nghia'] or "hòa" in ban_qua['y_nghia']:
            giai_thich.append("   • Quan hệ sẽ tiến triển tích cực")
            giai_thich.append("   • Có thể có tin vui (đính hôn, cưới)")
            giai_thich.append("   • Gia đình hai bên ủng hộ")
        else:
            giai_thich.append("   • Cần thời gian để hiểu nhau hơn")
            giai_thich.append("   • Có thể có mâu thuẫn nhỏ")
            giai_thich.append("   • Nên kiên nhẫn, không vội vàng")
    
    elif chu_de in ["Sức Khỏe", "Bệnh Tật"]:
        giai_thich.append("   🏥 Sự việc sẽ xảy ra:")
        if "Cát" in ban_qua['y_nghia']:
            giai_thich.append("   • Sức khỏe sẽ cải thiện")
            giai_thich.append("   • Bệnh sẽ thuyên giảm dần")
            giai_thich.append("   • Thuốc men có hiệu quả")
        else:
            giai_thich.append("   • Cần theo dõi sức khỏe sát sao")
            giai_thich.append("   • Nên đi khám bác sĩ sớm")
            giai_thich.append("   • Chú ý nghỉ ngơi, không quá lao lực")
    
    giai_thich.append("")
    
    # PHẦN 4: XU HƯỚNG BIẾN HÓA
    giai_thich.append(f"   🔄 Xu hướng biến hóa ({qua_bien['ten']}):")
    giai_thich.append(f"   {qua_bien['y_nghia']}")
    giai_thich.append("")
    giai_thich.append(f"   📈 Từ '{ban_qua['ten']}' → '{qua_bien['ten']}':")
    
    if ban_qua['so'] == qua_bien['so']:
        giai_thich.append("   • Tình hình ổn định, ít thay đổi")
        giai_thich.append("   • Kết quả như dự kiến ban đầu")
    else:
        giai_thich.append("   • Sẽ có sự thay đổi rõ rệt")
        giai_thich.append("   • Cần chuẩn bị cho tình huống mới")
        giai_thich.append("   • Linh hoạt ứng biến")
    
    giai_thich.append("")
    
    # PHẦN 5: THỜI GIAN ỨNG NGHIỆM
    giai_thich.append("   ⏰ THỜI GIAN ỨNG NGHIỆM:")
    
    # Dựa vào Hào Động
    if hao_dong <= 2:
        giai_thich.append("   • Ngắn hạn: 1-3 ngày (Hào động ở dưới)")
    elif hao_dong <= 4:
        giai_thich.append("   • Trung hạn: 1-2 tuần (Hào động ở giữa)")
    else:
        giai_thich.append("   • Dài hạn: 1-3 tháng (Hào động ở trên)")
    
    # Dựa vào Ngũ Hành
    if qua_thuong['hanh'] == "Hỏa":
        giai_thich.append("   • Nhanh (Hỏa - nhanh chóng)")
    elif qua_thuong['hanh'] == "Thủy":
        giai_thich.append("   • Linh hoạt (Thủy - thay đổi)")
    elif qua_thuong['hanh'] == "Thổ":
        giai_thich.append("   • Chậm (Thổ - ổn định)")
    
    giai_thich.append("")
    
    # PHẦN 6: LỜI KHUYÊN
    giai_thich.append("💡 LỜI KHUYÊN HÀNH ĐỘNG:")
    giai_thich.append("")
    giai_thich.append("   ✓ NÊN:")
    giai_thich.append(f"   • Hành động khi Hào {hao_dong} động - Đây là thời điểm quan trọng")
    giai_thich.append("   • Chuẩn bị cho sự chuyển biến từ Bản Quẻ sang Quẻ Biến")
    giai_thich.append("   • Theo dõi các dấu hiệu từ Bát Quái tượng")
    giai_thich.append("")
    giai_thich.append("   ✗ TRÁNH:")
    giai_thich.append("   • Hành động ngược với Ngũ Hành của quẻ")
    giai_thich.append("   • Bỏ qua cảnh báo từ Quẻ Biến")
    giai_thich.append("   • Quá chủ quan hoặc quá bi quan")
    giai_thich.append("")
    giai_thich.append("="*95)
    
    return "\n".join(giai_thich)


# Test
if __name__ == "__main__":
    print("=== TEST MAI HOA THEO CHỦ ĐỀ ===\n")
    
    from datetime import datetime
    
    # Tính quẻ
    now = datetime.now()
    ket_qua = tinh_qua_theo_thoi_gian(now.year, now.month, now.day, now.hour)
    
    # Giải theo chủ đề Kinh Doanh
    giai_thich = giai_mai_hoa_theo_chu_de_cu_the(ket_qua, "Kinh Doanh")
    print(giai_thich)
    
    print("\n✅ Test hoàn thành!")
