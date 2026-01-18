# -*- coding: utf-8 -*-
"""
HỆ THỐNG DIỄN GIẢI ĐỘNG - LINH HOẠT THEO TỪNG TỔ HỢP CỤ THỂ
Mỗi tổ hợp Sao-Môn-Thần-Ngũ Hành sẽ có diễn giải riêng biệt cho từng chủ đề
"""

from qmdg_data import KY_MON_DATA, tinh_ngu_hanh_sinh_khac
from master_knowledge_database import KY_MON_MASTER_KNOWLEDGE
from extended_knowledge_database import LUC_NHAM_THAN_KHOA, BAT_TU_TU_TRU

# ============================================================================
# PHẦN 1: TRI THỨC ĐỘNG VỀ SAO (CỬU TINH)
# ============================================================================

SAO_CHI_TIET_THEO_CHU_DE = {
    "Thiên Phụ": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Cổ phiếu Blue-chip, vốn hóa lớn, ổn định",
            "Khuyến_Nghị": "Tập trung vào ngân hàng, bất động sản, năng lượng - các mã có nền tảng vững chắc",
            "Dự_Báo": "Tăng trưởng ổn định 8-12%/năm, rủi ro thấp"
        },
        "Thi Đại Học": {
            "Ý_Nghĩa": "Nền tảng kiến thức vững chắc, thầy giỏi",
            "Khuyến_Nghị": "Phù hợp ngành Y, Dược, Luật, Kinh tế - các ngành cần học thuật cao",
            "Dự_Báo": "Khả năng đỗ 85-90%, điểm số ổn định trên 8.0"
        },
        "Xin Việc Làm": {
            "Ý_Nghĩa": "CV ấn tượng, bằng cấp tốt, trình độ cao",
            "Khuyến_Nghị": "Nhấn mạnh học vấn và kinh nghiệm chuyên môn trong phỏng vấn",
            "Dự_Báo": "Pass vòng hồ sơ 90%, được đánh giá cao về năng lực"
        },
        "Mua Nhà Đất": {
            "Ý_Nghĩa": "Pháp lý rõ ràng, giấy tờ đầy đủ",
            "Khuyến_Nghị": "Thời điểm tốt để mua, thủ tục nhanh gọn",
            "Dự_Báo": "Không có rủi ro pháp lý, an tâm giao dịch"
        },
        "Phẫu Thuật": {
            "Ý_Nghĩa": "Bệnh viện uy tín, trang thiết bị hiện đại",
            "Khuyến_Nghị": "Yên tâm về cơ sở y tế và đội ngũ bác sĩ",
            "Dự_Báo": "Phẫu thuật thành công tốt đẹp"
        }
    },
    
    "Thiên Tâm": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Phân tích kỹ thuật tốt, chiến lược thông minh",
            "Khuyến_Nghị": "Dùng phân tích kỹ thuật và đọc biểu đồ để quyết định",
            "Dự_Báo": "Khả năng chọn đúng điểm vào/ra cao"
        },
        "Thi Đại Học": {
            "Ý_Nghĩa": "Tư duy logic tốt, giải quyết vấn đề sáng tạo",
            "Khuyến_Nghị": "Phù hợp ngành Công nghệ thông tin, Kỹ thuật, Toán - Tin",
            "Dự_Báo": "Khả năng đỗ 80%, đặc biệt tốt với các môn tư duy"
        },
        "Xin Việc Làm": {
            "Ý_Nghĩa": "Gây ấn tượng trong vòng phỏng vấn",
            "Khuyến_Nghị": "Thể hiện khả năng giải quyết vấn đề và tư duy sáng tạo",
            "Dự_Báo": "Pass phỏng vấn 85%, nhà tuyển dụng đánh giá cao"
        },
        "Phẫu Thuật": {
            "Ý_Nghĩa": "Bác sĩ giỏi, tay nghề cao",
            "Khuyến_Nghị": "Đã gặp đúng bác sĩ, yên tâm phẫu thuật",
            "Dự_Báo": "Thành công tốt đẹp, ít biến chứng"
        }
    },
    
    "Thiên Nhuế": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Thị trường bệnh hoạn, biến động mạnh",
            "Khuyến_Nghị": "Tránh penny stock và mã nhỏ, rủi ro cực cao",
            "Dự_Báo": "Thị trường không ổn định, nên giữ tiền mặt"
        },
        "Thi Đại Học": {
            "Ý_Nghĩa": "Sức khỏe không tốt, tâm lý bất ổn",
            "Khuyến_Nghị": "Nghỉ ngơi đầy đủ, tránh stress trước kỳ thi",
            "Dự_Báo": "Cần chú ý sức khỏe để không ảnh hưởng phong độ"
        },
        "Phẫu Thuật": {
            "Ý_Nghĩa": "Bệnh tình phức tạp, cần theo dõi sát",
            "Khuyến_Nghị": "Chuẩn bị tinh thần cho quá trình điều trị dài hạn",
            "Dự_Báo": "Cần theo dõi sau mổ kỹ càng"
        },
        "Sinh Con": {
            "Ý_Nghĩa": "Thai nhi yếu hoặc chậm phát triển",
            "Khuyến_Nghị": "Khám thai định kỳ đầy đủ, theo dõi sát",
            "Dự_Báo": "Cần chăm sóc đặc biệt"
        }
    },
    
    "Thiên Anh": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Cổ phiếu công nghệ, quốc phòng đang nổi sóng",
            "Khuyến_Nghị": "Tăng điểm mạnh nhưng cần chốt lời kịp thời",
            "Dự_Báo": "Biến động mạnh, phù hợp giao dịch ngắn hạn"
        },
        "Thi Đại Học": {
            "Ý_Nghĩa": "Bài thi nổi bật, gây ấn tượng mạnh",
            "Khuyến_Nghị": "Tự tin thể hiện, có thể đạt điểm cao hơn mong đợi",
            "Dự_Báo": "Có thể đạt điểm cao hơn dự kiến 1-2 điểm"
        }
    },
    
    "Thiên Trụ": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Cổ phiếu nhà nước, doanh nghiệp có bảo trợ chính phủ",
            "Khuyến_Nghị": "Đầu tư dài hạn vào các mã này rất an toàn",
            "Dự_Báo": "Tăng trưởng ổn định, rủi ro thấp"
        }
    }
}

# ============================================================================
# PHẦN 2: TRI THỨC ĐỘNG VỀ MÔN (BÁT MÔN)
# ============================================================================

MON_CHI_TIET_THEO_CHU_DE = {
    "Sinh": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Điểm mua VÀNG, dòng tiền chảy mạnh",
            "Khuyến_Nghị": "Thời điểm tuyệt vời để mua vào",
            "Dự_Báo": "Giá sẽ tăng trong 3-7 ngày tới",
            "Hành_Động": "Mua ngay, không chần chừ"
        },
        "Thi Đại Học": {
            "Ý_Nghĩa": "Kiến thức đang được củng cố tốt",
            "Khuyến_Nghị": "Tiếp tục ôn tập đều đặn",
            "Dự_Báo": "Điểm số ổn định ở mức khá (7.5-8.5)",
            "Hành_Động": "Duy trì nhịp độ học tập hiện tại"
        },
        "Xin Việc Làm": {
            "Ý_Nghĩa": "Vị trí phù hợp, có cơ hội phát triển",
            "Khuyến_Nghị": "Công việc này rất hợp với bạn",
            "Dự_Báo": "Mức lương tăng dần theo năng lực",
            "Hành_Động": "Nên nhận offer này"
        },
        "Mua Nhà Đất": {
            "Ý_Nghĩa": "Sinh khí vượng, phong thủy tuyệt vời",
            "Khuyến_Nghị": "Rất tốt cho sức khỏe và tài lộc",
            "Dự_Báo": "Nên mua ngay nếu giá hợp lý",
            "Hành_Động": "Đặt cọc để giữ chỗ"
        },
        "Phẫu Thuật": {
            "Ý_Nghĩa": "Sinh lực vượng, cơ thể hồi phục nhanh",
            "Khuyến_Nghị": "Thời điểm tốt để phẫu thuật",
            "Dự_Báo": "Nên phẫu thuật trong tuần này",
            "Hành_Động": "Sắp xếp lịch mổ sớm"
        },
        "Sinh Con": {
            "Ý_Nghĩa": "Quá trình sinh thuận lợi",
            "Khuyến_Nghị": "Mẹ tròn con vuông",
            "Dự_Báo": "Nếu sinh thường, thời gian chuyển dạ ngắn",
            "Hành_Động": "Chuẩn bị đồ đạc cho ngày sinh"
        }
    },
    
    "Khai": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Cơ hội mở rộng, thị trường đa dạng",
            "Khuyến_Nghị": "Phân tán danh mục vào 3-5 mã",
            "Dự_Báo": "Nhiều cơ hội mới xuất hiện",
            "Hành_Động": "Không all-in một mã"
        },
        "Xin Việc Làm": {
            "Ý_Nghĩa": "Cơ hội rộng mở, nhiều công ty tuyển dụng",
            "Khuyến_Nghị": "Thời điểm vàng để xin việc",
            "Dự_Báo": "Sẽ nhận được 2-3 offer trong 2 tuần",
            "Hành_Động": "Nộp đơn cho nhiều công ty"
        },
        "Mua Nhà Đất": {
            "Ý_Nghĩa": "Vị trí đắc địa, kinh doanh tốt",
            "Khuyến_Nghị": "Gần trục đường lớn, thuận tiện",
            "Dự_Báo": "Phù hợp mở cửa hàng, văn phòng hoặc cho thuê",
            "Hành_Động": "Cân nhắc mục đích kinh doanh"
        },
        "Cầu Hôn": {
            "Ý_Nghĩa": "Cánh cửa tình yêu rộng mở",
            "Khuyến_Nghị": "Nên cầu hôn trong tuần này",
            "Dự_Báo": "Vào buổi tối, tại nơi có ý nghĩa",
            "Hành_Động": "Chuẩn bị nhẫn và lời cầu hôn"
        }
    },
    
    "Tử": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Thị trường đóng băng, thanh khoản thấp",
            "Khuyến_Nghị": "NGỪNG MUA, chỉ nên giữ",
            "Dự_Báo": "Không nên mua thêm",
            "Hành_Động": "Chờ đợi, không giao dịch"
        },
        "Xin Việc Làm": {
            "Ý_Nghĩa": "Thị trường việc làm đóng băng",
            "Khuyến_Nghị": "Công ty đang cắt giảm nhân sự",
            "Dự_Báo": "Khó khăn, nên mở rộng tìm kiếm",
            "Hành_Động": "Tìm sang lĩnh vực khác"
        },
        "Mua Nhà Đất": {
            "Ý_Nghĩa": "Tử khí nặng, phong thủy xấu",
            "Khuyến_Nghị": "Có thể từng xảy ra chuyện không may",
            "Dự_Báo": "KHÔNG NÊN MUA",
            "Hành_Động": "Tìm căn khác"
        },
        "Phẫu Thuật": {
            "Ý_Nghĩa": "Sinh lực yếu, cơ thể chưa sẵn sàng",
            "Khuyến_Nghị": "Nên hoãn nếu không cấp cứu",
            "Dự_Báo": "Hoãn 2-4 tuần để cơ thể phục hồi",
            "Hành_Động": "Tăng cường dinh dưỡng trước"
        }
    },
    
    "Thương": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Biến động mạnh, tranh chấp giữa mua/bán",
            "Khuyến_Nghị": "Chỉ nên giao dịch ngắn hạn (day trading)",
            "Dự_Báo": "Rủi ro cao, cần stop-loss chặt",
            "Hành_Động": "Không nắm giữ qua đêm"
        }
    },
    
    "Hưu": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Điểm bán, thị trường sắp nghỉ ngơi",
            "Khuyến_Nghị": "Nếu đang lãi, chốt lời 30-50%",
            "Dự_Báo": "Thị trường sắp vào giai đoạn nghỉ ngơi",
            "Hành_Động": "Chốt lời một phần"
        },
        "Mua Nhà Đất": {
            "Ý_Nghĩa": "Vị trí yên tĩnh, thích hợp nghỉ dưỡng",
            "Khuyến_Nghị": "Tốt để ở, không ồn ào",
            "Dự_Báo": "Không phù hợp kinh doanh",
            "Hành_Động": "Mua để ở, không để kinh doanh"
        }
    },
    
    "Kinh": {
        "Đầu Tư Chứng Khoán": {
            "Ý_Nghĩa": "Hoảng loạn thị trường, bán tháo",
            "Khuyến_Nghị": "BÁN GẤP nếu đang lỗ sâu",
            "Dự_Báo": "Cắt lỗ để bảo toàn vốn",
            "Hành_Động": "Nếu đang lãi, chốt 70-80%"
        },
        "Sinh Con": {
            "Ý_Nghĩa": "Quá trình sinh khó khăn",
            "Khuyến_Nghị": "Có thể gặp khó khăn",
            "Dự_Báo": "Chuẩn bị tinh thần cho phương án mổ",
            "Hành_Động": "Trao đổi với bác sĩ về phương án dự phòng"
        }
    },
    
    "Cảnh": {
        "Thi Đại Học": {
            "Ý_Nghĩa": "Bài thi xuất sắc, văn phong mạch lạc",
            "Khuyến_Nghị": "Các môn Văn, Sử, Địa, Ngoại ngữ sẽ rất cao",
            "Dự_Báo": "Điểm 8.5-9.5 cho các môn xã hội",
            "Hành_Động": "Tập trung vào các môn này"
        }
    }
}

# ============================================================================
# PHẦN 3: HÀM DIỄN GIẢI ĐỘNG CHÍNH
# ============================================================================

def tao_dien_giai_dong(chu_de, chu, khach, mqh):
    """
    Tạo diễn giải động dựa trên tổ hợp Sao-Môn-Thần-Ngũ Hành cụ thể
    
    Args:
        chu_de: Chủ đề cần phân tích
        chu: Dict thông tin cung Chủ {sao, cua, than, hanh, can_thien, can_dia...}
        khach: Dict thông tin cung Khách
        mqh: Mối quan hệ Ngũ Hành
        
    Returns:
        str: Diễn giải chi tiết, linh hoạt theo tình huống
    """
    
    dien_giai = []
    
    # 1. PHÂN TÍCH SAO (CỬU TINH)
    sao_chu = chu.get('sao', 'N/A')
    sao_khach = khach.get('sao', 'N/A')
    
    if sao_chu in SAO_CHI_TIET_THEO_CHU_DE:
        sao_data = SAO_CHI_TIET_THEO_CHU_DE[sao_chu].get(chu_de)
        if sao_data:
            dien_giai.append(f"⭐ {sao_chu}: {sao_data['Ý_Nghĩa']}")
            dien_giai.append(f"   → {sao_data['Khuyến_Nghị']}")
            if 'Dự_Báo' in sao_data:
                dien_giai.append(f"   → {sao_data['Dự_Báo']}")
    
    # 2. PHÂN TÍCH MÔN (BÁT MÔN)
    mon_chu = chu.get('cua', 'N/A')
    mon_khach = khach.get('cua', 'N/A')
    
    if mon_chu in MON_CHI_TIET_THEO_CHU_DE:
        mon_data = MON_CHI_TIET_THEO_CHU_DE[mon_chu].get(chu_de)
        if mon_data:
            dien_giai.append(f"\n🚪 {mon_chu} Môn: {mon_data['Ý_Nghĩa']}")
            dien_giai.append(f"   → {mon_data['Khuyến_Nghị']}")
            if 'Hành_Động' in mon_data:
                dien_giai.append(f"   ✅ Hành động: {mon_data['Hành_Động']}")
    
    # 3. PHÂN TÍCH NGŨ HÀNH (SINH KHẮC)
    dien_giai.append(f"\n🔄 Ngũ Hành: {mqh}")
    dien_giai_ngu_hanh = _phan_tich_ngu_hanh_theo_chu_de(chu_de, chu, khach, mqh)
    if dien_giai_ngu_hanh:
        dien_giai.append(dien_giai_ngu_hanh)
    
    # 4. PHÂN TÍCH THẦN (BÁT THẦN)
    than_chu = chu.get('than', 'N/A')
    than_khach = khach.get('than', 'N/A')
    
    dien_giai_than = _phan_tich_than_theo_chu_de(chu_de, than_chu, than_khach)
    if dien_giai_than:
        dien_giai.append(f"\n{dien_giai_than}")
    
    # 5. PHÂN TÍCH CAN CHI (CÁCH CỤC)
    can_thien = chu.get('can_thien', 'N/A')
    can_dia = chu.get('can_dia', 'N/A')
    
    dien_giai_can = _phan_tich_can_theo_chu_de(chu_de, can_thien, can_dia)
    if dien_giai_can:
        dien_giai.append(f"\n{dien_giai_can}")
    
    # 6. KẾT LUẬN TỔNG HỢP
    ket_luan = _tao_ket_luan_tong_hop(chu_de, chu, khach, mqh)
    if ket_luan:
        dien_giai.append(f"\n{ket_luan}")
    
    return "\n".join(dien_giai)


def _phan_tich_ngu_hanh_theo_chu_de(chu_de, chu, khach, mqh):
    """Phân tích Ngũ Hành theo từng chủ đề cụ thể"""
    
    if "Sinh" in mqh and khach['hanh'] in mqh.split()[0]:
        # Khách sinh Chủ
        if chu_de == "Đầu Tư Chứng Khoán":
            return "   → Thị trường đang tự sinh lời cho bạn. Chiến lược 'mua và giữ' trong 1-3 tháng sẽ mang lại lợi nhuận tốt."
        elif chu_de in ["Thi Đại Học", "Thi Tốt Nghiệp"]:
            return "   → Đề thi sẽ dễ hơn dự kiến. Tập trung vào các câu hỏi cơ bản và trung bình để đảm bảo không mất điểm."
        elif chu_de == "Xin Việc Làm":
            return "   → Công ty đang rất cần bạn. Hãy tự tin thể hiện bản thân và đưa ra mức lương mong muốn."
        elif chu_de == "Mua Nhà Đất":
            return "   → Nhà đất sinh bản mệnh. Giao dịch mua bán diễn ra suôn sẻ, bạn dễ dàng đàm phán được giá hời."
        elif chu_de == "Cầu Hôn Đính Hôn":
            return "   → Đối phương yêu bạn rất nhiều và đang mong chờ ngày này. Hãy mạnh dạn cầu hôn."
            
    elif "Sinh" in mqh and chu['hanh'] in mqh.split()[0]:
        # Chủ sinh Khách
        if chu_de == "Đầu Tư Chứng Khoán":
            return "   → Bạn đang bỏ ra nhiều vốn nhưng lợi nhuận chưa về ngay. Hãy kiên nhẫn ít nhất 2-4 tuần để thấy kết quả."
        elif chu_de in ["Thi Đại Học", "Thi Tốt Nghiệp"]:
            return "   → Bạn phải nỗ lực hết mình mới có thể đạt kết quả tốt. Đừng quá trông chờ vào sự may mắn."
        elif chu_de == "Cầu Hôn Đính Hôn":
            return "   → Bạn yêu nhiều hơn. Đối phương cũng có tình cảm nhưng cần thời gian suy nghĩ."
            
    elif "Khắc" in mqh and chu['hanh'] in mqh.split()[0]:
        # Chủ khắc Khách
        if chu_de == "Đầu Tư Chứng Khoán":
            return "   → Bạn đang nắm thế chủ động. Có thể dùng margin (vay ký quỹ) nhưng chỉ ở mức an toàn 30-40% giá trị tài khoản."
        elif chu_de == "Xin Việc Làm":
            return "   → Bạn đang ở thế chủ động. Có thể chọn lọc kỹ công ty và vị trí, không cần vội vàng nhận offer đầu tiên."
        elif chu_de == "Mua Nhà Đất":
            return "   → Bạn làm chủ cuộc chơi. Có thể ép giá xuống 10-15% so với giá rao bán. Chủ nhà đang cần bán gấp."
        elif chu_de == "Ly Hôn Chia Tay":
            return "   → Bạn có lợi thế. Trong phân chia tài sản và quyền nuôi con, bạn sẽ được ưu ái hơn."
            
    elif "Khắc" in mqh and khach['hanh'] in mqh.split()[0]:
        # Khách khắc Chủ
        if chu_de == "Đầu Tư Chứng Khoán":
            return "   → RỦI RO CAO: Thị trường đang đi ngược lại bạn. TUYỆT ĐỐI KHÔNG vay ký quỹ. Nên giảm tỷ trọng cổ phiếu xuống 50%."
        elif chu_de in ["Thi Đại Học", "Thi Tốt Nghiệp"]:
            return "   → Đề thi có thể khó hơn mong đợi. Cần ôn kỹ cả các phần nâng cao và luyện đề thi thử nhiều hơn."
        elif chu_de == "Mua Nhà Đất":
            return "   → CẢNH BÁO: Nhà đất khắc bản mệnh. Ở hoặc làm việc tại đây dễ sinh bất an, mệt mỏi. Cần hóa giải phong thủy."
        elif chu_de == "Phẫu Thuật":
            return "   → Cơ thể đang yếu, nguy cơ biến chứng cao hơn. Cần theo dõi sát sau mổ."
    
    return ""


def _phan_tich_than_theo_chu_de(chu_de, than_chu, than_khach):
    """Phân tích Bát Thần theo chủ đề"""
    
    dien_giai = []
    
    # Phân tích Thần Chủ
    if than_chu == "Lục Hợp":
        if chu_de in ["Cầu Hôn Đính Hôn", "Tình Duyên Hôn Nhân"]:
            dien_giai.append("💍 Lục Hợp lâm cung: Duyên phận đã định. Khả năng đối phương đồng ý là 95%.")
        elif chu_de == "Xin Việc Làm":
            dien_giai.append("🤝 Lục Hợp: Đồng nghiệp thân thiện, sếp dễ tính. Bạn sẽ hòa nhập nhanh.")
    
    elif than_chu == "Trực Phù":
        if chu_de in ["Thi Đại Học", "Thi Tốt Nghiệp"]:
            dien_giai.append("😌 Trực Phù: Tâm lý vững, bình tĩnh trong phòng thi, không bị áp lực.")
    
    elif than_chu == "Bạch Hổ":
        if chu_de in ["Thi Đại Học", "Thi Tốt Nghiệp"]:
            dien_giai.append("😰 Bạch Hổ: Áp lực cao, dễ căng thẳng. Cần luyện tập kỹ thuật thở sâu.")
        elif chu_de == "Xin Việc Làm":
            dien_giai.append("⚠️ Bạch Hổ: Môi trường căng thẳng, áp lực cao. Cần chuẩn bị tinh thần.")
        elif chu_de == "Ly Hôn Chia Tay":
            dien_giai.append("⚔️ Bạch Hổ: Xung đột gay gắt, nhiều tranh cãi và bạo lực lời nói.")
    
    elif than_chu == "Huyền Vũ":
        if chu_de == "Ly Hôn Chia Tay":
            dien_giai.append("🕵️ Huyền Vũ: Ngoại tình. Có dấu hiệu một bên hoặc cả hai có người thứ ba.")
    
    elif than_chu == "Đằng Xà":
        if chu_de == "Ly Hôn Chia Tay":
            dien_giai.append("🐍 Đằng Xà: Lừa dối. Một bên đã che giấu nhiều điều quan trọng (tài chính, quá khứ...).")
    
    elif than_chu == "Thái Âm":
        if chu_de == "Cầu Hôn Đính Hôn":
            dien_giai.append("🌙 Thái Âm: Đối phương đang có cảm xúc tốt. Nên cầu hôn trong không gian riêng tư, ấm cúng.")
    
    return "\n".join(dien_giai) if dien_giai else ""


def _phan_tich_can_theo_chu_de(chu_de, can_thien, can_dia):
    """Phân tích Can Thiên/Can Địa theo chủ đề"""
    
    dien_giai = []
    
    # Phân tích Can Thiên
    if can_thien == "Đinh" or can_dia == "Đinh":
        if chu_de in ["Thi Đại Học", "Thi Tốt Nghiệp"]:
            dien_giai.append("🔥 Can Đinh (Văn tinh): Đặc biệt tốt cho các môn khoa học tự nhiên (Lý, Hóa, Sinh). Cộng thêm 0.5-1.0 điểm.")
    
    elif can_thien == "Ất" or can_dia == "Ất":
        if chu_de in ["Thi Đại Học", "Thi Tốt Nghiệp"]:
            dien_giai.append("🌿 Can Ất (Văn xương): Tốt cho các môn xã hội (Văn, Sử, Địa). Cộng thêm 0.3-0.5 điểm.")
    
    elif can_thien == "Mậu" or can_dia == "Mậu":
        if chu_de in ["Đầu Tư Chứng Khoán", "Kinh Doanh Tổng Quát"]:
            dien_giai.append("💰 Can Mậu (Tài tinh): Vận may về tiền bạc. Thích hợp giải ngân hoặc thu hồi nợ.")
        elif chu_de == "Xin Việc Làm":
            dien_giai.append("💰 Can Mậu: Có thể đàm phán được mức lương cao hơn 10-15% so với đề xuất ban đầu.")
        elif chu_de == "Mua Nhà Đất":
            dien_giai.append("🏗️ Can Mậu: Nền móng vững chắc, chất lượng xây dựng tốt.")
    
    return "\n".join(dien_giai) if dien_giai else ""


def _tao_ket_luan_tong_hop(chu_de, chu, khach, mqh):
    """Tạo kết luận tổng hợp dựa trên tất cả yếu tố"""
    
    # Tính điểm tổng hợp (đơn giản)
    diem_chu = 50
    diem_khach = 50
    
    # Điểm từ Ngũ Hành
    if "Sinh" in mqh and khach['hanh'] in mqh.split()[0]:
        diem_chu += 20
    elif "Sinh" in mqh and chu['hanh'] in mqh.split()[0]:
        diem_chu -= 10
    elif "Khắc" in mqh and chu['hanh'] in mqh.split()[0]:
        diem_chu += 25
        diem_khach -= 25
    elif "Khắc" in mqh and khach['hanh'] in mqh.split()[0]:
        diem_chu -= 25
        diem_khach += 25
    
    # Điểm từ Môn
    mon_tot = ["Sinh", "Khai", "Cảnh", "Hưu"]
    mon_xau = ["Tử", "Kinh", "Thương"]
    
    if chu.get('cua') in mon_tot:
        diem_chu += 15
    elif chu.get('cua') in mon_xau:
        diem_chu -= 15
    
    # Kết luận
    ket_luan = "\n🎯 KẾT LUẬN TỔNG HỢP:\n"
    
    if diem_chu >= 70:
        ket_luan += "✅ TÌNH HÌNH CỰC KỲ THUẬN LỢI\n"
        ket_luan += _tao_khuyen_nghi_tich_cuc(chu_de)
    elif diem_chu >= 55:
        ket_luan += "✅ TÌNH HÌNH KHẤTỐT\n"
        ket_luan += _tao_khuyen_nghi_trung_binh(chu_de)
    elif diem_chu >= 45:
        ket_luan += "⚖️ TÌNH HÌNH TRUNG LẬP\n"
        ket_luan += _tao_khuyen_nghi_can_nhac(chu_de)
    else:
        ket_luan += "⚠️ TÌNH HÌNH KHÓ KHĂN\n"
        ket_luan += _tao_khuyen_nghi_than_trong(chu_de)
    
    return ket_luan


def _tao_khuyen_nghi_tich_cuc(chu_de):
    """Khuyến nghị khi tình hình tốt"""
    khuyen_nghi = {
        "Đầu Tư Chứng Khoán": "• Mua ngay, không chần chừ\n• Có thể tăng tỷ trọng lên 70%\n• Nắm giữ 3-6 tháng để tối đa hóa lợi nhuận",
        "Thi Đại Học": "• Tự tin vào khả năng của mình\n• Ngủ đủ giấc trước kỳ thi\n• Có thể đăng ký nguyện vọng cao hơn dự kiến",
        "Xin Việc Làm": "• Đàm phán mức lương cao hơn 10-15%\n• Yêu cầu các phúc lợi bổ sung\n• Có thể chọn lọc giữa nhiều offer",
        "Mua Nhà Đất": "• Đặt cọc ngay để giữ chỗ\n• Đàm phán giá tốt hơn 5-10%\n• Đây là cơ hội hiếm có",
        "Cầu Hôn Đính Hôn": "• Chuẩn bị nhẫn và lời cầu hôn lãng mạn\n• Chọn địa điểm có ý nghĩa\n• Khả năng thành công 95%"
    }
    return khuyen_nghi.get(chu_de, "• Hãy hành động ngay\n• Đây là thời điểm tốt\n• Tận dụng cơ hội")


def _tao_khuyen_nghi_trung_binh(chu_de):
    """Khuyến nghị khi tình hình khá tốt"""
    return "• Tình hình tốt nhưng cần cẩn trọng\n• Chuẩn bị kỹ càng trước khi hành động\n• Có thể tiến hành nhưng theo dõi sát"


def _tao_khuyen_nghi_can_nhac(chu_de):
    """Khuyến nghị khi tình hình trung lập"""
    return "• Cân nhắc kỹ trước khi quyết định\n• Thu thập thêm thông tin\n• Có thể đợi thêm 1-2 tuần để quan sát"


def _tao_khuyen_nghi_than_trong(chu_de):
    """Khuyến nghị khi tình hình khó khăn"""
    khuyen_nghi = {
        "Đầu Tư Chứng Khoán": "• KHÔNG mua thêm\n• Cắt lỗ nếu lỗ quá sâu (>15%)\n• Giữ tiền mặt 70%",
        "Mua Nhà Đất": "• KHÔNG NÊN MUA\n• Tìm bất động sản khác\n• Đợi thời điểm tốt hơn",
        "Phẫu Thuật": "• Hoãn nếu không cấp cứu\n• Tìm bác sĩ giỏi hơn\n• Tăng cường sức khỏe trước"
    }
    return khuyen_nghi.get(chu_de, "• Nên hoãn lại\n• Không hành động vội vàng\n• Đợi thời cơ tốt hơn")


# ============================================================================
# PHẦN 4: HÀM HỖ TRỢ
# ============================================================================

def lay_tri_thuc_master(chu_de):
    """Lấy tri thức từ Master Knowledge Database"""
    # Tích hợp với master_knowledge_database.py
    return KY_MON_MASTER_KNOWLEDGE.get("CACH_CUC_CHINH_XAC", {})


# Export
__all__ = ['tao_dien_giai_dong', 'SAO_CHI_TIET_THEO_CHU_DE', 'MON_CHI_TIET_THEO_CHU_DE']
