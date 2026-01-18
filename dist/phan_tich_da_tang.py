# -*- coding: utf-8 -*-
"""
MODULE PHÂN TÍCH ĐA TẦNG
Hệ thống phân tích chuyên sâu với Dụng Thần làm trung tâm
"""

from database_tuong_tac import *
from datetime import datetime

# ============================================================================
# PHẦN 1: LOGIC CHỌN DỤNG THẦN VÀ LỤC THÂN
# ============================================================================

def chon_dung_than_theo_chu_de(chu_de):
    """
    Chọn Dụng Thần phù hợp nhất cho chủ đề
    
    Args:
        chu_de: Tên chủ đề cần phân tích
    
    Returns:
        dict: {
            'ten': Tên Dụng Thần,
            'dung_than_phu': List Dụng Thần phụ,
            'trong_so': Trọng số
        }
    """
    # Tìm trong database
    for key, value in QUY_TAC_CHON_DUNG_THAN.items():
        if key.lower() in chu_de.lower():
            return {
                'ten': value['dung_than_chinh'],
                'dung_than_phu': value['dung_than_phu'],
                'trong_so': value['trong_so'],
                'cung_uu_tien': value['cung_uu_tien'],
                'ngu_hanh_tot': value['ngu_hanh_tot']
            }
    
    # Mặc định
    return {
        'ten': 'Thiên Phụ',
        'dung_than_phu': ['Thiên Tâm'],
        'trong_so': 1.0,
        'cung_uu_tien': [],
        'ngu_hanh_tot': []
    }


def xac_dinh_luc_than(ngu_hanh_chu_the, doi_tuong):
    """
    Xác định Lục Thân dựa trên Ngũ Hành
    
    Args:
        ngu_hanh_chu_the: Ngũ hành của chủ thể (Mộc/Hỏa/Thổ/Kim/Thủy)
        doi_tuong: Đối tượng được chọn (Bản thân/Anh chị em/...)
    
    Returns:
        dict: Thông tin Lục Thân
    """
    # Lấy thông tin cơ bản từ mapping
    if doi_tuong in LUC_THAN_MAPPING:
        luc_than_info = LUC_THAN_MAPPING[doi_tuong].copy()
        luc_than_info['doi_tuong'] = doi_tuong
        return luc_than_info
    
    # Mặc định
    return LUC_THAN_MAPPING["Bản thân"].copy()


def phan_tich_sinh_khac_hop(ngu_hanh_dung_than, ngu_hanh_doi_tuong):
    """
    Phân tích mối quan hệ Sinh/Khắc/Hợp giữa Dụng Thần và đối tượng
    
    Args:
        ngu_hanh_dung_than: Ngũ hành của Dụng Thần
        ngu_hanh_doi_tuong: Ngũ hành của đối tượng
    
    Returns:
        dict: {
            'quan_he': Loại quan hệ,
            'loai': sinh_ta/ta_sinh/khac_ta/ta_khac/cung_hanh,
            'diem': Điểm số (0-100),
            'y_nghia': Ý nghĩa,
            'loi_khuyen': Lời khuyên
        }
    """
    key = (ngu_hanh_dung_than, ngu_hanh_doi_tuong)
    
    if key in SINH_KHAC_MATRIX:
        return SINH_KHAC_MATRIX[key].copy()
    
    # Mặc định nếu không tìm thấy
    return {
        'quan_he': 'Không xác định',
        'loai': 'khong_ro',
        'diem': 50,
        'y_nghia': 'Cần phân tích thêm',
        'loi_khuyen': 'Xem xét kỹ các yếu tố khác'
    }


# ============================================================================
# PHẦN 2: PHÂN TÍCH TƯƠNG TÁC TRONG CUNG
# ============================================================================

def phan_tich_tuong_tac_trong_cung(cung_info, dung_than_info):
    """
    Phân tích cách các yếu tố trong cung tác động lên Dụng Thần
    
    Args:
        cung_info: Dict chứa thông tin cung (sao, môn, thần, ngũ hành...)
        dung_than_info: Dict thông tin Dụng Thần
    
    Returns:
        dict: Kết quả phân tích chi tiết
    """
    ket_qua = {
        'diem_tong': 0,
        'chi_tiet': {},
        'diem_thanh_phan': {}
    }
    
    dung_than_ten = dung_than_info.get('ten', 'Thiên Phụ')
    
    # 1. Phân tích Sao (Cửu Tinh)
    sao = cung_info.get('sao', '')
    if sao == dung_than_ten:
        diem_sao = 100
        y_nghia_sao = f"Dụng Thần {dung_than_ten} chính tại cung - CỰC TỐT"
    else:
        diem_sao = 70
        y_nghia_sao = f"Sao {sao} hỗ trợ gián tiếp"
    
    ket_qua['chi_tiet']['sao'] = {
        'ten': sao,
        'diem': diem_sao,
        'y_nghia': y_nghia_sao
    }
    ket_qua['diem_thanh_phan']['sao'] = diem_sao * TRONG_SO_YEU_TO['sao']
    
    # 2. Phân tích Môn (Bát Môn)
    mon = cung_info.get('mon', '')
    key_sao_mon = (dung_than_ten, mon)
    
    if key_sao_mon in TUONG_TAC_SAO_MON:
        tuong_tac = TUONG_TAC_SAO_MON[key_sao_mon]
        diem_mon = tuong_tac['diem']
        y_nghia_mon = tuong_tac['y_nghia']
    else:
        diem_mon = 60
        y_nghia_mon = f"Môn {mon} - ảnh hưởng trung bình"
    
    ket_qua['chi_tiet']['mon'] = {
        'ten': mon,
        'diem': diem_mon,
        'y_nghia': y_nghia_mon
    }
    ket_qua['diem_thanh_phan']['mon'] = diem_mon * TRONG_SO_YEU_TO['mon']
    
    # 3. Phân tích Thần (Bát Thần)
    than = cung_info.get('than', '')
    diem_than = 70  # Mặc định
    y_nghia_than = f"Thần {than}"
    
    ket_qua['chi_tiet']['than'] = {
        'ten': than,
        'diem': diem_than,
        'y_nghia': y_nghia_than
    }
    ket_qua['diem_thanh_phan']['than'] = diem_than * TRONG_SO_YEU_TO['than']
    
    # 4. Phân tích Ngũ Hành
    ngu_hanh = cung_info.get('ngu_hanh', 'Thổ')
    diem_ngu_hanh = 75
    y_nghia_ngu_hanh = f"Ngũ hành {ngu_hanh}"
    
    ket_qua['chi_tiet']['ngu_hanh'] = {
        'ten': ngu_hanh,
        'diem': diem_ngu_hanh,
        'y_nghia': y_nghia_ngu_hanh
    }
    ket_qua['diem_thanh_phan']['ngu_hanh'] = diem_ngu_hanh * TRONG_SO_YEU_TO['ngu_hanh']
    
    # 5. Dụng Thần (trọng số cao nhất)
    diem_dung_than = diem_sao  # Dựa vào sao
    ket_qua['diem_thanh_phan']['dung_than'] = diem_dung_than * TRONG_SO_YEU_TO['dung_than']
    
    # Tính tổng điểm
    ket_qua['diem_tong'] = sum(ket_qua['diem_thanh_phan'].values())
    
    return ket_qua


# ============================================================================
# PHẦN 3: PHÂN TÍCH TƯƠNG TÁC GIỮA CÁC CUNG
# ============================================================================

def phan_tich_tuong_tac_giua_cac_cung(cung_chu, cung_khach, cac_cung_lien_quan=None):
    """
    Phân tích mối quan hệ giữa cung chủ và cung khách
    
    Args:
        cung_chu: Dict thông tin cung chủ
        cung_khach: Dict thông tin cung khách
        cac_cung_lien_quan: List các cung liên quan khác
    
    Returns:
        dict: Kết quả phân tích
    """
    ket_qua = {
        'diem_tong': 0,
        'quan_he_ngu_hanh': {},
        'uu_the': '',
        'y_nghia': ''
    }
    
    # Phân tích Ngũ Hành giữa 2 cung
    ngu_hanh_chu = cung_chu.get('ngu_hanh', 'Thổ')
    ngu_hanh_khach = cung_khach.get('ngu_hanh', 'Thổ')
    
    sinh_khac = phan_tich_sinh_khac_hop(ngu_hanh_chu, ngu_hanh_khach)
    ket_qua['quan_he_ngu_hanh'] = sinh_khac
    
    # Xác định ưu thế
    if sinh_khac['loai'] == 'ta_khac':
        ket_qua['uu_the'] = 'CHỦ'
        ket_qua['diem_tong'] = sinh_khac['diem']
        ket_qua['y_nghia'] = f"Chủ khắc Khách - {sinh_khac['y_nghia']}"
    elif sinh_khac['loai'] == 'sinh_ta':
        ket_qua['uu_the'] = 'CHỦ'
        ket_qua['diem_tong'] = sinh_khac['diem']
        ket_qua['y_nghia'] = f"Khách sinh Chủ - {sinh_khac['y_nghia']}"
    elif sinh_khac['loai'] == 'khac_ta':
        ket_qua['uu_the'] = 'KHÁCH'
        ket_qua['diem_tong'] = 100 - sinh_khac['diem']
        ket_qua['y_nghia'] = f"Khách khắc Chủ - {sinh_khac['y_nghia']}"
    elif sinh_khac['loai'] == 'ta_sinh':
        ket_qua['uu_the'] = 'KHÁCH'
        ket_qua['diem_tong'] = 100 - sinh_khac['diem']
        ket_qua['y_nghia'] = f"Chủ sinh Khách - {sinh_khac['y_nghia']}"
    else:  # cung_hanh
        ket_qua['uu_the'] = 'NGANG BẰNG'
        ket_qua['diem_tong'] = sinh_khac['diem']
        ket_qua['y_nghia'] = f"Ngang hàng - {sinh_khac['y_nghia']}"
    
    return ket_qua


# ============================================================================
# PHẦN 4: PHÂN TÍCH YẾU TỐ THỜI GIAN
# ============================================================================

def phan_tich_yeu_to_thoi_gian(dt_obj, dung_than_info, cung_info):
    """
    Phân tích ảnh hưởng của thời gian (mùa, tháng, giờ)
    
    Args:
        dt_obj: Datetime object
        dung_than_info: Dict thông tin Dụng Thần
        cung_info: Dict thông tin cung
    
    Returns:
        dict: Kết quả phân tích
    """
    ket_qua = {
        'diem_tong': 70,  # Điểm mặc định
        'he_so_mua': 1.0,
        'mua': '',
        'y_nghia': ''
    }
    
    # Xác định mùa
    thang = dt_obj.month
    if thang in [1, 2, 3]:
        mua = "Xuân"
    elif thang in [4, 5, 6]:
        mua = "Hạ"
    elif thang in [7, 8, 9]:
        mua = "Thu"
    else:
        mua = "Đông"
    
    ket_qua['mua'] = mua
    
    # Lấy Ngũ Hành của cung
    ngu_hanh = cung_info.get('ngu_hanh', 'Thổ')
    
    # Tính hệ số theo mùa
    if mua in ANH_HUONG_MUA and ngu_hanh in ANH_HUONG_MUA[mua]:
        he_so = ANH_HUONG_MUA[mua][ngu_hanh]
        ket_qua['he_so_mua'] = he_so
        
        if he_so >= 1.3:
            trang_thai = "VƯỢNG"
            ket_qua['diem_tong'] = 90
        elif he_so >= 1.1:
            trang_thai = "TƯỚNG"
            ket_qua['diem_tong'] = 80
        elif he_so >= 0.9:
            trang_thai = "HƯU"
            ket_qua['diem_tong'] = 70
        elif he_so >= 0.7:
            trang_thai = "TÙ"
            ket_qua['diem_tong'] = 50
        else:
            trang_thai = "TỬ"
            ket_qua['diem_tong'] = 30
        
        ket_qua['y_nghia'] = f"Mùa {mua}, {ngu_hanh} {trang_thai} (hệ số {he_so})"
    
    return ket_qua


# ============================================================================
# PHẦN 5: TỔNG HỢP ĐIỂM SỐ
# ============================================================================

def tinh_diem_tong_hop(phan_tich_chu, phan_tich_khach, tuong_tac_giua_cung, 
                       anh_huong_thoi_gian, sinh_khac_luc_than=None):
    """
    Tính điểm tổng hợp với trọng số
    
    Args:
        phan_tich_chu: Kết quả phân tích trong cung Chủ
        phan_tich_khach: Kết quả phân tích trong cung Khách
        tuong_tac_giua_cung: Kết quả phân tích giữa các cung
        anh_huong_thoi_gian: Kết quả phân tích thời gian
        sinh_khac_luc_than: Kết quả phân tích Lục Thân (optional)
    
    Returns:
        dict: Điểm tổng hợp và kết luận
    """
    # Điểm trong cung (50%)
    diem_trong_cung_chu = phan_tich_chu['diem_tong']
    diem_trong_cung_khach = phan_tich_khach['diem_tong']
    diem_trong_cung = (diem_trong_cung_chu - diem_trong_cung_khach) / 2 + 50
    
    # Điểm giữa các cung (35%)
    diem_giua_cung = tuong_tac_giua_cung['diem_tong']
    
    # Điểm thời gian (15%)
    diem_thoi_gian = anh_huong_thoi_gian['diem_tong']
    
    # Tính tổng với trọng số
    diem_tong = (
        diem_trong_cung * TRONG_SO_PHAN_TICH['trong_cung'] +
        diem_giua_cung * TRONG_SO_PHAN_TICH['giua_cac_cung'] +
        diem_thoi_gian * TRONG_SO_PHAN_TICH['thoi_gian']
    )
    
    # Điều chỉnh theo Lục Thân nếu có
    if sinh_khac_luc_than:
        he_so_luc_than = sinh_khac_luc_than.get('diem', 70) / 100
        diem_tong = diem_tong * (0.8 + 0.4 * he_so_luc_than)  # Điều chỉnh ±20%
    
    # Kết luận
    if diem_tong >= 80:
        ket_luan = "CỰC KỲ TỐT - Chủ có ưu thế tuyệt đối"
        mau_sac = "#4CAF50"
    elif diem_tong >= 65:
        ket_luan = "TỐT - Chủ có ưu thế rõ rệt"
        mau_sac = "#8BC34A"
    elif diem_tong >= 50:
        ket_luan = "TRUNG BÌNH - Chủ có lợi thế nhẹ"
        mau_sac = "#FFC107"
    elif diem_tong >= 35:
        ket_luan = "KHÓ KHĂN - Khách có lợi thế"
        mau_sac = "#FF9800"
    else:
        ket_luan = "RẤT KHÓ - Khách có ưu thế lớn"
        mau_sac = "#F44336"
    
    return {
        'diem_tong': round(diem_tong, 1),
        'diem_trong_cung': round(diem_trong_cung, 1),
        'diem_giua_cung': round(diem_giua_cung, 1),
        'diem_thoi_gian': round(diem_thoi_gian, 1),
        'ket_luan': ket_luan,
        'mau_sac': mau_sac,
        'chi_tiet': {
            'chu': phan_tich_chu,
            'khach': phan_tich_khach,
            'tuong_tac': tuong_tac_giua_cung,
            'thoi_gian': anh_huong_thoi_gian,
            'luc_than': sinh_khac_luc_than
        }
    }


# ============================================================================
# PHẦN 6: HÀM TỔNG HỢP - PHÂN TÍCH TOÀN DIỆN
# ============================================================================

def phan_tich_toan_dien(chu_de, cung_chu, cung_khach, dt_obj, doi_tuong="Bản thân"):
    """
    Phân tích toàn diện với tất cả các tầng
    
    Args:
        chu_de: Chủ đề cần phân tích
        cung_chu: Dict thông tin cung Chủ
        cung_khach: Dict thông tin cung Khách
        dt_obj: Datetime object
        doi_tuong: Đối tượng phân tích (Lục Thân)
    
    Returns:
        dict: Kết quả phân tích toàn diện
    """
    # 1. Chọn Dụng Thần
    dung_than_info = chon_dung_than_theo_chu_de(chu_de)
    
    # 2. Xác định Lục Thân
    ngu_hanh_chu = cung_chu.get('ngu_hanh', 'Thổ')
    luc_than_info = xac_dinh_luc_than(ngu_hanh_chu, doi_tuong)
    
    # 3. Phân tích Sinh/Khắc/Hợp với đối tượng
    # Giả sử Dụng Thần có Ngũ Hành (cần mapping riêng)
    ngu_hanh_dung_than = ngu_hanh_chu  # Tạm thời dùng ngũ hành cung
    sinh_khac_luc_than = phan_tich_sinh_khac_hop(ngu_hanh_dung_than, ngu_hanh_chu)
    
    # 4. Phân tích trong cung
    phan_tich_chu = phan_tich_tuong_tac_trong_cung(cung_chu, dung_than_info)
    phan_tich_khach = phan_tich_tuong_tac_trong_cung(cung_khach, dung_than_info)
    
    # 5. Phân tích giữa các cung
    tuong_tac_giua_cung = phan_tich_tuong_tac_giua_cac_cung(cung_chu, cung_khach)
    
    # 6. Phân tích thời gian
    anh_huong_thoi_gian = phan_tich_yeu_to_thoi_gian(dt_obj, dung_than_info, cung_chu)
    
    # 7. Tổng hợp điểm số
    ket_qua_tong_hop = tinh_diem_tong_hop(
        phan_tich_chu, phan_tich_khach,
        tuong_tac_giua_cung, anh_huong_thoi_gian,
        sinh_khac_luc_than
    )
    
    # Thêm thông tin Dụng Thần và Lục Thân
    ket_qua_tong_hop['dung_than'] = dung_than_info
    ket_qua_tong_hop['luc_than'] = luc_than_info
    ket_qua_tong_hop['sinh_khac_luc_than'] = sinh_khac_luc_than
    
    return ket_qua_tong_hop
