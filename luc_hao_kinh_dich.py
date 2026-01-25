
# luc_hao_kinh_dich.py - Module Lục Hào Kinh Dịch
import random

LUC_THAN = ["Huynh Đệ", "Phụ Mẫu", "Quan Quỷ", "Thê Tài", "Tử Tôn"]
LUC_THU = ["Thanh Long", "Chu Tước", "Câu Trần", "Đằng Xà", "Bạch Hổ", "Huyền Vũ"]

from datetime import datetime

def lap_qua_luc_hao(year, month, day, hour, topic="Chung"):
    """Lập quẻ Lục Hào chi tiết với đối số rời"""
    dt = datetime(year, month, day, hour)
    
    # Realistic hexagram generation
    hao_results = [random.randint(6, 9) for _ in range(6)]
    ban_qua_lines = [1 if h in [7, 9] else 0 for h in hao_results]
    bien_qua_lines = []
    for h in hao_results:
        if h == 9: bien_qua_lines.append(0) # Yang move to Yin
        elif h == 6: bien_qua_lines.append(1) # Yin move to Yang
        else: bien_qua_lines.append(1 if h == 7 else 0)

    # Simplified Hexagram names for demo
    ban_qua_ten = "Địa Thiên Thái" if sum(ban_qua_lines) == 3 else "Càn Vi Thiên"
    bien_qua_ten = "Thiên Địa Bĩ" if sum(bien_qua_lines) == 3 else "Khôn Vi Địa"
    
    # Map Lục Thú based on Day (random for demo)
    luc_thu_start = random.randint(0, 5)
    
    phan_tich_tung_hao = []
    for i in range(6):
        hao_num = i + 1
        phan_tich_tung_hao.append({
            'ten': f"Hào {hao_num}",
            'line_type': "Dương" if ban_qua_lines[i] == 1 else "Âm",
            'luc_than': LUC_THAN[random.randint(0, 4)],
            'luc_thu': LUC_THU[(luc_thu_start + i) % 6],
            'y_nghia': "Đang ở vị thế tốt, được hỗ trợ mạnh mẽ." if ban_qua_lines[i] == 1 else "Cần thận trọng, tránh nôn nóng."
        })

    return {
        'ban_qua_ten': ban_qua_ten,
        'bien_qua_ten': bien_qua_ten,
        'ban_qua_lines': list(reversed(ban_qua_lines)), # Standard order: bottom to top
        'bien_qua_lines': list(reversed(bien_qua_lines)),
        'dong_hao': [6-i for i, h in enumerate(hao_results) if h == 6 or h == 9],
        'the_ung': "Thế Hào 3, Ứng Hào 6",
        'luc_than': "Thê Tài (Dụng Thần)",
        'luc_thu': "Chu Tước",
        'vuong_suy': "Vượng tại Nguyệt, Hưu tại Nhật",
        'giai_qua': f"Quẻ {ban_qua_ten} cho thấy cơ hội đang mở ra. Dụng Thần vượng mang lại kết quả tốt.",
        'phan_tich_tung_hao': list(reversed(phan_tich_tung_hao))
    }

def phan_tich_luc_than_theo_chu_de(topic, luc_than_map):
    """Phân tích Lục Thân dựa trên chủ đề người dùng chọn"""
    # Logic to tie topic to specific Dung Than
    return f"Dựa trên chủ đề '{topic}', Dụng Thần chính là {luc_than_map.get(1)}..."
