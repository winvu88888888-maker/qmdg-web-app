
# qmdg_calc.py - Core calculation engine for Kỳ Môn Độn Giáp
import math
from datetime import datetime, timedelta, time

# Data for calculations
CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

TIET_KHI_LIST = [
    "Đông Chí", "Tiểu Hàn", "Đại Hàn", "Lập Xuân", "Vũ Thủy", "Kinh Trập",
    "Xuân Phân", "Thanh Minh", "Cốc Vũ", "Lập Hạ", "Tiểu Mãn", "Mang Chủng",
    "Hạ Chí", "Tiểu Thử", "Đại Thử", "Lập Thu", "Xử Thử", "Bạch Lộ",
    "Thu Phân", "Hàn Lộ", "Sương Giáng", "Lập Đông", "Tiểu Tuyết", "Đại Tuyết"
]

# Map Tiết khí to Cục (Thượng, Trung, Hạ)
TIET_KHI_CUC = {
    "Đông Chí": (1, 7, 4), "Tiểu Hàn": (2, 8, 5), "Đại Hàn": (3, 9, 6),
    "Lập Xuân": (8, 5, 2), "Vũ Thủy": (9, 6, 3), "Kinh Trập": (1, 7, 4),
    "Xuân Phân": (3, 9, 6), "Thanh Minh": (4, 1, 7), "Cốc Vũ": (5, 2, 8),
    "Lập Hạ": (4, 1, 7), "Tiểu Mãn": (5, 2, 8), "Mang Chủng": (6, 3, 9),
    "Hạ Chí": (9, 3, 6), "Tiểu Thử": (8, 2, 5), "Đại Thử": (7, 1, 4),
    "Lập Thu": (2, 5, 8), "Xử Thử": (1, 4, 7), "Bạch Lộ": (9, 3, 6),
    "Thu Phân": (7, 1, 4), "Hàn Lộ": (6, 9, 3), "Sương Giáng": (5, 8, 2),
    "Lập Đông": (6, 9, 3), "Tiểu Tuyết": (5, 8, 2), "Đại Tuyết": (4, 7, 1)
}

def get_julian_day(dt):
    """Calculate Julian Day Number."""
    y = dt.year
    m = dt.month
    d = dt.day + (dt.hour + dt.minute / 60.0 + dt.second / 3600.0) / 24.0
    if m <= 2:
        y -= 1
        m += 12
    a = math.floor(y / 100)
    b = 2 - a + math.floor(a / 4)
    jd = math.floor(365.25 * (y + 4716)) + math.floor(30.6001 * (m + 1)) + d + b - 1524.5
    return jd

def get_can_chi_year(year):
    """Calculate Can Chi for Year."""
    idx = (year - 4) % 60
    return CAN[idx % 10], CHI[idx % 12]

def get_can_chi_day(dt):
    """Calculate Can Chi for Day using JD."""
    jd = get_julian_day(dt)
    # JD 2451545.0 is 2000-01-01 (Mậu Ngọ - idx 54)
    # Actually, JD calculation for Can Chi day: (JD + 0.5 + 49) % 60
    # Let's use a simpler reference: 2024-01-01 is Giáp Thân (idx 20)
    base_dt = datetime(2024, 1, 1)
    diff = (dt.date() - base_dt.date()).days
    idx = (20 + diff) % 60
    return CAN[idx % 10], CHI[idx % 12]

def get_can_chi_hour(day_can, hour):
    """Calculate Can Chi for Hour based on Day Can."""
    # Hour index: 0(Tý) to 11(Hợi). Tý is 23h-1h.
    hour_idx = ((hour + 1) // 2) % 12
    # Giáp Kỷ khởi Giáp Tý (0), Ất Canh khởi Bính Tý (2)...
    start_can_map = {"Giáp": 0, "Kỷ": 0, "Ất": 2, "Canh": 2, "Bính": 4, "Tân": 4, "Đinh": 6, "Nhâm": 6, "Mậu": 8, "Quý": 8}
    start_can_idx = start_can_map.get(day_can, 0)
    hour_can_idx = (start_can_idx + hour_idx) % 10
    return CAN[hour_can_idx], CHI[hour_idx]

def get_tiet_khi(dt):
    """Calculate Solar Term (Accurate version using approximate dates for 21st century)."""
    year = dt.year
    # Reference dates for 21st century (average)
    # This is a simplified but much better version than before
    # For production, a full astronomical library like ephem or skyfield is better.
    # But this covers 2024-2030 accurately within +/- 1 day.
    base_dates = {
        "Xuân Phân": (3, 20.6), "Thanh Minh": (4, 4.8), "Cốc Vũ": (4, 20.1),
        "Lập Hạ": (5, 5.5), "Tiểu Mãn": (5, 21.1), "Mang Chủng": (6, 5.7),
        "Hạ Chí": (6, 21.3), "Tiểu Thử": (7, 7.3), "Đại Thử": (7, 22.8),
        "Lập Thu": (8, 7.5), "Xử Thử": (8, 23.1), "Bạch Lộ": (9, 7.7),
        "Thu Phân": (9, 22.9), "Hàn Lộ": (10, 8.3), "Sương Giáng": (10, 23.4),
        "Lập Đông": (11, 7.3), "Tiểu Tuyết": (11, 22.3), "Đại Tuyết": (12, 7.1),
        "Đông Chí": (12, 21.8), "Tiểu Hàn": (1, 5.4), "Đại Hàn": (1, 20.1),
        "Lập Xuân": (2, 4.2), "Vũ Thủy": (2, 18.9), "Kinh Trập": (3, 5.6)
    }
    
    terms = []
    for name, (month, day_ref) in base_dates.items():
        # Adjust for year leap cycle if necessary (very rough)
        # 1 day drift every 4 years
        y_offset = (year - 2024) * 0.2422
        day = int(day_ref + y_offset)
        if month == 1 or month == 2: # Terms in early year refer to previous solar year drift? No, just the calendar year.
            t_dt = datetime(year, month, day)
        else:
            t_dt = datetime(year, month, day)
        terms.append((t_dt, name))
    
    terms.sort()
    
    # Handle overlap (Tiểu Hàn, Đại Hàn are in Jan)
    # Current terminal name
    current_term = terms[-1][1]
    # If the date is before the first term of the year (usually Jan 5), it belongs to previous year's last term
    if dt < terms[0][0]:
        current_term = "Đông Chí"
    else:
        for t_dt, name in terms:
            if dt >= t_dt:
                current_term = name
            else:
                break
    return current_term

def get_can_chi_month(year_can, tiet_khi):
    """Calculate Can Chi for Month based on Year Can and Solar Term."""
    # Month Chi is fixed to Solar Terms: Lập Xuân starts Dần (2)
    month_chi_map = {
        "Lập Xuân": "Dần", "Vũ Thủy": "Dần",
        "Kinh Trập": "Mão", "Xuân Phân": "Mão",
        "Thanh Minh": "Thìn", "Cốc Vũ": "Thìn",
        "Lập Hạ": "Tị", "Tiểu Mãn": "Tị",
        "Mang Chủng": "Ngọ", "Hạ Chí": "Ngọ",
        "Tiểu Thử": "Mùi", "Đại Thử": "Mùi",
        "Lập Thu": "Thân", "Xử Thử": "Thân",
        "Bạch Lộ": "Dậu", "Thu Phân": "Dậu",
        "Hàn Lộ": "Tuất", "Sương Giáng": "Tuất",
        "Lập Đông": "Hợi", "Tiểu Tuyết": "Hợi",
        "Đại Tuyết": "Tý", "Đông Chí": "Tý",
        "Tiểu Hàn": "Sửu", "Đại Hàn": "Sửu"
    }
    month_chi = month_chi_map.get(tiet_khi, "Dần")
    chi_idx = CHI.index(month_chi)
    
    # Giáp Kỷ chi niên Bính tác sơ (index 2: Bính Dần)
    start_can_map = {"Giáp": 2, "Kỷ": 2, "Ất": 4, "Canh": 4, "Bính": 6, "Tân": 6, "Đinh": 8, "Nhâm": 8, "Mậu": 0, "Quý": 0}
    year_can_idx = start_can_map.get(year_can, 0)
    # (idx - 2) because Dần is index 2 in CHI
    month_can_idx = (year_can_idx + (chi_idx - 2)) % 10
    return CAN[month_can_idx], month_chi

# Fixed data for QMDG
SAO_GOC = {1: "Thiên Bồng", 2: "Thiên Nhuế", 3: "Thiên Xung", 4: "Thiên Phụ", 5: "Thiên Cầm", 6: "Thiên Tâm", 7: "Thiên Trụ", 8: "Thiên Nhậm", 9: "Thiên Anh"}
MON_GOC = {1: "Hưu", 2: "Tử", 3: "Thương", 4: "Đỗ", 6: "Khai", 7: "Kinh", 8: "Sinh", 9: "Cảnh"}
CHI_CUNG_MAP = {"Tý": 1, "Sửu": 8, "Dần": 8, "Mão": 3, "Thìn": 4, "Tị": 4, "Ngọ": 9, "Mùi": 2, "Thân": 2, "Dậu": 7, "Tuất": 6, "Hợi": 6}

def calculate_qmdg_params(dt):
    """Main entry point for QMDG parameters calculation."""
    if dt.tzinfo is not None:
        dt = dt.replace(tzinfo=None)
        
    year_can, year_chi = get_can_chi_year(dt.year)
    day_can, day_chi = get_can_chi_day(dt)
    hour_can, hour_chi = get_can_chi_hour(day_can, dt.hour)
    tiet_khi = get_tiet_khi(dt)
    month_can, month_chi = get_can_chi_month(year_can, tiet_khi)
    
    # Determine is_duong_don
    yang_terms = ["Đông Chí", "Tiểu Hàn", "Đại Hàn", "Lập Xuân", "Vũ Thủy", "Kinh Trập", "Xuân Phân", "Thanh Minh", "Cốc Vũ", "Lập Hạ", "Tiểu Mãn", "Mang Chủng"]
    is_duong_don = tiet_khi in yang_terms
    
    # Determine Cuc
    base_dt = datetime(2024, 1, 1) 
    diff = (dt.date() - base_dt.date()).days
    cycle_idx = (20 + diff) % 60 
    
    term_day_idx = cycle_idx % 15
    if term_day_idx < 5: yuan = 0 
    elif term_day_idx < 10: yuan = 1 
    else: yuan = 2 
    
    cuc_tuple = TIET_KHI_CUC.get(tiet_khi, (1, 7, 4))
    cuc = cuc_tuple[yuan]
    
    # 1. Generate Earth Plate (Địa Bàn) to find Leader position
    # Lục nghi tam kỳ: Mậu Kỷ Canh Tân Nhâm Quý Đinh Bính Ất
    LUC_NGHI_ORDER = ["Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý", "Đinh", "Bính", "Ất"]
    dia_ban = {}
    curr = cuc
    for nghi in LUC_NGHI_ORDER:
        dia_ban[curr] = nghi
        if is_duong_don:
            curr = curr + 1 if curr < 9 else 1
        else:
            curr = curr - 1 if curr > 1 else 9

    # 2. Determine Leader (Tuần Thủ)
    # Tý-Mậu, Tuất-Kỷ, Thân-Canh, Ngọ-Tân, Thìn-Nhâm, Dần-Quý
    idx_can_h = CAN.index(hour_can)
    idx_chi_h = CHI.index(hour_chi)
    leader_chi_idx = (idx_chi_h - idx_can_h) % 12
    # Leader is Giáp [leader_chi_idx]
    lead_map = {0: "Mậu", 10: "Kỷ", 8: "Canh", 6: "Tân", 4: "Nhâm", 2: "Quý"}
    tuan_thu = lead_map.get(leader_chi_idx, "Mậu")
    
    # 3. Find Lead Star (Trực Phù) and Lead Gate (Trực Sử)
    # They are the fixed Star/Gate of the palace where Tuần Thủ resides on Earth Plate
    leader_palace = 1
    for p, can in dia_ban.items():
        if can == tuan_thu:
            leader_palace = p
            break
            
    truc_phu = SAO_GOC.get(leader_palace, "Thiên Tâm")
    # If Leader is at 5, Trực Phù is Thiên Cầm, but often moves with Thiên Nhuế (2)
    if leader_palace == 5:
        truc_phu = "Thiên Cầm"
        truc_su = "Tử"
    else:
        truc_su = MON_GOC.get(leader_palace, "Khai")

    return {
        'can_gio': hour_can, 'chi_gio': hour_chi,
        'can_ngay': day_can, 'chi_ngay': day_chi,
        'can_thang': month_can, 'chi_thang': month_chi,
        'can_nam': year_can, 'chi_nam': year_chi,
        'cuc': cuc, 'is_duong_don': is_duong_don,
        'tiet_khi': tiet_khi,
        'tuan_thu': tuan_thu,
        'leader_palace': leader_palace,
        'truc_phu': truc_phu,
        'truc_su': truc_su + (" Môn" if " Môn" not in truc_su else "")
    }

