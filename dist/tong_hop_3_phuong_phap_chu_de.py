# -*- coding: utf-8 -*-
"""
TỔNG HỢP 3 PHƯƠNG PHÁP: KỲ MÔN + MAI HOA + KINH DỊCH
Phân tích tổng hợp cho So Sánh Chủ-Khách theo chủ đề
"""

from datetime import datetime
from mai_hoa_dich_so import tinh_qua_theo_thoi_gian, giai_qua
from luc_hao_kinh_dich import lap_qua_luc_hao

def tong_hop_3_phuong_phap_cho_chu_de(chu_de, chu_info, khach_info, dt_obj):
    """
    Tổng hợp phân tích từ 3 phương pháp cho một chủ đề cụ thể
    
    Args:
        chu_de: Chủ đề cần phân tích
        chu_info: Thông tin cung Chủ (từ Kỳ Môn)
        khach_info: Thông tin cung Khách (từ Kỳ Môn)
        dt_obj: Thời gian datetime
    
    Returns:
        Dict chứa phân tích tổng hợp từ 3 phương pháp
    """
    
    ket_qua = {
        "chu_de": chu_de,
        "thoi_gian": dt_obj.strftime("%H:%M - %d/%m/%Y"),
        "phan_tich_ky_mon": {},
        "phan_tich_mai_hoa": {},
        "phan_tich_kinh_dich": {},
        "ket_luan_tong_hop": ""
    }
    
    # ========================================================================
    # PHẦN 1: PHÂN TÍCH KỲ MÔN ĐỘN GIÁP
    # ========================================================================
    
    ket_qua["phan_tich_ky_mon"] = {
        "tieu_de": "🔮 KỲ MÔN ĐỘN GIÁP - Chiến Lược & Vị Thế",
        "chu": {
            "cung": f"Cung {chu_info['so']} - {chu_info['ten']}",
            "ngu_hanh": chu_info['hanh'],
            "cuu_tinh": chu_info['sao'],
            "bat_mon": chu_info['cua'],
            "bat_than": chu_info['than'],
            "can_thien": chu_info['can_thien'],
            "can_dia": chu_info['can_dia']
        },
        "khach": {
            "cung": f"Cung {khach_info['so']} - {khach_info['ten']}",
            "ngu_hanh": khach_info['hanh'],
            "cuu_tinh": khach_info['sao'],
            "bat_mon": khach_info['cua'],
            "bat_than": khach_info['than'],
            "can_thien": khach_info['can_thien'],
            "can_dia": khach_info['can_dia']
        }
    }
    
    # Phân tích Ngũ Hành
    from qmdg_data import tinh_ngu_hanh_sinh_khac
    mqh_chu_khach = tinh_ngu_hanh_sinh_khac(chu_info['hanh'], khach_info['hanh'])
    
    if "Sinh" in mqh_chu_khach and "Chủ" in mqh_chu_khach:
        ket_qua["phan_tich_ky_mon"]["ngu_hanh"] = f"✅ Chủ sinh Khách - Chủ có lợi thế, nhưng tốn sức"
    elif "Sinh" in mqh_chu_khach and "Khách" in mqh_chu_khach:
        ket_qua["phan_tich_ky_mon"]["ngu_hanh"] = f"⚠️ Khách sinh Chủ - Khách hỗ trợ Chủ, có lợi"
    elif "Khắc" in mqh_chu_khach and "Chủ" in mqh_chu_khach:
        ket_qua["phan_tich_ky_mon"]["ngu_hanh"] = f"💪 Chủ khắc Khách - Chủ áp đảo, rất có lợi"
    elif "Khắc" in mqh_chu_khach and "Khách" in mqh_chu_khach:
        ket_qua["phan_tich_ky_mon"]["ngu_hanh"] = f"❌ Khách khắc Chủ - Chủ bất lợi, cần cẩn trọng"
    else:
        ket_qua["phan_tich_ky_mon"]["ngu_hanh"] = f"⚖️ Cùng hành - Ngang sức, cần xem yếu tố khác"
    
    # Kết luận Kỳ Môn
    ket_qua["phan_tich_ky_mon"]["ket_luan"] = f"""
📊 KẾT LUẬN KỲ MÔN:
• Ngũ Hành: {mqh_chu_khach}
• Chủ ({chu_info['hanh']}) vs Khách ({khach_info['hanh']}): {ket_qua["phan_tich_ky_mon"]["ngu_hanh"]}
• Sao Chủ: {chu_info['sao']} | Sao Khách: {khach_info['sao']}
• Môn Chủ: {chu_info['cua']} | Môn Khách: {khach_info['cua']}
"""
    
    # ========================================================================
    # PHẦN 2: PHÂN TÍCH MAI HOA DỊCH SỐ
    # ========================================================================
    
    # Tính quẻ Mai Hoa theo thời gian
    ket_qua_mai_hoa = tinh_qua_theo_thoi_gian(
        dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour
    )
    
    # Giải quẻ theo chủ đề CỤ THỂ (sử dụng 200+ chủ đề Kỳ Môn)
    try:
        from mai_hoa_theo_chu_de import giai_mai_hoa_theo_chu_de_cu_the
        giai_thich_mai_hoa = giai_mai_hoa_theo_chu_de_cu_the(ket_qua_mai_hoa, chu_de)
    except:
        # Fallback về giải thích cũ nếu module mới không có
        giai_thich_mai_hoa = giai_qua(ket_qua_mai_hoa, chu_de)
    
    ket_qua["phan_tich_mai_hoa"] = {
        "tieu_de": "📖 MAI HOA DỊCH SỐ - Xu Hướng & Biến Hóa",
        "ban_qua": ket_qua_mai_hoa['ban_qua']['ten'],
        "qua_bien": ket_qua_mai_hoa['qua_bien']['ten'],
        "hao_dong": ket_qua_mai_hoa['hao_dong'],
        "giai_thich_day_du": giai_thich_mai_hoa,
        "ket_luan": f"""
📖 KẾT LUẬN MAI HOA (Theo chủ đề {chu_de}):
• Bản Quẻ: {ket_qua_mai_hoa['ban_qua']['ten']} - {ket_qua_mai_hoa['ban_qua']['y_nghia']}
• Quẻ Biến: {ket_qua_mai_hoa['qua_bien']['ten']} - {ket_qua_mai_hoa['qua_bien']['y_nghia']}
• Hào Động: Hào {ket_qua_mai_hoa['hao_dong']} - Điểm biến đổi quan trọng
• Xu hướng: Từ '{ket_qua_mai_hoa['ban_qua']['ten']}' → '{ket_qua_mai_hoa['qua_bien']['ten']}'
• Dựa trên Dụng Thần Kỳ Môn để giải thích chính xác
"""
    }
    
    # ========================================================================
    # PHẦN 3: PHÂN TÍCH LỤC HÀO KINH DỊCH
    # ========================================================================
    
    # Lập quẻ Lục Hào
    ket_qua_luc_hao = lap_qua_luc_hao(
        dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour, chu_de
    )
    
    # Giải quẻ theo chủ đề CỤ THỂ (sử dụng 200+ chủ đề Kỳ Môn)
    try:
        from luc_hao_theo_chu_de import giai_luc_hao_theo_chu_de_cu_the
        giai_thich_luc_hao = giai_luc_hao_theo_chu_de_cu_the(ket_qua_luc_hao, chu_de)
    except:
        # Fallback về giải thích cũ
        giai_thich_luc_hao = ket_qua_luc_hao['giai_thich']
    
    ket_qua["phan_tich_kinh_dich"] = {
        "tieu_de": "☯️ LỤC HÀO KINH DỊCH - Diễn Biến Chi Tiết",
        "chinh_quai": ket_qua_luc_hao['chinh_quai']['quai_info']['ten'],
        "ho_quai": ket_qua_luc_hao['ho_quai']['quai_info']['ten'],
        "bien_quai": ket_qua_luc_hao['bien_quai']['quai_info']['ten'],
        "giai_thich_day_du": giai_thich_luc_hao,
        "ket_luan": f"""
☯️ KẾT LUẬN LỤC HÀO (Theo chủ đề {chu_de}):
• Chính Quái: {ket_qua_luc_hao['chinh_quai']['quai_info']['ten']} - Tình hình hiện tại
• Hỗ Quái: {ket_qua_luc_hao['ho_quai']['quai_info']['ten']} - Yếu tố nội tại
• Biến Quái: {ket_qua_luc_hao['bien_quai']['quai_info']['ten']} - Kết quả tương lai
• 3 Quẻ cho thấy: Quá trình biến hóa từ bên trong ra bên ngoài
• Dựa trên Dụng Thần Kỳ Môn để xác định yếu tố quan trọng
"""
    }
    
    # ========================================================================
    # PHẦN 4: TỔNG HỢP 3 PHƯƠNG PHÁP
    # ========================================================================
    
    ket_luan_tong_hop = f"""
{'='*95}
🎯 KẾT LUẬN TỔNG HỢP 3 PHƯƠNG PHÁP - CHỦ ĐỀ: {chu_de.upper()}
{'='*95}

📌 TỔNG QUAN:
Thời gian: {dt_obj.strftime("%H:%M - %d/%m/%Y")}
Chủ đề: {chu_de}

🔮 1. KỲ MÔN ĐỘN GIÁP (Chiến Lược & Vị Thế):
{ket_qua["phan_tich_ky_mon"]["ket_luan"]}

📖 2. MAI HOA DỊCH SỐ (Xu Hướng & Biến Hóa):
{ket_qua["phan_tich_mai_hoa"]["ket_luan"]}

☯️ 3. LỤC HÀO KINH DỊCH (Diễn Biến Chi Tiết):
{ket_qua["phan_tich_kinh_dich"]["ket_luan"]}

{'='*95}
💡 TỔNG KẾT CUỐI CÙNG:
{'='*95}

"""
    
    # Phân tích tổng hợp dựa trên 3 phương pháp
    if "Khắc" in mqh_chu_khach and "Chủ" in mqh_chu_khach:
        ket_luan_tong_hop += """
✅ KẾT LUẬN CHUNG:
• Kỳ Môn: Chủ khắc Khách - Vị thế áp đảo
• Mai Hoa: Quẻ cho thấy xu hướng biến đổi theo chiều hướng tích cực
• Lục Hào: 3 quẻ xác nhận sự phát triển thuận lợi

🎯 HÀNH ĐỘNG NÊN LÀM:
1. Chủ động tiến công, tận dụng lợi thế
2. Nắm bắt thời cơ khi Hào Động xuất hiện
3. Theo dõi sát sao Quẻ Biến để điều chỉnh kịp thời
4. Duy trì vị thế mạnh, không chủ quan

⚠️ CẨN TRỌNG:
• Đừng quá cứng rắn dẫn đến phản tác dụng
• Chú ý Biến Quái để tránh bất ngờ
• Giữ thái độ khiêm tốn dù có lợi thế
"""
    elif "Khắc" in mqh_chu_khach and "Khách" in mqh_chu_khach:
        ket_luan_tong_hop += """
❌ KẾT LUẬN CHUNG:
• Kỳ Môn: Khách khắc Chủ - Vị thế bất lợi
• Mai Hoa: Cần chú ý Quẻ Biến để tìm cơ hội đảo ngược
• Lục Hào: Hỗ Quái và Biến Quái chỉ ra hướng giải quyết

🎯 HÀNH ĐỘNG NÊN LÀM:
1. Tránh đối đầu trực tiếp, tìm cách hóa giải
2. Chờ đợi thời cơ khi Hào Động chuyển biến
3. Tìm kiếm sự hỗ trợ từ bên ngoài
4. Chuẩn bị phương án dự phòng

⚠️ CẨN TRỌNG:
• Tuyệt đối không hành động vội vàng
• Chú ý Quẻ Biến - có thể là cơ hội đảo ngược
• Giữ bình tĩnh, kiên nhẫn chờ thời
"""
    else:
        ket_luan_tong_hop += """
⚖️ KẾT LUẬN CHUNG:
• Kỳ Môn: Lực lượng tương đương, cần xem yếu tố khác
• Mai Hoa: Hào Động và Quẻ Biến sẽ quyết định kết quả
• Lục Hào: 3 quẻ chỉ ra quá trình biến hóa phức tạp

🎯 HÀNH ĐỘNG NÊN LÀM:
1. Linh hoạt ứng biến theo tình hình
2. Tận dụng Hào Động để tạo đột phá
3. Chuẩn bị cho cả 2 kịch bản tốt/xấu
4. Tìm kiếm yếu tố bên ngoài để tạo lợi thế

⚠️ CẨN TRỌNG:
• Tình hình có thể thay đổi bất ngờ
• Theo dõi sát sao các dấu hiệu từ 3 phương pháp
• Không nên quá lạc quan hoặc bi quan
"""
    
    ket_qua["ket_luan_tong_hop"] = ket_luan_tong_hop
    
    return ket_qua


def tao_bao_cao_tong_hop_3pp(ket_qua_tong_hop):
    """
    Tạo báo cáo tổng hợp dễ đọc từ kết quả phân tích 3 phương pháp
    
    Args:
        ket_qua_tong_hop: Dict từ tong_hop_3_phuong_phap_cho_chu_de()
    
    Returns:
        String báo cáo đầy đủ
    """
    
    bao_cao = []
    
    # Header
    bao_cao.append("="*95)
    bao_cao.append("🔮 BÁO CÁO TỔNG HỢP 3 PHƯƠNG PHÁP: KỲ MÔN + MAI HOA + KINH DỊCH")
    bao_cao.append("="*95)
    bao_cao.append(f"Chủ đề: {ket_qua_tong_hop['chu_de']}")
    bao_cao.append(f"Thời gian: {ket_qua_tong_hop['thoi_gian']}")
    bao_cao.append("")
    
    # Phần 1: Kỳ Môn
    bao_cao.append("─"*95)
    bao_cao.append(ket_qua_tong_hop['phan_tich_ky_mon']['tieu_de'])
    bao_cao.append("─"*95)
    bao_cao.append(ket_qua_tong_hop['phan_tich_ky_mon']['ket_luan'])
    bao_cao.append("")
    
    # Phần 2: Mai Hoa
    bao_cao.append("─"*95)
    bao_cao.append(ket_qua_tong_hop['phan_tich_mai_hoa']['tieu_de'])
    bao_cao.append("─"*95)
    bao_cao.append(ket_qua_tong_hop['phan_tich_mai_hoa']['ket_luan'])
    bao_cao.append("")
    bao_cao.append("📄 GIẢI THÍCH CHI TIẾT:")
    bao_cao.append(ket_qua_tong_hop['phan_tich_mai_hoa']['giai_thich_day_du'])
    bao_cao.append("")
    
    # Phần 3: Lục Hào
    bao_cao.append("─"*95)
    bao_cao.append(ket_qua_tong_hop['phan_tich_kinh_dich']['tieu_de'])
    bao_cao.append("─"*95)
    bao_cao.append(ket_qua_tong_hop['phan_tich_kinh_dich']['ket_luan'])
    bao_cao.append("")
    bao_cao.append("📄 GIẢI THÍCH CHI TIẾT:")
    bao_cao.append(ket_qua_tong_hop['phan_tich_kinh_dich']['giai_thich_day_du'])
    bao_cao.append("")
    
    # Kết luận tổng hợp
    bao_cao.append(ket_qua_tong_hop['ket_luan_tong_hop'])
    
    return "\n".join(bao_cao)


# Test
if __name__ == "__main__":
    print("=== TEST TỔNG HỢP 3 PHƯƠNG PHÁP ===\n")
    
    # Giả lập dữ liệu
    chu_info = {
        'so': 1,
        'ten': 'Khảm',
        'hanh': 'Thủy',
        'sao': 'Thiên Phụ',
        'cua': 'Sinh',
        'than': 'Thanh Long',
        'can_thien': 'Giáp',
        'can_dia': 'Mậu'
    }
    
    khach_info = {
        'so': 9,
        'ten': 'Ly',
        'hanh': 'Hỏa',
        'sao': 'Thiên Anh',
        'cua': 'Cảnh',
        'than': 'Chu Tước',
        'can_thien': 'Bính',
        'can_dia': 'Canh'
    }
    
    dt_obj = datetime.now()
    
    # Tổng hợp
    ket_qua = tong_hop_3_phuong_phap_cho_chu_de("Kinh Doanh", chu_info, khach_info, dt_obj)
    
    # Tạo báo cáo
    bao_cao = tao_bao_cao_tong_hop_3pp(ket_qua)
    print(bao_cao)
    
    print("\n✅ Test hoàn thành!")
