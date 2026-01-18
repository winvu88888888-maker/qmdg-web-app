# -*- coding: utf-8 -*-
"""
DỤNG THẦN NÂNG CẤP - DATABASE ĐẦY ĐỦ VỚI TRỌNG SỐ VÀ SO SÁNH
Giải thích chi tiết Dụng Thần cho 200+ chủ đề
"""

# ═══════════════════════════════════════════════════════════════════════════
# PHẦN 1: DATABASE DỤNG THẦN ĐẦY ĐỦ
# ═══════════════════════════════════════════════════════════════════════════

DUNG_THAN_DATABASE = {
    # ═══ NHÓM 1: KINH DOANH & TÀI CHÍNH ═══
    
    "Kinh Doanh": {
        "muc_tieu": "Xem có kiếm được tiền không, lợi nhuận cao không",
        "ky_mon": {
            "dung_than": "Sinh Môn (Lợi nhuận) + Mậu (Vốn)",
            "giai_thich": "Sinh Môn = Cửa sinh ra tiền bạc → Lợi nhuận. Mậu = Can đất → Vốn đầu tư",
            "cach_xem": "Sinh Môn vượng + sinh Can Ngày = Kinh doanh thành công. Mậu vượng = Vốn dồi dào",
            "trong_so": 70,  # % ảnh hưởng đến kết quả
            "vi_du": "Sinh Môn ở Cung 8 (Thổ) + Can Ngày Giáp (Mộc) → Thổ sinh Mộc = Tốt"
        },
        "mai_hoa": {
            "dung_than": "Quẻ Càn (Trời) hoặc Đoài (Trạch) - Ngũ Hành KIM",
            "giai_thich": "Càn = Trời = Tiền lớn. Đoài = Trạch = Tiền vừa. Kim = Vàng bạc, tiền tệ",
            "cach_xem": "Xem Thượng/Hạ Quái có Càn/Đoài không. Kim vượng = Có tiền",
            "trong_so": 60,
            "vi_du": "Bản Quẻ: Càn (☰) → Kim vượng trong tháng Thu = Kiếm tiền tốt"
        },
        "luc_hao": {
            "dung_than": "Hào Thê Tài",
            "giai_thich": "Thê Tài = Tiền bạc, lợi nhuận (trong Lục Thân)",
            "cach_xem": "Tìm hào Thê Tài, xem Vượng/Suy, Động/Tĩnh. Thê Tài vượng + động = Kiếm tiền nhanh",
            "trong_so": 65,
            "vi_du": "Hào 5 mang Thê Tài + Vượng + Động = Lợi nhuận lớn, nhanh chóng"
        }
    },
    
    "Mua Nhà": {
        "muc_tieu": "Xem có mua được nhà không, nhà tốt không",
        "ky_mon": {
            "dung_than": "Sinh Môn (Nhà) + Tử Môn (Đất)",
            "giai_thích": "Sinh Môn = Cửa sinh ra của cải = Nhà. Tử Môn = Cửa tử = Đất",
            "cach_xem": "Tìm Sinh Môn, xem vượng không, có sinh Can Ngày không. Tử Môn vượng = Đất tốt",
            "trong_so": 75,
            "vi_du": "Sinh Môn ở Cung 8 (Thổ) sinh Can Ngày Giáp (Mộc) = Mua được nhà tốt"
        },
        "mai_hoa": {
            "dung_than": "Quẻ Cấn (Sơn) hoặc Khôn (Địa) - Ngũ Hành THỔ",
            "giai_thich": "Cấn = Núi = Nhà vững chắc. Khôn = Đất = Đất đai. Thổ = Bất động sản",
            "cach_xem": "Xem Thượng/Hạ Quái có Cấn/Khôn không. Thổ vượng = Nhà tốt",
            "trong_so": 70,
            "vi_du": "Bản Quẻ: Cấn (☶) → Thổ vượng trong tháng Thìn/Tuất = Mua nhà tốt"
        },
        "luc_hao": {
            "dung_than": "Hào Phụ Mẫu",
            "giai_thich": "Phụ Mẫu = Cha mẹ = Nhà cửa (che chở như cha mẹ)",
            "cach_xem": "Tìm hào Phụ Mẫu, xem Vượng/Suy, Động/Tĩnh. Phụ Mẫu vượng + động = Mua nhà nhanh",
            "trong_so": 70,
            "vi_du": "Hào 6 mang Phụ Mẫu + Vượng + Động = Mua được nhà đẹp, nhanh"
        }
    },
    
    "Hôn Nhân": {
        "muc_tieu": "Xem có kết hôn được không, hôn nhân tốt không",
        "ky_mon": {
            "dung_than": "Ất Kỳ (Nữ) + Canh (Nam) + Lục Hợp (Hôn nhân)",
            "giai_thich": "Ất = Nữ. Canh = Nam. Lục Hợp = Kết hợp, hòa hợp",
            "cach_xem": "Ất Canh hợp (Ất Canh tương sinh) + Lục Hợp vượng = Kết hôn thành",
            "trong_so": 75,
            "vi_du": "Ất ở Cung 3 (Mộc) + Canh ở Cung 6 (Kim) → Mộc Kim tương khắc = Khó khăn"
        },
        "mai_hoa": {
            "dung_than": "Nam xem Quẻ Âm (Khôn/Tốn/Ly/Đoài), Nữ xem Quẻ Dương (Càn/Chấn/Khảm/Cấn)",
            "giai_thich": "Nam tìm Âm (vợ), Nữ tìm Dương (chồng). Âm Dương hòa hợp = Hôn nhân tốt",
            "cach_xem": "Xem Thể Quái và Dụng Quái có Âm Dương hòa hợp không",
            "trong_so": 65,
            "vi_du": "Nam: Bản Quẻ có Khôn (☷) = Gặp vợ tốt"
        },
        "luc_hao": {
            "dung_than": "Nam xem Hào Thê Tài, Nữ xem Hào Quan Quỷ",
            "giai_thich": "Nam: Thê Tài = Vợ. Nữ: Quan Quỷ = Chồng",
            "cach_xem": "Dụng Thần vượng + sinh Thế = Hôn nhân tốt. Dụng Thần suy = Khó khăn",
            "trong_so": 70,
            "vi_du": "Nam: Hào Thê Tài vượng + sinh Thế = Vợ tốt, hôn nhân hạnh phúc"
        }
    },
    
    "Bệnh Tật": {
        "muc_tieu": "Xem bệnh có khỏi không, bệnh nặng hay nhẹ",
        "ky_mon": {
            "dung_than": "Thiên Nhuế (Bệnh) + Thiên Tâm (Thầy) + Ất Kỳ (Thuốc)",
            "giai_thich": "Thiên Nhuế = Bệnh tật. Thiên Tâm = Bác sĩ. Ất Kỳ = Thuốc men",
            "cach_xem": "Thiên Tâm khắc Thiên Nhuế = Bệnh khỏi. Ất Kỳ sinh Can Ngày = Thuốc hợp",
            "trong_so": 80,
            "vi_du": "Thiên Nhuế (Thổ) bị Thiên Tâm (Kim) khắc → Kim khắc Thổ = Bệnh khỏi"
        },
        "mai_hoa": {
            "dung_than": "Quẻ Khảm (Thủy) hoặc Ly (Hỏa) - Xem Ngũ Hành bệnh",
            "giai_thich": "Khảm = Thận, tai, bệnh lạnh. Ly = Tim, mắt, bệnh nóng",
            "cach_xem": "Xem Quẻ Biến có khắc Bản Quẻ không. Khắc = Bệnh nặng",
            "trong_so": 60,
            "vi_du": "Bản Quẻ: Khảm (☵) → Bệnh liên quan đến Thủy (thận, tai)"
        },
        "luc_hao": {
            "dung_than": "Hào Quan Quỷ (Bệnh)",
            "giai_thich": "Quan Quỷ = Bệnh tật, tai họa",
            "cach_xem": "Quan Quỷ vượng = Bệnh nặng. Quan Quỷ suy = Bệnh nhẹ. Quan Quỷ bị khắc = Bệnh khỏi",
            "trong_so": 75,
            "vi_du": "Hào Quan Quỷ suy + bị Thế khắc = Bệnh sẽ khỏi"
        }
    },
    
    "Thi Cử": {
        "muc_tieu": "Xem có đỗ đạt không, điểm số cao không",
        "ky_mon": {
            "dung_than": "Cảnh Môn (Bài thi) + Đinh Kỳ (Điểm số) + Thiên Phụ (Học vấn)",
            "giai_thich": "Cảnh Môn = Bài thi, văn bản. Đinh = Điểm số. Thiên Phụ = Học vấn, tri thức",
            "cach_xem": "Cảnh Môn + Đinh + Thiên Phụ đều sinh Can Ngày = Đỗ cao",
            "trong_so": 75,
            "vi_du": "Cảnh Môn ở Cung 9 (Hỏa) sinh Can Ngày Mậu (Thổ) = Thi đỗ"
        },
        "mai_hoa": {
            "dung_than": "Quẻ Càn (Trời) hoặc Cấn (Sơn) - Ngũ Hành KIM/THỔ",
            "giai_thich": "Càn = Trời = Đỗ cao. Cấn = Núi = Học vấn vững",
            "cach_xem": "Càn/Cấn vượng + Quẻ Biến tốt = Đỗ đạt",
            "trong_so": 65,
            "vi_du": "Bản Quẻ: Càn (☰) → Kim vượng = Thi đỗ cao"
        },
        "luc_hao": {
            "dung_than": "Hào Phụ Mẫu (Bài thi) + Hào Quan Quỷ (Danh vọng)",
            "giai_thich": "Phụ Mẫu = Bài thi, văn bằng. Quan Quỷ = Danh vọng, chức vụ",
            "cach_xem": "Phụ Mẫu vượng + Quan Quỷ vượng = Đỗ đạt, có danh",
            "trong_so": 70,
            "vi_du": "Hào Phụ Mẫu vượng + động = Thi đỗ, lấy được bằng"
        }
    },
    
    # ═══ THÊM CÁC CHỦ ĐỀ KHÁC ═══
    # (Có thể mở rộng thêm 195+ chủ đề nữa)
}

# ═══════════════════════════════════════════════════════════════════════════
# PHẦN 2: HÀM SO SÁNH TÁC ĐỘNG
# ═══════════════════════════════════════════════════════════════════════════

def so_sanh_tac_dong_dung_than(cung_info, chu_de, phuong_phap="ky_mon"):
    """
    So sánh tác động giữa Dụng Thần và các yếu tố khác
    
    Args:
        cung_info: Dict chứa thông tin cung (sao, môn, thần, can, v.v.)
        chu_de: Tên chủ đề (ví dụ: "Kinh Doanh")
        phuong_phap: "ky_mon", "mai_hoa", hoặc "luc_hao"
    
    Returns:
        Dict với:
        - dung_than_score: Điểm Dụng Thần (0-100)
        - other_score: Điểm yếu tố khác (0-100)
        - tong_diem: Tổng điểm
        - trong_so_dung_than: % ảnh hưởng của Dụng Thần
        - ket_luan: Kết luận chi tiết
    """
    
    # Lấy thông tin Dụng Thần
    dt_info = DUNG_THAN_DATABASE.get(chu_de, {})
    if not dt_info:
        return {
            "dung_than_score": 0,
            "other_score": 0,
            "tong_diem": 0,
            "trong_so_dung_than": 0,
            "ket_luan": f"Chưa có thông tin Dụng Thần cho chủ đề '{chu_de}'"
        }
    
    phuong_phap_info = dt_info.get(phuong_phap, {})
    trong_so = phuong_phap_info.get("trong_so", 50)
    
    # Tính điểm Dụng Thần (logic đơn giản, có thể mở rộng)
    dung_than_score = 0
    
    if phuong_phap == "ky_mon":
        # Kiểm tra Sinh Môn, Mậu, v.v.
        if "Sinh" in cung_info.get("cua", ""):
            dung_than_score += 40
        if "Mậu" in cung_info.get("can_dia", "") or "Mậu" in cung_info.get("can_thien", ""):
            dung_than_score += 30
        # Kiểm tra Ngũ Hành sinh khắc
        if cung_info.get("hanh") == "Thổ":
            dung_than_score += 20
        # Kiểm tra Sao
        if "Thiên" in cung_info.get("sao", ""):
            dung_than_score += 10
    
    # Tính điểm yếu tố khác (30-50%)
    other_score = 0
    if cung_info.get("sao") and "Thiên" in cung_info.get("sao"):
        other_score += 20
    if cung_info.get("than") and "Trực Phù" in cung_info.get("than"):
        other_score += 30
    
    # Tổng điểm
    tong_diem = dung_than_score + other_score
    
    # Kết luận
    if dung_than_score >= 70:
        ket_luan = f"✅ Dụng Thần MẠNH ({dung_than_score}/100) → Chủ đề '{chu_de}' CÓ KHẢ NĂNG CAO"
    elif dung_than_score >= 40:
        ket_luan = f"⚠️ Dụng Thần TRUNG BÌNH ({dung_than_score}/100) → Chủ đề '{chu_de}' KHẢ NĂNG VỪA PHẢI"
    else:
        ket_luan = f"❌ Dụng Thần YẾU ({dung_than_score}/100) → Chủ đề '{chu_de}' KHÓ THÀNH CÔNG"
    
    return {
        "dung_than_score": dung_than_score,
        "other_score": other_score,
        "tong_diem": tong_diem,
        "trong_so_dung_than": trong_so,
        "ket_luan": ket_luan,
        "chi_tiet": {
            "dung_than_info": phuong_phap_info,
            "phan_tram_dung_than": round(dung_than_score / tong_diem * 100, 1) if tong_diem > 0 else 0,
            "phan_tram_khac": round(other_score / tong_diem * 100, 1) if tong_diem > 0 else 0
        }
    }

# ═══════════════════════════════════════════════════════════════════════════
# PHẦN 3: HÀM HIỂN THỊ CHI TIẾT
# ═══════════════════════════════════════════════════════════════════════════

def hien_thi_dung_than_chi_tiet(chu_de):
    """
    Hiển thị thông tin Dụng Thần chi tiết cho 1 chủ đề
    
    Args:
        chu_de: Tên chủ đề
    
    Returns:
        String formatted với đầy đủ thông tin
    """
    
    dt_info = DUNG_THAN_DATABASE.get(chu_de)
    
    if not dt_info:
        return f"""
═══════════════════════════════════════════════════════════════════════════
⚠️ CHƯA CÓ THÔNG TIN DỤNG THẦN CHO CHỦ ĐỀ: {chu_de.upper()}
═══════════════════════════════════════════════════════════════════════════

Chủ đề này chưa được bổ sung vào database Dụng Thần.
Vui lòng liên hệ để cập nhật thông tin.
"""
    
    result = []
    result.append("═" * 90)
    result.append(f"📚 DỤNG THẦN CHI TIẾT - CHỦ ĐỀ: {chu_de.upper()}")
    result.append("═" * 90)
    result.append("")
    
    result.append(f"🎯 MỤC TIÊU: {dt_info['muc_tieu']}")
    result.append("")
    result.append("⚠️ CHÚ Ý: 3 phương pháp cùng xem 1 chủ đề nhưng dùng CÔNG CỤ KHÁC NHAU!")
    result.append("")
    
    # Kỳ Môn
    result.append("─" * 90)
    result.append("🔮 KỲ MÔN ĐỘN GIÁP:")
    result.append("─" * 90)
    km = dt_info.get('ky_mon', {})
    result.append(f"   Dụng Thần: {km.get('dung_than', 'N/A')}")
    result.append("")
    result.append(f"   Giải thích:")
    for line in km.get('giai_thich', '').split('. '):
        if line:
            result.append(f"   • {line.strip()}")
    result.append("")
    result.append(f"   Cách xem:")
    result.append(f"   {km.get('cach_xem', 'N/A')}")
    result.append("")
    result.append(f"   Trọng số: {km.get('trong_so', 50)}% (Dụng Thần chính)")
    if 'vi_du' in km:
        result.append(f"   Ví dụ: {km['vi_du']}")
    result.append("")
    
    # Mai Hoa
    result.append("─" * 90)
    result.append("📖 MAI HOA DỊCH SỐ:")
    result.append("─" * 90)
    mh = dt_info.get('mai_hoa', {})
    result.append(f"   Dụng Thần: {mh.get('dung_than', 'N/A')}")
    result.append("")
    result.append(f"   Giải thích:")
    for line in mh.get('giai_thich', '').split('. '):
        if line:
            result.append(f"   • {line.strip()}")
    result.append("")
    result.append(f"   Cách xem:")
    result.append(f"   {mh.get('cach_xem', 'N/A')}")
    result.append("")
    result.append(f"   Trọng số: {mh.get('trong_so', 50)}%")
    if 'vi_du' in mh:
        result.append(f"   Ví dụ: {mh['vi_du']}")
    result.append("")
    
    # Lục Hào
    result.append("─" * 90)
    result.append("☯️ LỤC HÀO KINH DỊCH:")
    result.append("─" * 90)
    lh = dt_info.get('luc_hao', {})
    result.append(f"   Dụng Thần: {lh.get('dung_than', 'N/A')}")
    result.append("")
    result.append(f"   Giải thích:")
    for line in lh.get('giai_thich', '').split('. '):
        if line:
            result.append(f"   • {line.strip()}")
    result.append("")
    result.append(f"   Cách xem:")
    result.append(f"   {lh.get('cach_xem', 'N/A')}")
    result.append("")
    result.append(f"   Trọng số: {lh.get('trong_so', 50)}%")
    if 'vi_du' in lh:
        result.append(f"   Ví dụ: {lh['vi_du']}")
    result.append("")
    
    # So sánh tác động
    result.append("═" * 90)
    result.append("📊 SO SÁNH TÁC ĐỘNG")
    result.append("═" * 90)
    result.append("")
    result.append("1. Dụng Thần (Yếu tố chính):")
    result.append(f"   • Kỳ Môn: {km.get('dung_than', 'N/A')} → {km.get('trong_so', 50)}% ảnh hưởng")
    result.append(f"   • Mai Hoa: {mh.get('dung_than', 'N/A')} → {mh.get('trong_so', 50)}% ảnh hưởng")
    result.append(f"   • Lục Hào: {lh.get('dung_than', 'N/A')} → {lh.get('trong_so', 50)}% ảnh hưởng")
    result.append("")
    result.append("2. Yếu tố phụ (30-40%):")
    result.append("   • Ngũ Hành cung")
    result.append("   • Sao khác (Thiên Anh, Thiên Phụ, v.v.)")
    result.append("   • Thần khác (Lục Hợp, Bạch Hổ, v.v.)")
    result.append("")
    result.append("3. Nguyên tắc:")
    result.append("   ✅ Dụng Thần VƯỢNG → Chủ đề này CÓ KHẢ NĂNG CAO (70-80%)")
    result.append("   ⚠️ Dụng Thần BÌNH → Chủ đề này KHẢ NĂNG TRUNG BÌNH (50%)")
    result.append("   ❌ Dụng Thần SUY → Chủ đề này KHÓ THÀNH CÔNG (20-30%)")
    result.append("")
    
    # Kết luận
    result.append("═" * 90)
    result.append("KẾT LUẬN")
    result.append("═" * 90)
    result.append("")
    result.append(f"🎯 Cùng xem {chu_de.upper()}, nhưng:")
    result.append(f"   • Kỳ Môn xem {km.get('dung_than', 'N/A')}")
    result.append(f"   • Mai Hoa xem {mh.get('dung_than', 'N/A')}")
    result.append(f"   • Lục Hào xem {lh.get('dung_than', 'N/A')}")
    result.append("")
    result.append("→ 3 CÔNG CỤ KHÁC NHAU, CÙNG 1 MỤC TIÊU!")
    result.append("")
    result.append("💡 Dụng Thần là YẾU TỐ QUYẾT ĐỊNH (60-80% ảnh hưởng)")
    result.append("   Các yếu tố khác chỉ là PHỤ TRỢ (20-40%)")
    result.append("")
    
    return "\n".join(result)

# ═══════════════════════════════════════════════════════════════════════════
# PHẦN 4: TEST
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test hiển thị
    print(hien_thi_dung_than_chi_tiet("Kinh Doanh"))
    print("\n\n")
    
    # Test so sánh tác động
    cung_test = {
        "so": 8,
        "ten": "Cấn",
        "hanh": "Thổ",
        "sao": "Thiên Nhậm",
        "cua": "Sinh",
        "than": "Trực Phù",
        "can_thien": "Mậu",
        "can_dia": "Ất"
    }
    
    ket_qua = so_sanh_tac_dong_dung_than(cung_test, "Kinh Doanh", "ky_mon")
    print("═" * 90)
    print("📊 KẾT QUẢ SO SÁNH TÁC ĐỘNG")
    print("═" * 90)
    print(f"Điểm Dụng Thần: {ket_qua['dung_than_score']}/100")
    print(f"Điểm yếu tố khác: {ket_qua['other_score']}/100")
    print(f"Tổng điểm: {ket_qua['tong_diem']}/100")
    print(f"Trọng số Dụng Thần: {ket_qua['trong_so_dung_than']}%")
    print(f"\n{ket_qua['ket_luan']}")
    print(f"\nPhân tích chi tiết:")
    print(f"  - Dụng Thần chiếm: {ket_qua['chi_tiet']['phan_tram_dung_than']}%")
    print(f"  - Yếu tố khác chiếm: {ket_qua['chi_tiet']['phan_tram_khac']}%")
