
import sys
import os
from datetime import datetime

# Add the current directory to sys.path so we can import the modules
sys.path.append(os.getcwd())

from super_detailed_analysis import phan_tich_sieu_chi_tiet_chu_de

def test_interpretations():
    # Mock data for Palaces
    # Palace 1 (Chu) - Business focus
    chu_biz = {
        'so': 8,
        'ten': 'Cấn',
        'hanh': 'Thổ',
        'sao': 'Thiên Nhậm',
        'cua': 'Sinh',
        'than': 'Trực Phù',
        'can_thien': 'Mậu',
        'can_dia': 'Bính'
    }
    
    # Palace 2 (Khach) - Partner/Market
    khach_biz = {
        'so': 1,
        'ten': 'Khảm',
        'hanh': 'Thủy',
        'sao': 'Thiên Bồng',
        'cua': 'Hưu',
        'than': 'Huyền Vũ',
        'can_thien': 'Canh',
        'can_dia': 'Nhâm'
    }
    
    dt_obj = datetime.now()
    
    topics = ['Kinh Doanh Tổng Quát', 'Tình Duyên Hôn Nhân', 'Kiện Tụng', 'Bệnh Tật Chữa Trị', 'Trận Đấu Bóng Đá', 'Bất động sản', 'Xuất hành', 'Thi cử', 'Tìm đồ vật']
    
    for topic in topics:
        print(f"\n{'='*20} {topic} {'='*20}")
        result = phan_tich_sieu_chi_tiet_chu_de(topic, chu_biz, khach_biz, dt_obj)
        
        # Print main conclusion
        print(f"DIỄN GIẢI KỲ MÔN:")
        # In the real app, this comes from _phan_tich_ky_mon_chi_tiet -> ket_luan
        print(result['phan_tich_9_phuong_phap']['ky_mon']['ket_luan'])
        
        print(f"\nDIỄN GIẢI THÔNG MINH (Five Elements):")
        # In phan_tich_sieu_chi_tiet_chu_de, it calls _phan_tich_tung_khia_canh
        # which uses _tao_dien_giai_mqh_thong_minh via other helpers
        # Let's see the main flow.
        
        # Actually, phan_tich_sieu_chi_tiet_chu_de returns a big dict.
        # Let's print the detailed aspects.
        if 'chi_tiet_tung_khia_canh' in result:
            for k, v in result['chi_tiet_tung_khia_canh'].items():
                print(f"--- {v['tieu_de']} ---")
                for line in v['noi_dung']:
                    print(f"  {line}")

if __name__ == "__main__":
    test_interpretations()
