# -*- coding: utf-8 -*-
"""
DỤNG THẦN CHI TIẾT - GIẢI THÍCH SỰ KHÁC BIỆT GIỮA 3 PHƯƠNG PHÁP
Kỳ Môn, Mai Hoa, Lục Hào cùng xem 1 chủ đề nhưng dùng CÔNG CỤ KHÁC NHAU
"""

# VÍ DỤ MẪU: MUA NHÀ
VI_DU_MUA_NHA = """
===================================================================================
CHỦ ĐỀ: MUA NHÀ
MỤC TIÊU CHUNG: Xem có mua được nhà không, nhà tốt không
===================================================================================

3 PHƯƠNG PHÁP KHÁC NHAU:

🔮 KỲ MÔN ĐỘN GIÁP:
   Dụng Thần: SINH MÔN (Cửa) + TỬ MÔN (Cửa) + THIÊN PHỤ/MẪU (Sao)
   
   Giải thích:
   - SINH MÔN = Đại diện cho NHÀ (cửa sinh ra của cải)
   - TỬ MÔN = Đại diện cho ĐẤT (cửa tử = đất)
   - THIÊN PHỤ/MẪU = Sao cha mẹ = nhà cửa
   
   Cách xem:
   1. Tìm SINH MÔN ở cung nào
   2. Xem Sinh Môn có VƯỢNG không
   3. Xem Sinh Môn có SINH cho Giá Phù (người mua) không
   → Sinh Môn vượng + sinh Giá Phù = MUA ĐƯỢC NHÀ TỐT

📖 MAI HOA DỊCH SỐ:
   Dụng Thần: QUẺ CẤN (Sơn) hoặc QUẺ KHÔN (Địa)
   
   Giải thích:
   - CẤN = Núi = Nhà (nhà như núi, vững chắc)
   - KHÔN = Đất = Đất đai
   - NGŨ HÀNH THỔ = Đất đai, bất động sản
   
   Cách xem:
   1. Xem Thượng Quái hoặc Hạ Quái có phải Cấn/Khôn không
   2. Xem Ngũ Hành THỔ có VƯỢNG không
   3. Xem Quẻ Biến có tốt hơn Bản Quẻ không
   → Cấn/Khôn vượng + Quẻ Biến tốt = CÓ NHÀ

☯️ LỤC HÀO KINH DỊCH:
   Dụng Thần: HÀO PHỤ MẪU (1 trong 6 Lục Thân)
   
   Giải thích:
   - PHỤ MẪU = Cha mẹ = Nhà cửa (nhà như cha mẹ che chở)
   - THÊ TÀI = Tiền mua nhà (phụ)
   
   Cách xem:
   1. Tìm HÀO nào mang Phụ Mẫu
   2. Xem Phụ Mẫu VƯỢNG hay SUY
   3. Xem Phụ Mẫu ĐỘNG hay TĨNH
   → Phụ Mẫu vượng + động = MUA ĐƯỢC NHÀ NHANH

===================================================================================
KẾT LUẬN: 
- Cùng xem MUA NHÀ
- Kỳ Môn xem SINH MÔN (Cửa)
- Mai Hoa xem QUẺ CẤN/KHÔN (Quẻ)
- Lục Hào xem HÀO PHỤ MẪU (Hào)
→ 3 CÔNG CỤ KHÁC NHAU, CÙNG 1 MỤC TIÊU!
===================================================================================
"""

# Database đầy đủ
DUNG_THAN_CHI_TIET = {
    "Mua Nhà": {
        "muc_tieu": "Xem có mua được nhà không, nhà tốt không",
        "ky_mon": {
            "dung_than": "Sinh Môn (Nhà) + Tử Môn (Đất)",
            "giai_thich": "Sinh Môn = Cửa sinh ra của cải = Nhà. Tử Môn = Cửa tử = Đất",
            "cach_xem": "Tìm Sinh Môn, xem vượng không, có sinh Giá Phù không"
        },
        "mai_hoa": {
            "dung_than": "Quẻ Cấn (Sơn) hoặc Khôn (Địa)",
            "giai_thich": "Cấn = Núi = Nhà vững. Khôn = Đất = Đất đai",
            "cach_xem": "Xem Thượng/Hạ Quái có Cấn/Khôn không, Thổ vượng không"
        },
        "luc_hao": {
            "dung_than": "Hào Phụ Mẫu",
            "giai_thich": "Phụ Mẫu = Cha mẹ = Nhà cửa (che chở như cha mẹ)",
            "cach_xem": "Tìm hào Phụ Mẫu, xem Vượng/Suy, Động/Tĩnh"
        }
    },
    
    "Kinh Doanh": {
        "muc_tieu": "Xem có kiếm được tiền không, lợi nhuận cao không",
        "ky_mon": {
            "dung_than": "Sinh Môn (Lợi nhuận) + Giáp Tử Mậu (Vốn)",
            "giai_thich": "Sinh Môn = Sinh ra tiền. Giáp Tử Mậu = Vốn đầu tư",
            "cach_xem": "Sinh Môn vượng + sinh Nhật Can = Kinh doanh thành công"
        },
        "mai_hoa": {
            "dung_than": "Quẻ Càn/Đoài (Kim)",
            "giai_thich": "Càn = Trời = Tiền lớn. Đoài = Trạch = Tiền vừa. Kim = Tiền bạc",
            "cach_xem": "Xem Càn/Đoài, Kim vượng không, Quẻ Biến tốt không"
        },
        "luc_hao": {
            "dung_than": "Hào Thê Tài",
            "giai_thich": "Thê Tài = Tiền bạc, lợi nhuận",
            "cach_xem": "Thê Tài vượng + động = Kiếm được tiền nhanh"
        }
    },
    
    "Hôn Nhân": {
        "muc_tieu": "Xem có kết hôn được không, hôn nhân tốt không",
        "ky_mon": {
            "dung_than": "Ất Kỳ (Nữ) + Canh (Nam) + Lục Hợp (Hôn nhân)",
            "giai_thich": "Ất = Nữ. Canh = Nam. Lục Hợp = Kết hợp",
            "cach_xem": "Ất Canh hợp + Lục Hợp vượng = Kết hôn thành"
        },
        "mai_hoa": {
            "dung_than": "Nam xem Quẻ Âm (Khôn/Tốn/Ly/Đoài), Nữ xem Quẻ Dương (Càn/Chấn/Khảm/Cấn)",
            "giai_thích": "Nam tìm Âm (vợ), Nữ tìm Dương (chồng)",
            "cach_xem": "Âm Dương hòa hợp = Hôn nhân tốt"
        },
        "luc_hao": {
            "dung_than": "Nam xem Hào Thê Tài, Nữ xem Hào Quan Quỷ",
            "giai_thich": "Nam: Thê Tài = Vợ. Nữ: Quan Quỷ = Chồng",
            "cach_xem": "Dụng Thần vượng + sinh Thế = Hôn nhân tốt"
        }
    }
}

# Template cho các chủ đề khác
DUNG_THAN_MAC_DINH = {
    "muc_tieu": "Xem theo chủ đề cụ thể",
    "ky_mon": {
        "dung_than": "Nhật Can (Người hỏi) + Thời Can (Sự việc)",
        "giai_thich": "Kỳ Môn xem qua CỬU TINH, BÁT MÔN, BÁT THẦN",
        "cach_xem": "Xem Dụng Thần vượng không, có sinh Nhật Can không"
    },
    "mai_hoa": {
        "dung_than": "Thể Quái (Người hỏi) + Dụng Quái (Sự việc)",
        "giai_thich": "Mai Hoa xem qua BÁT QUẺ, NGŨ HÀNH",
        "cach_xem": "Xem Thể Dụng sinh khắc, Ngũ Hành vượng suy"
    },
    "luc_hao": {
        "dung_than": "Lục Thân (Phụ Mẫu/Quan Quỷ/Thê Tài/Huynh Đệ/Tử Tôn)",
        "giai_thich": "Lục Hào xem qua LỤC THÂN, VƯỢNG SUY, ĐỘNG TĨNH",
        "cach_xem": "Tìm Dụng Thần, xem Vượng/Suy, Động/Tĩnh"
    }
}

def lay_dung_than_chi_tiet(chu_de):
    return DUNG_THAN_CHI_TIET.get(chu_de, DUNG_THAN_MAC_DINH)

def hien_thi_dung_than(chu_de):
    info = lay_dung_than_chi_tiet(chu_de)
    
    result = []
    result.append("="*90)
    result.append(f"📚 DỤNG THẦN CHI TIẾT - CHỦ ĐỀ: {chu_de.upper()}")
    result.append("="*90)
    result.append("")
    
    result.append(f"🎯 MỤC TIÊU: {info['muc_tieu']}")
    result.append("")
    result.append("⚠️ CHÚ Ý: 3 phương pháp cùng xem 1 chủ đề nhưng dùng CÔNG CỤ KHÁC NHAU!")
    result.append("")
    
    # Kỳ Môn
    km = info['ky_mon']
    result.append("🔮 KỲ MÔN ĐỘN GIÁP:")
    result.append(f"   Dụng Thần: {km['dung_than']}")
    result.append(f"   Giải thích: {km['giai_thich']}")
    result.append(f"   Cách xem: {km['cach_xem']}")
    result.append("")
    
    # Mai Hoa
    mh = info['mai_hoa']
    result.append("📖 MAI HOA DỊCH SỐ:")
    result.append(f"   Dụng Thần: {mh['dung_than']}")
    result.append(f"   Giải thích: {mh['giai_thich']}")
    result.append(f"   Cách xem: {mh['cach_xem']}")
    result.append("")
    
    # Lục Hào
    lh = info['luc_hao']
    result.append("☯️ LỤC HÀO KINH DỊCH:")
    result.append(f"   Dụng Thần: {lh['dung_than']}")
    result.append(f"   Giải thích: {lh['giai_thich']}")
    result.append(f"   Cách xem: {lh['cach_xem']}")
    result.append("")
    
    result.append("="*90)
    result.append("KẾT LUẬN: Cùng 1 chủ đề, 3 công cụ khác nhau!")
    result.append("="*90)
    
    return "\n".join(result)

if __name__ == "__main__":
    print(VI_DU_MUA_NHA)
    print("\n\n")
    print(hien_thi_dung_than("Kinh Doanh"))
