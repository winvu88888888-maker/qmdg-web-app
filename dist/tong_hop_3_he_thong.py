# -*- coding: utf-8 -*-
"""
TỔNG HỢP 3 HỆ THỐNG DỰ ĐOÁN
Kỳ Môn Độn Giáp + Mai Hoa Dịch Số + Lục Hào Kinh Dịch
"""

from datetime import datetime
from mai_hoa_dich_so import tinh_qua_theo_thoi_gian, giai_qua
from luc_hao_kinh_dich import lap_qua_luc_hao

def tong_hop_3_he_thong(ket_qua_ky_mon, dt_obj, chu_de="Tổng Quát"):
    """
    Tổng hợp kết quả từ 3 hệ thống dự đoán
    
    Args:
        ket_qua_ky_mon: Kết quả phân tích từ Kỳ Môn
        dt_obj: datetime object
        chu_de: Chủ đề cần phân tích
    
    Returns:
        dict: Kết quả tổng hợp từ 3 hệ thống
    """
    
    # 1. Tính Mai Hoa 64 Quẻ
    ket_qua_mai_hoa = tinh_qua_theo_thoi_gian(
        dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour
    )
    giai_thich_mai_hoa = giai_qua(ket_qua_mai_hoa, chu_de)
    
    # 2. Tính Lục Hào Kinh Dịch
    ket_qua_luc_hao = lap_qua_luc_hao(
        dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour, chu_de
    )
    
    # 3. Tính điểm cho từng hệ thống
    diem_ky_mon = tinh_diem_ky_mon(ket_qua_ky_mon)
    diem_mai_hoa = tinh_diem_mai_hoa(ket_qua_mai_hoa)
    diem_luc_hao = tinh_diem_luc_hao(ket_qua_luc_hao)
    
    # 4. Tính điểm trung bình
    diem_trung_binh = (diem_ky_mon + diem_mai_hoa + diem_luc_hao) / 3
    
    # 5. Xác định kết luận chung
    ket_luan_chung = xac_dinh_ket_luan(diem_trung_binh, chu_de)
    
    # 6. Tổng hợp lời khuyên
    loi_khuyen = tong_hop_loi_khuyen(
        ket_qua_ky_mon, ket_qua_mai_hoa, ket_qua_luc_hao, 
        diem_ky_mon, diem_mai_hoa, diem_luc_hao, chu_de
    )
    
    # 7. Dự đoán thời gian
    thoi_gian_ung = du_doan_thoi_gian(
        ket_qua_ky_mon, ket_qua_mai_hoa, ket_qua_luc_hao, dt_obj
    )
    
    return {
        'ky_mon': {
            'ket_qua': ket_qua_ky_mon,
            'diem': diem_ky_mon
        },
        'mai_hoa': {
            'ket_qua': ket_qua_mai_hoa,
            'giai_thich': giai_thich_mai_hoa,
            'diem': diem_mai_hoa
        },
        'luc_hao': {
            'ket_qua': ket_qua_luc_hao,
            'diem': diem_luc_hao
        },
        'tong_hop': {
            'diem_trung_binh': int(diem_trung_binh),
            'ket_luan_chung': ket_luan_chung,
            'loi_khuyen': loi_khuyen,
            'thoi_gian_ung': thoi_gian_ung
        }
    }


def tinh_diem_ky_mon(ket_qua_ky_mon):
    """Tính điểm từ kết quả Kỳ Môn (0-100)"""
    diem = 50  # Điểm cơ bản
    
    # Lấy thông tin từ kết quả
    if not ket_qua_ky_mon or 'tong_hop' not in ket_qua_ky_mon:
        return diem
    
    tong_hop = ket_qua_ky_mon.get('tong_hop', {})
    
    # Phân tích quan hệ Ngũ Hành
    mqh = tong_hop.get('mqh', '')
    if 'sinh' in mqh.lower():
        if 'Khách sinh Chủ' in mqh:
            diem += 30  # Rất tốt
        else:
            diem -= 15  # Chủ sinh Khách - hao tổn
    elif 'khắc' in mqh.lower():
        if 'Chủ khắc Khách' in mqh:
            diem += 20  # Tốt
        else:
            diem -= 25  # Khách khắc Chủ - rất xấu
    
    # Phân tích Cửa
    chu_info = ket_qua_ky_mon.get('chu', {})
    if chu_info.get('cua') in ['Sinh', 'Khai', 'Cảnh']:
        diem += 10
    elif chu_info.get('cua') in ['Tử', 'Kinh', 'Thương']:
        diem -= 10
    
    # Phân tích Thần
    if chu_info.get('than') in ['Trực Phù', 'Lục Hợp', 'Thanh Long']:
        diem += 10
    elif chu_info.get('than') in ['Bạch Hổ', 'Huyền Vũ', 'Đằng Xà']:
        diem -= 10
    
    # Giới hạn 0-100
    return max(0, min(100, diem))


def tinh_diem_mai_hoa(ket_qua_mai_hoa):
    """Tính điểm từ kết quả Mai Hoa (0-100)"""
    diem = 50  # Điểm cơ bản
    
    if not ket_qua_mai_hoa:
        return diem
    
    # Phân tích Ngũ Hành của quẻ
    ban_qua = ket_qua_mai_hoa.get('ban_qua', {})
    qua_bien = ket_qua_mai_hoa.get('qua_bien', {})
    
    ban_hanh = ban_qua.get('hanh', '')
    bien_hanh = qua_bien.get('hanh', '')
    
    # Quan hệ sinh khắc
    if ban_hanh and bien_hanh:
        if sinh_khac_mai_hoa(ban_hanh, bien_hanh) == 'sinh':
            diem += 20  # Tốt
        elif sinh_khac_mai_hoa(ban_hanh, bien_hanh) == 'khac':
            diem -= 15  # Không tốt
        else:
            diem += 5  # Bình thường
    
    # Hào động
    hao_dong = ket_qua_mai_hoa.get('hao_dong', 0)
    if hao_dong in [1, 5, 6]:  # Hào tốt
        diem += 10
    elif hao_dong in [2, 4]:  # Hào trung bình
        diem += 5
    
    return max(0, min(100, diem))


def tinh_diem_luc_hao(ket_qua_luc_hao):
    """Tính điểm từ kết quả Lục Hào (0-100)"""
    diem = 50  # Điểm cơ bản
    
    if not ket_qua_luc_hao:
        return diem
    
    chinh_quai = ket_qua_luc_hao.get('chinh_quai', {})
    bien_quai = ket_qua_luc_hao.get('bien_quai', {})
    
    # Phân tích Ngũ Hành
    chinh_hanh = chinh_quai.get('bat_quai_thuong', {}).get('hanh', '')
    bien_hanh = bien_quai.get('bat_quai_thuong', {}).get('hanh', '')
    
    if chinh_hanh and bien_hanh:
        if sinh_khac_mai_hoa(chinh_hanh, bien_hanh) == 'sinh':
            diem += 25  # Rất tốt
        elif sinh_khac_mai_hoa(chinh_hanh, bien_hanh) == 'khac':
            diem -= 20  # Không tốt
        else:
            diem += 10  # Bình hòa
    
    # Hào động
    dong_hao = chinh_quai.get('dong_hao', [0])[0]
    if dong_hao in [5, 6]:  # Hào cao - tốt
        diem += 15
    elif dong_hao in [1, 2]:  # Hào thấp
        diem += 5
    
    return max(0, min(100, diem))


def sinh_khac_mai_hoa(hanh1, hanh2):
    """Xác định quan hệ sinh khắc"""
    sinh = {
        "Kim": "Thủy", "Thủy": "Mộc", "Mộc": "Hỏa",
        "Hỏa": "Thổ", "Thổ": "Kim"
    }
    khac = {
        "Kim": "Mộc", "Mộc": "Thổ", "Thổ": "Thủy",
        "Thủy": "Hỏa", "Hỏa": "Kim"
    }
    
    if sinh.get(hanh1) == hanh2:
        return 'sinh'
    elif khac.get(hanh1) == hanh2:
        return 'khac'
    else:
        return 'binh_hoa'


def xac_dinh_ket_luan(diem, chu_de):
    """Xác định kết luận dựa trên điểm số"""
    if diem >= 75:
        return f"🌟 RẤT THUẬN LỢI - Cả 3 phương pháp đều chỉ ra tín hiệu cực kỳ tích cực cho {chu_de}. Đây là thời điểm vàng để hành động!"
    elif diem >= 60:
        return f"✅ THUẬN LỢI - Đa số phương pháp cho thấy xu hướng tốt cho {chu_de}. Có cơ hội thành công cao."
    elif diem >= 45:
        return f"⚖️ TRUNG BÌNH - Tình hình {chu_de} ở mức cân bằng. Cần thận trọng và chuẩn bị kỹ."
    elif diem >= 30:
        return f"⚠️ CẦN THẬN TRỌNG - Có nhiều rủi ro cho {chu_de}. Nên cân nhắc kỹ trước khi quyết định."
    else:
        return f"🚫 KHÔNG THUẬN LỢI - Cả 3 phương pháp đều cảnh báo về {chu_de}. Nên hoãn lại hoặc tìm phương án khác."


def tong_hop_loi_khuyen(ky_mon, mai_hoa, luc_hao, diem_km, diem_mh, diem_lh, chu_de):
    """Tổng hợp lời khuyên từ 3 hệ thống"""
    loi_khuyen = []
    
    # Phân tích điểm số
    diem_cao_nhat = max(diem_km, diem_mh, diem_lh)
    diem_thap_nhat = min(diem_km, diem_mh, diem_lh)
    
    # Lời khuyên chung
    if diem_cao_nhat - diem_thap_nhat > 30:
        loi_khuyen.append("⚡ Có sự bất đồng lớn giữa các phương pháp. Cần quan sát thêm các dấu hiệu thực tế.")
    
    # Từ Kỳ Môn
    if diem_km >= 60:
        loi_khuyen.append(f"🔮 Kỳ Môn ({diem_km}/100): Thời điểm và không gian thuận lợi. Hãy tận dụng!")
    elif diem_km <= 40:
        loi_khuyen.append(f"🔮 Kỳ Môn ({diem_km}/100): Cần cẩn thận với quan hệ Chủ-Khách. Tìm người trung gian hỗ trợ.")
    
    # Từ Mai Hoa
    if diem_mh >= 60:
        loi_khuyen.append(f"📖 Mai Hoa ({diem_mh}/100): Xu hướng biến hóa tích cực. Hãy kiên trì!")
    elif diem_mh <= 40:
        loi_khuyen.append(f"📖 Mai Hoa ({diem_mh}/100): Cần chờ đợi thời cơ tốt hơn.")
    
    # Từ Lục Hào
    if diem_lh >= 60:
        loi_khuyen.append(f"☯️ Lục Hào ({diem_lh}/100): 3 quẻ đều hỗ trợ. Hành động với tự tin!")
    elif diem_lh <= 40:
        loi_khuyen.append(f"☯️ Lục Hào ({diem_lh}/100): Hào động cảnh báo rủi ro. Cần thận trọng.")
    
    # Lời khuyên cụ thể theo chủ đề
    loi_khuyen.extend(loi_khuyen_theo_chu_de(chu_de, (diem_km + diem_mh + diem_lh) / 3))
    
    return loi_khuyen


def loi_khuyen_theo_chu_de(chu_de, diem_tb):
    """Lời khuyên cụ thể theo từng chủ đề"""
    loi_khuyen = []
    
    if chu_de == "Kinh Doanh":
        if diem_tb >= 60:
            loi_khuyen.append("💼 Đây là thời điểm tốt để mở rộng kinh doanh hoặc ký kết hợp đồng lớn.")
        else:
            loi_khuyen.append("💼 Nên tập trung củng cố nội lực, tránh đầu tư mạo hiểm.")
    
    elif chu_de == "Hôn Nhân":
        if diem_tb >= 60:
            loi_khuyen.append("💑 Mối quan hệ đang phát triển tốt. Hãy dành thời gian chất lượng cho nhau.")
        else:
            loi_khuyen.append("💑 Cần giao tiếp cởi mở hơn để giải quyết hiểu lầm.")
    
    elif chu_de == "Sức Khỏe":
        if diem_tb >= 60:
            loi_khuyen.append("🏥 Sức khỏe đang phục hồi tốt. Duy trì chế độ điều trị.")
        else:
            loi_khuyen.append("🏥 Cần kiểm tra sức khỏe kỹ hơn và tìm phương pháp điều trị phù hợp.")
    
    elif chu_de == "Công Việc":
        if diem_tb >= 60:
            loi_khuyen.append("💼 Cơ hội thăng tiến đang đến gần. Hãy thể hiện năng lực!")
        else:
            loi_khuyen.append("💼 Tập trung hoàn thành tốt công việc hiện tại, tránh xung đột.")
    
    return loi_khuyen


def du_doan_thoi_gian(ky_mon, mai_hoa, luc_hao, dt_obj):
    """Dự đoán thời gian ứng nghiệm"""
    # Phân tích từ các yếu tố
    thoi_gian = []
    
    # Từ Kỳ Môn - dựa vào Cửa
    chu_info = ky_mon.get('chu', {}) if ky_mon else {}
    cua = chu_info.get('cua', '')
    
    if cua in ['Sinh', 'Khai']:
        thoi_gian.append("Trong vòng 7-15 ngày")
    elif cua in ['Cảnh', 'Tử']:
        thoi_gian.append("Trong vòng 1-3 tháng")
    else:
        thoi_gian.append("Trong vòng 30-60 ngày")
    
    # Từ Mai Hoa - dựa vào hào động
    hao_dong = mai_hoa.get('hao_dong', 3) if mai_hoa else 3
    if hao_dong <= 2:
        thoi_gian.append("Sớm (1-2 tuần)")
    elif hao_dong <= 4:
        thoi_gian.append("Trung bình (2-4 tuần)")
    else:
        thoi_gian.append("Muộn (1-2 tháng)")
    
    # Tổng hợp
    return f"⏰ Thời gian ứng nghiệm dự kiến: {', '.join(set(thoi_gian))}"


def tao_bao_cao_tong_hop(ket_qua_3_he_thong, chu_de):
    """Tạo báo cáo tổng hợp dễ đọc"""
    bao_cao = []
    
    bao_cao.append("═" * 80)
    bao_cao.append("📊 BÁO CÁO TỔNG HỢP 3 PHƯƠNG PHÁP DỰ ĐOÁN")
    bao_cao.append("═" * 80)
    bao_cao.append(f"Chủ đề: {chu_de}")
    bao_cao.append("")
    
    # Điểm số từng hệ thống
    bao_cao.append("📈 ĐIỂM SỐ TỪNG PHƯƠNG PHÁP:")
    bao_cao.append("─" * 80)
    bao_cao.append(f"  🔮 Kỳ Môn Độn Giáp:     {ket_qua_3_he_thong['ky_mon']['diem']}/100")
    bao_cao.append(f"  📖 Mai Hoa 64 Quẻ:      {ket_qua_3_he_thong['mai_hoa']['diem']}/100")
    bao_cao.append(f"  ☯️  Lục Hào Kinh Dịch:   {ket_qua_3_he_thong['luc_hao']['diem']}/100")
    bao_cao.append("")
    bao_cao.append(f"  ⭐ TỔNG HỢP:            {ket_qua_3_he_thong['tong_hop']['diem_trung_binh']}/100")
    bao_cao.append("")
    
    # Kết luận
    bao_cao.append("🎯 KẾT LUẬN:")
    bao_cao.append("─" * 80)
    bao_cao.append(f"  {ket_qua_3_he_thong['tong_hop']['ket_luan_chung']}")
    bao_cao.append("")
    
    # Lời khuyên
    bao_cao.append("💡 LỜI KHUYÊN:")
    bao_cao.append("─" * 80)
    for i, lk in enumerate(ket_qua_3_he_thong['tong_hop']['loi_khuyen'], 1):
        bao_cao.append(f"  {i}. {lk}")
    bao_cao.append("")
    
    # Thời gian
    bao_cao.append(f"  {ket_qua_3_he_thong['tong_hop']['thoi_gian_ung']}")
    bao_cao.append("")
    bao_cao.append("═" * 80)
    
    return "\n".join(bao_cao)


# Test
if __name__ == "__main__":
    print("=== TEST TỔNG HỢP 3 HỆ THỐNG ===\n")
    
    # Giả lập kết quả Kỳ Môn
    ket_qua_ky_mon = {
        'chu': {'cua': 'Sinh', 'than': 'Thanh Long', 'hanh': 'Mộc'},
        'khach': {'hanh': 'Thủy'},
        'tong_hop': {'mqh': 'Thủy sinh Mộc (Khách sinh Chủ)'}
    }
    
    dt_obj = datetime(2026, 1, 11, 23, 30)
    
    ket_qua = tong_hop_3_he_thong(ket_qua_ky_mon, dt_obj, "Kinh Doanh")
    
    bao_cao = tao_bao_cao_tong_hop(ket_qua, "Kinh Doanh")
    print(bao_cao)
    
    print("\n✅ Test hoàn thành!")
