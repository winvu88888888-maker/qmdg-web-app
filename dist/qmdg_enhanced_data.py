# -*- coding: utf-8 -*-
"""
Kỳ Môn Độn Giáp - Enhanced Data Module
Dữ liệu chi tiết từ các nguồn chuẩn quốc tế:
- Joey Yap's Qi Men Dun Jia System
- Master Qimen (大师奇门)
- Cong Zhen Qimen (从真奇门)
- Classical texts and modern professional applications
"""

# ======================================================================
# CỬU TINH (NINE STARS) - DETAILED INTERPRETATIONS
# ======================================================================

DETAILED_NINE_STARS = {
    "Thiên Bồng": {
        "Hành": "Thủy",
        "Loại": "Hung Tinh",
        "Tính_Chất_Cơ_Bản": "Tướng quân, thích hợp trộm cướp, binh đao.",
        "Ý_Nghĩa_Chi_Tiết": """
Thiên Bồng là sao Thủy, tượng trưng cho sự ẩn náu, bí mật và chiến lược quân sự.
Trong thời cổ đại, đây là sao của các tướng lĩnh và chiến thuật.
Đại diện cho sự che giấu, bảo vệ, nhưng cũng có thể chỉ trộm cắp, lừa đảo.
        """,
        "Ứng_Dụng_Thực_Tế": {
            "Tốt_Cho": ["Chiến lược quân sự", "Bảo mật", "Điều tra", "An ninh", "Ẩn náu"],
            "Tránh": ["Khai trương", "Kết hôn", "Giao dịch công khai", "Xây dựng"],
            "Sự_Nghiệp": "Phù hợp với công việc bảo mật, điều tra, an ninh, quân đội",
            "Tài_Vận": "Không tốt cho cầu tài, dễ thất thoát",
            "Hôn_Nhân": "Không tốt, dễ có bí mật, ngoại tình"
        },
        "Kết_Hợp_Cung": {
            "Sinh_Cung": "Tốt, được cung hỗ trợ, giảm hung tính",
            "Khắc_Cung": "Xấu, hung tính tăng, nhiều trở ngại",
            "Cung_Sinh": "Trung bình, tiêu hao năng lượng",
            "Cung_Khắc": "Tốt, cung kiểm soát sao, giảm hung"
        },
        "Tham_Khảo": "Joey Yap's Qi Men Compendium, Master Qimen App"
    },
    
    "Thiên Nhậm": {
        "Hành": "Thổ",
        "Loại": "Hung Tinh",
        "Tính_Chất_Cơ_Bản": "Điền sản, tài lộc, chậm chạp.",
        "Ý_Nghĩa_Chi_Tiết": """
Thiên Nhậm là sao Thổ, tượng trưng cho đất đai, bất động sản và sự chậm rãi.
Mặc dù là hung tinh, nhưng có liên quan đến tài sản, đất đai.
Đại diện cho sự trì trệ, chậm chạp, nhưng cũng có tính ổn định.
        """,
        "Ứng_Dụng_Thực_Tế": {
            "Tốt_Cho": ["Mua đất", "Bất động sản", "Nông nghiệp", "Xây dựng nền móng"],
            "Tránh": ["Việc cần nhanh chóng", "Kinh doanh linh hoạt", "Du lịch"],
            "Sự_Nghiệp": "Phù hợp với bất động sản, nông nghiệp, xây dựng",
            "Tài_Vận": "Tốt cho tài sản lâu dài, đất đai",
            "Hôn_Nhân": "Chậm tiến triển, cần kiên nhẫn"
        },
        "Kết_Hợp_Cung": {
            "Sinh_Cung": "Tốt, được hỗ trợ, tài sản ổn định",
            "Khắc_Cung": "Xấu, mất tài sản, tranh chấp đất đai",
            "Cung_Sinh": "Trung bình, tiêu hao tài sản",
            "Cung_Khắc": "Tốt, kiểm soát được tài sản"
        },
        "Tham_Khảo": "Classical QMDJ texts, Cong Zhen Qimen"
    },
    
    "Thiên Xung": {
        "Hành": "Mộc",
        "Loại": "Tiểu Cát Tinh",
        "Tính_Chất_Cơ_Bản": "Năng động, tích cực, thích hợp khởi nghiệp.",
        "Ý_Nghĩa_Chi_Tiết": """
Thiên Xung là sao Mộc, tượng trưng cho sự năng động, tích cực và khởi đầu mới.
Là tiểu cát tinh với đặc tính hỗn hợp, vừa có mặt tốt vừa có thách thức.
Đại diện cho sự đột phá, tiến công, nhưng cũng có thể quá nóng vội.
        """,
        "Ứng_Dụng_Thực_Tế": {
            "Tốt_Cho": ["Khởi nghiệp", "Đầu tư", "Kinh doanh mới", "Thể thao", "Cạnh tranh"],
            "Tránh": ["Việc cần thận trọng", "Hợp đồng lâu dài", "Kết hôn"],
            "Sự_Nghiệp": "Phù hợp với doanh nhân, vận động viên, nhà đầu tư",
            "Tài_Vận": "Tốt cho đầu tư ngắn hạn, rủi ro cao",
            "Hôn_Nhân": "Nóng nảy, cần kiểm soát cảm xúc"
        },
        "Kết_Hợp_Cung": {
            "Sinh_Cung": "Rất tốt, năng lượng mạnh mẽ",
            "Khắc_Cung": "Cẩn thận, dễ thất bại",
            "Cung_Sinh": "Tốt, được hỗ trợ phát triển",
            "Cung_Khắc": "Xấu, bị kìm hãm"
        },
        "Tham_Khảo": "Douglas Chan's QMDJ Guide, Imperial Harvest"
    },
    
    "Thiên Phụ": {
        "Hành": "Mộc",
        "Loại": "Cát Tinh",
        "Tính_Chất_Cơ_Bản": "Trí tuệ, cố vấn, giáo dục, kế hoạch.",
        "Ý_Nghĩa_Chi_Tiết": """
Thiên Phụ là sao Mộc cát, tượng trưng cho trí tuệ, học vấn và sự cố vấn.
Là sao của các nhà tư vấn, giáo viên, và người lập kế hoạch.
Đại diện cho sự khôn ngoan, lịch sự, và tính chăm sóc người khác.
        """,
        "Ứng_Dụng_Thực_Tế": {
            "Tốt_Cho": ["Thi cử", "Giảng dạy", "Giáo dục", "Lập kế hoạch", "Tư vấn"],
            "Tránh": ["Hành động vội vàng", "Quyết định nhanh"],
            "Sự_Nghiệp": "Phù hợp với giáo viên, cố vấn, nhà hoạch định",
            "Tài_Vận": "Ổn định, thu nhập từ tri thức",
            "Hôn_Nhân": "Tốt, hòa hợp, tôn trọng lẫn nhau"
        },
        "Kết_Hợp_Cung": {
            "Sinh_Cung": "Rất tốt, trí tuệ phát triển",
            "Khắc_Cung": "Trung bình, cần nỗ lực hơn",
            "Cung_Sinh": "Tốt, được hỗ trợ",
            "Cung_Khắc": "Xấu, trí tuệ bị kìm hãm"
        },
        "Tham_Khảo": "Joey Yap's Mastery Academy, Master Qimen"
    },
    
    "Thiên Anh": {
        "Hành": "Hỏa",
        "Loại": "Cát Tinh",
        "Tính_Chất_Cơ_Bản": "Văn minh, danh vọng, hỏa hoạn.",
        "Ý_Nghĩa_Chi_Tiết": """
Thiên Anh là sao Hỏa cát, tượng trưng cho danh tiếng, văn hóa và ánh sáng.
Là sao của những người nổi tiếng, nghệ sĩ, và người có ảnh hưởng.
Đại diện cho sự rực rỡ, nổi bật, nhưng cũng cần cẩn thận hỏa hoạn.
        """,
        "Ứng_Dụng_Thực_Tế": {
            "Tốt_Cho": ["Quảng cáo", "Marketing", "Nghệ thuật", "Biểu diễn", "Truyền thông"],
            "Tránh": ["Công việc kín đáo", "Bí mật"],
            "Sự_Nghiệp": "Phù hợp với nghệ sĩ, diễn viên, marketer",
            "Tài_Vận": "Tốt, thu nhập từ danh tiếng",
            "Hôn_Nhân": "Rực rỡ nhưng cần cẩn thận tranh cãi"
        },
        "Kết_Hợp_Cung": {
            "Sinh_Cung": "Rất tốt, danh vọng tăng cao",
            "Khắc_Cung": "Cẩn thận, danh tiếng bị tổn hại",
            "Cung_Sinh": "Tốt, được hỗ trợ phát triển",
            "Cung_Khắc": "Xấu, bị kìm hãm"
        },
        "Tham_Khảo": "Feng Shui Ed, Entrieri QMDJ"
    },
    
    "Thiên Nhuế": {
        "Hành": "Thủy",
        "Loại": "Hung Tinh",
        "Tính_Chất_Cơ_Bản": "Mất mát, thất thoát, tài chính.",
        "Ý_Nghĩa_Chi_Tiết": """
Thiên Nhuế là sao Thủy hung, tượng trưng cho sự mất mát và thất thoát.
Là sao không tốt cho tài chính, dễ bị lừa đảo hoặc mất tiền.
Đại diện cho sự rò rỉ, thất thoát, không giữ được của cải.
        """,
        "Ứng_Dụng_Thực_Tế": {
            "Tốt_Cho": ["Không có việc đặc biệt tốt"],
            "Tránh": ["Đầu tư", "Kinh doanh", "Kết hôn", "Chuyển nhà"],
            "Sự_Nghiệp": "Khó khăn, dễ thất bại",
            "Tài_Vận": "Rất xấu, mất tiền, thất thoát",
            "Hôn_Nhân": "Không tốt, dễ ly hôn"
        },
        "Kết_Hợp_Cung": {
            "Sinh_Cung": "Giảm hung, nhưng vẫn cẩn thận",
            "Khắc_Cung": "Rất xấu, mất mát lớn",
            "Cung_Sinh": "Tiêu hao nhiều",
            "Cung_Khắc": "Tốt hơn, được kiểm soát"
        },
        "Tham_Khảo": "Classical texts, Douglas Chan"
    },
    
    "Thiên Trụ": {
        "Hành": "Kim",
        "Loại": "Hung Tinh",
        "Tính_Chất_Cơ_Bản": "Phá hoại, tranh chấp, bất lợi.",
        "Ý_Nghĩa_Chi_Tiết": """
Thiên Trụ là sao Kim hung, tượng trưng cho sự phá hoại và tranh chấp.
Là sao rất không tốt cho kinh doanh, hôn nhân, và các mối quan hệ.
Đại diện cho sự cãi vã, tranh luận, phá hủy, và quyết đoán thái quá.
        """,
        "Ứng_Dụng_Thực_Tế": {
            "Tốt_Cho": ["Phá bỏ cái cũ", "Kết thúc hợp đồng"],
            "Tránh": ["Kinh doanh", "Kết hôn", "Đàm phán", "Hợp tác"],
            "Sự_Nghiệp": "Gây tranh chấp, khó hợp tác",
            "Tài_Vận": "Xấu, mất tiền do tranh chấp",
            "Hôn_Nhân": "Rất xấu, cãi vã, ly hôn"
        },
        "Kết_Hợp_Cung": {
            "Sinh_Cung": "Giảm hung, nhưng vẫn cẩn thận",
            "Khắc_Cung": "Rất xấu, phá hoại lớn",
            "Cung_Sinh": "Tiêu hao, mất mát",
            "Cung_Khắc": "Tốt hơn, được kiểm soát"
        },
        "Tham_Khảo": "Master Qimen, Cong Zhen Qimen"
    },
    
    "Thiên Tâm": {
        "Hành": "Kim",
        "Loại": "Đại Cát Tinh",
        "Tính_Chất_Cơ_Bản": "Trí tuệ, lãnh đạo, hướng dẫn, nuôi dưỡng.",
        "Ý_Nghĩa_Chi_Tiết": """
Thiên Tâm là sao Kim đại cát, tượng trưng cho trí tuệ cao, lãnh đạo và sự hướng dẫn.
Là sao tốt nhất trong Cửu Tinh, đại diện cho người lãnh đạo có tâm.
Khi kết hợp với Sinh Môn, rất tốt cho vai trò lãnh đạo chiến lược.
        """,
        "Ứng_Dụng_Thực_Tế": {
            "Tốt_Cho": ["Lãnh đạo", "Quản lý", "Tư vấn", "Y tế", "Chăm sóc"],
            "Tránh": ["Không có việc cần tránh đặc biệt"],
            "Sự_Nghiệp": "Rất tốt, phù hợp lãnh đạo, quản lý cao cấp",
            "Tài_Vận": "Rất tốt, thu nhập ổn định và cao",
            "Hôn_Nhân": "Rất tốt, hòa hợp, chăm sóc lẫn nhau"
        },
        "Kết_Hợp_Cung": {
            "Sinh_Cung": "Rất tốt, phát triển mạnh mẽ",
            "Khắc_Cung": "Trung bình, cần nỗ lực",
            "Cung_Sinh": "Rất tốt, được hỗ trợ",
            "Cung_Khắc": "Giảm cát, nhưng vẫn tốt"
        },
        "Tham_Khảo": "Joey Yap, Douglas Chan, Imperial Harvest"
    },
    
    "Thiên Cầm": {
        "Hành": "Thổ",
        "Loại": "Hung Tinh",
        "Tính_Chất_Cơ_Bản": "Giam cầm, trì trệ, bệnh tật.",
        "Ý_Nghĩa_Chi_Tiết": """
Thiên Cầm là sao Thổ hung, tượng trưng cho sự giam cầm và trì trệ.
Thường nằm ở Trung Cung (Cung 5), đại diện cho sự bế tắc.
Không tốt cho mọi việc, đặc biệt là sức khỏe và tự do.
        """,
        "Ứng_Dụng_Thực_Tế": {
            "Tốt_Cho": ["Thiền định", "Tu luyện", "Nghỉ ngơi"],
            "Tránh": ["Mọi hoạt động quan trọng", "Du lịch", "Kinh doanh"],
            "Sự_Nghiệp": "Trì trệ, không tiến triển",
            "Tài_Vận": "Xấu, bị giam giữ tài sản",
            "Hôn_Nhân": "Không tốt, cảm giác bị gò bó"
        },
        "Kết_Hợp_Cung": {
            "Sinh_Cung": "Giảm hung nhẹ",
            "Khắc_Cung": "Rất xấu, bị giam cầm",
            "Cung_Sinh": "Tiêu hao năng lượng",
            "Cung_Khắc": "Tốt hơn, giảm trì trệ"
        },
        "Tham_Khảo": "Classical QMDJ texts"
    }
}

# ======================================================================
# BÁT MÔN (EIGHT DOORS) - DETAILED INTERPRETATIONS
# ======================================================================

DETAILED_EIGHT_DOORS = {
    "Khai": {
        "Loại": "Đại Cát Môn",
        "Ngũ_Hành": "Kim",
        "Tính_Chất_Cơ_Bản": "Thành công, tài lộc, cơ hội mở, tăng trưởng kinh doanh.",
        "Ý_Nghĩa_Chi_Tiết": """
Khai Môn là cửa mở, tượng trưng cho sự khởi đầu, cơ hội và thành công.
Là một trong ba cửa cát nhất (Khai, Hưu, Sinh), rất tốt cho kinh doanh.
Đại diện cho sự mở rộng, phát triển, vượt qua trở ngại, và đạt được mục tiêu.
        """,
        "Thời_Gian_Tốt": "Mọi thời điểm đều tốt khi gặp Khai Môn",
        "Việc_Nên_Làm": [
            "Khai trương kinh doanh",
            "Ký hợp đồng quan trọng",
            "Nhậm chức mới",
            "Xuất hành, du lịch",
            "Đàm phán, thương lượng",
            "Tìm kiếm cơ hội mới",
            "Mở rộng kinh doanh"
        ],
        "Việc_Tránh": [
            "Không có việc cần tránh đặc biệt",
            "Chỉ cần cẩn thận nếu kết hợp với hung tinh"
        ],
        "Kết_Hợp_Sao": {
            "Thiên Tâm": "Tuyệt vời, lãnh đạo thành công",
            "Thiên Phụ": "Rất tốt, trí tuệ và cơ hội",
            "Thiên Anh": "Tốt, danh vọng và thành công",
            "Thiên Xung": "Tốt, năng động và cơ hội",
            "Thiên Trụ": "Giảm cát, cẩn thận tranh chấp",
            "Thiên Nhuế": "Giảm cát, cẩn thận mất mát"
        },
        "Ứng_Dụng_Chủ_Đề": {
            "Sự_Nghiệp": "Rất tốt, thăng tiến, cơ hội mới",
            "Tài_Vận": "Rất tốt, thu nhập tăng, đầu tư thành công",
            "Hôn_Nhân": "Tốt, mở lòng, hòa hợp",
            "Sức_Khỏe": "Tốt, bệnh tật thuyên giảm",
            "Học_Tập": "Rất tốt, tiếp thu kiến thức mới",
            "Pháp_Lý": "Tốt, giải quyết thuận lợi"
        },
        "Tham_Khảo": "Douglas Chan, Scribd QMDJ Guide"
    },
    
    "Hưu": {
        "Loại": "Cát Môn",
        "Ngũ_Hành": "Thủy",
        "Tính_Chất_Cơ_Bản": "Nghỉ ngơi, hồi phục, thư giãn, ổn định.",
        "Ý_Nghĩa_Chi_Tiết": """
Hưu Môn là cửa nghỉ ngơi, tượng trưng cho sự hồi phục, chữa lành và bình an.
Rất tốt cho sức khỏe, chăm sóc bản thân, và nuôi dưỡng mối quan hệ.
Đại diện cho sự ổn định, tiến triển suôn sẻ, và hòa bình.
        """,
        "Thời_Gian_Tốt": "Tốt cho mọi thời điểm cần nghỉ ngơi, chữa bệnh",
        "Việc_Nên_Làm": [
            "Chữa bệnh, điều trị",
            "Nghỉ ngơi, thư giãn",
            "Chăm sóc sức khỏe",
            "Nuôi dưỡng mối quan hệ",
            "Kết hôn (ổn định)",
            "Ký hợp đồng lâu dài",
            "Đầu tư an toàn"
        ],
        "Việc_Tránh": [
            "Hành động vội vàng",
            "Quyết định nhanh chóng",
            "Cạnh tranh gay gắt"
        ],
        "Kết_Hợp_Sao": {
            "Thiên Tâm": "Rất tốt, lãnh đạo ổn định",
            "Thiên Phụ": "Rất tốt, trí tuệ và bình an",
            "Thiên Anh": "Tốt, danh vọng ổn định",
            "Thiên Bồng": "Giảm cát, cẩn thận bí mật",
            "Thiên Nhuế": "Giảm cát, cẩn thận mất mát"
        },
        "Ứng_Dụng_Chủ_Đề": {
            "Sự_Nghiệp": "Ổn định, phát triển đều đặn",
            "Tài_Vận": "Ổn định, thu nhập đều",
            "Hôn_Nhân": "Rất tốt, hòa hợp, bình yên",
            "Sức_Khỏe": "Rất tốt, hồi phục nhanh",
            "Học_Tập": "Tốt, tiếp thu ổn định",
            "Pháp_Lý": "Tốt, giải quyết hòa bình"
        },
        "Tham_Khảo": "Douglas Chan, Feng Shui Ed"
    },
    
    "Sinh": {
        "Loại": "Đại Cát Môn",
        "Ngũ_Hành": "Thổ",
        "Tính_Chất_Cơ_Bản": "Tăng trưởng, tài lộc, sức khỏe, thịnh vượng.",
        "Ý_Nghĩa_Chi_Tiết": """
Sinh Môn là cửa sinh trưởng, tượng trưng cho sự phát triển, thịnh vượng và cơ hội.
Là cửa tốt nhất cho tài chính, sức khỏe, và phát triển cá nhân.
Đại diện cho sự sinh sôi, nảy nở, khởi đầu mới, và tiềm năng lớn.
        """,
        "Thời_Gian_Tốt": "Mọi thời điểm đều tốt, đặc biệt cho cầu tài",
        "Việc_Nên_Làm": [
            "Cầu tài, đầu tư",
            "Kinh doanh mới",
            "Sinh con",
            "Trồng trọt",
            "Xây dựng",
            "Học tập mới",
            "Phát triển sản phẩm mới"
        ],
        "Việc_Tránh": [
            "Không có việc cần tránh đặc biệt",
            "Chỉ cần cẩn thận nếu kết hợp với hung tinh mạnh"
        ],
        "Kết_Hợp_Sao": {
            "Thiên Tâm": "Tuyệt vời, lãnh đạo phát triển",
            "Thiên Phụ": "Rất tốt, trí tuệ và tăng trưởng",
            "Thiên Anh": "Rất tốt, danh vọng và thịnh vượng",
            "Thiên Xung": "Rất tốt, năng động và phát triển",
            "Thiên Trụ": "Giảm cát, cẩn thận tranh chấp",
            "Thiên Nhuế": "Giảm cát, cẩn thận thất thoát"
        },
        "Ứng_Dụng_Chủ_Đề": {
            "Sự_Nghiệp": "Rất tốt, phát triển mạnh mẽ",
            "Tài_Vận": "Rất tốt, thu nhập tăng cao",
            "Hôn_Nhân": "Tốt, sinh sôi nảy nở",
            "Sức_Khỏe": "Rất tốt, sức khỏe dồi dào",
            "Học_Tập": "Rất tốt, tiếp thu nhanh",
            "Pháp_Lý": "Tốt, có lợi cho mình"
        },
        "Tham_Khảo": "Joey Yap, Douglas Chan, Imperial Harvest"
    },
    
    "Thương": {
        "Loại": "Hung Môn",
        "Ngũ_Hành": "Mộc",
        "Tính_Chất_Cơ_Bản": "Nguy hiểm, xung đột, thương tích, thất bại.",
        "Ý_Nghĩa_Chi_Tiết": """
Thương Môn là cửa thương tổn, tượng trưng cho nguy hiểm, xung đột và tổn thất.
Rất không tốt cho hầu hết các việc, dễ gây ra thương tích hoặc mất mát.
Đại diện cho sự tổn hại gây ra cho người khác hoặc bị người khác gây hại.
        """,
        "Thời_Gian_Tốt": "Không có thời gian tốt, nên tránh",
        "Việc_Nên_Làm": [
            "Săn bắn (thời cổ)",
            "Phá bỏ cái cũ",
            "Kết thúc mối quan hệ xấu"
        ],
        "Việc_Tránh": [
            "Khai trương",
            "Kết hôn",
            "Ký hợp đồng",
            "Đầu tư",
            "Du lịch",
            "Phẫu thuật",
            "Tranh tụng"
        ],
        "Kết_Hợp_Sao": {
            "Thiên Tâm": "Giảm hung, nhưng vẫn cẩn thận",
            "Thiên Phụ": "Giảm hung, trí tuệ giúp tránh nguy",
            "Thiên Trụ": "Rất xấu, phá hoại lớn",
            "Thiên Bồng": "Xấu, bí mật gây hại"
        },
        "Ứng_Dụng_Chủ_Đề": {
            "Sự_Nghiệp": "Xấu, thất bại, tranh chấp",
            "Tài_Vận": "Xấu, mất tiền, đầu tư thất bại",
            "Hôn_Nhân": "Rất xấu, xung đột, bạo lực",
            "Sức_Khỏe": "Rất xấu, thương tích, bệnh tật",
            "Học_Tập": "Xấu, khó tiếp thu",
            "Pháp_Lý": "Rất xấu, thua kiện"
        },
        "Tham_Khảo": "Scribd QMDJ, Classical texts"
    },
    
    "Đỗ": {
        "Loại": "Trung Bình Môn",
        "Ngũ_Hành": "Mộc",
        "Tính_Chất_Cơ_Bản": "Trở ngại, chậm trễ, bí mật, kết quả không mong đợi.",
        "Ý_Nghĩa_Chi_Tiết": """
Đỗ Môn là cửa tắc nghẽn, tượng trưng cho trở ngại, chậm trễ và bí mật.
Không tốt cho các việc cần tiến triển nhanh, nhưng tốt cho việc giữ bí mật.
Đại diện cho sự thiếu cơ hội, ẩn náu, hoặc kết quả không như mong đợi.
        """,
        "Thời_Gian_Tốt": "Tốt cho việc cần bí mật, ẩn náu",
        "Việc_Nên_Làm": [
            "Giữ bí mật",
            "Nghiên cứu kín",
            "Tu luyện",
            "Ẩn náu",
            "Bảo vệ tài sản"
        ],
        "Việc_Tránh": [
            "Khai trương",
            "Giao dịch công khai",
            "Tìm kiếm cơ hội",
            "Mở rộng kinh doanh",
            "Kết hôn"
        ],
        "Kết_Hợp_Sao": {
            "Thiên Tâm": "Giảm xấu, lãnh đạo khôn ngoan",
            "Thiên Phụ": "Tốt, nghiên cứu sâu",
            "Thiên Bồng": "Tốt, bí mật được bảo vệ",
            "Thiên Xung": "Xấu, năng lượng bị tắc"
        },
        "Ứng_Dụng_Chủ_Đề": {
            "Sự_Nghiệp": "Trì trệ, ít cơ hội",
            "Tài_Vận": "Trung bình, khó kiếm tiền",
            "Hôn_Nhân": "Không tốt, thiếu giao tiếp",
            "Sức_Khỏe": "Trung bình, bệnh ẩn",
            "Học_Tập": "Tốt cho nghiên cứu sâu",
            "Pháp_Lý": "Không tốt, bị che giấu sự thật"
        },
        "Tham_Khảo": "Douglas Chan, Scribd"
    },
    
    "Cảnh": {
        "Loại": "Trung Bình Môn",
        "Ngũ_Hành": "Hỏa",
        "Tính_Chất_Cơ_Bản": "Hiển thị, danh tiếng, sáng tạo, cũng có thể hời hợt.",
        "Ý_Nghĩa_Chi_Tiết": """
Cảnh Môn là cửa cảnh quan, tượng trưng cho sự hiển thị, danh tiếng và sáng tạo.
Tốt cho các việc liên quan đến hình ảnh, quảng cáo, nghệ thuật.
Đại diện cho sự rõ ràng, lộ diện, nhưng cũng có thể chỉ bề ngoài, hời hợt.
        """,
        "Thời_Gian_Tốt": "Tốt cho quảng cáo, truyền thông",
        "Việc_Nên_Làm": [
            "Quảng cáo",
            "Marketing",
            "Nghệ thuật",
            "Biểu diễn",
            "Truyền thông",
            "Tạo hình ảnh",
            "Sự kiện công khai"
        ],
        "Việc_Tránh": [
            "Giữ bí mật",
            "Hợp đồng kín",
            "Đầu tư dài hạn (nếu chỉ dựa vào bề ngoài)"
        ],
        "Kết_Hợp_Sao": {
            "Thiên Anh": "Rất tốt, danh vọng tăng cao",
            "Thiên Tâm": "Tốt, lãnh đạo có uy tín",
            "Thiên Phụ": "Tốt, trí tuệ được công nhận",
            "Thiên Nhuế": "Xấu, danh tiếng bị tổn"
        },
        "Ứng_Dụng_Chủ_Đề": {
            "Sự_Nghiệp": "Tốt cho nghề truyền thông, nghệ thuật",
            "Tài_Vận": "Trung bình, thu nhập từ hình ảnh",
            "Hôn_Nhân": "Rực rỡ bên ngoài, cần chất lượng bên trong",
            "Sức_Khỏe": "Trung bình, cần kiểm tra kỹ",
            "Học_Tập": "Tốt cho nghệ thuật, sáng tạo",
            "Pháp_Lý": "Trung bình, sự thật được lộ"
        },
        "Tham_Khảo": "Douglas Chan, Scribd"
    },
    
    "Tử": {
        "Loại": "Hung Môn",
        "Ngũ_Hành": "Thổ",
        "Tính_Chất_Cơ_Bản": "Kết thúc, đóng cửa, phá hủy, nguy hiểm, trì trệ.",
        "Ý_Nghĩa_Chi_Tiết": """
Tử Môn là cửa chết, tượng trưng cho sự kết thúc, phá hủy và nguy hiểm.
Rất không tốt cho hầu hết các việc, đặc biệt là khởi đầu mới.
Đại diện cho sự đóng cửa, dừng lại, năng lượng tiêu cực, và chậm trễ.
        """,
        "Thời_Gian_Tốt": "Không có, nên tránh hoàn toàn",
        "Việc_Nên_Làm": [
            "Kết thúc mối quan hệ xấu",
            "Phá bỏ cái cũ",
            "Tang lễ"
        ],
        "Việc_Tránh": [
            "Khai trương",
            "Kết hôn",
            "Sinh con",
            "Ký hợp đồng",
            "Đầu tư",
            "Du lịch",
            "Mọi việc quan trọng"
        ],
        "Kết_Hợp_Sao": {
            "Thiên Tâm": "Giảm hung, nhưng vẫn không tốt",
            "Thiên Phụ": "Giảm hung nhẹ",
            "Thiên Trụ": "Rất xấu, phá hoại cực lớn",
            "Thiên Nhuế": "Rất xấu, mất mát lớn"
        },
        "Ứng_Dụng_Chủ_Đề": {
            "Sự_Nghiệp": "Rất xấu, thất bại, kết thúc",
            "Tài_Vận": "Rất xấu, mất tiền, phá sản",
            "Hôn_Nhân": "Rất xấu, ly hôn, kết thúc",
            "Sức_Khỏe": "Rất xấu, bệnh nặng",
            "Học_Tập": "Rất xấu, thất bại",
            "Pháp_Lý": "Rất xấu, thua kiện nặng"
        },
        "Tham_Khảo": "Classical texts, Douglas Chan"
    },
    
    "Kinh": {
        "Loại": "Hung Môn",
        "Ngũ_Hành": "Kim",
        "Tính_Chất_Cơ_Bản": "Sợ hãi, lo lắng, nghi ngờ, cản trở.",
        "Ý_Nghĩa_Chi_Tiết": """
Kinh Môn là cửa kinh hoàng, tượng trưng cho sợ hãi, lo lắng và tranh chấp.
Không tốt cho hầu hết các việc, gây ra nghi ngờ và cản trở.
Đại diện cho sự tranh cãi, kiện tụng, sợ hãi, và kết quả không tốt.
        """,
        "Thời_Gian_Tốt": "Tốt cho kiện tụng (nếu muốn gây áp lực)",
        "Việc_Nên_Làm": [
            "Kiện tụng (nếu là nguyên đơn)",
            "Tranh cãi (nếu cần)",
            "Báo động",
            "Cảnh báo"
        ],
        "Việc_Tránh": [
            "Khai trương",
            "Kết hôn",
            "Ký hợp đồng hòa bình",
            "Đầu tư",
            "Hợp tác",
            "Đàm phán"
        ],
        "Kết_Hợp_Sao": {
            "Thiên Tâm": "Giảm hung, lãnh đạo khôn ngoan",
            "Thiên Phụ": "Giảm hung, trí tuệ giúp giải quyết",
            "Thiên Trụ": "Rất xấu, tranh chấp lớn",
            "Thiên Bồng": "Xấu, bí mật gây sợ hãi"
        },
        "Ứng_Dụng_Chủ_Đề": {
            "Sự_Nghiệp": "Xấu, tranh chấp, lo lắng",
            "Tài_Vận": "Xấu, lo lắng về tài chính",
            "Hôn_Nhân": "Xấu, cãi vã, nghi ngờ",
            "Sức_Khỏe": "Xấu, lo lắng, stress",
            "Học_Tập": "Xấu, sợ hãi, áp lực",
            "Pháp_Lý": "Tốt nếu là nguyên đơn, xấu nếu là bị đơn"
        },
        "Tham_Khảo": "Scribd, Classical texts"
    }
}

# Tiếp tục trong phần 2...
