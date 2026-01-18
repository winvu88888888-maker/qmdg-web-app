from super_detailed_analysis import phan_tich_sieu_chi_tiet_chu_de
from qmdg_data import KY_MON_DATA

def test_full_layers():
    # Giả lập dữ liệu Cung (Cung 1 - Khảm)
    # Trong Khảm cố định có Hưu Môn, Thiên Bồng, Thiên Nhâm...
    # Giả sử Thiên Bồng và Hưu Môn đang ở đây
    chu = {
        'so': 2, # Cung Khôn - Bế tắc
        'cua': 'Tử',
        'sao': 'Thiên Nhuế',
        'than': 'Huyền Vũ',
        'can_thien': 'Canh',
        'can_dia': 'Nhâm',
        'hanh': 'Thổ'
    }
    khach = {
        'so': 1,
        'cua': 'Khai',
        'sao': 'Thiên Tâm',
        'than': 'Trực Phù',
        'can_thien': 'Giáp',
        'can_dia': 'Mậu',
        'hanh': 'Thủy'
    }
    
    # Test với chủ đề có nguy cơ để xem phần hóa giải
    import datetime
    now = datetime.datetime.now()
    result = phan_tich_sieu_chi_tiet_chu_de("Xem Bệnh Tật", chu, khach, now)
    
    # Lấy kết luận tổng hợp hoặc kết luận từ Kỳ Môn
    ket_luan = result.get('tong_hop', {}).get('ket_luan', '')
    if not ket_luan:
        ket_luan = result.get('phan_tich_9_phuong_phap', {}).get('ky_mon', {}).get('ket_luan', '')
    
    print(f"DEBUG: ket_luan length = {len(ket_luan)}")
    print(f"DEBUG: ket_luan sample = {ket_luan[:1000]}")
    print(f"DEBUG: advanced_kb keys = {KY_MON_DATA.get('ADVANCED_KNOWLEDGE', {}).keys()}")
    print(f"DEBUG: enriched_data (Excel) present = {'ENRICHED_DATA' in KY_MON_DATA}")
    
    print("--- KIỂM TRA TẦNG DỮ LIỆU ---")
    
    if "💡 DỤNG THẦN & GỢI Ý CHUYÊN SÂU" in ket_luan:
        print("✅ Tầng 1 (Cơ bản): OK")
    else:
        print("❌ Tầng 1 (Cơ bản): MISSING")
        
    if "📝【NHÂN VẬT PHÍA CHỦ】" in ket_luan:
        print("✅ Tầng 2 (Excel Profiling): OK")
    else:
        print("❌ Tầng 2 (Excel Profiling): MISSING")
        
    if "🌌【TƯỢNG Ý SIÊU CHI TIẾT - CHỦ】" in ket_luan:
        print("✅ Tầng 3 (Advanced/PDF Tượng): OK")
        # Check specific content from our newly created JSON
        if "Tượng Âm Bàn: Trí tuệ, tặc tinh" in ket_luan:
             print("   >> Nội dung Tượng Âm Bàn: OK")
    else:
        print("❌ Tầng 3 (Advanced/PDF Tượng): MISSING")
        
    if "🔮【CHỈ DẪN HÓA GIẢI ĐẠO GIA" in ket_luan:
        print("✅ Tầng 4 (Hóa giải Tháo Bổ Di): OK")
    else:
        print("❌ Tầng 4 (Hóa giải Tháo Bổ Di): MISSING")

if __name__ == "__main__":
    test_full_layers()
