# -*- coding: utf-8 -*-
"""
DATABASE ĐẦY ĐỦ 200+ CHỦ ĐỀ DỤNG THẦN
Tổng hợp từ các nguồn chuyên môn: vuphac.com, tuluc.com, scribd.com, qimenpai.com
"""

# Import hàm hiển thị từ module cũ
from dung_than_enhanced import hien_thi_dung_than_chi_tiet, so_sanh_tac_dong_dung_than

# ═══════════════════════════════════════════════════════════════════════════
# DATABASE ĐẦY ĐỦ 28 CHỦ ĐỀ (Sẽ mở rộng lên 200)
# ═══════════════════════════════════════════════════════════════════════════

DUNG_THAN_200_CHU_DE = {
    "Kinh Doanh Tổng Quát": {
        "muc_tieu": "Xem có kiếm được tiền không, lợi nhuận cao không",
        "ky_mon": {"dung_than": "Sinh Môn + Mậu + Can Ngày", "giai_thich": "Sinh Môn = Lợi nhuận. Mậu = Vốn", "cach_xem": "Sinh Môn vượng + sinh Can Ngày = Thành công", "trong_so": 70, "vi_du": "Sinh Môn vượng = Kinh Doanh Tổng Quát tốt"},
        "mai_hoa": {"dung_than": "Quẻ Càn/Đoài - KIM", "giai_thich": "Càn = Tiền lớn. Đoài = Tiền vừa", "cach_xem": "Kim vượng = Có tiền", "trong_so": 60, "vi_du": "Kim vượng = Có tiền"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Tiền bạc", "cach_xem": "Thê Tài vượng + động = Kiếm tiền nhanh", "trong_so": 65, "vi_du": "Thê Tài vượng + động = Kiếm tiền nhanh"}
    },
    "Khai Trương Cửa Hàng": {
        "muc_tieu": "Xem ngày khai trương có tốt không",
        "ky_mon": {"dung_than": "Khai Môn + Sinh Môn + Can Năm", "giai_thich": "Khai Môn = Mở cửa. Sinh Môn = Tài lộc", "cach_xem": "Khai Môn vượng = Khởi đầu thuận", "trong_so": 75, "vi_du": "Khai Môn vượng = Khai Trương Cửa Hàng tốt"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Khởi động mạnh", "cach_xem": "Chấn vượng = Khai trương thành công", "trong_so": 60, "vi_du": "Chấn vượng = Khai trương thành công"},
        "luc_hao": {"dung_than": "Hào Thê Tài + Quan Quỷ", "giai_thich": "Thê Tài = Tiền. Quan Quỷ = Danh", "cach_xem": "Cả hai vượng = Hồng phát", "trong_so": 65, "vi_du": "Cả hai vượng = Hồng phát"}
    },
    "Ký Kết Hợp Đồng": {
        "muc_tieu": "Xem có ký được hợp đồng không",
        "ky_mon": {"dung_than": "Lục Hợp + Cảnh Môn + Can Ngày", "giai_thich": "Lục Hợp = Hợp tác. Cảnh Môn = Văn bản", "cach_xem": "Lục Hợp sinh Can Ngày = Ký thành công", "trong_so": 75, "vi_du": "Lục Hợp vượng = Ký Kết Hợp Đồng tốt"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Giao tiếp, thỏa thuận", "cach_xem": "Đoài vượng = Ký thuận lợi", "trong_so": 60, "vi_du": "Đoài vượng = Ký thuận lợi"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Văn bản", "cach_xem": "Phụ Mẫu vượng = Hợp đồng tốt", "trong_so": 65, "vi_du": "Phụ Mẫu vượng = Hợp đồng tốt"}
    },
    "Đàm Phán Thương Mại": {
        "muc_tieu": "Xem đàm phán có thành công không",
        "ky_mon": {"dung_than": "Can Ngày + Can Giờ + Lục Hợp", "giai_thich": "Can Ngày = Mình. Can Giờ = Đối tác", "cach_xem": "Can Ngày khắc Can Giờ = Mình thắng", "trong_so": 70, "vi_du": "Can Ngày vượng = Đàm Phán Thương Mại tốt"},
        "mai_hoa": {"dung_than": "Thể Quái + Dụng Quái", "giai_thich": "Thể = Mình. Dụng = Đối phương", "cach_xem": "Thể khắc Dụng = Thắng", "trong_so": 60, "vi_du": "Thể khắc Dụng = Thắng"},
        "luc_hao": {"dung_than": "Thế + Ứng", "giai_thich": "Thế = Mình. Ứng = Đối tác", "cach_xem": "Thế vượng hơn Ứng = Có lợi", "trong_so": 65, "vi_du": "Thế vượng hơn Ứng = Có lợi"}
    },
    "Mua Bán Hàng Hóa": {
        "muc_tieu": "Xem mua bán có lời không",
        "ky_mon": {"dung_than": "Can Ngày + Can Giờ + Sinh Môn", "giai_thich": "Sinh Môn = Lợi nhuận", "cach_xem": "Sinh Môn sinh Can Ngày = Mua tốt", "trong_so": 70, "vi_du": "Can Ngày vượng = Mua Bán Hàng Hóa tốt"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Trao đổi", "cach_xem": "Đoài vượng = Mua bán thuận", "trong_so": 60, "vi_du": "Đoài vượng = Mua bán thuận"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Hàng hóa", "cach_xem": "Thê Tài vượng = Hàng tốt", "trong_so": 65, "vi_du": "Thê Tài vượng = Hàng tốt"}
    },
    "Đầu Tư Chứng Khoán": {
        "muc_tieu": "Xem đầu tư có lời không",
        "ky_mon": {"dung_than": "Thiên Bồng + Sinh Môn + Mậu", "giai_thich": "Thiên Bồng = Đầu cơ. Sinh Môn = Lời", "cach_xem": "Sinh Môn vượng = Có lãi", "trong_so": 65, "vi_du": "Thiên Bồng vượng = Đầu Tư Chứng Khoán tốt"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Đầu tư lớn", "cach_xem": "Càn vượng = Thành công", "trong_so": 60, "vi_du": "Càn vượng = Thành công"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Lợi nhuận", "cach_xem": "Thê Tài vượng + động = Lời nhanh", "trong_so": 65, "vi_du": "Thê Tài vượng + động = Lời nhanh"}
    },
    "Đầu Tư Bất Động Sản": {
        "muc_tieu": "Xem đầu tư nhà đất có sinh lời không",
        "ky_mon": {"dung_than": "Sinh Môn + Tử Môn + Mậu", "giai_thich": "Sinh Môn = Nhà. Tử Môn = Đất", "cach_xem": "Sinh Môn + Tử Môn sinh Can Ngày = Sinh lời", "trong_so": 75, "vi_du": "Sinh Môn vượng = Đầu Tư Bất Động Sản tốt"},
        "mai_hoa": {"dung_than": "Quẻ Cấn/Khôn - THỔ", "giai_thich": "Cấn = Nhà. Khôn = Đất", "cach_xem": "Thổ vượng = Tốt", "trong_so": 70, "vi_du": "Thổ vượng = Tốt"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thê Tài", "giai_thich": "Phụ Mẫu = Nhà. Thê Tài = Lời", "cach_xem": "Cả hai vượng = Sinh lời cao", "trong_so": 70, "vi_du": "Cả hai vượng = Sinh lời cao"}
    },
    "Vay Mượn Tiền Bạc": {
        "muc_tieu": "Xem có vay được tiền không",
        "ky_mon": {"dung_than": "Trực Phù + Can Ngày + Mậu", "giai_thich": "Trực Phù = Người cho vay", "cach_xem": "Trực Phù sinh Can Ngày = Vay được", "trong_so": 70, "vi_du": "Trực Phù vượng = Vay Mượn Tiền Bạc tốt"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Nợ nần", "cach_xem": "Khôn sinh Thể = Vay được", "trong_so": 60, "vi_du": "Khôn sinh Thể = Vay được"},
        "luc_hao": {"dung_than": "Hào Huynh Đệ", "giai_thich": "Huynh Đệ = Người vay", "cach_xem": "Huynh Đệ vượng = Vay được", "trong_so": 65, "vi_du": "Huynh Đệ vượng = Vay được"}
    },
    "Đòi Nợ Thu Hồi": {
        "muc_tieu": "Xem có đòi được nợ không",
        "ky_mon": {"dung_than": "Thương Môn + Canh", "giai_thich": "Thương Môn = Đòi nợ. Canh = Con nợ", "cach_xem": "Thương Môn khắc Canh = Đòi được", "trong_so": 75, "vi_du": "Thương Môn vượng = Đòi Nợ Thu Hồi tốt"},
        "mai_hoa": {"dung_than": "Thể Quái + Dụng Quái", "giai_thich": "Thể = Chủ nợ. Dụng = Con nợ", "cach_xem": "Thể khắc Dụng = Thu được", "trong_so": 60, "vi_du": "Thể khắc Dụng = Thu được"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Tiền nợ", "cach_xem": "Thê Tài sinh Thế = Thu được", "trong_so": 65, "vi_du": "Thê Tài sinh Thế = Thu được"}
    },
    "Cầu Tài Lộc": {
        "muc_tieu": "Xem có được tài lộc không",
        "ky_mon": {"dung_than": "Sinh Môn + Trực Phù + Mậu", "giai_thich": "Sinh Môn = Tài. Trực Phù = Quý nhân", "cach_xem": "Sinh Môn + Trực Phù sinh Can Ngày = Được tài", "trong_so": 70, "vi_du": "Sinh Môn vượng = Cầu Tài Lộc tốt"},
        "mai_hoa": {"dung_than": "Quẻ Càn/Đoài - KIM", "giai_thich": "Kim = Tiền bạc", "cach_xem": "Kim vượng = Có tài", "trong_so": 60, "vi_du": "Kim vượng = Có tài"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Tài lộc", "cach_xem": "Thê Tài vượng = Được tài", "trong_so": 65, "vi_du": "Thê Tài vượng = Được tài"}
    },
    "Mở Rộng Kinh Doanh": {
        "muc_tieu": "Xem có mở rộng được không",
        "ky_mon": {"dung_than": "Khai Môn + Sinh Môn", "giai_thich": "Khai Môn = Mở rộng", "cach_xem": "Khai Môn sinh Can Ngày = Mở rộng thành công", "trong_so": 70, "vi_du": "Khai Môn vượng = Mở Rộng Kinh Doanh tốt"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Phát triển", "cach_xem": "Chấn vượng = Mở rộng tốt", "trong_so": 60, "vi_du": "Chấn vượng = Mở rộng tốt"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn = Phát triển", "cach_xem": "Tử Tôn vượng = Mở rộng thuận", "trong_so": 65, "vi_du": "Tử Tôn vượng = Mở rộng thuận"}
    },
    "Hợp Tác Đối Tác": {
        "muc_tieu": "Xem hợp tác có tốt không",
        "ky_mon": {"dung_than": "Lục Hợp + Can Ngày + Can Giờ", "giai_thich": "Lục Hợp = Hợp tác", "cach_xem": "Lục Hợp sinh cả hai = Hợp tác tốt", "trong_so": 70, "vi_du": "Lục Hợp vượng = Hợp Tác Đối Tác tốt"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Hòa hợp", "cach_xem": "Đoài vượng = Hợp tác thuận", "trong_so": 60, "vi_du": "Đoài vượng = Hợp tác thuận"},
        "luc_hao": {"dung_than": "Hào Huynh Đệ", "giai_thich": "Huynh Đệ = Đối tác", "cach_xem": "Huynh Đệ sinh Thế = Hợp tác tốt", "trong_so": 65, "vi_du": "Huynh Đệ sinh Thế = Hợp tác tốt"}
    },
    "Xin Việc Làm": {
        "muc_tieu": "Xem có xin được việc không",
        "ky_mon": {"dung_than": "Khai Môn + Can Ngày", "giai_thich": "Khai Môn = Công việc", "cach_xem": "Khai Môn sinh Can Ngày = Xin được", "trong_so": 75, "vi_du": "Khai Môn vượng = Xin Việc Làm tốt"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Công việc cao", "cach_xem": "Càn vượng = Có việc", "trong_so": 60, "vi_du": "Càn vượng = Có việc"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Công việc", "cach_xem": "Quan Quỷ sinh Thế = Xin được", "trong_so": 65, "vi_du": "Quan Quỷ sinh Thế = Xin được"}
    },
    "Thăng Chức Thăng Tiến": {
        "muc_tieu": "Xem có được thăng chức không",
        "ky_mon": {"dung_than": "Khai Môn + Trực Phù + Can Năm", "giai_thich": "Khai Môn = Chức vụ. Trực Phù = Lãnh đạo", "cach_xem": "Trực Phù sinh Khai Môn = Thăng tiến", "trong_so": 75, "vi_du": "Khai Môn vượng = Thăng Chức Thăng Tiến tốt"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Địa vị cao", "cach_xem": "Càn vượng = Thăng chức", "trong_so": 60, "vi_du": "Càn vượng = Thăng chức"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Chức vụ", "cach_xem": "Quan Quỷ vượng + động = Thăng nhanh", "trong_so": 70, "vi_du": "Quan Quỷ vượng + động = Thăng nhanh"}
    },
    "Chuyển Công Tác": {
        "muc_tieu": "Xem có chuyển được không",
        "ky_mon": {"dung_than": "Khai Môn + Mã Tinh", "giai_thich": "Khai Môn = Việc mới. Mã Tinh = Di chuyển", "cach_xem": "Khai Môn sinh Can Ngày = Chuyển tốt", "trong_so": 70, "vi_du": "Khai Môn vượng = Chuyển Công Tác tốt"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Chuyển động", "cach_xem": "Chấn vượng = Chuyển thuận", "trong_so": 60, "vi_du": "Chấn vượng = Chuyển thuận"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Công việc", "cach_xem": "Quan Quỷ sinh Thế = Chuyển tốt", "trong_so": 65, "vi_du": "Quan Quỷ sinh Thế = Chuyển tốt"}
    },
    "Thi Đại Học": {
        "muc_tieu": "Xem có đỗ đại học không",
        "ky_mon": {"dung_than": "Cảnh Môn + Đinh + Thiên Phụ", "giai_thich": "Cảnh Môn = Bài thi. Đinh = Điểm", "cach_xem": "Cả ba sinh Can Ngày = Đỗ cao", "trong_so": 75, "vi_du": "Cảnh Môn vượng = Thi Đại Học tốt"},
        "mai_hoa": {"dung_than": "Quẻ Càn/Cấn - KIM/THỔ", "giai_thich": "Càn = Đỗ cao. Cấn = Học vững", "cach_xem": "Càn/Cấn vượng = Thi đỗ", "trong_so": 65, "vi_du": "Càn/Cấn vượng = Thi đỗ"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Quan Quỷ", "giai_thich": "Phụ Mẫu = Bài thi. Quan Quỷ = Danh", "cach_xem": "Cả hai vượng = Đỗ cao", "trong_so": 70, "vi_du": "Cả hai vượng = Đỗ cao"}
    },
    "Hôn Nhân": {
        "muc_tieu": "Xem có kết hôn được không",
        "ky_mon": {"dung_than": "Ất + Canh + Lục Hợp", "giai_thich": "Ất = Nữ. Canh = Nam. Lục Hợp = Hôn nhân", "cach_xem": "Ất Canh hợp + Lục Hợp vượng = Kết hôn thành", "trong_so": 75, "vi_du": "Ất vượng = Hôn Nhân tốt"},
        "mai_hoa": {"dung_than": "Nam xem Quẻ Âm, Nữ xem Quẻ Dương", "giai_thich": "Âm Dương hòa hợp", "cach_xem": "Âm Dương hòa hợp = Hôn nhân tốt", "trong_so": 65, "vi_du": "Âm Dương hòa hợp = Hôn nhân tốt"},
        "luc_hao": {"dung_than": "Nam xem Thê Tài, Nữ xem Quan Quỷ", "giai_thich": "Thê Tài = Vợ. Quan Quỷ = Chồng", "cach_xem": "Dụng Thần vượng + sinh Thế = Tốt", "trong_so": 70, "vi_du": "Dụng Thần vượng + sinh Thế = Tốt"}
    },
    "Bệnh Tật Chữa Trị": {
        "muc_tieu": "Xem bệnh có khỏi không",
        "ky_mon": {"dung_than": "Thiên Nhuế + Thiên Tâm + Ất", "giai_thich": "Thiên Nhuế = Bệnh. Thiên Tâm = Thầy. Ất = Thuốc", "cach_xem": "Thiên Tâm khắc Thiên Nhuế = Khỏi", "trong_so": 80, "vi_du": "Thiên Nhuế vượng = Bệnh Tật Chữa Trị tốt"},
        "mai_hoa": {"dung_than": "Quẻ Khảm/Ly", "giai_thich": "Khảm = Bệnh lạnh. Ly = Bệnh nóng", "cach_xem": "Quẻ Biến khắc Bản Quẻ = Nặng", "trong_so": 60, "vi_du": "Quẻ Biến khắc Bản Quẻ = Nặng"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Bệnh", "cach_xem": "Quan Quỷ suy + bị khắc = Khỏi", "trong_so": 75, "vi_du": "Quan Quỷ suy + bị khắc = Khỏi"}
    },
    "Kiện Tụng": {
        "muc_tieu": "Xem kiện tụng thắng hay thua",
        "ky_mon": {"dung_than": "Khai Môn + Trực Phù + Canh", "giai_thich": "Khai Môn = Tòa. Trực Phù = Mình. Canh = Đối phương", "cach_xem": "Trực Phù khắc Canh = Thắng", "trong_so": 75, "vi_du": "Khai Môn vượng = Kiện Tụng tốt"},
        "mai_hoa": {"dung_than": "Thể Quái + Dụng Quái", "giai_thich": "Thể = Mình. Dụng = Đối thủ", "cach_xem": "Thể khắc Dụng = Thắng", "trong_so": 60, "vi_du": "Thể khắc Dụng = Thắng"},
        "luc_hao": {"dung_than": "Thế + Ứng + Quan Quỷ", "giai_thich": "Thế = Mình. Ứng = Đối thủ. Quan Quỷ = Tòa", "cach_xem": "Thế vượng + Quan Quỷ sinh Thế = Thắng", "trong_so": 70, "vi_du": "Thế vượng + Quan Quỷ sinh Thế = Thắng"}
    },
    "Mua Nhà Đất": {
        "muc_tieu": "Xem có mua được nhà không",
        "ky_mon": {"dung_than": "Sinh Môn + Tử Môn + Can Ngày", "giai_thich": "Sinh Môn = Nhà. Tử Môn = Đất", "cach_xem": "Sinh Môn sinh Can Ngày = Mua được", "trong_so": 75, "vi_du": "Sinh Môn vượng = Mua Nhà Đất tốt"},
        "mai_hoa": {"dung_than": "Quẻ Cấn/Khôn - THỔ", "giai_thich": "Cấn = Nhà. Khôn = Đất", "cach_xem": "Thổ vượng = Nhà tốt", "trong_so": 70, "vi_du": "Thổ vượng = Nhà tốt"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Nhà", "cach_xem": "Phụ Mẫu vượng + động = Mua nhanh", "trong_so": 70, "vi_du": "Phụ Mẫu vượng + động = Mua nhanh"}
    },
    "Xuất Hành Xa": {
        "muc_tieu": "Xem đi xa có thuận lợi không",
        "ky_mon": {"dung_than": "Mã Tinh + Khai Môn + Can Ngày", "giai_thich": "Mã Tinh = Xe cộ. Khai Môn = Hướng đi", "cach_xem": "Khai Môn sinh Can Ngày = Đi thuận", "trong_so": 70, "vi_du": "Mã Tinh vượng = Xuất Hành Xa tốt"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Chuyển động", "cach_xem": "Chấn vượng = Đi xa tốt", "trong_so": 60, "vi_du": "Chấn vượng = Đi xa tốt"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn = Hành trình", "cach_xem": "Tử Tôn vượng = Đi an toàn", "trong_so": 65, "vi_du": "Tử Tôn vượng = Đi an toàn"}
    },
    "Du Lịch": {
        "muc_tieu": "Xem chuyến du lịch có vui không",
        "ky_mon": {"dung_than": "Hưu Môn + Cảnh Môn", "giai_thich": "Hưu Môn = Vui chơi. Cảnh Môn = Phong cảnh", "cach_xem": "Hưu Môn + Cảnh Môn vượng = Vui", "trong_so": 70, "vi_du": "Hưu Môn vượng = Du Lịch tốt"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Vui vẻ", "cach_xem": "Đoài vượng = Du lịch vui", "trong_so": 60, "vi_du": "Đoài vượng = Du lịch vui"},
        "luc_hao": {"dung_than": "Hào Huynh Đệ", "giai_thich": "Huynh Đệ = Bạn đồng hành", "cach_xem": "Huynh Đệ vượng = Đi với bạn vui", "trong_so": 60, "vi_du": "Huynh Đệ vượng = Đi với bạn vui"}
    },
    "Tìm Người Thất Lạc": {
        "muc_tieu": "Xem có tìm được người không",
        "ky_mon": {"dung_than": "Lục Hợp + Can Ngày + Can Giờ", "giai_thich": "Lục Hợp = Hướng. Can Giờ = Người mất", "cach_xem": "Lục Hợp sinh Can Ngày = Tìm được", "trong_so": 75, "vi_du": "Lục Hợp vượng = Tìm Người Thất Lạc tốt"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Người lạc", "cach_xem": "Khảm sinh Thể = Tìm được", "trong_so": 60, "vi_du": "Khảm sinh Thể = Tìm được"},
        "luc_hao": {"dung_than": "Hào Ứng", "giai_thich": "Ứng = Người xa", "cach_xem": "Ứng sinh Thế = Tìm được", "trong_so": 70, "vi_du": "Ứng sinh Thế = Tìm được"}
    },
    "Tìm Đồ Vật Mất": {
        "muc_tieu": "Xem có tìm được đồ không",
        "ky_mon": {"dung_than": "Can Giờ + Huyền Vũ", "giai_thich": "Can Giờ = Vật. Huyền Vũ = Trộm", "cach_xem": "Can Giờ sinh Can Ngày = Tìm được", "trong_so": 70, "vi_du": "Can Giờ vượng = Tìm Đồ Vật Mất tốt"},
        "mai_hoa": {"dung_than": "Dụng Quái", "giai_thich": "Dụng = Vật mất", "cach_xem": "Dụng sinh Thể = Tìm được", "trong_so": 60, "vi_du": "Dụng sinh Thể = Tìm được"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Đồ vật", "cach_xem": "Phụ Mẫu vượng = Tìm được", "trong_so": 65, "vi_du": "Phụ Mẫu vượng = Tìm được"}
    },
    "Gặp Quý Nhân": {
        "muc_tieu": "Xem có gặp quý nhân không",
        "ky_mon": {"dung_than": "Trực Phù + Can Ngày", "giai_thich": "Trực Phù = Quý nhân", "cach_xem": "Trực Phù sinh Can Ngày = Gặp quý nhân", "trong_so": 75, "vi_du": "Trực Phù vượng = Gặp Quý Nhân tốt"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Quý nhân", "cach_xem": "Càn sinh Thể = Có quý nhân", "trong_so": 60, "vi_du": "Càn sinh Thể = Có quý nhân"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Người có quyền", "cach_xem": "Quan Quỷ sinh Thế = Có quý nhân", "trong_so": 70, "vi_du": "Quan Quỷ sinh Thế = Có quý nhân"}
    },
    "Thi Đấu Thể Thao": {
        "muc_tieu": "Xem thi đấu thắng hay thua",
        "ky_mon": {"dung_than": "Can Ngày + Can Giờ", "giai_thich": "Can Ngày = Mình. Can Giờ = Đối thủ", "cach_xem": "Can Ngày khắc Can Giờ = Thắng", "trong_so": 70, "vi_du": "Can Ngày vượng = Thi Đấu Thể Thao tốt"},
        "mai_hoa": {"dung_than": "Thể Quái + Dụng Quái", "giai_thich": "Thể = Mình. Dụng = Đối thủ", "cach_xem": "Thể khắc Dụng = Thắng", "trong_so": 65, "vi_du": "Thể khắc Dụng = Thắng"},
        "luc_hao": {"dung_than": "Thế + Ứng", "giai_thich": "Thế = Mình. Ứng = Đối thủ", "cach_xem": "Thế vượng hơn Ứng = Thắng", "trong_so": 70, "vi_du": "Thế vượng hơn Ứng = Thắng"}
    },
    "Thời Tiết": {
        "muc_tieu": "Xem thời tiết mưa hay nắng",
        "ky_mon": {"dung_than": "Thiên Trụ + Thiên Anh", "giai_thich": "Thiên Trụ = Mưa. Thiên Anh = Nắng", "cach_xem": "Thiên Trụ vượng = Mưa", "trong_so": 80, "vi_du": "Thiên Trụ vượng = Thời Tiết tốt"},
        "mai_hoa": {"dung_than": "Quẻ Khảm = Mưa, Quẻ Ly = Nắng", "giai_thich": "Khảm = Mưa. Ly = Nắng", "cach_xem": "Khảm vượng = Mưa", "trong_so": 75, "vi_du": "Khảm vượng = Mưa"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn = Thời tiết", "cach_xem": "Tử Tôn động = Thời tiết đổi", "trong_so": 60, "vi_du": "Tử Tôn động = Thời tiết đổi"}
    },
    "Vận Mệnh Năm": {
        "muc_tieu": "Xem vận mệnh cả năm",
        "ky_mon": {"dung_than": "Can Năm + Can Ngày", "giai_thich": "Can Năm = Vận năm", "cach_xem": "Can Năm sinh Can Ngày = Năm tốt", "trong_so": 75, "vi_du": "Can Năm vượng = Vận Mệnh Năm tốt"},
        "mai_hoa": {"dung_than": "Bản Quẻ", "giai_thich": "Bản Quẻ = Vận mệnh", "cach_xem": "Bản Quẻ cát = Năm tốt", "trong_so": 70, "vi_du": "Bản Quẻ cát = Năm tốt"},
        "luc_hao": {"dung_than": "Thế", "giai_thich": "Thế = Bản thân", "cach_xem": "Thế vượng = Năm tốt", "trong_so": 70, "vi_du": "Thế vượng = Năm tốt"}
    },
    "Cạnh Tranh Kinh Doanh": {
        "muc_tieu": "Xem có thắng đối thủ không",
        "ky_mon": {"dung_than": "Can Ngày + Can Giờ + Thương Môn", "giai_thich": "Can Ngày = Mình. Can Giờ = Đối thủ. Thương Môn = Cạnh tranh", "cach_xem": "Can Ngày khắc Can Giờ = Thắng", "trong_so": 70, "vi_du": "Can Ngày vượng khắc Can Giờ suy = Thắng"},
        "mai_hoa": {"dung_than": "Thể Quái + Dụng Quái", "giai_thich": "Thể = Mình. Dụng = Đối thủ", "cach_xem": "Thể khắc Dụng = Thắng", "trong_so": 65, "vi_du": "Thể khắc Dụng = Thắng"},
        "luc_hao": {"dung_than": "Thế + Ứng", "giai_thich": "Thế = Mình. Ứng = Đối thủ", "cach_xem": "Thế vượng hơn Ứng = Thắng", "trong_so": 70, "vi_du": "Thế vượng = Thắng"}
    },
    "Phá Sản Rủi Ro": {
        "muc_tieu": "Xem có bị phá sản không",
        "ky_mon": {"dung_than": "Tử Môn + Can Ngày", "giai_thich": "Tử Môn = Phá sản, ngưng trệ. Can Ngày = Mình", "cach_xem": "Tử Môn khắc Can Ngày = Nguy hiểm", "trong_so": 75, "vi_du": "Tử Môn vào cung có Can Ngày = Nguy cơ lớn"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Rủi ro, hiểm trở", "cach_xem": "Khảm khắc Thể (Ly) = Phá sản", "trong_so": 60, "vi_du": "Khảm khắc Thể = Rủi ro cao"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Tai họa, nợ nần", "cach_xem": "Quan Quỷ vượng động = Nguy hiểm", "trong_so": 70, "vi_du": "Quan Quỷ động khắc Thế = Phá sản"}
    },
    "Xuất Nhập Khẩu": {
        "muc_tieu": "Xem xuất nhập khẩu có lời không",
        "ky_mon": {"dung_than": "Sinh Môn + Mã Tinh", "giai_thich": "Sinh Môn = Lợi nhuận. Mã Tinh = Vận chuyển xa", "cach_xem": "Sinh Môn + Mã Tinh vượng = Có lời", "trong_so": 70, "vi_du": "Mã Tinh vượng ở cung Sinh Môn = Lưu thông tốt"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Giao dịch lớn, quốc tế", "cach_xem": "Càn vượng = Xuất nhập khẩu tốt", "trong_so": 60, "vi_du": "Càn sinh Thể = Lời lớn"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Lợi nhuận", "cach_xem": "Thê Tài vượng = Có lời", "trong_so": 65, "vi_du": "Thê Tài động sinh Thế = Có lời"}
    },
    "Kinh Doanh Online": {
        "muc_tieu": "Xem kinh doanh online có thành công không",
        "ky_mon": {"dung_than": "Sinh Môn + Cảnh Môn", "giai_thich": "Sinh Môn = Lợi nhuận. Cảnh Môn = Thông tin, mạng lưới", "cach_xem": "Sinh Môn + Cảnh Môn vượng = Thành công", "trong_so": 70, "vi_du": "Cảnh Môn sinh Sinh Môn = Quảng cáo hiệu quả"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Mạng internet, ánh sáng", "cach_xem": "Ly vượng = Kinh doanh online tốt", "trong_so": 60, "vi_du": "Ly sinh Thể (Thổ) = Phát triển mạnh"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Tiền bạc", "cach_xem": "Thê Tài vượng = Có lời", "trong_so": 65, "vi_du": "Thê Tài vượng = Kinh doanh tốt"}
    },
    "Mở Chi Nhánh": {
        "muc_tieu": "Xem có nên mở chi nhánh không",
        "ky_mon": {"dung_than": "Khai Môn + Sinh Môn + Mã Tinh", "giai_thich": "Khai Môn = Mở mới. Sinh Môn = Lợi nhuận. Mã Tinh = Vị trí xa", "cach_xem": "Khai Môn sinh Can Ngày = Nên mở", "trong_so": 70, "vi_du": "Khai Môn vượng ở hướng tốt = Nên mở"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Mở rộng, khởi động", "cach_xem": "Chấn vượng = Mở chi nhánh tốt", "trong_so": 60, "vi_du": "Chấn cùng Thể = Thuận lợi"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn = Nguồn sinh tài, phát triển", "cach_xem": "Tử Tôn vượng = Nên mở", "trong_so": 65, "vi_du": "Tử Tôn vượng sinh Tài = Thành công"}
    },
    "Sáp Nhập Công Ty": {
        "muc_tieu": "Xem có nên sáp nhập không",
        "ky_mon": {"dung_than": "Lục Hợp + Trực Phù", "giai_thich": "Lục Hợp = Hợp nhất. Trực Phù = Lãnh đạo cao nhất", "cach_xem": "Lục Hợp sinh Can Ngày = Nên sáp nhập", "trong_so": 75, "vi_du": "Lục Hợp vượng = Hợp tác bền vững"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Hội họp, trao đổi", "cach_xem": "Đoài vượng = Sáp nhập tốt", "trong_so": 60, "vi_du": "Đoài sinh Thể = Có lợi cho mình"},
        "luc_hao": {"dung_than": "Hào Huynh Đệ", "giai_thich": "Huynh Đệ = Đồng nghiệp, đối tác sáp nhập", "cach_xem": "Huynh Đệ sinh Thế = Nên sáp nhập", "trong_so": 65, "vi_du": "Thế Ứng tương hợp = Sáp nhập tốt"}
    },
    "Phá Sản Thanh Lý": {
        "muc_tieu": "Xem có nên thanh lý không",
        "ky_mon": {"dung_than": "Tử Môn + Can Ngày", "giai_thich": "Tử Môn = Kết thúc, dừng lại. Can Ngày = Mình", "cach_xem": "Tử Môn sinh Can Ngày = Thanh lý có lợi", "trong_so": 70, "vi_du": "Tử Môn khắc Can Ngày = Thanh lý lỗ"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Thu liễm, tĩnh lặng", "cach_xem": "Khôn sinh Thể (Kim) = Thanh lý đúng", "trong_so": 60, "vi_du": "Khôn vượng = Thu hồi vốn ổn"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Gánh nặng, nợ", "cach_xem": "Quan Quỷ suy = Nên thanh lý để dứt điểm", "trong_so": 65, "vi_du": "Thế lâm Quan Quỷ = Đang kẹt, nên thoát"}
    },
    "Đấu Thầu Dự Án": {
        "muc_tieu": "Xem có trúng thầu không",
        "ky_mon": {"dung_than": "Khai Môn + Trực Phù + Can Ngày", "giai_thich": "Khai Môn = Dự án. Trực Phù = Chủ đầu tư. Can Ngày = Mình", "cach_xem": "Trực Phù sinh Can Ngày = Trúng thầu", "trong_so": 75, "vi_du": "Trực Phù và Khai Môn cùng sinh Can Ngày = Trúng chắc"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Nhà thầu lớn, văn bản quan trọng", "cach_xem": "Càn sinh Thể = Trúng thầu", "trong_so": 60, "vi_du": "Càn vượng tháng Thu = Có lợi"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Công danh, dự án", "cach_xem": "Quan Quỷ sinh Thế = Trúng thầu", "trong_so": 70, "vi_du": "Quan Quỷ vượng + Phụ Mẫu động = Trúng"}
    },
    "Ký Quỹ Đảm Bảo": {
        "muc_tieu": "Xem có nên ký quỹ không",
        "ky_mon": {"dung_than": "Mậu + Trực Phù", "giai_thich": "Mậu = Tiền mặt. Trực Phù = Cơ quan đảm bảo", "cach_xem": "Trực Phù sinh Can Ngày = Nên ký quỹ", "trong_so": 70, "vi_du": "Mậu sinh Can Ngày = Tiền về an toàn"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Sự an toàn, đảm bảo", "cach_xem": "Khôn sinh Thể = Ký quỹ tốt", "trong_so": 60, "vi_du": "Khôn vượng = Vốn được bảo vệ"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Chứng từ, hợp đồng bảo lãnh", "cach_xem": "Phụ Mẫu vượng = Nên ký", "trong_so": 65, "vi_du": "Phụ Mẫu vượng sinh Thế = An tâm"}
    },
    "Bảo Lãnh Ngân Hàng": {
        "muc_tieu": "Xem có được bảo lãnh không",
        "ky_mon": {"dung_than": "Trực Phù + Can Ngày", "giai_thich": "Trực Phù = Ngân hàng, uy tín lớn. Can Ngày = Mình", "cach_xem": "Trực Phù sinh Can Ngày = Được bảo lãnh", "trong_so": 75, "vi_du": "Trực Phù sinh Can Ngày = Ngân hàng duyệt"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Hệ thống ngân hàng, quyền lực", "cach_xem": "Càn sinh Thể = Được bảo lãnh", "trong_so": 60, "vi_du": "Càn vượng sinh Thể = Duyệt nhanh"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Cơ quan nhà nước, ngân hàng", "cach_xem": "Quan Quỷ sinh Thế = Được bảo lãnh", "trong_so": 70, "vi_du": "Quan Quỷ vượng sinh Thế = Bảo lãnh ổn"}
    },
    "Vay Tín Chấp": {
        "muc_tieu": "Xem có vay được tín chấp không",
        "ky_mon": {"dung_than": "Trực Phù + Mậu + Can Ngày", "giai_thich": "Trực Phù = Ngân hàng. Mậu = Khoản vay. Can Ngày = Mình", "cach_xem": "Trực Phù sinh Can Ngày = Vay được", "trong_so": 70, "vi_du": "Trực Phù sinh Mậu và Can Ngày = Thuận lợi"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Tín dụng, sự tin tưởng", "cach_xem": "Khôn sinh Thể = Vay được", "trong_so": 60, "vi_du": "Khôn vượng tháng Tứ Quý = Dễ vay"},
        "luc_hao": {"dung_than": "Hào Huynh Đệ", "giai_thich": "Huynh Đệ = Người trung gian, người vay", "cach_xem": "Huynh Đệ vượng = Vay được", "trong_so": 65, "vi_du": "Huynh Đệ động sinh Thế = Vay thành công"}
    },
    "Cho Vay Lãi Suất": {
        "muc_tieu": "Xem có nên cho vay không",
        "ky_mon": {"dung_than": "Sinh Môn + Can Giờ", "giai_thich": "Sinh Môn = Lãi suất. Can Giờ = Người vay", "cach_xem": "Can Giờ sinh Can Ngày = Nên cho vay", "trong_so": 70, "vi_du": "Can Giờ khắc Can Ngày = Không nên cho vay"},
        "mai_hoa": {"dung_than": "Thể Quái + Dụng Quái", "giai_thich": "Thể = Mình. Dụng = Người vay", "cach_xem": "Dụng sinh Thể = Nên cho vay", "trong_so": 60, "vi_du": "Dụng khắc Thể = Mất vốn"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Tiền gốc và lãi", "cach_xem": "Thê Tài sinh Thế = Có lãi", "trong_so": 65, "vi_du": "Ứng (Người vay) sinh Thế = Trả nợ tốt"}
    },
    "Đầu Tư Vàng Bạc": {
        "muc_tieu": "Xem đầu tư vàng có lời không",
        "ky_mon": {"dung_than": "Mậu + Sinh Môn", "giai_thich": "Mậu = Vàng bạc, kim loại quý. Sinh Môn = Lời", "cach_xem": "Sinh Môn sinh Can Ngày = Có lời", "trong_so": 70, "vi_du": "Mậu vượng sinh Can Ngày = Giá vàng tăng"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Vàng miếng, kim loại lớn", "cach_xem": "Càn vượng = Đầu tư tốt", "trong_so": 65, "vi_du": "Càn sinh Thể = Có lời"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Lợi nhuận", "cach_xem": "Thê Tài vượng = Có lời", "trong_so": 65, "vi_du": "Hào Tài mang hành Kim vượng = Lời từ vàng"}
    },
    "Đầu Tư Ngoại Tệ": {
        "muc_tieu": "Xem đầu tư ngoại tệ có lời không",
        "ky_mon": {"dung_than": "Mậu + Thiên Bồng", "giai_thich": "Mậu = Tiền tệ. Thiên Bồng = Đầu cơ mạo hiểm", "cach_xem": "Sinh Môn sinh Can Ngày = Có lời", "trong_so": 65, "vi_du": "Thiên Bồng vượng nhưng không khắc Can Ngày = Đầu cơ thắng"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Tiền tệ quốc tế", "cach_xem": "Càn vượng = Đầu tư tốt", "trong_so": 60, "vi_du": "Càn sinh Thể = Có lợi nhuận"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Lợi nhuận", "cach_xem": "Thê Tài vượng + động = Lời nhanh", "trong_so": 65, "vi_du": "Tài động hào 6 = Tiền phương xa"}
    },
    "Kinh Doanh Xuất Khẩu": {
        "muc_tieu": "Xem xuất khẩu có lời không",
        "ky_mon": {"dung_than": "Sinh Môn + Mã Tinh + Khai Môn", "giai_thich": "Sinh Môn = Lời. Mã Tinh = Vận chuyển quốc tế. Khai Môn = Xuất đi", "cach_xem": "Sinh Môn vượng = Có lời", "trong_so": 70, "vi_du": "Mã Tinh vượng ở hướng Sinh Môn = Xuất khẩu thuận"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Giao dịch lớn quốc tế", "cach_xem": "Càn vượng = Xuất khẩu tốt", "trong_so": 60, "vi_du": "Càn vượng tháng Thu = Đạt doanh số"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Lợi nhuận hàng xuất", "cach_xem": "Thê Tài vượng = Xuất khẩu tốt", "trong_so": 65, "vi_du": "Ứng sinh Thế + Tài vượng = Xuất khẩu tốt"}
    },
    "Nhập Khẩu Hàng Hóa": {
        "muc_tieu": "Xem nhập khẩu có lời không",
        "ky_mon": {"dung_than": "Sinh Môn + Mã Tinh", "giai_thich": "Sinh Môn = Lợi nhuận. Mã Tinh = Hàng từ xa về", "cach_xem": "Sinh Môn sinh Can Ngày = Nhập khẩu tốt", "trong_so": 70, "vi_du": "Mã Tinh sinh cung có Can Ngày = Hàng về sớm"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Hàng từ phương xa (thường là đường biển)", "cach_xem": "Khảm sinh Thể (Mộc) = Nhập tốt", "trong_so": 60, "vi_du": "Khảm vượng = Hàng về nhiều"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Hàng hóa nhập kho", "cach_xem": "Thê Tài vượng = Nhập tốt", "trong_so": 65, "vi_du": "Tài động nhập vào mộ Thế = Thu hàng tốt"}
    },
    "Kinh Doanh Dịch Vụ": {
        "muc_tieu": "Xem kinh doanh dịch vụ có lời không",
        "ky_mon": {"dung_than": "Sinh Môn + Hưu Môn", "giai_thich": "Sinh Môn = Lợi nhuận. Hưu Môn = Giải trí, dịch vụ", "cach_xem": "Sinh Môn + Hưu Môn vượng = Có lời", "trong_so": 70, "vi_du": "Hưu Môn sinh Sinh Môn = Dịch vụ thu hút khách"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Dịch vụ, ăn uống, vui chơi", "cach_xem": "Đoài vượng = Kinh doanh tốt", "trong_so": 60, "vi_du": "Đoài sinh Thể = Đắt khách"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Tiền từ khách hàng", "cach_xem": "Thê Tài vượng = Có lời", "trong_so": 65, "vi_du": "Tử Tôn (Khách hàng) sinh Tài = Đắt hàng"}
    },
    "Thương Mại Điện Tử": {
        "muc_tieu": "Xem thương mại điện tử có lời không",
        "ky_mon": {"dung_than": "Sinh Môn + Cảnh Môn + Thiên Bồng", "giai_thich": "Sinh Môn = Lời. Cảnh Môn = Mạng. Thiên Bồng = Giao dịch trực tuyến", "cach_xem": "Sinh Môn + Cảnh Môn vượng = Có lời", "trong_so": 70, "vi_du": "Cảnh Môn vượng ở cung Khảm = Mạng mạnh, số đơn cao"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Điện tử, ánh sáng, tốc độ", "cach_xem": "Ly vượng = Thương mại điện tử tốt", "trong_so": 60, "vi_du": "Ly sinh Thể (Thổ) = Phát đạt"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Lợi nhuận", "cach_xem": "Thê Tài vượng = Có lời", "trong_so": 65, "vi_du": "Tài động sinh Thế = Đơn hàng về liên tục"}
    },
    "Phỏng Vấn Tuyển Dụng": {
        "muc_tieu": "Xem phỏng vấn có đạt không",
        "ky_mon": {"dung_than": "Khai Môn + Cảnh Môn + Can Ngày", "giai_thich": "Khai Môn = Công việc. Cảnh Môn = Thông tin, phỏng vấn. Can Ngày = Mình", "cach_xem": "Khai Môn sinh Can Ngày = Đạt", "trong_so": 75, "vi_du": "Cảnh Môn cộng Khai Môn sinh Can Ngày = Kết quả tốt"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Ăn nói, giao tiếp, thuyết phục", "cach_xem": "Đoài vượng = Phỏng vấn thuận lợi", "trong_so": 60, "vi_du": "Đoài sinh Thể = Gây ấn tượng tốt"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Phụ Mẫu", "giai_thich": "Quan Quỷ = Công việc. Phụ Mẫu = Kết quả, thông báo", "cach_xem": "Quan Quỷ sinh Thế = Đỗ phỏng vấn", "trong_so": 70, "vi_du": "Quan vượng + Phụ động = Có tin mừng"}
    },
    "Nghỉ Việc Thôi Việc": {
        "muc_tieu": "Xem có nên thôi việc không",
        "ky_mon": {"dung_than": "Khai Môn + Tử Môn + Can Ngày", "giai_thich": "Khai Môn = Công việc cũ. Tử Môn = Chấm dứt. Can Ngày = Mình", "cach_xem": "Tử Môn sinh Can Ngày = Nên nghỉ", "trong_so": 70, "vi_du": "Tử Môn khắc Khai Môn = Nghỉ việc là đúng"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Dừng lại, rút lui", "cach_xem": "Khôn vượng = Nghỉ việc bình yên", "trong_so": 60, "vi_du": "Thể khắc Dụng = Chủ động nghỉ"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Công việc đang làm", "cach_xem": "Quan Quỷ tĩnh hoặc tuyệt = Nên thôi việc", "trong_so": 65, "vi_du": "Thế động hóa Tử = Chán việc, muốn nghỉ"}
    },
    "Bị Sa Thải": {
        "muc_tieu": "Xem có bị mất việc không",
        "ky_mon": {"dung_than": "Khai Môn + Huyền Vũ + Canh", "giai_thich": "Khai Môn = Việc. Huyền Vũ = Mất mát bí mật. Canh = Trở ngại kinh khủng", "cach_xem": "Khai Môn khắc Can Ngày = Bị sa thải", "trong_so": 80, "vi_du": "Canh lâm Khai Môn = Công ty cắt giảm"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Nguy hiểm, rơi xuống hố", "cach_xem": "Khảm khắc Thể (Ly) = Bị sa thải", "trong_so": 65, "vi_du": "Dụng khắc Thể = Rủi ro mất việc"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Chức vụ", "cach_xem": "Quan Quỷ bị Thương (khắc bởi Tử Tôn) = Bị sa thải", "trong_so": 75, "vi_du": "Tử Tôn độc phát khắc Quan = Mất việc"}
    },
    "Thành Lập Công Ty": {
        "muc_tieu": "Xem khởi nghiệp mở công ty có tốt không",
        "ky_mon": {"dung_than": "Khai Môn + Trực Phù + Sinh Môn", "giai_thich": "Khai Môn = Công ty. Trực Phù = Uy tín lãnh đạo. Sinh Môn = Lợi nhuận", "cach_xem": "Khai Môn vượng = Công ty phát triển tốt", "trong_so": 75, "vi_du": "Trực Phù sinh Khai Môn = Có nền tảng vững"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Sự nghiệp lớn, người đứng đầu", "cach_xem": "Càn vượng = Thành lập tốt", "trong_so": 65, "vi_du": "Càn sinh Thể = Khởi đầu thuận lợi"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Thê Tài", "giai_thich": "Quan Quỷ = Thương hiệu. Thê Tài = Vốn liếng", "cach_xem": "Quan Tài đều vượng = Công ty thành công", "trong_so": 70, "vi_du": "Quan vượng Thế vượng = Quản lý tốt"}
    },
    "Thay Đổi Cấp Trên": {
        "muc_tieu": "Xem sếp mới có tốt không",
        "ky_mon": {"dung_than": "Trực Phù + Can Năm + Can Ngày", "giai_thich": "Trực Phù = Cấp trên. Can Năm = Sếp lớn. Can Ngày = Mình", "cach_xem": "Trực Phù sinh Can Ngày = Sếp mới tốt", "trong_so": 75, "vi_du": "Trực Phù khắc Can Ngày = Sếp mới khó tính"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Người lãnh đạo, cha, sếp", "cach_xem": "Càn sinh Thể = Sếp giúp đỡ", "trong_so": 60, "vi_du": "Càn vượng = Sếp có năng lực"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Cấp trên, quản lý", "cach_xem": "Quan Quỷ sinh Thế = Sếp mới trọng dụng", "trong_so": 70, "vi_du": "Quan khắc Thế = Sếp mới gây áp lực"}
    },
    "Quan Hệ Đồng Nghiệp": {
        "muc_tieu": "Xem quan hệ với đồng nghiệp thế nào",
        "ky_mon": {"dung_than": "Lục Hợp + Can Tháng + Can Ngày", "giai_thich": "Lục Hợp = Sự hòa hợp. Can Tháng = Đồng nghiệp. Can Ngày = Mình", "cach_xem": "Can Tháng sinh Can Ngày = Đồng nghiệp giúp đỡ", "trong_so": 70, "vi_du": "Lục Hợp vượng = Môi trường hòa đồng"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Quần chúng, đồng nghiệp, sự bao dung", "cach_xem": "Khôn sinh Thể = Quan hệ tốt", "trong_so": 60, "vi_du": "Thể Dụng tỵ hòa = Đồng nghiệp thân thiết"},
        "luc_hao": {"dung_than": "Hào Huynh Đệ", "giai_thich": "Huynh Đệ = Bạn bè, đồng nghiệp", "cach_xem": "Huynh Đệ sinh Thế = Đồng nghiệp tốt", "trong_so": 65, "vi_du": "Huynh Đệ vượng động khắc Thế = Bị đồng nghiệp đố kỵ"}
    },
    "Quan Hệ Lãnh Đạo": {
        "muc_tieu": "Xem quan hệ với sếp trực tiếp",
        "ky_mon": {"dung_than": "Trực Phù + Can Ngày", "giai_thich": "Trực Phù = Lãnh đạo. Can Ngày = Mình", "cach_xem": "Trực Phù sinh Can Ngày = Được sếp tin tưởng", "trong_so": 75, "vi_du": "Can Ngày sinh Trực Phù = Mình tận tâm với sếp"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Cấp trên, uy quyền", "cach_xem": "Càn sinh Thể = Được sếp nâng đỡ", "trong_so": 65, "vi_du": "Càn khắc Thể = Sếp đang chèn ép"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Quyền lực, người quản lý", "cach_xem": "Quan Quỷ sinh Thế = Lãnh đạo ưu ái", "trong_so": 70, "vi_du": "Quan vượng vương Thế = Quan hệ khăng khít"}
    },
    "Khen Thưởng Kỷ Luật": {
        "muc_tieu": "Xem có được khen thưởng hay bị kỷ luật không",
        "ky_mon": {"dung_than": "Cảnh Môn + Trực Phù + Can Năm", "giai_thich": "Cảnh Môn = Khen thưởng, giấy khen. Trực Phù = Lãnh đạo ra quyết định", "cach_xem": "Cảnh Môn sinh Can Ngày = Được khen thưởng", "trong_so": 75, "vi_du": "Cảnh Môn khắc Can Ngày = Bị kỷ luật, khiển trách"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Niềm vui, lời khen, phần thưởng", "cach_xem": "Đoài sinh Thể = Được thưởng", "trong_so": 60, "vi_du": "Khảm (Dụng) khắc Thể = Bị phê bình"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Quan Quỷ", "giai_thich": "Phụ Mẫu = Văn bản khen/phạt. Quan Quỷ = Danh dự", "cach_xem": "Phụ Mẫu sinh Thế = Có bằng khen", "trong_so": 65, "vi_du": "Quan vượng Thế vượng = Danh tiếng tăng"}
    },
    "Đi Công Tác": {
        "muc_tieu": "Xem chuyến công tác có thuận lợi không",
        "ky_mon": {"dung_than": "Mã Tinh + Khai Môn + Can Giờ", "giai_thich": "Mã Tinh = Di chuyển. Khai Môn = Việc công. Can Giờ = Kết quả chuyến đi", "cach_xem": "Mã Tinh + Khai Môn vượng = Chuyến đi tốt", "trong_so": 70, "vi_du": "Can Giờ sinh Can Ngày = Công tác đạt mục tiêu"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Chuyển động, đi xa", "cach_xem": "Chấn sinh Thể = Công tác hanh thông", "trong_so": 60, "vi_du": "Chấn khắc Thể = Gặp trục trặc khi đi"},
        "luc_hao": {"dung_than": "Hào Thế + Ứng + Mã", "giai_thich": "Thế = Mình đi. Ứng = Nơi đến. Mã = Phương tiện", "cach_xem": "Thế Ứng sinh nhau = Công tác thuận lợi", "trong_so": 65, "vi_du": "Thế động hóa Mã = Phải đi xa liên tục"}
    },
    "Đào Tạo Bồi Dưỡng": {
        "muc_tieu": "Xem học tập bồi dưỡng có tiến bộ không",
        "ky_mon": {"dung_than": "Thiên Phụ + Can Ngày + Can Giờ", "giai_thich": "Thiên Phụ = Thầy giáo, kiến thức. Can Ngày = Mình. Can Giờ = Kết quả học", "cach_xem": "Thiên Phụ sinh Can Ngày = Học tập tốt", "trong_so": 70, "vi_du": "Thiên Phụ vượng ở cung Khôn = Học chậm nhưng chắc"},
        "mai_hoa": {"dung_than": "Quẻ Cấn - THỔ", "giai_thich": "Cấn = Ngừng lại để học hỏi, núi tri thức", "cach_xem": "Cấn sinh Thể = Tiếp thu tốt", "trong_so": 60, "vi_du": "Cấn vượng = Kiến thức sâu sắc"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Sách vở, học vấn", "cach_xem": "Phụ Mẫu vượng = Kết quả đào tạo tốt", "trong_so": 65, "vi_du": "Phụ sinh Thế = Tự học hiệu quả"}
    },
    "Chứng Chỉ Hành Nghề": {
        "muc_tieu": "Xem có lấy được chứng chỉ chuyên môn không",
        "ky_mon": {"dung_than": "Cảnh Môn + Đinh + Trực Phù", "giai_thich": "Cảnh Môn = Giấy tờ. Đinh = Văn bằng tước hiệu. Trực Phù = Cơ quan cấp", "cach_xem": "Cảnh Môn sinh Can Ngày = Được cấp chứng chỉ", "trong_so": 75, "vi_du": "Đinh vượng sinh Can Ngày = Có chứng chỉ sớm"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Văn bằng quan trọng, chứng nhận chính thức", "cach_xem": "Càn sinh Thể = Lấy được bằng", "trong_so": 60, "vi_du": "Càn vượng ở cung Đoài = Chứng chỉ uy tín"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Văn bằng, chứng chỉ", "cach_xem": "Phụ Mẫu vượng + động = Sắp có bằng", "trong_so": 70, "vi_du": "Phụ Mẫu lâm Không = Chưa lấy được bằng"}
    },
    "Bầu Cử Đề Bạt": {
        "muc_tieu": "Xem có được đề bạt vào vị trí mới không",
        "ky_mon": {"dung_than": "Trực Phù + Khai Môn + Can Ngày", "giai_thich": "Trực Phù = Cấp trên đề bạt. Khai Môn = Chức vụ mới. Can Ngày = Mình", "cach_xem": "Trực Phù sinh Can Ngày = Được đề bạt", "trong_so": 80, "vi_du": "Khai Môn vượng sinh Can Ngày = Đề bạt thành công"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Vị trí cao, được tôn vinh", "cach_xem": "Càn sinh Thể = Trúng cử", "trong_so": 65, "vi_du": "Càn vượng tháng Kim = Thời cơ đã tới"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Chức quyền, địa vị", "cach_xem": "Quan Quỷ vượng sinh Thế = Được đề bạt", "trong_so": 75, "vi_du": "Quan động hóa Tiến = Thăng tiến liên tục"}
    },
    "Chức Danh Nghề Nghiệp": {
        "muc_tieu": "Xem có đạt được học hàm/học vị/chức danh không",
        "ky_mon": {"dung_than": "Cảnh Môn + Đinh + Can Năm", "giai_thich": "Cảnh Môn = Danh hiệu. Đinh = Bằng cấp. Can Năm = Nhà nước/Cơ quan", "cach_xem": "Can Năm sinh Can Ngày = Được công nhận chức danh", "trong_so": 75, "vi_du": "Đinh vượng ở cung 9 = Danh tiếng lẫy lừng"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Chức danh chính thống, cao quý", "cach_xem": "Càn vượng = Chức danh bền vững", "trong_so": 60, "vi_du": "Càn sinh Thể = Đạt được danh hiệu"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Phụ Mẫu", "giai_thich": "Quan Quỷ = Chức danh. Phụ Mẫu = Bằng công nhận", "cach_xem": "Cả hai vượng = Đạt được chức danh", "trong_so": 70, "vi_du": "Quan Phụ tương hợp = Chức danh xứng đáng"}
    },
    "Môi Trường Làm Việc": {
        "muc_tieu": "Xem môi trường làm việc mới thế nào",
        "ky_mon": {"dung_than": "Khai Môn + Cung vị", "giai_thich": "Khai Môn = Công việc. Cung chứa Khai Môn = Môi trường (Cung 9: nóng, Cung 1: lạnh...)", "cach_xem": "Cung Khai Môn cát = Môi trường tốt", "trong_so": 70, "vi_du": "Khai Môn lâm Cửu Địa = Môi trường ổn định, trầm lắng"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Không gian làm việc, sự bao dung", "cach_xem": "Khôn vượng = Môi trường thoải mái", "trong_so": 60, "vi_du": "Dụng sinh Thể = Môi trường hỗ trợ mình"},
        "luc_hao": {"dung_than": "Hào Ứng", "giai_thich": "Ứng = Môi trường bên ngoài, chỗ làm việc", "cach_xem": "Ứng sinh Thế = Môi trường rất tốt", "trong_so": 65, "vi_du": "Ứng khắc Thế = Môi trường khắc nghiệt"}
    },
    "Áp Lực Công Việc": {
        "muc_tieu": "Xem công việc có quá áp lực không",
        "ky_mon": {"dung_than": "Canh + Khai Môn + Can Ngày", "giai_thich": "Canh = Áp lực, khó khăn. Khai Môn = Việc. Can Ngày = Mình", "cach_xem": "Canh lâm Khai Môn khắc Can Ngày = Áp lực lớn", "trong_so": 75, "vi_du": "Canh vượng khắc Can Ngày = Stress nặng"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Lo lắng, mệt mỏi, áp lực cân não", "cach_xem": "Khảm vượng = Công việc cực nhọc", "trong_so": 60, "vi_du": "Dụng khắc Thể = Bị công việc đè nặng"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Nỗi lo, áp lực", "cach_xem": "Quan Quỷ vượng khắc Thế = Áp lực quá tải", "trong_so": 70, "vi_du": "Quan vượng Thế suy = Kiệt sức vì việc"}
    },
    "Đánh Giá Nhân Sự": {
        "muc_tieu": "Xem đánh giá cuối năm có tốt không",
        "ky_mon": {"dung_than": "Trực Phù + Cảnh Môn + Can Ngày", "giai_thich": "Trực Phù = Người đánh giá. Cảnh Môn = Bản đánh giá", "cach_xem": "Trực Phù sinh Can Ngày = Đánh giá cao", "trong_so": 75, "vi_du": "Cảnh Môn vượng sinh Can Ngày = Kết quả xuất sắc"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Nhận xét, phê duyệt", "cach_xem": "Đoài sinh Thể = Nhận xét tốt", "trong_so": 60, "vi_du": "Đoài khắc Thể = Bị phê bình"},
        "luc_hao": {"dung_than": "Hào Ứng + Quan Quỷ", "giai_thich": "Ứng = Hội đồng đánh giá. Quan Quỷ = Kết quả", "cach_xem": "Ứng sinh Thế = Đánh giá tích cực", "trong_so": 70, "vi_du": "Quan vượng sinh Thế = Đánh giá rất tốt"}
    },
    "Lương Thưởng Phúc Lợi": {
        "muc_tieu": "Xem lương thưởng có tăng không",
        "ky_mon": {"dung_than": "Mậu + Sinh Môn + Can Ngày", "giai_thich": "Mậu = Lương cơ bản. Sinh Môn = Tiền thưởng. Can Ngày = Mình", "cach_xem": "Sinh Môn sinh Can Ngày = Có thưởng", "trong_so": 75, "vi_du": "Mậu sinh Can Ngày = Lương tăng"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Niềm vui tài lộc, quà tặng", "cach_xem": "Đoài sinh Thể = Có phúc lợi", "trong_so": 60, "vi_du": "Tốn (Dụng) khắc Thể = Lương bị chậm hoặc giảm"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Thu nhập từ việc làm", "cach_xem": "Thê Tài vượng sinh Thế = Lương thưởng tốt", "trong_so": 70, "vi_du": "Tài động hóa Tiến = Lương tăng đều"}
    },
    "Điều Động Luân Chuyển": {
        "muc_tieu": "Xem có bị luân chuyển công tác không",
        "ky_mon": {"dung_than": "Khai Môn + Mã Tinh + Can Ngày", "giai_thich": "Khai Môn = Việc. Mã Tinh = Điều động đi xa. Can Ngày = Mình", "cach_xem": "Mã Tinh động lâm Khai Môn = Chắc chắn luân chuyển", "trong_so": 75, "vi_du": "Khai Môn lâm Mã Tinh sinh Can Ngày = Chỗ mới tốt hơn"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Sự thay đổi, di chuyển", "cach_xem": "Chấn vượng = Sắp có biến động chỗ làm", "trong_so": 60, "vi_du": "Thể khắc Dụng = Mình xin chuyển"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Mã", "giai_thich": "Quan Quỷ = Công việc. Mã = Sự luân chuyển", "cach_xem": "Quan lâm Mã động = Luân chuyển nhanh", "trong_so": 70, "vi_du": "Thế động hóa Quan = Tự tìm cơ hội chuyển"}
    },
    "Nghỉ Hưu": {
        "muc_tieu": "Xem nghỉ hưu có an nhàn không",
        "ky_mon": {"dung_than": "Khai Môn + Hưu Môn + Tử Môn", "giai_thich": "Khai Môn = Sự nghiệp kết thúc. Hưu Môn = Nghỉ ngơi. Tử Môn = An nghỉ", "cach_xem": "Hưu Môn vượng sinh Can Ngày = Hưu trí an nhàn", "trong_so": 70, "vi_du": "Khai Môn lâm Tử Môn = Chắc chắn nghỉ hưu"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Sự tĩnh lặng, hưởng thọ, đất mẹ", "cach_xem": "Khôn sinh Thể = Hưu trí thảnh thơi", "trong_so": 60, "vi_du": "Khôn vượng = Tuổi già an vui"},
        "luc_hao": {"dung_than": "Hào Thế + Tử Tôn", "giai_thich": "Thế = Bản thân lúc già. Tử Tôn = An nhàn, phúc lộc", "cach_xem": "Thế vượng + Tử Tôn vượng = Nghỉ hưu tốt", "trong_so": 65, "vi_du": "Thế suy Quan mang Không = Thôi chức về nghỉ"}
    },
    "Khởi Nghiệp Tự Do": {
        "muc_tieu": "Xem làm Freelance/tự do có ổn không",
        "ky_mon": {"dung_than": "Sinh Môn + Thiên Nhuế + Can Ngày", "giai_thich": "Sinh Môn = Tiền tự kiếm. Thiên Nhuế = Chuyên môn cá nhân. Can Ngày = Mình", "cach_xem": "Sinh Môn vượng sinh Can Ngày = Freelance tốt", "trong_so": 75, "vi_du": "Thiên Nhuế vượng sinh Can Ngày = Tay nghề cao"},
        "mai_hoa": {"dung_than": "Quẻ Tốn - MỘC", "giai_thich": "Tốn = Sự linh hoạt, tự do như gió", "cach_xem": "Tốn vượng = Khởi nghiệp tự do thuận lợi", "trong_so": 60, "vi_du": "Tốn sinh Thể (Ly) = Làm tự do rất phát"},
        "luc_hao": {"dung_than": "Hào Tử Tôn + Thê Tài", "giai_thich": "Tử Tôn = Sáng tạo, tự do. Thê Tài = Lợi nhuận", "cach_xem": "Cả hai vượng = Làm tự do thành công", "trong_so": 70, "vi_du": "Thế lâm Tử Tôn = Người thích tự do"}
    },
    "Nghề Phụ Tay Trái": {
        "muc_tieu": "Xem làm thêm nghề tay trái có lời không",
        "ky_mon": {"dung_than": "Sinh Môn + Can Giờ", "giai_thich": "Sinh Môn = Lợi nhuận. Can Giờ = Nghề phụ (Giao dịch thêm)", "cach_xem": "Can Giờ sinh Can Ngày = Nghề phụ có lời", "trong_so": 70, "vi_du": "Sinh Môn vượng tháng sinh Can Ngày = Thu nhập phụ tốt"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Nghề phụ, kinh doanh nhỏ lẻ, niềm vui thêm", "cach_xem": "Đoài sinh Thể = Nghề phụ nuôi nghề chính", "trong_so": 60, "vi_du": "Thể Dụng tỵ hòa = Làm thêm tốt"},
        "luc_hao": {"dung_than": "Hào Thê Tài + Ứng", "giai_thich": "Thê Tài = Tiền kiếm thêm. Ứng = Công việc phụ", "cach_xem": "Tài vượng sinh Thế = Thu nhập phụ ổn", "trong_so": 65, "vi_du": "Hào 2 (Nghề phụ) vượng = Làm thêm tốt"}
    },
    "Uy Tín Thương Hiệu Cá Nhân": {
        "muc_tieu": "Xem thương hiệu cá nhân có lên không",
        "ky_mon": {"dung_than": "Cảnh Môn + Trực Phù + Thiên Anh", "giai_thich": "Cảnh Môn = Sự nổi tiếng. Trực Phù = Uy tín. Thiên Anh = Hình ảnh", "cach_xem": "Cảnh Môn sinh Can Ngày = Thương hiệu mạnh", "trong_so": 80, "vi_du": "Cảnh Môn vượng ở cung 9 = Vang danh bốn phương"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Sự rạng rỡ, hiển thị, danh tiếng", "cach_xem": "Ly sinh Thể = Uy tín tăng cao", "trong_so": 65, "vi_du": "Ly vượng tháng Hạ = Danh tiếng đỉnh cao"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Phụ Mẫu", "giai_thich": "Quan Quỷ = Danh tiếng. Phụ Mẫu = Sự lan tỏa", "cach_xem": "Quan vượng vương Thế = Uy tín cá nhân cao", "trong_so": 70, "vi_du": "Quan động hóa Tiến = Danh tiếng ngày càng xa"}
    },
    "Thi Tốt Nghiệp": {
        "muc_tieu": "Xem có đỗ tốt nghiệp không",
        "ky_mon": {"dung_than": "Cảnh Môn + Can Ngày + Can Giờ", "giai_thich": "Cảnh Môn = Văn bằng, kết quả thi. Can Ngày = Thí sinh", "cach_xem": "Cảnh Môn sinh Can Ngày = Đỗ tốt nghiệp", "trong_so": 70, "vi_du": "Cảnh Môn vượng tháng sinh Can Ngày = Kết quả cao"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Sự hoàn thành, chính quả, bằng cấp", "cach_xem": "Càn sinh Thể = Đỗ tốt nghiệp", "trong_so": 60, "vi_du": "Càn vượng ở cung Đoài = Danh lợi song toàn"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Văn bằng tốt nghiệp", "cach_xem": "Phụ Mẫu vượng = Đỗ tốt nghiệp", "trong_so": 65, "vi_du": "Phụ Mẫu vượng sinh Thế = Cầm bằng trong tay"}
    },
    "Thi Tuyển Sinh lớp 10": {
        "muc_tieu": "Xem có đỗ vào trường mong muốn không",
        "ky_mon": {"dung_than": "Khai Môn + Cảnh Môn + Thiên Phụ", "giai_thich": "Khai Môn = Trường học. Cảnh Môn = Bài thi. Thiên Phụ = Kiến thức", "cach_xem": "Khai Môn sinh Can Ngày = Đỗ vào trường", "trong_so": 75, "vi_du": "Khai Môn vượng ở cung 4 = Trường top đầu"},
        "mai_hoa": {"dung_than": "Quẻ Cấn - THỔ", "giai_thich": "Cấn = Trường học, cửa vào tri thức", "cach_xem": "Cấn vượng = Đỗ đạt", "trong_so": 60, "vi_du": "Cấn sinh Thể = Toại nguyện"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Quan Quỷ", "giai_thich": "Phụ Mẫu = Bài thi. Quan Quỷ = Danh dự, đỗ đạt", "cach_xem": "Phụ Mẫu sinh Thế = Đỗ vào lớp 10", "trong_so": 70, "vi_du": "Quan vượng Thế vượng = Đỗ điểm cao"}
    },
    "Thi THPT Quốc Gia": {
        "muc_tieu": "Xem kết quả thi THPT Quốc Gia",
        "ky_mon": {"dung_than": "Cảnh Môn + Đinh + Canh", "giai_thich": "Cảnh Môn = Đề thi. Đinh = Điểm số. Canh = Trở ngại", "cach_xem": "Cảnh Môn sinh Can Ngày = Thi tốt", "trong_so": 75, "vi_du": "Đinh vượng sinh Can Ngày = Điểm số cao"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Văn chương, bài thi, sự sáng tỏ", "cach_xem": "Ly sinh Thể = Kết quả rực rỡ", "trong_so": 65, "vi_du": "Ly vượng sinh Thể (Thổ) = Kết quả mỹ mãn"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Giấy báo điểm, bài làm", "cach_xem": "Phụ Mẫu vượng + động = Kết quả thi tốt", "trong_so": 70, "vi_du": "Phụ Mẫu sinh Thế = Đạt nguyện vọng"}
    },
    "Thi Chứng Chỉ Ngoại Ngữ": {
        "muc_tieu": "Xem có đạt chứng chỉ IELTS/TOEIC... không",
        "ky_mon": {"dung_than": "Cảnh Môn + Thiên Phụ + Canh", "giai_thich": "Cảnh Môn = Chứng chỉ. Thiên Phụ = Ngôn ngữ. Canh = Khó khăn bài thi", "cach_xem": "Thiên Phụ sinh Can Ngày = Tiếp thu tốt", "trong_so": 70, "vi_du": "Cảnh Môn sinh Can Ngày = Lấy được chứng chỉ"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Khẩu tài, ngôn ngữ, phát âm", "cach_xem": "Đoài vượng = Thi ngoại ngữ tốt", "trong_so": 60, "vi_du": "Đoài sinh Thể = Giao tiếp tự nhiên"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Chứng chỉ ngoại ngữ", "cach_xem": "Phụ Mẫu vượng = Đạt chứng chỉ", "trong_so": 65, "vi_du": "Phụ Mẫu vượng không bị khắc = Có bằng"}
    },
    "Thi Cao Học": {
        "muc_tieu": "Xem thi Thạc sĩ có đỗ không",
        "ky_mon": {"dung_than": "Thiên Phụ + Đinh + Cảnh Môn", "giai_thich": "Thiên Phụ = Tri thức cao. Đinh = Tước hiệu. Cảnh Môn = Bài thi", "cach_xem": "Thiên Phụ sinh Can Ngày = Đỗ cao học", "trong_so": 75, "vi_du": "Thiên Phụ vượng ở cung 3 = Học vấn sâu"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Học vị thạc sĩ, tột bậc của quẻ", "cach_xem": "Càn vượng sinh Thể = Đỗ cao học", "trong_so": 65, "vi_du": "Càn vượng tháng Kim = Thời công danh đến"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Phụ Mẫu", "giai_thich": "Quan Quỷ = Học vị. Phụ Mẫu = Học tập", "cach_xem": "Quan Mẫu đều vượng = Đỗ Thạc sĩ", "trong_so": 70, "vi_du": "Quan vượng sinh Thế = Đỗ thủ khoa"}
    },
    "Thi Tiến Sĩ": {
        "muc_tieu": "Xem bảo vệ luận án Tiến sĩ có thành công không",
        "ky_mon": {"dung_than": "Cảnh Môn + Trực Phù + Thiên Phụ", "giai_thich": "Cảnh Môn = Luận án. Trực Phù = Hội đồng chấm. Thiên Phụ = Kiến thức chuyên sâu", "cach_xem": "Trực Phù sinh Can Ngày = Hội đồng duyệt", "trong_so": 80, "vi_du": "Thiên Phụ vượng sinh Can Ngày = Kiến thức vững vàng"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Đỉnh cao học vấn, học vị cao nhất", "cach_xem": "Càn sinh Thể = Bảo vệ thành công", "trong_so": 70, "vi_du": "Càn vượng cung Càn = Danh trấn thiên hạ"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Quan Quỷ", "giai_thich": "Phụ Mẫu = Bản luận án. Quan Quỷ = Học vị Tiến sĩ", "cach_xem": "Phụ Mẫu vượng + Quan vượng = Thành công rực rỡ", "trong_so": 75, "vi_du": "Quan động hóa Tiến = Sự nghiệp đi lên"}
    },
    "Thi Nâng Bậc Chuyên Môn": {
        "muc_tieu": "Xem thi nâng ngạch, nâng bậc có đỗ không",
        "ky_mon": {"dung_than": "Khai Môn + Cảnh Môn + Can Ngày", "giai_thich": "Khai Môn = Ngạch công tác. Cảnh Môn = Bài thi sát hạch", "cach_xem": "Khai Môn vượng sinh Can Ngày = Nâng bậc thành công", "trong_so": 70, "vi_du": "Cảnh Môn sinh Khai Môn = Bài thi tốt"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Sự thăng tiến, vươn lên nấc thang mới", "cach_xem": "Chấn sinh Thể = Nâng bậc tốt", "trong_so": 60, "vi_du": "Chấn vượng = Năng lực được ghi nhận"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Phụ Mẫu", "giai_thich": "Quan Quỷ = Cấp bậc. Phụ Mẫu = Chứng nhận nâng bậc", "cach_xem": "Quan vượng sinh Thế = Được nâng ngạch", "trong_so": 70, "vi_du": "Quan động hóa Tài = Lương tăng theo bậc"}
    },
    "Thi Công Chức Viên Chức": {
        "muc_tieu": "Xem thi vào nhà nước có đỗ không",
        "ky_mon": {"dung_than": "Khai Môn + Trực Phù + Can Năm", "giai_thich": "Khai Môn = Cơ quan nhà nước. Trực Phù = Người tuyển dụng. Can Năm = Chính sách", "cach_xem": "Trực Phù sinh Can Ngày = Đỗ công chức", "trong_so": 80, "vi_du": "Can Năm sinh Can Ngày = Được tuyển dụng"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Cơ quan công quyền, hệ thống nhà nước", "cach_xem": "Càn sinh Thể = Trúng tuyển vào nhà nước", "trong_so": 65, "vi_du": "Càn vượng ở cung Cấn = Chỗ làm ổn định"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Chức nghiệp nhà nước", "cach_xem": "Quan Quỷ vượng sinh Thế = Đỗ công chức", "trong_so": 75, "vi_du": "Quan sinh Phụ(Kỳ thi) sinh Thế = Quá trình thuận lợi"}
    },
    "Học Bổng Du Học": {
        "muc_tieu": "Xem có xin được học bổng đi nước ngoài không",
        "ky_mon": {"dung_than": "Thiên Phụ + Cảnh Môn + Mã Tinh", "giai_thich": "Thiên Phụ = Học bổng. Cảnh Môn = Giấy tờ. Mã Tinh = Đi xa", "cach_xem": "Thiên Phụ sinh Can Ngày = Được học bổng", "trong_so": 75, "vi_du": "Mã Tinh vượng ở cung Thiên Phụ = Đi học phương xa"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Phương xa, hải ngoại, sự trôi chảy", "cach_xem": "Khảm sinh Thể (Mộc) = Du học thuận lợi", "trong_so": 60, "vi_du": "Dụng sinh Thể = Được đài thọ hoàn toàn"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thê Tài", "giai_thich": "Phụ Mẫu = Học tập. Thê Tài = Tiền học bổng", "cach_xem": "Tài vượng sinh Thế = Học bổng giá trị cao", "trong_so": 70, "vi_du": "Phụ Tài song vượng = Học giỏi có tiền"}
    },
    "Chọn Trường Học": {
        "muc_tieu": "Xem chọn trường này có tốt cho tương lai không",
        "ky_mon": {"dung_than": "Khai Môn + Thiên Phụ + Cung vị", "giai_thich": "Khai Môn = Trường học. Cung chứa Khai Môn = Chất lượng trường", "cach_xem": "Cung Khai Môn cát = Trường tốt", "trong_so": 70, "vi_du": "Khai Môn lâm Thiên Phụ = Trường có truyền thống hiếu học"},
        "mai_hoa": {"dung_than": "Quẻ Cấn - THỔ", "giai_thich": "Cấn = Ngôi trường, nơi đào tạo nhân tài", "cach_xem": "Cấn sinh Thể = Trường hợp với mình", "trong_so": 60, "vi_du": "Cấn vượng = Trường danh tiếng lâu đời"},
        "luc_hao": {"dung_than": "Hào Ứng", "giai_thich": "Ứng = Trường học mong muốn", "cach_xem": "Ứng sinh Thế = Trường rất tốt cho mình", "trong_so": 65, "vi_du": "Ứng khắc Thế = Trường này quá tầm hoặc không hợp"}
    },
    "Chọn Ngành Học": {
        "muc_tieu": "Xem chọn ngành này sau này có việc làm tốt không",
        "ky_mon": {"dung_than": "Khai Môn + Sinh Môn + Can Giờ", "giai_thich": "Khai Môn = Nghề nghiệp. Sinh Môn = Thu nhập sau này. Can Giờ = Kết quả", "cach_xem": "Khai Môn vượng = Ngành có tương lai", "trong_so": 75, "vi_du": "Sinh Môn vượng cung Khai Môn = Ngành hái ra tiền"},
        "mai_hoa": {"dung_than": "Ngũ hành của Quái", "giai_thich": "Ngành ứng với Ngũ hành (Mộc: sư phạm, Hỏa: IT...)", "cach_xem": "Ngũ hành quái sinh Thể = Ngành này rất hợp", "trong_so": 65, "vi_du": "Ly (Hỏa) sinh Thể (Thổ) = Ngành truyền thông/công nghệ cực tốt"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Sự nghiệp sau này", "cach_xem": "Quan Quỷ vượng = Ngành có địa vị lớn", "trong_so": 70, "vi_du": "Tài vượng sinh Quan = Ngành thu nhập cao"}
    },
    "Kết Quả Học Tập": {
        "muc_tieu": "Xem điểm số, học lực học kỳ này",
        "ky_mon": {"dung_than": "Cảnh Môn + Thiên Phụ + Can Ngày", "giai_thich": "Cảnh Môn = Điểm số. Thiên Phụ = Sức học. Can Ngày = Mình", "cach_xem": "Cảnh Môn vượng sinh Can Ngày = Điểm cao", "trong_so": 70, "vi_du": "Thiên Phụ sinh Cảnh Môn = Chăm học nên điểm cao"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Sự sáng suốt, văn hay chữ tốt, bảng điểm", "cach_xem": "Ly sinh Thể = Học lập thành danh", "trong_so": 60, "vi_du": "Ly vượng tháng Hạ = Học lực rất tốt"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Học hành, bài vở", "cach_xem": "Phụ Mẫu vượng = Học giỏi", "trong_so": 65, "vi_du": "Phụ vượng Thế vượng = Vững kiến thức"}
    },
    "Quan Hệ Thầy Trò": {
        "muc_tieu": "Xem quan hệ với thầy cô giáo",
        "ky_mon": {"dung_than": "Thiên Phụ + Can Ngày", "giai_thich": "Thiên Phụ = Thầy giáo. Can Ngày = Học trò", "cach_xem": "Thiên Phụ sinh Can Ngày = Được thầy yêu mến", "trong_so": 75, "vi_du": "Can Ngày sinh Thiên Phụ = Trò kính thầy"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Người thầy, người hướng dẫn, bậc bề trên", "cach_xem": "Càn sinh Thể = Thầy tận tâm chỉ dạy", "trong_so": 65, "vi_du": "Càn khắc Thể = Thầy khó tính, nghiêm khắc"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Thầy dạy bảo", "cach_xem": "Phụ Mẫu sinh Thế = Thầy trò hòa hợp", "trong_so": 70, "vi_du": "Phụ vượng không khắc Thế = Được giúp đỡ học tập"}
    },
    "Đỗ Hay Trượt": {
        "muc_tieu": "Xem kết quả thi cử cuối cùng",
        "ky_mon": {"dung_than": "Cảnh Môn + Khai Môn + Can Ngày", "giai_thich": "Cảnh Môn = Điểm. Khai Môn = Đỗ vào. Can Ngày = Mình", "cach_xem": "Cả Cảnh và Khai sinh Can Ngày = Chắc chắn đỗ", "trong_so": 80, "vi_du": "Khai Môn khắc Can Ngày = Trượt"},
        "mai_hoa": {"dung_than": "Thể Quái + Dụng Quái", "giai_thich": "Thể = Mình. Dụng = Kết quả thi", "cach_xem": "Dụng sinh Thể = Chắc chắn đỗ", "trong_so": 70, "vi_du": "Dụng khắc Thể = Thi hỏng"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Phụ Mẫu", "giai_thich": "Quan Quỷ = Đỗ đạt. Phụ Mẫu = Tên trên bảng vàng", "cach_xem": "Cả hai sinh Thế = Đỗ cao", "trong_so": 75, "vi_du": "Tử Tôn động khắc Quan = Thi hỏng"}
    },
    "Tìm Bạn Đời": {
        "muc_tieu": "Xem khi nào gặp được ý trung nhân",
        "ky_mon": {"dung_than": "Ất (Nữ) + Canh (Nam) + Lục Hợp", "giai_thich": "Ất = Nữ. Canh = Nam. Lục Hợp = Duyên phận", "cach_xem": "Cung có Lục Hợp sinh Can Ngày = Sắp gặp", "trong_so": 75, "vi_du": "Lục Hợp vượng ở cung Khảm = Gặp ở môi trường nước/phương Bắc"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Người yêu, sự vui vẻ, duyên dáng", "cach_xem": "Đoài sinh Thể = Dễ gặp người yêu", "trong_so": 60, "vi_du": "Dụng sinh Thể = Người kia chủ động tìm mình"},
        "luc_hao": {"dung_than": "Hào Thê Tài (Nam) / Quan Quỷ (Nữ)", "giai_thich": "Thê Tài = Vợ. Quan Quỷ = Chồng", "cach_xem": "Dụng Thần vượng sinh Thế = Gặp được bạn đời", "trong_so": 70, "vi_du": "Dụng vượng hóa Tiến = Duyên phận sâu dày"}
    },
    "Tình Duyên Tổng Quát": {
        "muc_tieu": "Xem vận trình tình cảm trong giai đoạn này",
        "ky_mon": {"dung_than": "Lục Hợp + Can Ngày + Can Giờ", "giai_thich": "Lục Hợp = Tình cảm. Can Ngày = Mình. Can Giờ = Chuyện tình cảm", "cach_xem": "Lục Hợp sinh Can Ngày = Tình cảm thuận lợi", "trong_so": 70, "vi_du": "Lục Hợp lâm Tử Môn = Tình cảm bế tắc"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Tình yêu, sự giao hòa", "cach_xem": "Đoài vượng = Tình duyên tốt", "trong_so": 65, "vi_du": "Đoài sinh Thể (Thủy) = Tình cảm nồng nàn"},
        "luc_hao": {"dung_than": "Hào Thế + Ứng", "giai_thich": "Thế = Mình. Ứng = Đối phương", "cach_xem": "Thế Ứng sinh hợp = Tình duyên mỹ mãn", "trong_so": 70, "vi_du": "Thế Ứng tương xung = Tình cảm dễ đổ vỡ"}
    },
    "Xem Tuổi Hợp Hôn Nhân": {
        "muc_tieu": "Xem hai người có hợp tuổi để kết hôn không",
        "ky_mon": {"dung_than": "Ất + Canh + Can Năm sinh của 2 người", "giai_thich": "Ất = Nữ. Canh = Nam. Can Năm = Mệnh tuổi", "cach_xem": "Can Năm của nam sinh Can Năm của nữ = Hợp", "trong_so": 75, "vi_du": "Can Năm của 2 người cùng cung = Vợ chồng đồng lòng"},
        "mai_hoa": {"dung_than": "Sự sinh khắc của Ngũ hành quái", "giai_thich": "Thể Quái tượng cho mình, Dụng Quái tượng cho người kia", "cach_xem": "Tỷ hòa hoặc sinh nhau = Rất hợp tuổi", "trong_so": 65, "vi_du": "Mộc (Thể) sinh Hỏa (Dụng) = Mình lo cho vợ/chồng nhiều hơn"},
        "luc_hao": {"dung_than": "Thế + Ứng + Lục Hợp trong quẻ", "giai_thich": "Thế = Mình. Ứng = Đối phương", "cach_xem": "Thế Ứng tương sinh = Tuổi hợp", "trong_so": 70, "vi_du": "Quẻ Lục Hợp = Vợ chồng trăm năm hạnh phúc"}
    },
    "Đính Hôn Ăn Hỏi": {
        "muc_tieu": "Xem lễ đính hôn có thuận lợi không",
        "ky_mon": {"dung_than": "Lục Hợp + Cảnh Môn + Can Ngày", "giai_thich": "Lục Hợp = Hôn ước. Cảnh Môn = Lễ nghi rình rang", "cach_xem": "Lục Hợp vượng sinh Can Ngày = Lễ hỏi tốt đẹp", "trong_so": 75, "vi_du": "Cảnh Môn vượng = Lễ hỏi sang trọng"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Sự vui vẻ, hứa hẹn, tiệc tùng", "cach_xem": "Đoài sinh Thể = Đính hôn suôn sẻ", "trong_so": 60, "vi_du": "Đoài vượng tháng Thu = Ngày tốt để ăn hỏi"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Thê Tài", "giai_thich": "Quan Tài lâm Thế Ứng = Danh phận đã định", "cach_xem": "Thế Ứng tương hợp = Lễ hỏi thành công", "trong_so": 70, "vi_du": "Quan Tài song vượng = Hai bên gia đình ưng thuận"}
    },
    "Đám Cưới": {
        "muc_tieu": "Xem việc tổ chức đám cưới",
        "ky_mon": {"dung_than": "Lục Hợp + Hưu Môn + Can Ngày", "giai_thich": "Lục Hợp = Hôn sự. Hưu Môn = Vui vẻ, nghỉ ngơi, ngày lễ", "cach_xem": "Hưu Môn sinh Can Ngày = Đám cưới đại cát", "trong_so": 75, "vi_du": "Lục Hợp lâm cung Càn = Đám cưới danh giá"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Đám cưới, tiệc mừng", "cach_xem": "Đoài sinh Thể = Ngày cưới thuận lợi", "trong_so": 65, "vi_du": "Thể Dụng tỵ hòa = Vợ chồng hòa thuận sau cưới"},
        "luc_hao": {"dung_than": "Quẻ Lục Hợp", "giai_thich": "Lục Hợp tượng cho sự kết hợp bền chặt", "cach_xem": "Gặp quẻ Lục Hợp là điềm báo cưới xin", "trong_so": 70, "vi_du": "Quan vượng Thế vượng = Vợ chồng môn đăng hộ đối"}
    },
    "Hòa Hợp Vợ Chồng": {
        "muc_tieu": "Xem đời sống vợ chồng có ấm êm không",
        "ky_mon": {"dung_than": "Lục Hợp + Can Ngày + Can Giờ", "giai_thich": "Lục Hợp = Sự hòa thuận. Can Ngày = Mình. Can Giờ = Bạn đời", "cach_xem": "Lục Hợp sinh cả Ngày và Giờ = Rất hòa hợp", "trong_so": 75, "vi_du": "Lục Hợp lâm cung Khôn = Vợ chồng bao dung nhau"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Sự nhu thuận, gia đình, đạo vợ chồng", "cach_xem": "Khôn sinh Thể = Vợ chồng ấm êm", "trong_so": 60, "vi_du": "Thể Dụng tương sinh = Đạo nghĩa vợ chồng sâu nặng"},
        "luc_hao": {"dung_than": "Hào Thế + Ứng", "giai_thich": "Thế = Mình. Ứng = Vợ/Chồng", "cach_xem": "Thế Ứng sinh hợp = Vợ chồng tâm đầu ý hợp", "trong_so": 70, "vi_du": "Hào Tài sinh Thế = Được vợ giúp đỡ nhiều"}
    },
    "Mâu Thuẫn Gia Đình": {
        "muc_tieu": "Xem nguyên nhân và cách hóa giải mâu thuẫn",
        "ky_mon": {"dung_than": "Canh + Thương Môn + Lục Hợp", "giai_thich": "Canh = Xung đột. Thương Môn = Cãi vã. Lục Hợp = Gia đình", "cach_xem": "Thương Môn lâm Lục Hợp = Gia đình bất hòa", "trong_so": 75, "vi_du": "Canh khắc Can Ngày = Mình bị áp lực từ gia đình"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Chấn động, tiếng sét, sự tranh cãi", "cach_xem": "Chấn động mạnh = Gia đình xào xáo", "trong_so": 60, "vi_du": "Dụng khắc Thể = Bị người nhà gây khó dễ"},
        "luc_hao": {"dung_than": "Hào Huynh Đệ", "giai_thich": "Huynh Đệ = Mâu thuẫn, cãi cọ, tị hiềm", "cach_xem": "Huynh Đệ vượng động = Xung đột gắt gao", "trong_so": 65, "vi_du": "Huynh Đệ khắc Tài = Vợ chồng cãi cọ vì tiền"}
    },
    "Ngoại Tình Người Thứ Ba": {
        "muc_tieu": "Xem có người thứ ba xen vào không",
        "ky_mon": {"dung_than": "Ất + Canh + Can Khác", "giai_thich": "Ất = Vợ/Nữ. Canh = Chồng/Nam. Can khác lâm Lục Hợp = Có người thứ ba", "cach_xem": "Thiên Nhuế lâm Lục Hợp = Tình cảm có lỗi", "trong_so": 80, "vi_du": "Canh lâm cung khác với Ất và có Đinh(Bồ nhí) = Chồng ngoại tình"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Sự quyến rũ bên ngoài, đào hoa sát", "cach_xem": "Đoài vượng ngoài Thể Dụng = Có người khác", "trong_so": 65, "vi_du": "Dụng quái sinh quẻ khác = Người kia đang để ý người khác"},
        "luc_hao": {"dung_than": "Hào Ứng hợp với hào khác", "giai_thich": "Ứng (Đối phương) không hợp Thế mà hợp hào khác", "cach_xem": "Ứng hợp hào khác = Đối phương có tư tình", "trong_so": 75, "vi_du": "Nam xem quẻ có 2 hào Tài = Có hai vợ hoặc có bồ"}
    },
    "Ly Hôn Ly Thân": {
        "muc_tieu": "Xem có dẫn đến ly hôn không",
        "ky_mon": {"dung_than": "Tử Môn + Lục Hợp + Can Ngày", "giai_thich": "Tử Môn = Chấm dứt. Lục Hợp = Hôn nhân", "cach_xem": "Tử Môn lâm Lục Hợp = Nguy cơ ly hôn", "trong_so": 80, "vi_du": "Lục Hợp lâm Không Vong = Hôn nhân hữu danh vô thực"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Sự chia lìa, đứt đoạn, lửa cháy khô hạn", "cach_xem": "Quẻ Ly vượng = Dễ dẫn đến chia ly", "trong_so": 65, "vi_du": "Quẻ Biến khắc Bản Quẻ = Kết cục là chia lìa"},
        "luc_hao": {"dung_than": "Quẻ Lục Xung", "giai_thich": "Lục Xung tượng cho sự tan rã, không bền", "cach_xem": "Gặp quẻ Lục Xung = Hôn nhân dễ gãy gánh", "trong_so": 75, "vi_du": "Thế Ứng tương xung = Vợ chồng không thể ở cùng"}
    },
    "Tái Hợp Người Yêu Cũ": {
        "muc_tieu": "Xem có quay lại với người cũ được không",
        "ky_mon": {"dung_than": "Canh + Ất + Trực Phù", "giai_thich": "Canh/Ất = Người cũ. Trực Phù = Phục ngâm (quay lại)", "cach_xem": "Gặp cách Phục Ngâm = Dễ quay lại", "trong_so": 70, "vi_du": "Lục Hợp sinh cung có Can Ngày = Có duyên gặp lại"},
        "mai_hoa": {"dung_than": "Quẻ Cấn - THỔ", "giai_thich": "Cấn = Quay lại, nhìn về phía sau, sự ổn định cũ", "cach_xem": "Cấn sinh Thể = Người cũ muốn quay lại", "trong_so": 60, "vi_du": "Biến Quái trùng Bản Quẻ = Quay lại chỗ cũ"},
        "luc_hao": {"dung_than": "Hào Thế Ứng tương hợp lại", "giai_thich": "Thế Ứng sau khi xung lại thấy hợp hoặc hợp trở lại", "cach_xem": "Dụng Thần hợp Thế = Quay lại với nhau", "trong_so": 65, "vi_du": "Ứng động hóa hợp Thế = Người cũ tìm mình"}
    },
    "Người Yêu Phương Xa": {
        "muc_tieu": "Xem tình cảm với người ở xa",
        "ky_mon": {"dung_than": "Lục Hợp + Mã Tinh", "giai_thich": "Lục Hợp = Tình cảm. Mã Tinh = Khoảng cách địa lý", "cach_xem": "Lục Hợp vượng = Tình cảm bền dù xa cách", "trong_so": 70, "vi_du": "Mã Tinh lâm Lục Hợp = Người yêu sắp về thăm"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự xa xôi, mịt mùng, đại dương", "cach_xem": "Khảm sinh Thể = Tình xa vẫn ấm", "trong_so": 60, "vi_du": "Khảm khắc Thể = Xa mặt cách lòng"},
        "luc_hao": {"dung_than": "Hào Ứng phương xa", "giai_thich": "Ứng ở hào 6 hoặc mang Mã Tinh", "cach_xem": "Ứng vượng sinh Thế = Người phương xa chung thủy", "trong_so": 65, "vi_du": "Ứng lâm Không = Người phương xa không có tin tức"}
    },
    "Tình Yêu Đơn Phương": {
        "muc_tieu": "Xem người kia có tình cảm với mình không",
        "ky_mon": {"dung_than": "Can Ngày + Can Giờ", "giai_thich": "Can Ngày = Mình. Can Giờ = Người mình thầm yêu", "cach_xem": "Can Giờ sinh Can Ngày = Người kia cũng thích mình", "trong_so": 75, "vi_du": "Can Giờ khắc Can Ngày = Người kia không có tình cảm"},
        "mai_hoa": {"dung_than": "Thể Quái + Dụng Quái", "giai_thich": "Thể = Mình. Dụng = Người ấy", "cach_xem": "Dụng sinh Thể = Người ấy có cảm tình", "trong_so": 65, "vi_du": "Thể sinh Dụng = Mình đang theo đuổi vô vọng"},
        "luc_hao": {"dung_than": "Hào Ứng + Thế", "giai_thich": "Thế = Mình. Ứng = Người ấy", "cach_xem": "Ứng sinh Thế = Tình cảm hai phía", "trong_so": 70, "vi_du": "Ứng khắc Thế = Người ấy từ chối mình"}
    },
    "Mai Mối Giới Thiệu": {
        "muc_tieu": "Xem người được giới thiệu có hợp không",
        "ky_mon": {"dung_than": "Lục Hợp + Can Tháng", "giai_thich": "Lục Hợp = Mai mối. Can Tháng = Người giới thiệu", "cach_xem": "Can Tháng sinh Can Ngày = Người giới thiệu có tâm", "trong_so": 70, "vi_du": "Cung mai mối có sao tốt = Người kia rất khá"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Ăn nói, mối lái, vui vẻ", "cach_xem": "Đoài sinh Thể = Mai mối thành công", "trong_so": 60, "vi_du": "Đoài vượng = Người được giới thiệu đẹp hớp hồn"},
        "luc_hao": {"dung_than": "Hào Ứng", "giai_thich": "Ứng = Người được giới thiệu", "cach_xem": "Ứng sinh Thế = Hợp nhau", "trong_so": 65, "vi_du": "Thế Ứng tương hợp = Gặp gỡ thuận lợi"}
    },
    "Con Cái Sau Hôn Nhân": {
        "muc_tieu": "Xem khi nào có con, con cái thế nào",
        "ky_mon": {"dung_than": "Sinh Môn + Thiên Nhuế", "giai_thich": "Sinh Môn = Sinh sản. Thiên Nhuế = Tử cung, thai nghén", "cach_xem": "Sinh Môn sinh Can Ngày = Sắp có con", "trong_so": 75, "vi_du": "Sinh Môn vượng ở cung 3/4 = Con khỏe mạnh"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Con trai, sự sinh trưởng mạnh", "cach_xem": "Chấn vượng = Dễ có con", "trong_so": 65, "vi_du": "Khôn (Mẹ) sinh Chấn (Con) = Thai nhi tốt"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn = Con cái", "cach_xem": "Tử Tôn vượng sinh Thế = Con cái hiếu thảo", "trong_so": 70, "vi_du": "Tử Tôn lâm Không = Hiếm muộn con cái"}
    },
    "Mẹ Chồng Nàng Dâu": {
        "muc_tieu": "Xem quan hệ giữa mẹ chồng và nàng dâu",
        "ky_mon": {"dung_than": "Can Năm (Mẹ) + Ất (Dâu)", "giai_thich": "Can Năm = Mẹ chồng. Ất = Nàng dâu", "cach_xem": "Can Năm sinh Ất = Mẹ chồng thương dâu", "trong_so": 75, "vi_du": "Can Năm khắc Ất = Mẹ chồng khắt khe"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Mẹ chồng, người phụ nữ lớn tuổi", "cach_xem": "Khôn sinh Thể = Mẹ chồng con dâu hòa hợp", "trong_so": 60, "vi_du": "Khôn khắc Thể = Hay xảy ra va chạm"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thê Tài", "giai_thich": "Phụ Mẫu = Mẹ chồng. Thê Tài = Con dâu", "cach_xem": "Tài sinh Phụ = Dâu hiếu thảo", "trong_so": 65, "vi_du": "Phụ khắc Tài = Mẹ chồng nàng dâu khắc khẩu"}
    },
    "Gia Đình Nội Ngoại": {
        "muc_tieu": "Xem quan hệ với hai bên gia đình",
        "ky_mon": {"dung_than": "Can Năm + Can Ngày", "giai_thich": "Can Năm = Bố mẹ/Hàng gia trưởng. Can Ngày = Vợ chồng", "cach_xem": "Can Năm sinh Can Ngày = Hai bên ủng hộ", "trong_so": 70, "vi_du": "Can Năm lâm cung xung với Can Ngày = Căng thẳng với bề trên"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Dòng họ, gia tộc, đất tổ", "cach_xem": "Khôn vượng = Gia đạo hưng vượng", "trong_so": 60, "vi_du": "Thể Dụng tỵ hòa = Hai nhà hòa hợp"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu = Cha mẹ, dòng tộc", "cach_xem": "Phụ Mẫu sinh Thế = Được họ hàng giúp đỡ", "trong_so": 65, "vi_du": "Phụ Mẫu vượng động = Gia đình có việc lớn"}
    },
    "Sự Phản Bội": {
        "muc_tieu": "Xem có bị phản bội trong tình cảm không",
        "ky_mon": {"dung_than": "Huyền Vũ + Thiên Nhuế + Lục Hợp", "giai_thich": "Huyền Vũ = Sự lừa dối. Thiên Nhuế = Sai lầm. Lục Hợp = Hôn nhân", "cach_xem": "Huyền Vũ lâm cung Lục Hợp = Bị lừa dối", "trong_so": 80, "vi_du": "Lục Hợp lâm Không Vong + Huyền Vũ = Tan vỡ vì lừa dối"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự bí mật, trơn trượt, hố sâu lừa lọc", "cach_xem": "Khảm vượng ẩn tàng = Có sự phản bội ngầm", "trong_so": 65, "vi_du": "Dụng quái biến Khảm = Lúc đầu tốt sau bị phản bội"},
        "luc_hao": {"dung_than": "Hào Ứng lâm Huyền Vũ", "giai_thich": "Huyền Vũ tượng cho mờ ám, không thật lòng", "cach_xem": "Ứng lâm Huyền Vũ khắc Thế = Bị phản bội", "trong_so": 75, "vi_du": "Thế lâm Câu Trần = Tình cảm mệt mỏi vì bị lừa"}
    },
    "Xem Ngày Kết Hôn": {
        "muc_tieu": "Xem ngày này cưới có đại cát không",
        "ky_mon": {"dung_than": "Can Ngày + Can Giờ + Lục Hợp", "giai_thich": "Can Ngày = Ngày cưới. Can Giờ = Giờ cưới. Lục Hợp = Sự kết hợp", "cach_xem": "Can Ngày sinh Can Giờ = Ngày giờ hợp nhau", "trong_so": 75, "vi_du": "Lục Hợp lâm cung tốt = Ngày cưới rất đẹp"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Niềm vui tột cùng, lễ hội cưới hỏi", "cach_xem": "Đoài vượng tháng cưới = Ngày tốt", "trong_so": 60, "vi_du": "Thể Dụng sinh hợp = Vợ chồng sau này giàu sang"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thế Ứng", "giai_thich": "Phụ Mẫu = Hôn thú. Thế Ứng = Vợ chồng", "cach_xem": "Phụ Mẫu vượng động = Ngày cưới đại cát", "trong_so": 70, "vi_du": "Quan Tài đều vượng = Ngày cưới hoàn hảo"}
    },
    "Hẹn Hò Lần Đầu": {
        "muc_tieu": "Xem buổi hẹn đầu tiên có ấn tượng tốt không",
        "ky_mon": {"dung_than": "Hưu Môn + Cảnh Môn + Can Ngày", "giai_thich": "Hưu Môn = Vui vẻ thư giãn. Cảnh Môn = Vẻ bề ngoài", "cach_xem": "Cảnh Môn vượng = Mình rất thu hút trong buổi hẹn", "trong_so": 70, "vi_du": "Hưu Môn sinh Can Ngày = Buổi hẹn thoải mái"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Gặp gỡ, nói chuyện, duyên dáng", "cach_xem": "Đoài sinh Thể = Hẹn hò thành công", "trong_so": 60, "vi_du": "Đoài vượng = Người kia rất hài lòng"},
        "luc_hao": {"dung_than": "Hào Thế + Ứng", "giai_thich": "Thế = Mình. Ứng = Đối phương hẹn hò", "cach_xem": "Thế Ứng tương sinh = Lần đầu gặp đã mến", "trong_so": 65, "vi_du": "Thế sinh Ứng = Mình rất thích người kia"}
    },
    "Sức Khỏe Tổng Quát": {
        "muc_tieu": "Xem tình trạng sức khỏe hiện tại",
        "ky_mon": {"dung_than": "Thiên Nhuế + Can Ngày + Trực Phù", "giai_thich": "Thiên Nhuế = Bệnh tật. Can Ngày = Bản thân. Trực Phù = Sức đề kháng", "cach_xem": "Thiên Nhuế suy yếu = Sức khỏe tốt", "trong_so": 75, "vi_du": "Can Ngày vượng sinh cung Thiên Nhuế = Mình đang chế ngự được bệnh"},
        "mai_hoa": {"dung_than": "Thể Quái", "giai_thich": "Thể Quái tượng cho cơ thể mình", "cach_xem": "Thể Quái vượng = Người khỏe mạnh", "trong_so": 70, "vi_du": "Dụng sinh Thể = Đang được bồi bổ tốt"},
        "luc_hao": {"dung_than": "Hào Thế", "giai_thich": "Thế là bản thân người xem bệnh", "cach_xem": "Thế vượng = Sức khỏe tốt ít bệnh", "trong_so": 75, "vi_du": "Thế lâm Nhật Nguyệt = Sức sống dồi dào"}
    },
    "Xem Bệnh Nan Y": {
        "muc_tieu": "Xem bệnh nặng có chữa được không",
        "ky_mon": {"dung_than": "Thiên Nhuế + Tử Môn + Thiên Tâm", "giai_thich": "Thiên Nhuế = Bệnh. Tử Môn = Nguy hiểm tính mạng. Thiên Tâm = Thầy thuốc", "cach_xem": "Thiên Tâm vượng khắc Thiên Nhuế = Có hy vọng", "trong_so": 80, "vi_du": "Tử Môn lâm cung có Can Ngày = Rất nguy kịch"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự hiểm nghèo, bệnh tật lâu ngày", "cach_xem": "Khảm vượng khắc Thể = Bệnh nan y khó qua", "trong_so": 70, "vi_du": "Biến Quái khắc Bản Quẻ = Bệnh diễn tiến xấu"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Bệnh tật", "cach_xem": "Quan Quỷ vượng động khắc Thế = Bệnh nặng nguy hiểm", "trong_so": 75, "vi_du": "Quan Quỷ hóa Tiến = Bệnh càng nặng thêm"}
    },
    "Phẫu Thuật Cấp Cứu": {
        "muc_tieu": "Xem ca mổ có thành công không",
        "ky_mon": {"dung_than": "Thiên Tâm + Canh + Thiên Nhuế", "giai_thich": "Thiên Tâm = Bác sĩ phẫu thuật. Canh = Dao kéo. Thiên Nhuế = Vết thương", "cach_xem": "Canh sinh Thiên Tâm = Mổ thuận lợi", "trong_so": 75, "vi_du": "Thiên Tâm vượng sinh Can Ngày = Bác sĩ tận tâm"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Dao kéo, sự dứt khoát, thiết bị y tế", "cach_xem": "Càn vượng = Ca mổ suôn sẻ", "trong_so": 65, "vi_du": "Càn khắc Thể (Mộc) = Phẫu thuật gây đau đớn nhiều"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn = Thuốc thang, giải quyết bệnh tật", "cach_xem": "Tử Tôn vượng động = Ca mổ đại thắng", "trong_so": 70, "vi_du": "Tử Tôn động khắc Quan Quỷ = Phẫu thuật triệt để bệnh"}
    },
    "Thai Sản Quá Trình": {
        "muc_tieu": "Xem quá trình mang thai có ổn định không",
        "ky_mon": {"dung_than": "Thiên Nhuế + Côn + Sinh Môn", "giai_thich": "Thiên Nhuế = Thai nhi. Côn = Mẹ mang bầu. Sinh Môn = Sự phát triển", "cach_xem": "Cung Khôn vượng = Thai kỳ ổn định", "trong_so": 75, "vi_du": "Sinh Môn lâm cung 8 = Thai nhi phát triển tốt"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Người mẹ, tử cung, bụng bầu", "cach_xem": "Khôn vượng = Mẹ tròn con vuông", "trong_so": 65, "vi_du": "Khôn sinh Chấn (Con) = Thai nhi khỏe mạnh"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn = Thai nhi", "cach_xem": "Tử Tôn vượng không bị xung khắc = Thai nhi an toàn", "trong_so": 70, "vi_du": "Tử Tôn phục dưới hào tài = Thai đang lớn"},
    },
    "Sinh Con Chuyển Dạ": {
        "muc_tieu": "Xem việc sinh nở có dễ dàng không",
        "ky_mon": {"dung_than": "Khai Môn + Sinh Môn + Thiên Nhuế", "giai_thich": "Khai Môn = Cửa tử cung mở. Sinh Môn = Đứa trẻ chào đời", "cach_xem": "Khai Môn vượng = Sinh nở nhanh chóng", "trong_so": 80, "vi_du": "Sinh Môn sinh cung của Mẹ = Mẹ tròn con vuông"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Sự ra đời, tiếng khóc đầu đời, chuyển động", "cach_xem": "Chấn vượng = Sinh con thuận lợi", "trong_so": 60, "vi_du": "Chấn sinh Thể (Ly) = Sinh nở vui vẻ"},
        "luc_hao": {"dung_than": "Hào Tử Tôn + Thai hào", "giai_thich": "Tử Tôn động = Sắp sinh con", "cach_xem": "Tử Tôn vượng động chuyển địa = Sinh nhanh", "trong_so": 70, "vi_du": "Tử Tôn hợp Thế = Con bám mẹ, sinh lâu"}
    },
    "Bệnh Tâm Thần Trầm Cảm": {
        "muc_tieu": "Xem tình trạng tâm lý, thần kinh",
        "ky_mon": {"dung_than": "Thiên Nhuế + Đằng Xà + Can Ngày", "giai_thich": "Thiên Nhuế = Bệnh. Đằng Xà = Tâm thần rối loạn. Can Ngày = Mình", "cach_xem": "Đằng Xà lâm Can Ngày = Tâm lý bất ổn", "trong_so": 75, "vi_du": "Thiên Nhuế lâm cung Khảm = Suy nghĩ u uất"},
        "mai_hoa": {"dung_than": "Quẻ Tốn - MỘC", "giai_thich": "Tốn = Thần kinh, suy nghĩ luẩn quẩn như gió", "cach_xem": "Tốn vượng quá mức = Suy nghĩ cực đoan", "trong_so": 60, "vi_du": "Dụng quái khắc Thể (Thổ) = Tâm bệnh nặng"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Đằng Xà", "giai_thich": "Quan Quỷ mang Đằng Xà = Lo âu, hoảng loạn", "cach_xem": "Quan lâm Đằng Xà khắc Thế = Trầm cảm nặng", "trong_so": 70, "vi_du": "Phụ Mẫu mang Chu Tước = Hay nghĩ ngợi lung tung"}
    },
    "Bệnh Xương Khớp": {
        "muc_tieu": "Xem bệnh về xương, cột sống",
        "ky_mon": {"dung_than": "Thiên Nhuế + Cung 6/7/8", "giai_thich": "Cung 6, 7, 8 tượng cho khung xương và tay chân", "cach_xem": "Thiên Nhuế lâm Cung Càn/Đoài = Đau xương", "trong_so": 70, "vi_du": "Cảnh Môn lâm Cung Cấn = Viêm khớp"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Khung xương, xương đầu, cột sống", "cach_xem": "Quẻ Càn bị khắc = Đau xương khớp", "trong_so": 65, "vi_du": "Ly (Hỏa) khắc Càn = Viêm khớp nóng đỏ"},
        "luc_hao": {"dung_than": "Hào mang hành Kim hoặc Thổ", "giai_thich": "Kim = Xương. Thổ = Cơ bắp bao quanh xương", "cach_xem": "Hào Kim bị xung = Gãy xương, trật khớp", "trong_so": 65, "vi_du": "Thế lâm Bạch Hổ hành Kim = Bệnh xương khớp kinh niên"}
    },
    "Bệnh Tiêu Hóa": {
        "muc_tieu": "Xem bệnh dạ dày, đường ruột",
        "ky_mon": {"dung_than": "Thiên Nhuế + Cung 2/5/8", "giai_thich": "Cung 2 (Khôn), 5 (Trung), 8 (Cấn) thuộc Thổ tượng cho hệ tiêu hóa", "cach_xem": "Thiên Nhuế lâm cung Khôn = Đau dạ dày", "trong_so": 75, "vi_du": "Thiên Nhuế lâm cung 2 + Canh = Tắc ruột"},
        "mai_hoa": {"dung_than": "Quẻ Khôn/Cấn - THỔ", "giai_thich": "Khôn = Bụng, dạ dày. Cấn = Ruột non/già", "cach_xem": "Thổ bị Mộc khắc = Rối loạn tiêu hóa", "trong_so": 60, "vi_du": "Chấn (Mộc) khắc Khôn = Đau bụng co thắt"},
        "luc_hao": {"dung_than": "Hào mang hành Thổ", "giai_thich": "Thổ tượng cho tì vị", "cach_xem": "Hào Thổ lâm Quan Quỷ = Bệnh đường tiêu hóa", "trong_so": 70, "vi_du": "Thế lâm Quan Quỷ hành Thổ = Đau bao tử mãn tính"}
    },
    "Bệnh Hô Hấp": {
        "muc_tieu": "Xem bệnh phổi, mũi họng",
        "ky_mon": {"dung_than": "Thiên Nhuế + Cung 7", "giai_thich": "Cung 7 (Đoài) tượng cho phổi và cuống họng", "cach_xem": "Thiên Nhuế lâm cung Đoài = Ho, viêm phổi", "trong_so": 70, "vi_du": "Thiên Nhuế + Bính lâm cung Đoài = Viêm họng hạt"},
        "mai_hoa": {"dung_than": "Quẻ Đoài/Tốn", "giai_thich": "Đoài = Phổi. Tốn = Khí quản, mũi", "cach_xem": "Quẻ Đoài bị khắc = Khó thở", "trong_so": 60, "vi_du": "Ly (Hỏa) khắc Đoài (Kim) = Viêm phổi cấp"},
        "luc_hao": {"dung_than": "Hào mang hành Kim + Chu Tước", "giai_thich": "Kim = Phổi. Chu Tước = Tiếng khò khè, ho", "cach_xem": "Hào Kim lâm Quan Quỷ = Bệnh hô hấp", "trong_so": 65, "vi_du": "Quan lâm Chu Tước = Ho nhiều, đau họng"}
    },
    "Bệnh Tim Mạch": {
        "muc_tieu": "Xem bệnh liên quan đến tim, huyết áp",
        "ky_mon": {"dung_than": "Thiên Nhuế + Cung 9", "giai_thich": "Cung 9 (Ly) tượng cho tim và huyết áp", "cach_xem": "Thiên Nhuế lâm cung Ly = Bệnh tim", "trong_so": 75, "vi_du": "Thiên Nhuế + Đinh lâm cung Ly = Huyết áp cao"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Tâm hỏa, tim, máu", "cach_xem": "Ly bị Khảm khắc = Suy tim, đột quỵ", "trong_so": 65, "vi_du": "Khảm (Thủy) khắc Ly (Hỏa) = Nhồi máu cơ tim"},
        "luc_hao": {"dung_than": "Hào mang hành Hỏa", "giai_thich": "Hỏa tượng cho lục phủ ngũ tạng là Tâm", "cach_xem": "Hào Hỏa lâm Quan Quỷ = Bệnh tim mạch", "trong_so": 70, "vi_du": "Thế lâm Quan Quỷ hành Hỏa = Huyết áp không ổn định"}
    },
    "Tìm Thầy Tìm Thuốc": {
        "muc_tieu": "Xem có gặp được bác sĩ giỏi không",
        "ky_mon": {"dung_than": "Thiên Tâm + Ất + Can Ngày", "giai_thich": "Thiên Tâm = Bác sĩ. Ất = Đơn thuốc. Can Ngày = Mình", "cach_xem": "Thiên Tâm sinh Can Ngày = Gặp thầy giỏi", "trong_so": 75, "vi_du": "Ất sinh Can Ngày = Thuốc hợp bệnh"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Lão y, bác sĩ có trình độ cao", "cach_xem": "Càn sinh Thể = Gặp được bác sĩ tốt", "trong_so": 60, "vi_du": "Dụng sinh Thể = Thuốc uống vào thấy hiệu quả ngay"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn là thuốc, là thầy cứu mạng", "cach_xem": "Tử Tôn vượng sinh Thế = Gặp thầy thuốc giỏi", "trong_so": 75, "vi_du": "Tử Tôn lâm Nhật Nguyệt = Thuốc quý cứu người"}
    },
    "Tai Nạn Thương Tích": {
        "muc_tieu": "Xem có gặp tai nạn đột ngột không",
        "ky_mon": {"dung_than": "Canh + Bạch Hổ + Can Ngày", "giai_thich": "Canh = Va chạm. Bạch Hổ = Máu huyết, tai nạn. Can Ngày = Mình", "cach_xem": "Bạch Hổ khắc Can Ngày = Gặp tai nạn", "trong_so": 80, "vi_du": "Canh lâm cung có Can Ngày = Có sự va chạm xe cộ"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Sự đột ngột, va chạm cơ khí", "cach_xem": "Chấn khắc Thể (Thổ) = Tai nạn chân tay", "trong_so": 65, "vi_du": "Quẻ Càn khắc Chấn = Tai nạn do kim loại"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Bạch Hổ", "giai_thich": "Bạch Hổ tượng cho đổ máu, tai nạn", "cach_xem": "Quan lâm Bạch Hổ động khắc Thế = Tai nạn bất ngờ", "trong_so": 75, "vi_du": "Thế lâm Quan Quỷ hóa xung = Gặp họa sát thân"}
    },
    "Sức Khỏe Người Già": {
        "muc_tieu": "Xem tình hình sức khỏe người lớn tuổi",
        "ky_mon": {"dung_than": "Thiên Nhuế + Can Năm + Trực Phù", "giai_thich": "Can Năm = Người già. Thiên Nhuế = Bệnh", "cach_xem": "Thiên Nhuế suy tại cung Can Năm = Sức khỏe ổn", "trong_so": 75, "vi_du": "Cửu Địa lâm cung Can Năm = Sức khỏe bình lặng"},
        "mai_hoa": {"dung_than": "Quẻ Càn/Khôn", "giai_thich": "Càn = Cha/Ông lớn tuổi. Khôn = Mẹ/Bà lớn tuổi", "cach_xem": "Càn/Khôn vượng = Người già khỏe mạnh", "trong_so": 65, "vi_du": "Khôn sinh Thể = Mẹ già được con cháu chăm tốt"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu tượng cho cha mẹ, người già", "cach_xem": "Phụ Mẫu vượng sinh Thế = Cha mẹ khỏe mạnh", "trong_so": 70, "vi_du": "Phụ Mẫu lâm Không = Cha mẹ sức khỏe yếu"}
    },
    "Sức Khỏe Trẻ Em": {
        "muc_tieu": "Xem trẻ nhỏ đau ốm thế nào",
        "ky_mon": {"dung_than": "Thiên Nhuế + Can Giờ", "giai_thich": "Can Giờ = Trẻ nhỏ. Thiên Nhuế = Bệnh", "cach_xem": "Thiên Nhuế khắc Can Giờ = Trẻ đang bị bệnh hành", "trong_so": 75, "vi_du": "Can Giờ vượng sinh Can Ngày = Trẻ mau lành bệnh"},
        "mai_hoa": {"dung_than": "Quẻ Cấn/Đoài", "giai_thich": "Cấn = Bé trai. Đoài = Bé gái", "cach_xem": "Cấn/Đoài vượng = Trẻ khỏe", "trong_so": 60, "vi_du": "Tốn (Mộc) khắc Cấn = Trẻ hay bị đau bụng/giun sán"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn là hào của trẻ nhỏ", "cach_xem": "Tử Tôn vượng = Trẻ hay ăn chóng lớn", "trong_so": 75, "vi_du": "Tử Tôn lâm Quan Quỷ = Trẻ hay bị quấy khóc, đau ốm"}
    },
    "Di Chứng Sau Bệnh": {
        "muc_tieu": "Xem bệnh có để lại di chứng không",
        "ky_mon": {"dung_than": "Phục Ngâm + Thiên Nhuế", "giai_thich": "Phục Ngâm = Sự dai dẳng, kéo dài", "cach_xem": "Thiên Nhuế lâm cung có Can Ngày = Bệnh còn gốc", "trong_so": 70, "vi_du": "Đế Vượng lâm Thiên Nhuế = Di chứng nặng"},
        "mai_hoa": {"dung_than": "Hỗ Quái", "giai_thich": "Hỗ Quái tượng cho quá trình trung gian và di chứng", "cach_xem": "Hỗ Quái khắc Thể = Còn di chứng khó chịu", "trong_so": 65, "vi_du": "Biến Quái sinh Hỗ Quái = Bệnh cũ dễ tái phát"},
        "luc_hao": {"dung_than": "Hào phục dưới hào Quan", "giai_thich": "Bệnh ẩn tàng không lộ ra", "cach_xem": "Quan phục dưới Tài = Di chứng do ăn uống", "trong_so": 65, "vi_du": "Thế lâm mồ Quan = Bệnh vẫn còn tàng ẩn trong người"}
    },
    "Ngày Đi Khám Bệnh": {
        "muc_tieu": "Xem chọn ngày nào đi khám cho chuẩn",
        "ky_mon": {"dung_than": "Thiên Tâm + Can Ngày + Can Giờ", "giai_thich": "Can Ngày = Ngày khám. Can Giờ = Kết quả khám", "cach_xem": "Thiên Tâm vượng vào ngày khám = Kết quả chính xác", "trong_so": 75, "vi_du": "Can Giờ sinh Can Ngày = Khám ra đúng bệnh"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Ăn nói, trao đổi với bác sĩ, kết quả", "cach_xem": "Đoài vượng tháng Thu = Đi khám ngày này tốt", "trong_so": 60, "vi_du": "Đoài sinh Thể = Bác sĩ tư vấn rất kỹ"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Tử Tôn", "giai_thich": "Phụ Mẫu = Kết quả xét nghiệm. Tử Tôn = Bác sĩ", "cach_xem": "Cả hai vượng = Đi khám suôn sẻ", "trong_so": 70, "vi_du": "Phụ Mẫu lâm Không = Kết quả chưa có ngay"}
    },
    "Hiếm Muộn Vô Sinh": {
        "muc_tieu": "Xem nguyên nhân và khả năng có con",
        "ky_mon": {"dung_than": "Sinh Môn + Thiên Nhuế + Tử Môn", "giai_thich": "Tử Môn lâm cung Thai = Khó có con. Sinh Môn lâm Không = Hết hy vọng", "cach_xem": "Thiên Tâm sinh cung Thai = Chữa được hiếm muộn", "trong_so": 80, "vi_du": "Thiên Nhuế vượng tại cung 2 = Có bệnh ở tử cung"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Sự màu mỡ của đất, tử cung", "cach_xem": "Khôn suy kiệt = Khó mang thai", "trong_so": 65, "vi_du": "Càn (Dụng) khắc Tốn (Thể) = Long mạch/Phong thủy nhà ảnh hưởng con cái"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn là con cái", "cach_xem": "Tử Tôn lâm Không phế = Khó có con", "trong_so": 75, "vi_du": "Tử Tôn phục dưới hào Quan = Có bệnh cản trở sinh nở"}
    },
    "Nguyên Nhân Bệnh Tật": {
        "muc_tieu": "Xem bệnh do tạng phủ hay do tâm linh",
        "ky_mon": {"dung_than": "Thiên Nhuế + Cửu Thiên / Cửu Địa", "giai_thich": "Cửu Thiên = Do thời tiết/trời. Cửu Địa = Do ăn uống/đất", "cach_xem": "Thiên Nhuế lâm Đằng Xà = Do tâm linh quay quắt", "trong_so": 75, "vi_du": "Canh lâm Thiên Nhuế = Do va chạm vật lý"},
        "mai_hoa": {"dung_than": "Quái tượng", "giai_thich": "Hỏa = Tim, Thổ = Dạ dày, Mộc = Gan...", "cach_xem": "Quẻ bị khắc thuộc ngũ hành nào thì bệnh ở đó", "trong_so": 65, "vi_du": "Quẻ Khảm (Thủy) vượng khắc Ly = Bệnh do lạnh/nước"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ lâm Lục Thần", "giai_thich": "Đằng Xà = Tâm linh. Bạch Hổ = Huyết quang. Huyền Vũ = Tà khí", "cach_xem": "Quan lâm Chu Tước = Bệnh do nói nhiều / Hỏa vượng", "trong_so": 70, "vi_du": "Quan lâm Đằng Xà = Bệnh tâm linh, hoang tưởng"}
    },
    "Phục Hồi Sức Khỏe": {
        "muc_tieu": "Xem sau ốm có mau khỏe lại không",
        "ky_mon": {"dung_than": "Thiên Tâm + Sinh Môn + Can Ngày", "giai_thich": "Thiên Tâm = Thuốc. Sinh Môn = Sức sống mới", "cach_xem": "Sinh Môn sinh Can Ngày = Phục hồi nhanh", "trong_so": 75, "vi_du": "Hưu Môn lâm Can Ngày = Cần nghỉ ngơi thêm mới khỏe"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Sự nảy mầm, hồi sinh, năng lượng dồi dào", "cach_xem": "Chấn sinh Thể = Phục hồi cực nhanh", "trong_so": 60, "vi_du": "Hỗ Quái sinh Thể = Dần dần bình phục"},
        "luc_hao": {"dung_than": "Hào Tử Tôn + Thế", "giai_thich": "Thế vượng dần lên = Đang khỏe lại", "cach_xem": "Tử Tôn vượng sinh Thế = Phục hồi tốt", "trong_so": 70, "vi_du": "Thế động hóa Tiến = Sức khỏe tiến triển tốt"}
    },
    "Thắng Thua Kiện Tụng": {
        "muc_tieu": "Xem kết quả cuối cùng của vụ kiện",
        "ky_mon": {"dung_than": "Khai Môn + Kinh Môn + Can Ngày", "giai_thich": "Khai Môn = Thẩm phán. Kinh Môn = Kiện tụng. Can Ngày = Mình", "cach_xem": "Khai Môn sinh Can Ngày = Mình thắng", "trong_so": 80, "vi_du": "Kinh Môn khắc Can Ngày = Mình gặp bất lợi"},
        "mai_hoa": {"dung_than": "Thể Quái + Dụng Quái", "giai_thich": "Thể = Mình. Dụng = Đối thủ kiện tụng", "cach_xem": "Thể khắc Dụng = Thắng kiện", "trong_so": 70, "vi_du": "Dụng khắc Thể = Thua kiện"},
        "luc_hao": {"dung_than": "Hào Thế + Ứng + Quan Quỷ", "giai_thich": "Thế = Mình. Ứng = Đối thủ. Quan = Tòa án", "cach_xem": "Quan Quỷ sinh Thế = Tòa xử có lợi cho mình", "trong_so": 75, "vi_du": "Thế vượng Ứng suy = Mình nắm lợi thế"}
    },
    "Thời Điểm Khởi Kiện": {
        "muc_tieu": "Xem khi nào nộp đơn kiện là tốt nhất",
        "ky_mon": {"dung_than": "Khai Môn + Can Ngày + Can Giờ", "giai_thich": "Khai Môn = Tòa tiếp nhận. Can Giờ = Kết quả nộp đơn", "cach_xem": "Khai Môn vượng sinh Can Ngày = Thời điểm tốt", "trong_so": 75, "vi_du": "Can Giờ sinh Can Ngày = Nộp đơn thuận lợi"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Khởi động, hành động quyết liệt", "cach_xem": "Chấn sinh Thể = Khởi kiện lúc này tốt", "trong_so": 60, "vi_du": "Chấn vượng tháng Xuân = Cơ hội thắng cao"},
        "luc_hao": {"dung_than": "Hào Thế động", "giai_thich": "Thế động tượng cho việc bắt đầu hành động", "cach_xem": "Thế động hóa cát = Khởi kiện thành công", "trong_so": 65, "vi_du": "Thế lâm Thanh Long động = Khởi kiện gặp may"}
    },
    "Thuê Luật Sư": {
        "muc_tieu": "Xem luật sư có giỏi và giúp được mình không",
        "ky_mon": {"dung_than": "Trực Phù + Thiên Tâm + Can Ngày", "giai_thich": "Trực Phù = Luật sư bảo vệ. Thiên Tâm = Trí tuệ luật pháp", "cach_xem": "Trực Phù sinh Can Ngày = Luật sư rất tốt", "trong_so": 75, "vi_du": "Thiên Tâm vượng sinh Can Ngày = Luật sư có mưu lược"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Luật sư chính nghĩa, có uy tín", "cach_xem": "Càn sinh Thể = Luật sư đắc lực", "trong_so": 60, "vi_du": "Càn vượng ở cung Đoài = Luật sư giỏi biện hộ"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu tượng cho người bảo hộ, luật sư", "cach_xem": "Phụ Mẫu vượng sinh Thế = Luật sư có tâm", "trong_so": 70, "vi_du": "Phụ Mẫu hợp Thế = Luật sư và mình đồng lòng"}
    },
    "Hòa Giải Dân Sự": {
        "muc_tieu": "Xem hai bên có thể hòa giải thỏa đáng không",
        "ky_mon": {"dung_than": "Lục Hợp + Can Ngày + Can Giờ", "giai_thich": "Lục Hợp = Sự thỏa hiệp, trung gian", "cach_xem": "Lục Hợp sinh cả hai cung = Hòa giải thành công", "trong_so": 80, "vi_du": "Lục Hợp lâm Tử Môn = Không thể hòa giải"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Thương lượng, nói chuyện phải trái", "cach_xem": "Đoài sinh Thể = Hòa giải có lợi cho mình", "trong_so": 65, "vi_du": "Thể Dụng tỵ hòa = Hai bên vui vẻ hòa giải"},
        "luc_hao": {"dung_than": "Hào Ứng sinh Thế", "giai_thich": "Đối thủ sinh mình = Dễ dàng thương lượng", "cach_xem": "Thế Ứng tương hợp = Hòa giải mỹ mãn", "trong_so": 70, "vi_du": "Lục Hợp hiện quẻ = Duyên hòa giải đã tới"}
    },
    "Bị Khởi Kiện": {
        "muc_tieu": "Xem mình bị người khác kiện có sao không",
        "ky_mon": {"dung_than": "Kinh Môn + Can Giờ + Can Ngày", "giai_thich": "Can Giờ = Người kiện mình. Kinh Môn = Rắc rối pháp lý", "cach_xem": "Can Giờ khắc Can Ngày = Nguy hiểm", "trong_so": 80, "vi_du": "Kinh Môn lâm cung có Can Ngày = Gặp rắc rối lớn"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự hãm hại, cạm bẫy pháp lý", "cach_xem": "Khảm khắc Thể = Bị kiện gặp bất lợi", "trong_so": 65, "vi_du": "Dụng khắc Thể = Đối phương nắm thế thượng phong"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Tai họa pháp luật, lệnh tòa", "cach_xem": "Quan Quỷ động khắc Thế = Bị kiện rất mệt mỏi", "trong_so": 75, "vi_du": "Ứng động khắc Thế = Đối thủ công kích mạnh"}
    },
    "Tranh Chấp Đất Đai": {
        "muc_tieu": "Xem kiện tụng về đất đai sẽ thế nào",
        "ky_mon": {"dung_than": "Tử Môn + Khai Môn + Thổ", "giai_thich": "Tử Môn = Đất đai. Khai Môn = Tòa xét xử", "cach_xem": "Tử Môn sinh Can Ngày = Đất về tay mình", "trong_so": 75, "vi_du": "Tử Môn + Kinh Môn = Tranh chấp đất căng thẳng"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Đất đai đang tranh chấp", "cach_xem": "Khôn sinh Thể = Thắng lợi về đất", "trong_so": 65, "vi_du": "Cấn (Địa) khắc Thủy (Thể) = Tranh chấp đất gây thiệt hại"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thổ", "giai_thich": "Phụ Mẫu = Giấy tờ đất. Thổ = Miếng đất", "cach_xem": "Phụ Mẫu vượng sinh Thế = Đất có giấy tờ rõ ràng", "trong_so": 70, "vi_du": "Thổ hào vượng sinh Thế = Được hưởng miếng đất"}
    },
    "Tranh Chấp Tài Sản": {
        "muc_tieu": "Xem kiện đòi lại tài sản/tiền bạc",
        "ky_mon": {"dung_than": "Mậu + Sinh Môn + Kinh Môn", "giai_thich": "Mậu = Tiền gốc. Sinh Môn = Tài sản. Kinh Môn = Tranh chấp", "cach_xem": "Sinh Môn sinh Can Ngày = Lấy lại được tài sản", "trong_so": 75, "vi_du": "Sinh Môn lâm Không = Tài sản đã mất khó đòi"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Vàng bạc, vật phẩm quý giá", "cach_xem": "Đoài sinh Thể = Đòi được của", "trong_so": 65, "vi_du": "Dụng sinh Thể = Đối phương tự nguyện trả"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Tài sản đang tranh chấp", "cach_xem": "Thê Tài vượng sinh Thế = Đòi được tài sản", "trong_so": 70, "vi_du": "Tài lâm Ứng = Tiền đang trong tay đối thủ"}
    },
    "Thừa Kế Pháp Luật": {
        "muc_tieu": "Xem việc phân chia thừa kế có công bằng không",
        "ky_mon": {"dung_than": "Can Năm + Lục Hợp + Sinh Môn", "giai_thich": "Can Năm = Tổ tiên để lại. Lục Hợp = Phân chia. Sinh Môn = Sản nghiệp", "cach_xem": "Sinh Môn sinh Can Ngày = Được hưởng thừa kế", "trong_so": 75, "vi_du": "Lục Hợp khắc Can Ngày = Chia chác không đều"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Của hồi môn, di sản gia đình", "cach_xem": "Khôn sinh Thể = Thừa kế thuận lợi", "trong_so": 60, "vi_du": "Khôn vượng = Di sản lớn"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thê Tài", "giai_thich": "Phụ Mẫu = Di chúc. Thê Tài = Tiền thừa kế", "cach_xem": "Phụ Mẫu vượng hợp Thế = Được chỉ định thừa kế", "trong_so": 70, "vi_du": "Phụ Mẫu lâm Không = Di chúc có vấn đề"}
    },
    "Thi Hành Bản Án": {
        "muc_tieu": "Xem bản án có được thực thi nhanh không",
        "ky_mon": {"dung_than": "Canh + Khai Môn + Trực Phù", "giai_thich": "Canh = Cưỡng chế. Khai Môn = Lệnh thi hành", "cach_xem": "Canh lâm Khai Môn = Thi hành quyết liệt", "trong_so": 75, "vi_du": "Khai Môn sinh Can Ngày = Thi hành có lợi cho mình"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Sự thực hiện, kết quả cuối cùng nổ ra", "cach_xem": "Chấn vượng = Thi hành nhanh", "trong_so": 60, "vi_du": "Chấn khắc Thể = Thi hành gây khó khăn"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ động", "giai_thich": "Quan Quỷ động tượng cho việc pháp luật vào cuộc", "cach_xem": "Quan động hóa Tiến = Thi hành triệt để", "trong_so": 65, "vi_du": "Quan động khắc Thế = Bị cưỡng chế thi hành"}
    },
    "Bị Bắt Giữ Tạm Giam": {
        "muc_tieu": "Xem người bị bắt có sớm được ra không",
        "ky_mon": {"dung_than": "Địa Vong + Kinh Môn + Can Ngày", "giai_thich": "Địa Vong = Lưới đất, giam giữ. Kinh Môn = Cửa ngục", "cach_xem": "Can Ngày lâm Không = Sớm được ra", "trong_so": 80, "vi_du": "Can Ngày lâm Địa Vong = Còn bị giam lâu"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Cầu tù, sự giam cầm, hầm tối", "cach_xem": "Khảm vượng = Không thoát được ngay", "trong_so": 65, "vi_du": "Khảm khắc Thể (Ly) = Bị giam giữ nghiêm ngặt"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Quan Quỷ", "giai_thich": "Phụ Mẫu = Nhà giam. Quan Quỷ = Lệnh bắt", "cach_xem": "Thế hào lâm mộ = Bị nhốt vào ngục", "trong_so": 75, "vi_du": "Thế động hóa tuyệt = Tình cảnh rất nguy nan"}
    },
    "Mua Nhà Chung Cư": {
        "muc_tieu": "Xem mua chung cư có tốt và pháp lý ổn không",
        "ky_mon": {"dung_than": "Sinh Môn + Cảnh Môn + Trực Phù", "giai_thich": "Sinh Môn = Nhà. Cảnh Môn = Giấy tờ pháp lý chung cư", "cach_xem": "Sinh Môn sinh Can Ngày = Nhà ở hợp", "trong_so": 75, "vi_du": "Cảnh Môn lâm Không = Pháp lý chung cư chưa xong"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Tòa nhà lớn, nhiều căn hộ", "cach_xem": "Khôn sinh Thể = Mua chung cư tốt", "trong_so": 60, "vi_du": "Khôn vượng = Căn hộ rộng rãi"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu tượng cho nhà cửa chung cư", "cach_xem": "Phụ Mẫu vượng sinh Thế = Nhà tốt", "trong_so": 70, "vi_du": "Phụ Mẫu lâm hào 5 hoặc 6 = Căn hộ ở tầng cao"}
    },
    "Bán Nhà Đất": {
        "muc_tieu": "Xem bán nhà có nhanh và được giá không",
        "ky_mon": {"dung_than": "Sinh Môn + Can Giờ + Can Ngày", "giai_thich": "Can Giờ = Người mua. Sinh Môn = Giá bán", "cach_xem": "Can Giờ sinh Can Ngày = Dễ bán", "trong_so": 75, "vi_du": "Sinh Môn vượng sinh Can Ngày = Bán được giá cao"},
        "mai_hoa": {"dung_than": "Thể Quái + Dụng Quái", "giai_thich": "Thể = Mình. Dụng = Người mua/Việc bán", "cach_xem": "Thể khắc Dụng = Mình làm chủ giá bán", "trong_so": 65, "vi_du": "Dụng sinh Thể = Người mua rất nhiệt tình"},
        "luc_hao": {"dung_than": "Hào Thế + Ứng + Thê Tài", "giai_thich": "Ứng = Người mua. Tài = Tiền bán nhà", "cach_xem": "Ứng sinh Thế = Bán nhanh", "trong_so": 70, "vi_du": "Tài vượng sinh Thế = Bán được lời lớn"}
    },
    "Sửa Chữa Nhà Cửa": {
        "muc_tieu": "Xem sửa nhà có thuận lợi, thợ tốt không",
        "ky_mon": {"dung_than": "Sinh Môn + Thiên Nhuế + Canh", "giai_thich": "Thiên Nhuế = Chỗ cần sửa. Canh = Thợ thuyền dao kéo", "cach_xem": "Sinh Môn vượng = Sửa xong nhà đẹp", "trong_so": 70, "vi_du": "Thiên Nhuế lâm Tử Môn = Chỗ sửa gặp đại hạn"},
        "mai_hoa": {"dung_than": "Quẻ Cấn - THỔ", "giai_thich": "Cấn = Ngôi nhà đang được gia cố, kiến trúc", "cach_xem": "Cấn sinh Thể = Sửa chữa suôn sẻ", "trong_so": 60, "vi_du": "Cấn vượng = Sửa xong nhà vững chãi"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Tử Tôn", "giai_thich": "Phụ Mẫu = Nhà. Tử Tôn = Thợ sửa chữa", "cach_xem": "Tử Tôn vượng sinh Phụ Mẫu = Thợ giỏi sửa tốt", "trong_so": 65, "vi_du": "Phụ Mẫu động = Nhà đang trong quá trình sửa"}
    },
    "Thuê Nhà Ở": {
        "muc_tieu": "Xem nhà thuê có hợp phong thủy, chủ nhà tốt không",
        "ky_mon": {"dung_than": "Sinh Môn + Trực Phù + Can Giờ", "giai_thich": "Trực Phù = Chủ nhà. Sinh Môn = Nhà thuê", "cach_xem": "Sinh Môn sinh Can Ngày = Nhà hợp", "trong_so": 75, "vi_du": "Trực Phù khắc Can Ngày = Chủ nhà khó tính"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Sự cư trú, nhà thuê của người khác", "cach_xem": "Khôn sinh Thể = Thuê nhà thuận lợi", "trong_so": 60, "vi_du": "Khôn vượng = Nhà thuê ấm cúng"},
        "luc_hao": {"dung_than": "Hào Ứng", "giai_thich": "Ứng tượng cho chủ nhà hoặc căn nhà thuê", "cach_xem": "Ứng sinh Thế = Thuê nhà gặp may", "trong_so": 65, "vi_du": "Ứng khắc Thế = Thuê nhà gặp rắc rối"}
    },
    "Thiết Kế Kiến Trúc": {
        "muc_tieu": "Xem thiết kế nhà có đẹp và hợp không",
        "ky_mon": {"dung_than": "Cảnh Môn + Sinh Môn + Thiên Phụ", "giai_thich": "Cảnh Môn = Bản vẽ. Thiên Phụ = Kiến trúc sư", "cach_xem": "Cảnh Môn vượng đẹp = Thiết kế xuất sắc", "trong_so": 70, "vi_du": "Cảnh Môn sinh Sinh Môn = Bản vẽ rất hợp với thực tế"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Mỹ thuật, trang trí, thẩm mỹ", "cach_xem": "Đoài sinh Thể = Thiết kế đẹp mắt", "trong_so": 60, "vi_du": "Đoài vượng = Nhà có tính thẩm mỹ cao"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thanh Long", "giai_thich": "Thanh Long tượng cho sự hoa mỹ, đẹp đẽ", "cach_xem": "Phụ Mẫu lâm Thanh Long = Nhà thiết kế rất đẹp", "trong_so": 65, "vi_du": "Phụ Mẫu lâm Chu Tước = Nhà thiết kế rực rỡ"}
    },
    "Chọn Hướng Nhà": {
        "muc_tieu": "Xem hướng nhà này có đại cát không",
        "ky_mon": {"dung_than": "Sinh Môn + Cung vị hướng nhà", "giai_thich": "Sinh Môn lâm hướng nào thì hướng đó quan trọng", "cach_xem": "Cung Sinh Môn vượng = Hướng nhà tốt", "trong_so": 80, "vi_du": "Hướng nhà sinh Can Ngày = Hướng nhà cực hợp mệnh"},
        "mai_hoa": {"dung_than": "Ngũ hành của Quái hướng", "giai_thich": "Hướng ứng với quẻ (Càn: Tây Bắc, Khảm: Bắc...)", "cach_xem": "Quái hướng sinh Thể = Hướng nhà đại cát", "trong_so": 70, "vi_du": "Quái hướng khắc Thể = Hướng nhà gây họa"},
        "luc_hao": {"dung_than": "Hào Thế + Cung quẻ hành", "giai_thich": "Hướng nhà ứng với phương vị của hào vượng", "cach_xem": "Hào vượng phương nào thì hướng đó tốt", "trong_so": 70, "vi_du": "Lục Hợp lâm hào hướng = Hướng nhà tụ khí"}
    },
    "Thủ Tục Đất Đai": {
        "muc_tieu": "Xem làm sổ đỏ, giấy tờ đất có thông không",
        "ky_mon": {"dung_than": "Cảnh Môn + Đinh + Trực Phù", "giai_thich": "Cảnh Môn = Giấy tờ. Đinh = Hồ sơ. Trực Phù = Cơ quan duyệt", "cach_xem": "Cảnh Môn sinh Can Ngày = Giấy tờ suôn sẻ", "trong_so": 75, "vi_du": "Cảnh Môn lâm Không = Giấy tờ bị đình trệ"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Văn bản pháp lý cao nhất, sổ đỏ", "cach_xem": "Càn sinh Thể = Làm sổ đỏ nhanh", "trong_so": 60, "vi_du": "Càn vượng tháng Kim = Thời điểm xong giấy tờ"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu tượng cho giấy chứng nhận quyền sử dụng đất", "cach_xem": "Phụ Mẫu vượng sinh Thế = Sổ đỏ về tay", "trong_so": 70, "vi_du": "Phụ Mẫu lâm động = Giấy tờ đang được luân chuyển làm"}
    },
    "Phong Thủy Nhà Ở": {
        "muc_tieu": "Xem phong thủy nhà có vượng tài lộc không",
        "ky_mon": {"dung_than": "Sinh Môn + Trực Phù + Cửu Địa", "giai_thich": "Sinh Môn = Khí của nhà. Cửu Địa = Khí của đất", "cach_xem": "Sinh Môn vượng + Cát thần = Phong thủy tốt", "trong_so": 85, "vi_du": "Sinh Môn lâm cung 1 (Khảm) = Nhà có thủy tụ tài"},
        "mai_hoa": {"dung_than": "Quẻ Cấn/Khôn - THỔ", "giai_thich": "Cấn = Sơn (núi), Khôn = Địa (đất) trong phong thủy", "cach_xem": "Cấn vượng = Nhà có chỗ dựa vững", "trong_so": 70, "vi_du": "Thể Dụng sinh hợp = Tàng phong tụ khí"},
        "luc_hao": {"dung_than": "Hào 2 và Hào 5", "giai_thich": "Hào 2 = Nhà, Hào 5 = Chủ nhà", "cach_xem": "Hào 2 sinh hào 5 = Đất dưỡng người (Phong thủy tốt)", "trong_so": 75, "vi_du": "Hào 2 vượng lâm Thanh Long = Cực phẩm phong thủy"}
    },
    "Chuyển Về Nhà Mới": {
        "muc_tieu": "Xem ngày giờ nhập trạch có đại cát không",
        "ky_mon": {"dung_than": "Sinh Môn + Hưu Môn + Can Ngày", "giai_thich": "Sinh Môn = Nhà mới. Hưu Môn = Sự an cư. Can Ngày = Mình", "cach_xem": "Sinh Môn sinh Can Ngày = Nhập trạch đại cát", "trong_so": 75, "vi_du": "Mã Tinh lâm Sinh Môn = Chuyển nhà nhanh gọn"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Sự khởi đầu mới, náo nhiệt lúc vào nhà", "cach_xem": "Chấn sinh Thể = Vào nhà mới gặp may", "trong_so": 60, "vi_du": "Chấn vượng = Khí thế nhà mới bừng bừng"},
        "luc_hao": {"dung_than": "Hào Thế động", "giai_thich": "Thế động tượng cho sự di chuyển chỗ ở", "cach_xem": "Thế động hóa Phụ Mẫu = Chuyển đến nhà mới tốt", "trong_so": 65, "vi_du": "Quẻ quy hồn = Chuyển nhà đi rồi lại muốn về"}
    },
    "Giải Phóng Mặt Bằng": {
        "muc_tieu": "Xem đền bù giải tỏa có thỏa đáng không",
        "ky_mon": {"dung_than": "Khai Môn + Tử Môn + Mậu", "giai_thich": "Khai Môn = Cơ quan nhà nước. Tử Môn = Đất bị thu hồi. Mậu = Tiền đền bù", "cach_xem": "Mậu sinh Can Ngày = Tiền đền bù cao", "trong_so": 75, "vi_du": "Tử Môn khắc Can Ngày = Việc thu hồi đất gây thiệt hại"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự khó khăn khi giải tỏa, vướng mắc", "cach_xem": "Khảm sinh Thể = Giải quyết đền bù ổn", "trong_so": 60, "vi_du": "Khảm khắc Thể = Giải tỏa gặp nhiều cản trở"},
        "luc_hao": {"dung_than": "Hào Thê Tài + Phụ Mẫu", "giai_thich": "Thê Tài = Tiền đền bù. Phụ Mẫu = Miếng đất bị thu hồi", "cach_xem": "Tài vượng sinh Thế = Đền bù thỏa đáng", "trong_so": 70, "vi_du": "Quan động khắc Thế = Bị ép giải tỏa"}
    },
    "Đi Xuất Khẩu Lao Động": {
        "muc_tieu": "Xem đi nước ngoài làm việc có tốt không",
        "ky_mon": {"dung_than": "Mã Tinh + Khai Môn + Thiên Phụ", "giai_thich": "Mã Tinh = Xuất ngoại. Khai Môn = Việc làm. Thiên Phụ = Kiến thức tay nghề", "cach_xem": "Khai Môn sinh Can Ngày = Công việc ổn định", "trong_so": 75, "vi_du": "Mã Tinh vượng ở cung Khảm/Chấn = Đi xa rất tốt"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Phương xa, hải ngoại, sự mưu sinh", "cach_xem": "Khảm sinh Thể = Đi làm ở nước ngoài có lời", "trong_so": 65, "vi_du": "Khảm vượng = Cơ hội ở nước ngoài rộng mở"},
        "luc_hao": {"dung_than": "Hào Thế + Ứng + Thê Tài", "giai_thich": "Ứng = Nước ngoài. Tài = Lương ở nước ngoài", "cach_xem": "Tài vượng sinh Thế = Đi làm có tiền", "trong_so": 70, "vi_du": "Thế động hóa Mã = Phải xuất ngoại gấp"}
    },
    "Thủ Tục Visa Hộ Chiếu": {
        "muc_tieu": "Xem xin visa có đạt không",
        "ky_mon": {"dung_than": "Cảnh Môn + Đinh + Trực Phù", "giai_thich": "Cảnh Môn = Visa. Đinh = Hộ chiếu. Trực Phù = Đại sứ quán", "cach_xem": "Trực Phù sinh Can Ngày = Visa được duyệt", "trong_so": 75, "vi_du": "Cảnh Môn lâm Không = Visa bị từ chối"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Văn bản pháp lý, cấp phép xuất nhập cảnh", "cach_xem": "Càn sinh Thể = Thủ tục suôn sẻ", "trong_so": 60, "vi_du": "Càn vượng tháng Thu = Nhanh có visa"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu tượng cho giấy thông hành và visa", "cach_xem": "Phụ Mẫu vượng sinh Thế = Có visa sớm", "trong_so": 70, "vi_du": "Phụ Mẫu lâm Không = Giấy tờ bị trục trặc"}
    },
    "Định Cư Nước Ngoài": {
        "muc_tieu": "Xem định cư lâu dài có ổn không",
        "ky_mon": {"dung_than": "Sinh Môn + Mã Tinh + Can Năm", "giai_thich": "Sinh Môn = Nơi ở mới. Mã Tinh = Sự di dời. Can Năm = Người lãnh đạo quốc gia", "cach_xem": "Sinh Môn sinh Can Ngày = Định cư rất tốt", "trong_so": 80, "vi_du": "Can Ngày lâm cung đối diện với nơi cũ = Định cư thành công"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự trôi dạt ra xa, sinh sống ở hải ngoại", "cach_xem": "Khảm sinh Thể = Định cư hải ngoại phát đạt", "trong_so": 65, "vi_du": "Khảm vượng tháng Đông = Thời điểm tốt để đi"},
        "luc_hao": {"dung_than": "Hào Thế + Ứng + Phụ Mẫu", "giai_thich": "Ứng = Nước sở tại. Phụ Mẫu = Nơi ở lâu dài", "cach_xem": "Ứng sinh Thế = Nước đó chào đón mình", "trong_so": 75, "vi_du": "Thế động hóa Ứng = Tự nguyện sang định cư"}
    },
    "Sự Cố Trên Đường Đi": {
        "muc_tieu": "Xem hành trình có gặp tai nạn/hỏng xe không",
        "ky_mon": {"dung_than": "Canh + Bạch Hổ + Cảnh Môn", "giai_thich": "Canh = Va chạm. Bạch Hổ = Tai nạn. Cảnh Môn = Lộ hành", "cach_xem": "Bạch Hổ lâm Lộ = Gặp sự cố lớn", "trong_so": 80, "vi_du": "Canh lâm cung Chấn = Hỏng xe trên đường"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Chấn động, tai nạn giao thông bất ngờ", "cach_xem": "Chấn khắc Thể = Hành trình gặp nạn", "trong_so": 60, "vi_du": "Chấn vượng nổ ra = Tai nạn liên hoàn"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Bạch Hổ", "giai_thich": "Bạch Hổ tượng cho đổ huyết trên đường", "cach_xem": "Quan lâm Bạch Hổ động = Gặp tai nạn", "trong_so": 70, "vi_du": "Thế lâm Quan Quỷ hóa xung = Đi đứng nguy hiểm"}
    },
    "Mất Hành Lý": {
        "muc_tieu": "Xem hành lý có bị thất lạc trên đường không",
        "ky_mon": {"dung_than": "Huyền Vũ + Can Ngày + Can Giờ", "giai_thich": "Huyền Vũ = Mất mát bí mật. Can Giờ = Hành lý", "cach_xem": "Can Giờ lâm Không = Mất hành lý", "trong_so": 75, "vi_du": "Huyền Vũ lâm cung Can Giờ = Bị lấy cắp đồ"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Cạm bẫy, sự thất lạc, không tìm thấy", "cach_xem": "Khảm vượng = Hành lý lạc trôi xa", "trong_so": 60, "vi_du": "Dụng khắc Thể = Bị mất đồ khó tìm"},
        "luc_hao": {"dung_than": "Hào Thê Tài lâm Không", "giai_thich": "Tài lâm Không tượng cho vật chất đã biến mất", "cach_xem": "Tài lâm Huyền Vũ = Bị người khác lấy mất", "trong_so": 65, "vi_du": "Tài phục dưới hào Quan = Đồ bị giấu đi"}
    },
    "Tìm Tài Liệu Mất": {
        "muc_tieu": "Xem tài liệu quan trọng bị mất ở đâu",
        "ky_mon": {"dung_than": "Cảnh Môn + Đinh + Can Ngày", "giai_thich": "Cảnh Môn = Tài liệu, sách vở. Đinh = Thông tin lưu trữ", "cach_xem": "Cảnh Môn sinh Can Ngày = Tìm thấy dễ dàng", "trong_so": 75, "vi_du": "Cảnh Môn ở cung Khảm = Tài liệu bị kẹt ở chỗ ẩm ướt"},
        "mai_hoa": {"dung_than": "Quẻ Tốn - MỘC", "giai_thich": "Tốn = Giấy tờ, văn thư, tài liệu mỏng", "cach_xem": "Tốn sinh Thể = Tìm thấy tài liệu", "trong_so": 60, "vi_du": "Tốn lâm cung Ly = Tài liệu để ở nơi sáng sủa"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu tượng cho sách vở, văn kiện, tài liệu", "cach_xem": "Phụ Mẫu vượng = Còn tìm thấy", "trong_so": 65, "vi_du": "Phụ Mẫu phục dưới hào Thế = Đồ quanh quẩn trong mình"}
    },
    "Tìm Thú Cưng Lạc": {
        "muc_tieu": "Xem thú cưng đi lạc về hướng nào",
        "ky_mon": {"dung_than": "Tử Tôn (Quái) + Thiên Nhuế + Cung", "giai_thich": "Thiên Nhuế = Vật nuôi bệnh/lạc. Cung = Hướng tìm", "cach_xem": "Thiên Nhuế ở cung nào thì tìm hướng đó", "trong_so": 75, "vi_du": "Thiên Nhuế lâm cung 3 = Thú cưng đang ở hướng Đông"},
        "mai_hoa": {"dung_than": "Quẻ Cấn - THỔ", "giai_thich": "Cấn = Vật nuôi trong nhà, ở gần các hốc kẹt", "cach_xem": "Cấn sinh Thể = Thú cưng sẽ tự về", "trong_so": 60, "vi_du": "Cấn vượng tháng Tứ Quý = Thú cưng vẫn an toàn"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn là lục súc, thú nuôi", "cach_xem": "Tử Tôn vượng động = Thú cưng đang chạy nhảy ở xa", "trong_so": 70, "vi_du": "Tử Tôn lâm Không = Thú đã bị người khác bắt hoặc chết"}
    },
    "Bị Lừa Đảo Tài Chính": {
        "muc_tieu": "Xem có bị kẻ gian lừa tiền không",
        "ky_mon": {"dung_than": "Huyền Vũ + Thiên Bồng + Mậu", "giai_thich": "Huyền Vũ = Kẻ gian. Thiên Bồng = Đại tặc. Mậu = Tiền", "cach_xem": "Huyền Vũ khắc Can Ngày = Chắc chắn bị lừa", "trong_so": 80, "vi_du": "Thiên Bồng lâm cung Mậu = Tiền đã bị lấy cắp sạch"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự gian xảo, lừa bịp, bóng tối mưu hèn", "cach_xem": "Khảm khắc Thể (Ly) = Bị lừa trắng tay", "trong_so": 65, "vi_du": "Dụng biến Khảm = Lúc đầu hứa hẹn sau cùng lừa lọc"},
        "luc_hao": {"dung_than": "Hào Ứng lâm Huyền Vũ", "giai_thich": "Ứng là đối tác, Huyền Vũ là dối trá", "cach_xem": "Ứng lâm Huyền Vũ khắc Thế = Đối phương đang lừa mình", "trong_so": 75, "vi_du": "Tài lâm Không + Quan vượng = Bị lừa tiền qua mạng"}
    },
    "Thông Tin Sai Lệch": {
        "muc_tieu": "Xem tin đồn hoặc thông tin nhận được có thật không",
        "ky_mon": {"dung_than": "Cảnh Môn + Đinh + Đằng Xà", "giai_thich": "Cảnh Môn = Tin tức. Đằng Xà = Sự giả tạo, không thật", "cach_xem": "Đằng Xà lâm Cảnh Môn = Tin vịt, thất thiệt", "trong_so": 75, "vi_du": "Cảnh Môn lâm Cửu Thiên = Tin tức đã được thổi phồng"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Sự ảo giác, hư ảnh, tin đồn gây xôn xao", "cach_xem": "Ly vượng sinh Thể = Tin tốt nhưng chưa chắc thật", "trong_so": 60, "vi_du": "Dụng quái khắc Thể = Tin xấu đồn thổi làm hại danh tiếng"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu lâm Chu Tước", "giai_thich": "Chu Tước tượng cho lời nói, tin đồn", "cach_xem": "Phụ Mẫu lâm Chu Tước hóa Không = Tin đồn giả", "trong_so": 65, "vi_du": "Phụ Mẫu lâm Đằng Xà = Tin tức lắt léo, khó tin"}
    },
    "Gia Nhập Câu Lạc Bộ": {
        "muc_tieu": "Xem tham gia hội nhóm có vui và lợi không",
        "ky_mon": {"dung_than": "Lục Hợp + Hưu Môn + Can Ngày", "giai_thich": "Lục Hợp = Hội nhóm. Hưu Môn = Vui chơi giải trí", "cach_xem": "Lục Hợp sinh Can Ngày = Nhóm này rất hợp", "trong_so": 70, "vi_du": "Hưu Môn vượng = Hoạt động nhóm rất sôi nổi"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Nhóm bạn, sự tụ tập, giao lưu", "cach_xem": "Đoài sinh Thể = Tham gia nhóm rất vui", "trong_so": 60, "vi_du": "Đoài vượng tháng Thu = Nhóm có uy tín"},
        "luc_hao": {"dung_than": "Hào Huynh Đệ", "giai_thich": "Huynh Đệ tượng cho bạn bè trong hội", "cach_xem": "Huynh Đệ sinh Thế = Hội nhóm giúp ích cho mình", "trong_so": 65, "vi_du": "Huynh Đệ khắc Tài = Tham gia nhóm tốn tiền"}
    },
    "Tổ Chức Sự Kiện": {
        "muc_tieu": "Xem sự kiện nổ ra có thành công tốt đẹp không",
        "ky_mon": {"dung_than": "Cảnh Môn + Trực Phù + Can Giờ", "giai_thich": "Cảnh Môn = Sự kiện vinh quang. Can Giờ = Kết quả buổi lễ", "cach_xem": "Cảnh Môn vượng sinh Can Ngày = Sự kiện vang dội", "trong_so": 75, "vi_du": "Cảnh Môn lâm Kinh Môn = Sự kiện gặp sự cố cãi vã"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Sự huy hoàng, bắt mắt, ánh sáng sự kiện", "cach_xem": "Ly sinh Thể = Sự kiện thành công mỹ mãn", "trong_so": 65, "vi_du": "Ly vượng tháng Hạ = Sự kiện thu hút nhiều người"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Phụ Mẫu", "giai_thich": "Quan Quỷ = Quy mô. Phụ Mẫu = Truyền thông sự kiện", "cach_xem": "Quan Phụ song vượng = Sự kiện lớn và uy tín", "trong_so": 70, "vi_du": "Phụ Mẫu lâm Thanh Long = Sự kiện sang trọng"}
    },
    "Thi Đấu Esport": {
        "muc_tieu": "Xem thi đấu game điện tử có thắng không",
        "ky_mon": {"dung_than": "Khai Môn + Cảnh Môn + Thiên Bồng", "giai_thich": "Khai Môn = Trận đấu. Cảnh Môn = Mạng/Skill. Thiên Bồng = Chiến thuật", "cach_xem": "Can Ngày khắc Can Giờ = Thắng trận", "trong_so": 70, "vi_du": "Cảnh Môn vượng ở cung Khảm = Skill xử lý rất nhanh"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Điện tử, ánh sáng màn hình, tốc độ xử lý", "cach_xem": "Ly sinh Thể = Chơi game đạt phong độ cao", "trong_so": 60, "vi_du": "Dụng khắc Thể = Bị đối thủ lật kèo"},
        "luc_hao": {"dung_than": "Hào Thế + Ứng", "giai_thich": "Thế = Team mình. Ứng = Team bạn", "cach_xem": "Thế vượng hơn Ứng = Thắng trận game", "trong_so": 70, "vi_du": "Thế lâm Thanh Long = Team chơi cực hay"}
    },
    "Dẫn Đầu Xu Hướng": {
        "muc_tieu": "Xem mình có tạo được trend thành công không",
        "ky_mon": {"dung_than": "Thiên Anh + Cảnh Môn + Can Ngày", "giai_thich": "Thiên Anh = Sự nổi bật. Cảnh Môn = Trendy. Can Ngày = Mình", "cach_xem": "Cảnh Môn sinh Can Ngày = Tạo trend thành công", "trong_so": 75, "vi_du": "Thiên Anh vượng ở cung 9 = Trend bùng nổ mạnh"},
        "mai_hoa": {"dung_than": "Quẻ Tốn - MỘC", "giai_thich": "Tốn = Sự lan tỏa như gió, sự phổ biến rộng rãi", "cach_xem": "Tốn sinh Thể = Trend do mình tạo được hưởng ứng tốt", "trong_so": 60, "vi_du": "Tốn vượng tháng Xuân = Trend lan đi rất nhanh"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Chu Tước", "giai_thich": "Quan Quỷ = Danh tiếng. Chu Tước = Sự bàn tán", "cach_xem": "Quan lâm Chu Tước vượng = Cộng đồng nhắc tên nhiều", "trong_so": 70, "vi_du": "Quan động hóa Tiến = Xu hướng ngày càng nóng"}
    },
    "Gặp Gỡ Thần Tượng": {
        "muc_tieu": "Xem có cơ hội gặp người mình hâm mộ không",
        "ky_mon": {"dung_than": "Thiên Anh + Trực Phù + Can Ngày", "giai_thich": "Thiên Anh = Ngôi sao/Thần tượng. Can Ngày = Mình", "cach_xem": "Thiên Anh sinh Can Ngày = Được gặp thần tượng", "trong_so": 70, "vi_du": "Trực Phù lâm Thiên Anh = Thần tượng rất thân thiện"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Người nổi tiếng, hào quang rực rỡ", "cach_xem": "Ly sinh Thể = Được diện kiến thần tượng", "trong_so": 60, "vi_du": "Dụng sinh Thể = Thần tượng chú ý đến mình"},
        "luc_hao": {"dung_than": "Hào Ứng cao cấp", "giai_thich": "Ứng tượng cho thần tượng (thường ở hào thượng)", "cach_xem": "Ứng sinh Thế = Buổi gặp mặt như ý", "trong_so": 65, "vi_du": "Ứng lâm Thanh Long = Thần tượng rất đẹp và tài"},
    },
    "Tìm Đồ May Mắn": {
        "muc_tieu": "Xem tìm vật phẩm phong thủy/may mắn bị lạc",
        "ky_mon": {"dung_than": "Lục Hợp + Thiên Tâm + Can Ngày", "giai_thich": "Lục Hợp = Vật phẩm gắn kết. Thiên Tâm = Đồ có giá trị tinh thần", "cach_xem": "Lục Hợp sinh Can Ngày = Tìm thấy lại được", "trong_so": 70, "vi_du": "Cung có Lục Hợp cát = Đồ vẫn nguyên vẹn"},
        "mai_hoa": {"dung_than": "Quẻ Càn/Khôn", "giai_thich": "Tượng cho vật báu, linh vật phong thủy", "cach_xem": "Quái sinh Thể = Vật may mắn sẽ quay về", "trong_so": 60, "vi_du": "Càn sinh Thể = Đồ vật tâm linh rất linh ứng"},
        "luc_hao": {"dung_than": "Hào Thê Tài lâm Thanh Long", "giai_thich": "Thanh Long tượng cho vật quý giá, may mắn", "cach_xem": "Thê Tài sinh Thế = Tìm thấy vật quý", "trong_so": 65, "vi_du": "Tài lâm hào 5 = Đồ ở trên cao hoặc bàn thờ"}
    },
    "Xung Đột Hàng Xóm": {
        "muc_tieu": "Xem mâu thuẫn với hàng xóm có giải quyết được không",
        "ky_mon": {"dung_than": "Lục Hợp + Thương Môn + Can Giờ", "giai_thich": "Can Giờ = Hàng xóm. Thương Môn = Cãi vã. Lục Hợp = Quan hệ", "cach_xem": "Lục Hợp vượng sinh Can Ngày = Hòa giải tốt", "trong_so": 75, "vi_du": "Can Giờ khắc Can Ngày = Hàng xóm gây khó dễ"},
        "mai_hoa": {"dung_than": "Quẻ Chấn/Đoài", "giai_thich": "Tượng cho vách ngăn, sự ồn ào vách bên", "cach_xem": "Tỵ hòa = Hàng xóm êm đẹp", "trong_so": 60, "vi_du": "Chấn khắc Thể = Hàng xóm gây ồn ào cản trở"},
        "luc_hao": {"dung_than": "Hào Ứng", "giai_thich": "Ứng là nước láng giềng hoặc người hàng xóm", "cach_xem": "Ứng sinh Thế = Hàng xóm tốt bụng", "trong_so": 65, "vi_du": "Ứng lâm Huyền Vũ = Hàng xóm ranh ma lén lút"}
    },
    "Tham Gia Biểu Diễn": {
        "muc_tieu": "Xem buổi biểu diễn sân khấu có thành công không",
        "ky_mon": {"dung_than": "Cảnh Môn + Thiên Anh + Can Ngày", "giai_thich": "Cảnh Môn = Sân khấu rực lửa. Thiên Anh = Tài năng diễn xuất", "cach_xem": "Cảnh Môn vượng sinh Can Ngày = Biểu diễn xuất thần", "trong_so": 75, "vi_du": "Thiên Anh vượng tháng Hạ = Tiếng vang lớn"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Sự phô diễn, ánh sáng đèn khấu, cái đẹp", "cach_xem": "Ly sinh Thể = Khán giả vỗ tay không ngớt", "trong_so": 65, "vi_du": "Ly vượng = Diễn xuất có hồn, rất thu hút"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Chu Tước", "giai_thich": "Chu Tước tượng cho tiếng hát, lời thoại trên sân khấu", "cach_xem": "Quan lâm Chu Tước vượng = Danh tiếng sau biểu diễn tăng", "trong_so": 70, "vi_du": "Phụ Mẫu sinh Thế = Kịch bản/Bài hát rất hay"}
    },
    "Xem Ngày Xuất Hành": {
        "muc_tieu": "Xem chọn ngày giờ đi xa cho đại cát",
        "ky_mon": {"dung_than": "Mã Tinh + Hưu Môn + Can Ngày", "giai_thich": "Mã Tinh = Sự chuyển dịch. Hưu Môn = Điềm lành khi đi", "cach_xem": "Hưu Môn lâm cung Mã Tinh = Đi cực tốt", "trong_so": 75, "vi_du": "Can Giờ sinh Can Ngày = Chuyến đi suôn sẻ tuyệt đối"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Sự lên đường, khởi động máy móc tàu xe", "cach_xem": "Chấn sinh Thể = Khởi hành ngày này hanh thông", "trong_so": 60, "vi_du": "Chấn vượng tháng Xuân = Đi lại nhiều may mắn"},
        "luc_hao": {"dung_than": "Hào Thế động hóa Mã", "giai_thich": "Tượng cho việc nhấc chân lên đường", "cach_xem": "Thế động sinh hợp = Ngày đi rất đẹp", "trong_so": 65, "vi_du": "Thế lâm Thanh Long động = Xuất hành gặp quý nhân"}
    },
    "Gặp Tin Tức Giả": {
        "muc_tieu": "Xem thông tin này có phải lừa bịp không",
        "ky_mon": {"dung_than": "Huyền Vũ + Đằng Xà + Cảnh Môn", "giai_thich": "Huyền Vũ = Mờ ám. Đằng Xà = Giả dối. Cảnh Môn = Tin tức", "cach_xem": "Hai thần này lâm Cảnh Môn = Chắc chắn tin giả", "trong_so": 80, "vi_du": "Cảnh Môn lâm Tử Môn = Thông tin đã lạc hậu, vô hiệu"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự giả dối, giấu đầu hở đuôi, thông tin đen", "cach_xem": "Khảm vượng = Tin tức đầy rẫy lừa lọc", "trong_so": 65, "vi_du": "Dụng khắc Thể = Tin giả làm mình điêu đứng"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu lâm Đằng Xà", "giai_thich": "Đằng Xà tượng cho sự biến hóa lắt léo, dối gạt", "cach_xem": "Phụ Mẫu lâm Đằng Xà hóa Không = Tin giả hoàn toàn", "trong_so": 70, "vi_du": "Phụ Mẫu lâm Huyền Vũ = Tin có mục đích xấu"}
    },
    "Thi Tuyển Idol": {
        "muc_tieu": "Xem thi vào làm thực tập sinh/Idol có đỗ không",
        "ky_mon": {"dung_than": "Thiên Anh + Cảnh Môn + Trực Phù", "giai_thich": "Thiên Anh = Tài năng tỏa sáng. Cảnh Môn = Ngành giải trí", "cach_xem": "Thiên Anh sinh Can Ngày = Được chọn làm Idol", "trong_so": 75, "vi_du": "Trực Phù vượng = Công ty giải trí lớn tuyển dụng"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Hào quang, sự rực rỡ nghệ thuật", "cach_xem": "Ly sinh Thể = Đỗ tuyển Idol", "trong_so": 65, "vi_du": "Ly vượng tháng Hạ = Năng khiếu bẩm sinh tốt"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Thanh Long", "giai_thich": "Quan Quỷ = Chức danh nghệ sĩ. Thanh Long = Vẻ đẹp", "cach_xem": "Quan lâm Thanh Long sinh Thế = Trúng tuyển Idol", "trong_so": 70, "vi_du": "Thế lâm Chu Tước = Có giọng hát tốt"}
    },
    "Công Việc Freelance": {
        "muc_tieu": "Xem làm nghề tự do có ổn định thu nhập không",
        "ky_mon": {"dung_than": "Sinh Môn + Khai Môn + Can Ngày", "giai_thich": "Sinh Môn = Lợi nhuận. Khai Môn = Tính chất việc", "cach_xem": "Sinh Môn vượng = Thu nhập Freelance tốt", "trong_so": 70, "vi_du": "Can Ngày lâm cung Sinh Môn = Tự mình làm chủ kinh tế"},
        "mai_hoa": {"dung_than": "Quẻ Tốn - MỘC", "giai_thich": "Tốn = Sự linh hoạt, tự do như gió, không gò bó", "cach_xem": "Tốn sinh Thể = Nghề tự do rất phát", "trong_so": 60, "vi_du": "Tốn vượng tháng Xuân = Việc Freelance nhiều vô kể"},
        "luc_hao": {"dung_than": "Hào Tử Tôn + Thê Tài", "giai_thich": "Tử Tôn = Tự do sáng tạo. Thê Tài = Tiền kiếm được", "cach_xem": "Tử Tài song vượng = Freelance giàu có", "trong_so": 70, "vi_du": "Thế lâm Tử Tôn = Người không thích bị quản thúc"}
    },
    "Xây Dựng Website": {
        "muc_tieu": "Xem làm web có thu hút nhiều người truy cập không",
        "ky_mon": {"dung_than": "Cảnh Môn + Khai Môn + Thiên Bồng", "giai_thich": "Cảnh Môn = Giao diện web. Khai Môn = Public. Thiên Bồng = Online", "cach_xem": "Cảnh Môn vượng sinh Can Ngày = Web rất đẹp và thu hút", "trong_so": 75, "vi_du": "Cảnh Môn lâm cung Khảm = Web vận hành trơn tru"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Mạng internet, công nghệ số, ánh sáng màn hình", "cach_xem": "Ly vượng sinh Thể = Web nhận được nhiều tương tác", "trong_so": 65, "vi_du": "Ly sinh Thể (Thổ) = Web có nền tảng vững chắc"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Chu Tước", "giai_thich": "Phụ Mẫu = Nội dung web. Chu Tước = Truyền bá thông tin", "cach_xem": "Phụ Mẫu vượng sinh Thế = Web có nội dung chất lượng", "trong_so": 70, "vi_du": "Chu Tước động = Web đang lan tỏa mạnh"}
    },
    "Dịch Vụ Tư Vấn": {
        "muc_tieu": "Xem làm nghề tư vấn có đắt khách không",
        "ky_mon": {"dung_than": "Thiên Tâm + Thiên Phụ + Can Ngày", "giai_thich": "Thiên Tâm = Lời khuyên. Thiên Phụ = Kiến thức tư vấn", "cach_xem": "Cung Can Ngày sinh Can Giờ = Khách nghe lời tư vấn", "trong_so": 70, "vi_du": "Thiên Tâm sinh Can Ngày = Mình có tố chất tư vấn giỏi"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Lời nói, thuyết phục, tư vấn tâm lý", "cach_xem": "Đoài sinh Thể = Khách hàng tin tưởng lời mình", "trong_so": 60, "vi_du": "Đoài vượng tháng Thu = Nghề tư vấn gặp thời"},
        "luc_hao": {"dung_than": "Hào Ứng sinh Thế", "giai_thich": "Khách hàng (Ứng) tìm đến mình (Thế)", "cach_xem": "Ứng vượng sinh Thế = Khách rất tin cậy lời tư vấn", "trong_so": 65, "vi_du": "Thế lâm Thanh Long = Tư vấn chuyên nghiệp"}
    },
    "Trở Thành Youtuber": {
        "muc_tieu": "Xem làm kênh Youtube có thành công, nổi tiếng không",
        "ky_mon": {"dung_than": "Cảnh Môn + Thiên Anh + Thiên Bồng", "giai_thich": "Thiên Anh = Hình ảnh cá nhân. Cảnh Môn = Kênh nội dung", "cach_xem": "Cảnh Môn sinh Can Ngày = Kênh thành công", "trong_so": 75, "vi_du": "Thiên Anh vượng = Có sức hút hình ảnh rất lớn"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Video, truyền hình, sự nổi tiếng rực rỡ", "cach_xem": "Ly sinh Thể = Kênh phát triển mạnh mẽ", "trong_so": 65, "vi_du": "Ly vượng tháng Hạ = Lượng Sub tăng nhanh chóng"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Chu Tước", "giai_thich": "Quan Quỷ = Danh tiếng kênh. Chu Tước = Lan truyền mạng", "cach_xem": "Quan vượng sinh Thế = Trở thành Youtuber nổi tiếng", "trong_so": 70, "vi_du": "Tài động hóa Tiến = Doanh thu từ Youtube tăng cao"}
    },
    "Quay Phim Chụp Ảnh": {
        "muc_tieu": "Xem buổi quay/chụp có cho sản phẩm đẹp không",
        "ky_mon": {"dung_than": "Cảnh Môn + Thiên Anh + Canh", "giai_thich": "Cảnh Môn = Sản phẩm hình ảnh. Thiên Anh = Mỹ thuật", "cach_xem": "Cảnh Môn sinh Can Ngày = Ảnh/phim rất đẹp", "trong_so": 70, "vi_du": "Cảnh Môn vượng ở cung 9 = Màu sắc tuyệt vời"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Máy ảnh, ống kính, ánh sáng, thị giác", "cach_xem": "Ly sinh Thể = Chụp/quay rất thành công", "trong_so": 60, "vi_du": "Ly vượng sinh Thể = Hình ảnh sắc nét, có hồn"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thanh Long", "giai_thich": "Phụ Mẫu = Bức ảnh. Thanh Long = Vẻ đẹp tinh tế", "cach_xem": "Phụ Mẫu lâm Thanh Long = Ảnh đẹp như vẽ", "trong_so": 65, "vi_du": "Phụ Mẫu lâm hào 5/6 = Ảnh chụp phong cảnh đẹp"}
    },
    "Thiết Kế Nội Thất": {
        "muc_tieu": "Xem trang trí nhà cửa có đẹp và hợp ý không",
        "ky_mon": {"dung_than": "Sinh Môn + Cảnh Môn + Thiên Phụ", "giai_thich": "Sinh Môn = Ngôi nhà. Cảnh Môn = Nội thất thẩm mỹ", "cach_xem": "Cảnh Môn sinh Sinh Môn = Nội thất hợp với nhà", "trong_so": 70, "vi_du": "Cảnh Môn vượng = Đồ nội thất cao cấp"},
        "mai_hoa": {"dung_than": "Quẻ Tốn - MỘC", "giai_thich": "Tốn = Nghệ thuật sắp đặt, đường nét mềm mại", "cach_xem": "Tốn sinh Thể = Thiết kế nội thất tinh tế", "trong_so": 60, "vi_du": "Tốn vượng tháng Xuân = Thiết kế mang hơi thở thiên nhiên"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Câu Trần", "giai_thich": "Câu Trần tượng cho sự trang hoàng, kiến thiết nhà cửa", "cach_xem": "Phụ Mẫu lâm Câu Trần vượng = Nội thất bền đẹp", "trong_so": 65, "vi_du": "Phụ Mẫu lâm Thanh Long = Nội thất sang quý"}
    },
    "Làm Nghề Thủ Công": {
        "muc_tieu": "Xem làm đồ Handmade có khách mua không",
        "ky_mon": {"dung_than": "Thiên Nhuế + Sinh Môn + Can Ngày", "giai_thich": "Thiên Nhuế = Kỹ năng tay chân. Sinh Môn = Bán đồ có lời", "cach_xem": "Sinh Môn sinh Can Ngày = Đồ Handmade bán chạy", "trong_so": 70, "vi_du": "Thiên Nhuế vượng cung 2 = Tay nghề rất khéo"},
        "mai_hoa": {"dung_than": "Quẻ Tốn/Cấn", "giai_thich": "Tốn = Sự tỉ mỉ. Cấn = Đồ thủ công bằng đất/đá/gỗ", "cach_xem": "Quái sinh Thể = Đồ Handmade có giá trị cao", "trong_so": 60, "vi_du": "Tốn sinh Thể = Đồ Handmade tinh xảo"},
        "luc_hao": {"dung_than": "Hào Tử Tôn + Thê Tài", "giai_thich": "Tử Tôn = Công sức tỉ mỉ. Thê Tài = Lợi nhuận bán đồ", "cach_xem": "Tử Tài đều vượng = Nghề thủ công sống tốt", "trong_so": 65, "vi_du": "Thế lâm Tử Tôn = Người có đôi bàn tay khéo"}
    },
    "Viết Sách Tác Giả": {
        "muc_tieu": "Xem viết sách có nổi tiếng và xuất bản được không",
        "ky_mon": {"dung_than": "Cảnh Môn + Thiên Phụ + Can Ngày", "giai_thich": "Cảnh Môn = Cuốn sách. Thiên Phụ = Văn chương chữ nghĩa", "cach_xem": "Cảnh Môn vượng sinh Can Ngày = Sách bán chạy", "trong_so": 75, "vi_du": "Thiên Phụ sinh Cảnh Môn = Văn hay chữ tốt"},
        "mai_hoa": {"dung_than": "Quẻ Tốn - MỘC", "giai_thich": "Tốn = Sách vở, văn chương lan tỏa", "cach_xem": "Tốn sinh Thể = Tác phẩm tâm đắc", "trong_so": 65, "vi_du": "Tốn vượng ở cung Càn = Tác phẩm có giá trị cao"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Chu Tước", "giai_thich": "Phụ Mẫu = Bản thảo. Chu Tước = Sự bàn tán, khen ngợi", "cach_xem": "Phụ Mẫu vượng sinh Thế = Xuất bản thành công", "trong_so": 70, "vi_du": "Phụ Mẫu lâm Thanh Long = Tác phẩm để đời"}
    },
    "Thiết Kế Đồ Họa": {
        "muc_tieu": "Xem sản phẩm Design có được khách duyệt không",
        "ky_mon": {"dung_than": "Cảnh Môn + Thiên Anh + Can Giờ", "giai_thich": "Cảnh Môn = Bản thiết kế. Can Giờ = Khách hàng", "cach_xem": "Can Giờ sinh Can Ngày = Khách ưng ý ngay", "trong_so": 75, "vi_du": "Cảnh Môn vượng cung 9 = Thiết kế rất bắt mắt"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Đồ họa, màu sắc, bố cục thị giác", "cach_xem": "Ly sinh Thể = Thiết kế đồ họa xuất sắc", "trong_so": 60, "vi_du": "Ly vượng sinh Thể (Thổ) = Thiết kế chuẩn mực"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Ứng", "giai_thich": "Phụ Mẫu = Sản phẩm. Ứng = Khách hàng duyệt", "cach_xem": "Phụ Mẫu sinh Ứng = Thiết kế đúng yêu cầu khách", "trong_so": 65, "vi_du": "Phụ Mẫu lâm Thanh Long = Design cực đẹp"}
    },
    "Học Nghề Làm Đẹp": {
        "muc_tieu": "Xem học nghề Spa/Makeup... có thành công không",
        "ky_mon": {"dung_than": "Thiên Anh + Cảnh Môn + Can Ngày", "giai_thich": "Thiên Anh = Thẩm mỹ. Cảnh Môn = Nghề làm đẹp", "cach_xem": "Cảnh Môn sinh Can Ngày = Học nghề làm đẹp hợp", "trong_so": 70, "vi_du": "Thiên Anh vượng = Có gu thẩm mỹ tốt"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Sự xinh đẹp, trang điểm, dịch vụ thẩm mỹ", "cach_xem": "Đoài sinh Thể = Thành nghề nhanh", "trong_so": 60, "vi_du": "Đoài vượng tháng Thu = Nghề nghiệp phát triển"},
        "luc_hao": {"dung_than": "Hào Tử Tôn + Thanh Long", "giai_thich": "Thanh Long tượng cho vẻ đẹp rạng ngời", "cach_xem": "Thế lâm Tử Tôn vượng = Có khiếu làm đẹp", "trong_so": 65, "vi_du": "Tài vượng sinh Thế = Nghề này kiếm bộn tiền"}
    },
    "Sáng Tạo Nội Dung": {
        "muc_tieu": "Xem làm Content Creator có nhiều Follow không",
        "ky_mon": {"dung_than": "Cảnh Môn + Thiên Anh + Can Giờ", "giai_thich": "Cảnh Môn = Content. Thiên Anh = Sáng tạo. Can Giờ = Fans", "cach_xem": "Can Giờ sinh Can Ngày = Có nhiều Fans ủng hộ", "trong_so": 75, "vi_du": "Cảnh Môn vượng ở cung Càn = Nội dung đẳng cấp"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Sự phô diễn nội dung, nổi tiếng mạng xã hội", "cach_xem": "Ly sinh Thể = Kênh tăng trưởng nhanh", "trong_so": 65, "vi_du": "Ly vượng tháng Hạ = Content nổ ra cực Hot"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ + Chu Tước", "giai_thich": "Chu Tước tượng cho thông tin lan truyền", "cach_xem": "Quan vượng sinh Thế = Content tạo tiếng vang", "trong_so": 70, "vi_du": "Thế lâm Thanh Long = Content sáng tạo cực hay"}
    },
    "Cầu Tự Cúng Bái": {
        "muc_tieu": "Xem việc cúng bái có được linh ứng không",
        "ky_mon": {"dung_than": "Trực Phù + Thiên Nhuế + Can Ngày", "giai_thich": "Trực Phù = Thần linh. Thiên Nhuế = Vật cúng. Can Ngày = Người cúng", "cach_xem": "Trực Phù sinh Can Ngày = Cầu khấn linh ứng", "trong_so": 80, "vi_du": "Trực Phù vinh hiển = Đắc được thần lực giúp đỡ"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Trời, thần tiên, năng lượng tâm linh cao", "cach_xem": "Càn sinh Thể = Cầu xin được chứng giám", "trong_so": 65, "vi_du": "Dụng sinh Thể = Lời cầu nguyện thành hiện thực"},
        "luc_hao": {"dung_than": "Hào Thế vượng lâm Thanh Long", "giai_thich": "Thanh Long tượng cho niềm vui tâm linh, điềm lành", "cach_xem": "Thế vượng lâm Phúc thần = Cúng bái đại cát", "trong_so": 70, "vi_du": "Tử Tôn vượng động = Tai qua nạn khỏi nhờ cúng tế"}
    },
    "Giải Hạn Tam Tai": {
        "muc_tieu": "Xem giải hạn có bớt vận rủi không",
        "ky_mon": {"dung_than": "Thiên Tâm + Lục Hợp + Can Ngày", "giai_thich": "Thiên Tâm = Sự cứu giải. Lục Hợp = Hóa giải xung đột", "cach_xem": "Thiên Tâm khắc cung có hung thần = Giải hạn tốt", "trong_so": 75, "vi_du": "Can Ngày lâm Không = Hạn tự tan biến"},
        "mai_hoa": {"dung_than": "Quẻ Khảm/Ly", "giai_thich": "Khảm = Hạn nước, Ly = Hạn lửa/tai tiếng", "cach_xem": "Thể vượng khắc Chế Dụng = Vượt qua hạn tam tai", "trong_so": 60, "vi_du": "Biến Quái sinh Bản Quẻ = Gặp rủi hóa may"},
        "luc_hao": {"dung_than": "Hào Tử Tôn động", "giai_thich": "Tử Tôn là khắc tinh của Quan Quỷ (Hạn)", "cach_xem": "Tử Tôn động hóa cát = Giải hạn thành công", "trong_so": 70, "vi_du": "Tử Tôn lâm Nhật Nguyệt = Hạn nhẹ như không"}
    },
    "Xem Đồng Thầy": {
        "muc_tieu": "Xem thầy cúng có thực tài và định hướng đúng không",
        "ky_mon": {"dung_than": "Trực Phù + Thiên Tâm + Can Ngày", "giai_thich": "Trực Phù = Thầy có căn cơ. Thiên Tâm = Đạo hạnh", "cach_xem": "Trực Phù sinh Can Ngày = Thầy rất hợp và giỏi", "trong_so": 75, "vi_du": "Thiên Tâm vượng = Thầy có đức độ cao"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Bậc trưởng bối, thầy có uy tín lớn", "cach_xem": "Càn sinh Thể = Thầy chỉ bảo tận tình", "trong_so": 60, "vi_du": "Càn vượng tháng Thu = Thầy đang ở thời kỳ đỉnh cao đạo lực"},
        "luc_hao": {"dung_than": "Hào Ứng sinh Thế", "giai_thich": "Ứng là thầy. Thế là trò", "cach_xem": "Ứng vượng sinh Thế = Thầy có tâm đức truyền dạy", "trong_so": 70, "vi_du": "Ứng lâm Thanh Long = Thầy là bậc chính nhân quân tử"}
    },
    "Mồ Mả Gia Tiên": {
        "muc_tieu": "Xem mồ mả có yên ổn hay bị động",
        "ky_mon": {"dung_than": "Tử Môn + Can Năm + Cửu Địa", "giai_thich": "Tử Môn = Ngôi mộ. Can Năm = Tổ tiên. Cửu Địa = Đất mộ", "cach_xem": "Tử Môn vượng yên tĩnh = Mồ mả yên ổn", "trong_so": 85, "vi_du": "Tử Môn lâm Không = Ngôi mộ bị thất lạc hoặc hư hỏng"},
        "mai_hoa": {"dung_than": "Quẻ Cấn - THỔ", "giai_thich": "Cấn = Ngôi mộ, sự tĩnh mịch, đất đá bao quanh mộ", "cach_xem": "Cấn vượng = Mồ mả vững chãi, đất phát", "trong_so": 70, "vi_du": "Cấn bị khắc = Mồ mả bị rễ cây đâm hoặc sạt lở"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thổ", "giai_thich": "Phụ Mẫu = Mồ mả cha ông. Thổ = Đất cát", "cach_xem": "Phụ Mẫu vượng tĩnh = Mồ mả yên ổn", "trong_so": 75, "vi_du": "Phụ Mẫu mang Bạch Hổ động = Mồ mả đang bị động, rất xấu"}
    },
    "Tu Tập Thiền Định": {
        "muc_tieu": "Xem việc tu tập có tiến bộ, tâm có tịnh không",
        "ky_mon": {"dung_than": "Hưu Môn + Thiên Tâm + Can Ngày", "giai_thich": "Hưu Môn = Trạng thái tĩnh. Thiên Tâm = Tâm linh cao", "cach_xem": "Hưu Môn lâm Can Ngày = Tâm đang rất tịnh", "trong_so": 70, "vi_du": "Thiên Tâm vượng ở cung Khảm = Huệ căn phát triển"},
        "mai_hoa": {"dung_than": "Quẻ Cấn - THỔ", "giai_thich": "Cấn = Sự dừng lại, tĩnh lặng, thiền định", "cach_xem": "Cấn sinh Thể = Thiền định đạt kết quả cao", "trong_so": 65, "vi_du": "Cấn vượng tháng Tứ Quý = Nhập định dễ dàng"},
        "luc_hao": {"dung_than": "Hào Thế lâm Không", "giai_thich": "Không tượng cho tâm vô ngã, hư không", "cach_xem": "Thế lâm Không vượng = Cảnh giới tu tập cao", "trong_so": 70, "vi_du": "Tử Tôn sinh Thế = Tu tập gặp nhiều niềm hỷ lạc"}
    },
    "Vật Phẩm Tâm Linh": {
        "muc_tieu": "Xem linh vật/vòng tay có năng lượng tốt không",
        "ky_mon": {"dung_than": "Trực Phù + Thiên Tâm + Cảnh Môn", "giai_thich": "Trực Phù = Linh khí. Thiên Tâm = Sự hộ mệnh. Cảnh Môn = Vẻ ngoài", "cach_xem": "Trực Phù sinh Can Ngày = Vật phẩm rất linh lực", "trong_so": 75, "vi_du": "Cảnh Môn vượng = Vật phẩm được khai quang tốt"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Vật phẩm quý giá, trang sức đá quý tâm linh", "cach_xem": "Càn sinh Thể = Vật phẩm bổ trợ tốt cho chủ", "trong_so": 60, "vi_du": "Càn vượng = Năng lượng của vật phẩm rất mạnh"},
        "luc_hao": {"dung_than": "Hào Tài lâm Thanh Long", "giai_thich": "Thê Tài là vật phẩm quý. Thanh Long là cát thần", "cach_xem": "Tài vượng sinh Thế = Vật phẩm mang lại may mắn lớn", "trong_so": 70, "vi_du": "Phụ Mẫu mang linh khí sinh Thế = Vật hộ thân đắc lực"}
    },
    "Mua Xe Ô Tô": {
        "muc_tieu": "Xem mua xe có bền, đi đứng an toàn không",
        "ky_mon": {"dung_than": "Khai Môn + Cảnh Môn + Mã Tinh", "giai_thich": "Khai Môn = Máy móc. Cảnh Môn = Ngoại thất. Mã Tinh = Di chuyển", "cach_xem": "Khai Môn sinh Can Ngày = Xe đi rất lành", "trong_so": 75, "vi_du": "Cảnh Môn lâm Bạch Hổ = Xe dễ gặp tai nạn va quệt"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Xe cộ, động cơ, sự chuyển động", "cach_xem": "Chấn sinh Thể = Mua xe đi lại gặp nhiều may mắn", "trong_so": 65, "vi_du": "Chấn vượng tháng Xuân = Xe vận hành rất khỏe"},
        "luc_hao": {"dung_than": "Hào Ứng", "giai_thich": "Ứng tượng cho chiếc xe định mua", "cach_xem": "Ứng vượng sinh Thế = Xe tốt và bền", "trong_so": 70, "vi_du": "Ứng lâm Quan Quỷ mang Bạch Hổ = Xe hay hỏng hóc hoặc có dông"}
    },
    "Mất Điện Thoại": {
        "muc_tieu": "Xem điện thoại mất có tìm lại được không",
        "ky_mon": {"dung_than": "Cảnh Môn + Đinh + Huyền Vũ", "giai_thich": "Cảnh Môn = Điện thoại. Đinh = Chíp/Sim. Huyền Vũ = Mất trộm", "cach_xem": "Cảnh Môn sinh Can Ngày = Tìm lại được máy", "trong_so": 75, "vi_du": "Huyền Vũ lâm cung Cảnh Môn = Chắc chắn bị trộm lấy"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Thiết bị điện tử, màn hình điện thoại", "cach_xem": "Ly sinh Thể = Tìm lại được điện thoại", "trong_so": 60, "vi_du": "Dụng khắc Thể = Mất điện thoại vĩnh viễn"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài = Giá trị món đồ (điện thoại)", "cach_xem": "Tài lâm Không = Không tìm thấy lại được", "trong_so": 65, "vi_du": "Tài phục dưới hào Quan = Đồ đã bị đem đi tiêu thụ/giấu kỹ"}
    },
    "Đồ Vật Gia Bảo": {
        "muc_tieu": "Xem đồ cổ/đồ gia bảo trong nhà có linh không",
        "ky_mon": {"dung_than": "Cửu Địa + Can Năm + Trực Phù", "giai_thich": "Cửu Địa = Đồ lâu đời. Can Năm = Tổ tiên để lại", "cach_xem": "Cửu Địa vượng sinh Can Ngày = Đồ có tính bảo hộ cao", "trong_so": 75, "vi_du": "Trực Phù lâm cung Cửu Địa = Đồ vật rất quý giá và linh"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Sự cũ kỹ, đồ vật từ xưa, di sản", "cach_xem": "Khôn sinh Thể = Đồ vật tổ tiên để lại phù hộ cho mình", "trong_so": 60, "vi_du": "Khôn vượng tháng Tứ Quý = Giá trị đồ vật rất lớn"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thanh Long", "giai_thich": "Phụ Mẫu là vật truyền đời. Thanh Long là sự sang quý", "cach_xem": "Phụ Mẫu vượng sinh Thế = Được hưởng đồ gia bảo tốt", "trong_so": 70, "vi_du": "Phụ Mẫu hào thượng = Đồ vật được đặt ở nơi cao quý nhất nhà"}
    },
    "Thời Tiết Đi Du Lịch": {
        "muc_tieu": "Xem ngày đi du lịch trời có đẹp không",
        "ky_mon": {"dung_than": "Thiên Anh + Thiên Trụ + Can Giờ", "giai_thich": "Thiên Anh = Trời nắng đẹp. Thiên Trụ = Mưa bão", "cach_xem": "Thiên Anh vượng = Trời nắng ráo", "trong_so": 70, "vi_du": "Thiên Trụ vượng + Can Giờ khắc Can Ngày = Đi gặp bão lớn"},
        "mai_hoa": {"dung_than": "Quẻ Ly/Khảm", "giai_thich": "Ly = Nắng, Khảm = Mưa", "cach_xem": "Ly vượng = Thời tiết du lịch tuyệt vời", "trong_so": 60, "vi_du": "Khảm sinh Thể (Mộc) = Mưa nhỏ không ảnh hưởng nhiều"},
        "luc_hao": {"dung_than": "Hào mang Chu Tước / Huyền Vũ", "giai_thich": "Chu Tước = Trời hưởng nắng. Huyền Vũ = Trời âm u/mưa", "cach_xem": "Chu Tước vượng = Đi du lịch gặp nắng đẹp", "trong_so": 65, "vi_du": "Huyền Vũ động = Có mưa bất chợt trên đường đi"}
    },
    "Dự Báo Mưa Bão": {
        "muc_tieu": "Xem sắp tới có mưa to bão lớn không",
        "ky_mon": {"dung_than": "Thiên Trụ + Thiên Phụ + Thiên Bồng", "giai_thich": "Thiên Trụ = Gió bão. Thiên Bồng = Mưa lớn", "cach_xem": "Hai sao này lâm vượng địa = Sắp có bão mạnh", "trong_so": 80, "vi_du": "Thiên Trụ khắc cung có Can Ngày = Bão gây thiệt hại cho mình"},
        "mai_hoa": {"dung_than": "Quẻ Khảm/Tốn", "giai_thich": "Khảm = Mưa to. Tốn = Gió lớn", "cach_xem": "Khảm Tốn cùng xuất hiện = Mưa bão dữ dội", "trong_so": 70, "vi_du": "Dụng khắc Thể = Bão gây đổ nát nhà cửa"},
        "luc_hao": {"dung_than": "Hào mang Huyền Vũ + Đằng Xà", "giai_thich": "Huyền Vũ = Thủy (mưa). Đằng Xà = Gió lốc", "cach_xem": "Huyền Vũ động hóa Tiến = Mưa kéo dài không dứt", "trong_so": 75, "vi_du": "Quan Quỷ động mang Bạch Hổ = Bão tố gây hiểm họa lớn"}
    },
    "Thiên Tai Động Đất": {
        "muc_tieu": "Xem vùng này có nguy cơ thiên tai không",
        "ky_mon": {"dung_than": "Tử Môn + Thiên Nhuế + Cửu Địa", "giai_thich": "Tử Môn = Đất chết. Thiên Nhuế = Tai ương. Cửu Địa = Địa tầng", "cach_xem": "Tử Môn lâm Chấn (3/4) = Nguy cơ động đất cao", "trong_so": 85, "vi_du": "Thiên Nhuế lâm vượng địa = Tai nạn đất đai rất nặng"},
        "mai_hoa": {"dung_than": "Quẻ Cấn/Chấn", "giai_thich": "Cấn = Núi đất, Chấn = Chấn động địa chất", "cach_xem": "Cấn biến Chấn = Nguy cơ sạt lở hoặc động đất", "trong_so": 75, "vi_du": "Dụng khắc Thể = Thiên tai gây họa cho bản thân"},
        "luc_hao": {"dung_than": "Hào Thổ động mang Bạch Hổ", "giai_thich": "Thổ động = Đất rung chuyển. Bạch Hổ = Tang thương", "cach_xem": "Thổ hào vượng động = Động đất thực sự nổ ra", "trong_so": 80, "vi_du": "Thế lâm mồ Thổ = Bị ảnh hưởng bởi thiên tai đất đai"}
    },
    "Vụ Mùa Bội Thu": {
        "muc_tieu": "Xem mùa màng nông nghiệp có được mùa không",
        "ky_mon": {"dung_than": "Sinh Môn + Thiên Nhuế + Can Năm", "giai_thich": "Sinh Môn = Sản vật. Thiên Nhuế = Đất/Nông nghiệp", "cach_xem": "Sinh Môn sinh Can Năm = Mùa màng bội thu", "trong_so": 75, "vi_du": "Sinh Môn lâm Không = Mất mùa trắng tay"},
        "mai_hoa": {"dung_than": "Quẻ Khôn - THỔ", "giai_thich": "Khôn = Đất đai canh tác, sự sinh sản của đất", "cach_xem": "Khôn vượng = Mùa màng xanh tốt", "trong_so": 65, "vi_du": "Khôn sinh Thể = Năng suất nông nghiệp rất cao"},
        "luc_hao": {"dung_than": "Hào Tử Tôn + Thê Tài", "giai_thich": "Tử Tôn = Sản lượng. Thê Tài = Giá trị nông phẩm", "cach_xem": "Tử Tài đều vượng = Được mùa được giá", "trong_so": 70, "vi_du": "Tử Tôn lâm Nhật Nguyệt = Cây cối phát triển cực tốt"}
    },
    "Phát Triển Chăn Nuôi": {
        "muc_tieu": "Xem nuôi gia súc có thuận lợi không",
        "ky_mon": {"dung_than": "Thiên Nhuế + Sinh Môn + Thiên Bồng", "giai_thich": "Thiên Nhuế = Con giống. Sinh Môn = Phát triển. Thiên Bồng = Lợn/Thủy sản", "cach_xem": "Sinh Môn sinh Thiên Nhuế = Vật nuôi chóng lớn", "trong_so": 75, "vi_du": "Thiên Nhuế lâm Tử Môn = Vật nuôi dễ bị dịch bệnh chết"},
        "mai_hoa": {"dung_than": "Quẻ Cấn/Chấn", "giai_thich": "Cấn = Con vật ở núi, Chấn = Con vật mau lớn", "cach_xem": "Cấn sinh Thể = Chăn nuôi gặp may", "trong_so": 60, "vi_du": "Dụng khắc Thể = Gia súc gây thiệt hại kinh tế"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn tượng cho các loại lục súc, vật nuôi", "cach_xem": "Tử Tôn vượng = Chăn nuôi phát đạt", "trong_so": 70, "vi_du": "Tử Tôn lâm mồ Quan = Vật nuôi hay bị bệnh ẩn tàng"}
    },
    "Đánh Bắt Thủy Sản": {
        "muc_tieu": "Xem đi biển, đánh cá có trúng đậm không",
        "ky_mon": {"dung_than": "Thiên Bồng + Hưu Môn + Thê Tài", "giai_thich": "Thiên Bồng = Cá/Thủy sản. Hưu Môn = Sông biển", "cach_xem": "Thiên Bồng sinh Can Ngày = Đánh bắt được nhiều", "trong_so": 75, "vi_du": "Hưu Môn lâm cung 1 (Khảm) = Đi biển gặp nhiều tôm cá"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sông, ngòi, biển cả, tôm cá", "cach_xem": "Khảm sinh Thể = Thu hoạch thủy sản dồi dào", "trong_so": 65, "vi_du": "Khảm vượng tháng Đông = Thời điểm đánh bắt vàng"},
        "luc_hao": {"dung_than": "Hào Thê Tài hành Thủy", "giai_thich": "Tài hành Thủy tượng cho lợi nhuận từ nước", "cach_xem": "Tài vượng sinh Thế = Đánh bắt có lời lớn", "trong_so": 70, "vi_du": "Thế lâm Huyền Vũ = Đi biển cần cẩn thận kẻo bị lạc"}
    },
    "Tìm Nguồn Nước": {
        "muc_tieu": "Xem khoan giếng, tìm mạch nước có được không",
        "ky_mon": {"dung_than": "Hưu Môn + Thiên Bồng + Khảm", "giai_thich": "Hưu Môn = Nguồn nước. Thiên Bồng = Nước ngầm", "cach_xem": "Cung Khảm vượng địa = Mạch nước dồi dào", "trong_so": 70, "vi_du": "Hưu Môn lâm vượng địa = Nước sạch và nhiều"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Nguồn nước ngầm dưới đất", "cach_xem": "Khảm sinh Thể = Tìm được mạch nước tốt", "trong_so": 60, "vi_du": "Khảm vượng sinh hợp = Mạch nước không bao giờ cạn"},
        "luc_hao": {"dung_than": "Hào mang hành Thủy", "giai_thich": "Thủy hào tượng cho mạch nước ngầm", "cach_xem": "Thủy hào vượng phục dưới hào Thổ = Có mạch nước sâu", "trong_so": 65, "vi_du": "Thủy hào lâm Không = Giếng bị cạn nước"}
    },
    "Xem Cảnh Đẹp Thiên Nhiên": {
        "muc_tieu": "Xem đi ngắm cảnh có thấy được cảnh đẹp không",
        "ky_mon": {"dung_than": "Cảnh Môn + Thiên Anh + Can Ngày", "giai_thich": "Cảnh Môn = Cảnh đẹp. Thiên Anh = Sự mỹ lệ", "cach_xem": "Cảnh Môn sinh Can Ngày = Thấy cảnh đẹp tuyệt vời", "trong_so": 70, "vi_du": "Cảnh Môn lâm Cửu Thiên = Cảnh trí hùng vĩ"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Mỹ cảnh, sự phô diễn của thiên nhiên", "cach_xem": "Ly vượng sinh Thể = Gặp cảnh sắc rực rỡ", "trong_so": 60, "vi_du": "Ly biến Càn = Cảnh sắc tráng lệ như cung đình"},
        "luc_hao": {"dung_than": "Hào Thế lâm Thanh Long", "giai_thich": "Thanh Long tượng cho vẻ đẹp tự nhiên, thanh tao", "cach_xem": "Thế vượng lâm Thanh Long = Thưởng ngoạn cảnh đẹp mỹ mãn", "trong_so": 65, "vi_du": "Ứng lâm Thanh Long = Cảnh vật rất hữu tình"}
    },
    "Bảo Vệ Môi Trường": {
        "muc_tieu": "Xem dự án môi trường có tác động tốt không",
        "ky_mon": {"dung_than": "Thiên Phụ + Sinh Môn + Thiên Tâm", "giai_thich": "Thiên Phụ = Cây xanh/Môi trường. Sinh Môn = Sự sống mới", "cach_xem": "Thiên Phụ sinh Sinh Môn = Dự án môi trường rất hiệu quả", "trong_so": 75, "vi_du": "Thiên Phụ vượng ở cung 3/4 = Rừng cây phát triển tốt"},
        "mai_hoa": {"dung_than": "Quẻ Tốn/Chấn - MỘC", "giai_thich": "Tượng cho cây cối, sự tươi mát của môi trường", "cach_xem": "Mộc vượng sinh Thể (Hỏa) = Môi trường cải thiện đời sống", "trong_so": 60, "vi_du": "Mộc vượng tháng Xuân = Thiên nhiên đang phục hồi"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn tượng cho sự trong sạch, không ô nhiễm", "cach_xem": "Tử Tôn vượng = Môi trường sạch sẽ lành mạnh", "trong_so": 65, "vi_du": "Tử Tôn lâm Thanh Long = Không khí cực kỳ trong lành"}
    },
    "Dự Báo Lũ Lụt": {
        "muc_tieu": "Xem nước lũ có tràn về gây hại không",
        "ky_mon": {"dung_than": "Thiên Bồng + Hưu Môn + Huyền Vũ", "giai_thich": "Thiên Bồng = Nguồn nước lớn. Huyền Vũ = Sự tràn lan", "cach_xem": "Thiên Bồng vượng khắc cung Khôn/Cấn = Đất không giữ được nước (lũ)", "trong_so": 80, "vi_du": "Hưu Môn lâm cung Chấn = Nước lũ dâng nhanh"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự nguy hiểm của dòng nước, lũ lụt", "cach_xem": "Khảm vượng khắc Thể (Ly) = Lũ lụt gây họa lớn", "trong_so": 70, "vi_du": "Bản Quẻ là Khảm = Vùng đất dễ bị ngập lụt"},
        "luc_hao": {"dung_than": "Hào Thủy vượng động mang Bạch Hổ", "giai_thich": "Thủy động = Nước dâng. Bạch Hổ = Tai họa đổ máu", "cach_xem": "Thủy hào hóa Tiến = Nước lũ đang lên cao cực độ", "trong_so": 75, "vi_du": "Quan lâm Thủy hào = Nước lũ mang theo tai ương pháp lý/tính mạng"}
    },
    "Sự Việc Đột Xuất": {
        "muc_tieu": "Xem sự việc bất ngờ xảy ra là cát hay hung",
        "ky_mon": {"dung_than": "Thương Môn + Can Giờ + Trực Phù", "giai_thich": "Thương Môn = Sự đột ngột. Can Giờ = Sự việc nảy sinh", "cach_xem": "Can Giờ sinh Can Ngày = Việc bất ngờ mang lại lợi ích", "trong_so": 70, "vi_du": "Can Giờ khắc Can Ngày = Việc bất ngờ gây sốc/họa"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Sấm sét, sự việc xảy ra trong chớp mắt", "cach_xem": "Chấn sinh Thể = Tin mừng bất ngờ", "trong_so": 60, "vi_du": "Chấn khắc Thể = Tai họa trời giáng"},
        "luc_hao": {"dung_than": "Hào động trong quẻ", "giai_thich": "Hào động tượng cho sự biến đổi bất ngờ", "cach_xem": "Hào động sinh Thế = Việc bất ngờ có lợi", "trong_so": 65, "vi_du": "Hào động hóa xung = Sự việc chuyển biến xấu nhanh chóng"}
    },
    "Lựa Chọn Phương Án": {
        "muc_tieu": "Xem phương án nào tối ưu nhất lúc này",
        "ky_mon": {"dung_than": "Khai Môn + Thiên Tâm + Trực Phù", "giai_thich": "Khai Môn = Giải pháp. Thiên Tâm = Sự sáng suốt", "cach_xem": "Cung Khai Môn vượng nhất là phương án tốt", "trong_so": 75, "vi_du": "Trực Phù lâm cung nào thì phương án đó uy tín nhất"},
        "mai_hoa": {"dung_than": "Quẻ Thể + Dụng", "giai_thich": "So sánh các cặp Quái tượng để chọn", "cach_xem": "Dụng sinh Thể = Phương án này mang lại lợi ích lớn", "trong_so": 65, "vi_du": "Hỗ Quái là phương án trung gian dự phòng"},
        "luc_hao": {"dung_than": "Hào Thế + Tử Tôn", "giai_thich": "Tử Tôn là hào sinh ra phương kế, giải pháp", "cach_xem": "Hào Tử Tôn vượng là phương án khả thi cao", "trong_so": 70, "vi_du": "Thế động hóa cát = Chọn phương án mới sẽ tốt"}
    },
    "Xem Điềm Báo Giấc Mơ": {
        "muc_tieu": "Xem giấc mơ đêm qua báo hiệu điều gì",
        "ky_mon": {"dung_than": "Đằng Xà + Cảnh Môn + Can Ngày", "giai_thich": "Đằng Xà = Giấc mơ kịch tính. Cảnh Môn = Hình ảnh trong mơ", "cach_xem": "Đằng Xà sinh Can Ngày = Mơ báo điềm lành", "trong_so": 75, "vi_du": "Đằng Xà mang Tử Môn = Giấc mơ cảnh báo nguy hiểm"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Sự ảo mộng, huyễn giác, điềm báo qua hình ảnh", "cach_xem": "Ly sinh Thể = Giấc mơ báo tin vui sắp tới", "trong_so": 60, "vi_du": "Ly biến Khảm = Giấc mơ báo hiệu sự lo âu, cạm bẫy"},
        "luc_hao": {"dung_than": "Hào Thế lâm Đằng Xà", "giai_thich": "Đằng Xà tượng cho sự quay quắt của tâm trí trong mơ", "cach_xem": "Thế lâm Đằng Xà vượng = Giấc mơ có ý nghĩa linh báo mạnh", "trong_so": 70, "vi_du": "Quan lâm Đằng Xà = Giấc mơ do lo lắng công việc mà ra"}
    },
    "Kế Hoạch Dự Phòng": {
        "muc_tieu": "Xem có cần kế hoạch B cho công việc không",
        "ky_mon": {"dung_than": "Hỗ Quái (trong logic) + Thiên Tâm + Cửu Địa", "giai_thich": "Cửu Địa = Sự phòng thủ vững chắc. Thiên Tâm = Mưu lược", "cach_xem": "Cung Cửu Địa vượng = Kế hoạch dự phòng rất hiệu quả", "trong_so": 70, "vi_du": "Thiên Tâm lâm cung Khảm = Kế hoạch bí mật rất sâu sắc"},
        "mai_hoa": {"dung_than": "Hỗ Quái", "giai_thich": "Hỗ Quái tượng cho việc ẩn tàng, dự phòng phía sau", "cach_xem": "Hỗ Quái sinh Thể = Kế hoạch B sẽ cứu nguy lúc cần", "trong_so": 65, "vi_du": "Hỗ Quái khắc Thể = Kế hoạch dự phòng cũng không ăn thua"},
        "luc_hao": {"dung_than": "Hào Thế Phục dưới hào khác", "giai_thich": "Tượng cho sự ẩn náu, chờ thời, phương án ẩn", "cach_xem": "Hào Phục vượng sinh Thế = Phương án ẩn rất mạnh", "trong_so": 65, "vi_du": "Phục dưới hào Quan = Kế hoạch do cấp trên vạch sẵn"}
    },
    "Tìm Quý Nhân Giúp Đỡ": {
        "muc_tieu": "Xem quý nhân ở phương nào, là ai",
        "ky_mon": {"dung_than": "Trực Phù + Thiên Ất + Can Ngày", "giai_thich": "Trực Phù = Quý nhân lớn nhất. Thiên Ất = Người trợ giúp", "cach_xem": "Trực Phù ở cung nào thì quý nhân ở hướng đó", "trong_so": 80, "vi_du": "Trực Phù sinh Can Ngày = Quý nhân tự tìm đến giúp"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Người có quyền chức, bậc trưởng thượng giúp mình", "cach_xem": "Càn sinh Thể = Gặp được quý nhân đại cát", "trong_so": 65, "vi_du": "Dụng sinh Thể = Có người mang cơ hội đến cho mình"},
        "luc_hao": {"dung_than": "Hào Ứng sinh Thế + Thanh Long", "giai_thich": "Ứng là người ngoài, Thanh Long là điềm cát", "cach_xem": "Ứng vượng sinh Thế = Quý nhân phù trợ hết mình", "trong_so": 75, "vi_du": "Quý nhân hào ứng lâm Nhật Nguyệt = Sức giúp đỡ vô cùng lớn"}
    },
    "Chống Lại Áp Lực": {
        "muc_tieu": "Xem khả năng chịu đựng và vượt qua áp lực",
        "ky_mon": {"dung_than": "Trực Phù + Thiên Tâm + Can Ngày", "giai_thich": "Trực Phù = Khả năng chịu đựng. Can Ngày = Bản thân", "cach_xem": "Can Ngày vượng địa = Vượt qua áp lực dễ dàng", "trong_so": 70, "vi_du": "Kinh Môn khắc Can Ngày = Áp lực tâm lý rất lớn"},
        "mai_hoa": {"dung_than": "Quẻ Thể - Bản thân", "giai_thich": "Thể vượng biểu thị nội lực mạnh mẽ trước khó khăn", "cach_xem": "Thể vượng khắc Dụng = Chế ngự được hoàn cảnh áp lực", "trong_so": 60, "vi_du": "Thể suy bị Dụng khắc = Kiệt sức vì áp lực bộn bề"},
        "luc_hao": {"dung_than": "Hào Thế vượng mang Bạch Hổ", "giai_thich": "Bạch Hổ tượng cho sức mạnh kiên cường, gai góc", "cach_xem": "Thế vượng lâm Bạch Hổ = Càng áp lực càng tỏa sáng", "trong_so": 70, "vi_du": "Thế lâm mồ Quan = Bị áp lực đè nén không thoát ra được"}
    },
    "Mở Rộng Tầm Nhìn": {
        "muc_tieu": "Xem có nên thay đổi tư duy, hướng đi mới không",
        "ky_mon": {"dung_than": "Cửu Thiên + Thiên Phụ + Can Ngày", "giai_thich": "Cửu Thiên = Tầm nhìn xa. Thiên Phụ = Kiến thức mới", "cach_xem": "Cửu Thiên vượng sinh Can Ngày = Tầm nhìn mới rất sáng", "trong_so": 70, "vi_du": "Cảnh Môn lâm Cửu Thiên = Hào quang rộng mở phía trước"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Sự sáng suốt, tầm nhìn, hiểu biết rộng mở", "cach_xem": "Ly sinh Thể = Tư duy mới mang lại bước ngoặt lớn", "trong_so": 65, "vi_du": "Biến Quái vượng = Hướng đi mới cực kỳ triển vọng"},
        "luc_hao": {"dung_than": "Hào Thế động hóa Tiến", "giai_thich": "Tượng cho sự phát triển vươn lên tầm cao mới", "cach_xem": "Thế động hóa Tiến sinh hợp = Tầm nhìn mới đại thành công", "trong_so": 70, "vi_du": "Thế lâm Thanh Long động = Sự thay đổi mang lại vinh hiển"}
    },
    "Gìn Giữ Hòa Khí": {
        "muc_tieu": "Xem cách duy trì các mối quan hệ êm đẹp",
        "ky_mon": {"dung_than": "Lục Hợp + Hưu Môn + Can Ngày", "giai_thich": "Lục Hợp = Sự gắn kết. Hưu Môn = Sự hòa nhã", "cach_xem": "Lục Hợp sinh cả Can Ngày và Can Giờ = Hòa khí đại cát", "trong_so": 75, "vi_du": "Thương Môn lâm Lục Hợp = Hòa khí bị đe dọa bởi lời nói"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Sự vui vẻ, nhu thuận trong giao tiếp", "cach_xem": "Đoài vượng sinh hợp = Mọi người thân ái với nhau", "trong_so": 60, "vi_du": "Thể Dụng tỵ hòa = Không cần lo lắng về mâu thuẫn"},
        "luc_hao": {"dung_than": "Hào Thế Ứng tương hợp", "giai_thich": "Lục hợp tượng cho sự khăng khít, hòa thuận", "cach_xem": "Thế Ứng tương hợp sinh nhau = Hòa khí bền lâu", "trong_so": 70, "vi_du": "Tuất Thổ Thế hợp Mão Mộc Ứng = Tình cảm gắn bó keo sơn"}
    },
    "Vay Vốn Ngân Hàng": {
        "muc_tieu": "Xem vay ngân hàng có được giải ngân không",
        "ky_mon": {"dung_than": "Mậu (Vốn) + Khai Môn (Ngân hàng) + Trực Phù", "giai_thich": "Mậu là tiền vay. Khai Môn là tổ chức tín dụng", "cach_xem": "Khai Môn sinh Can Ngày = Ngân hàng duyệt vay", "trong_so": 75, "vi_du": "Mậu lâm Không = Khoản vay bị treo hoặc không có vốn"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Cơ quan nhà nước, ngân hàng lớn uy tín", "cach_xem": "Càn sinh Thể = Vay tiền thuận lợi nhanh chóng", "trong_so": 65, "vi_du": "Càn khắc Thể = Ngân hàng từ chối cho vay"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Thê Tài", "giai_thich": "Phụ Mẫu = Hợp đồng tín dụng. Tài = Khoản vay", "cach_xem": "Phụ Mẫu vượng sinh Thế = Ký được hợp đồng vay vốn", "trong_so": 70, "vi_du": "Tài lâm hào Ứng = Tiền đang đợi ở phía ngân hàng"}
    },
    "Thanh Toán Nợ Nần": {
        "muc_tieu": "Xem chủ nợ có đòi gắt không, trả được không",
        "ky_mon": {"dung_than": "Can Ngày (Mình) + Can Giờ (Chủ nợ) + Mậu", "giai_thich": "Mậu là số tiền nợ cần trả", "cach_xem": "Can Ngày sinh Can Giờ = Mình chủ động trả nợ tốt", "trong_so": 75, "vi_du": "Can Giờ khắc Can Ngày = Chủ nợ đòi rất quyết liệt"},
        "mai_hoa": {"dung_than": "Quẻ Thể (Mình) + Dụng (Nợ)", "giai_thich": "Dụng tượng cho gánh nặng nợ nần cần giải quyết", "cach_xem": "Thể khắc Dụng = Mình trả nợ xong xuôi", "trong_so": 60, "vi_du": "Dụng khắc Thể = Nợ nần đè nặng vất vả"},
        "luc_hao": {"dung_than": "Hào Ứng là chủ nợ", "giai_thich": "Ứng tượng cho đối phương đang cầm giấy nợ", "cach_xem": "Ứng vượng khắc Thế = Bị đòi nợ căng thẳng", "trong_so": 70, "vi_du": "Tài vượng sinh Thế = Có tiền để thanh toán hết nợ"}
    },
    "Tranh Chấp Bản Quyền": {
        "muc_tieu": "Xem kiện tụng về bản quyền, chất xám",
        "ky_mon": {"dung_than": "Thiên Phụ + Cảnh Môn + Kinh Môn", "giai_thich": "Thiên Phụ = Trí tuệ. Cảnh Môn = Tác phẩm. Kinh Môn = Kiện tụng", "cach_xem": "Thiên Phụ sinh Can Ngày = Mình nắm lợi thế bản quyền", "trong_so": 75, "vi_du": "Cảnh Môn lâm Huyền Vũ = Tác phẩm bị đạo nhái"},
        "mai_hoa": {"dung_than": "Quẻ Tốn - MỘC", "giai_thich": "Tốn = Sự sao chép, lan tỏa, văn chương", "cach_xem": "Tốn sinh Thể = Bảo vệ được bản quyền", "trong_so": 60, "vi_du": "Tốn khắc Thể = Bản quyền bị xâm phạm gây thiệt hại"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu tượng cho bản quyền, giấy tờ chứng nhận", "cach_xem": "Phụ Mẫu vượng sinh Thế = Chứng cứ bản quyền vững chắc", "trong_so": 70, "vi_du": "Phụ Mẫu lâm Không = Thiếu bằng chứng bản quyền"}
    },
    "Bảo Mật Thông Tin": {
        "muc_tieu": "Xem dữ liệu có bị rò rỉ hoặc hacker tấn công không",
        "ky_mon": {"dung_than": "Huyền Vũ + Thiên Bồng + Cảnh Môn", "giai_thich": "Huyền Vũ = Hacker/Kẻ trộm tin. Cảnh Môn = Thông tin bảo mật", "cach_xem": "Huyền Vũ sinh Cảnh Môn = Nguy cơ bị xâm nhập cao", "trong_so": 80, "vi_du": "Cửu Địa lâm Cảnh Môn = Thông tin được bảo vệ rất kín"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự bí mật, ẩn tối, kẽ hở bảo mật", "cach_xem": "Khảm vượng mang hung = Bị lộ thông tin", "trong_so": 65, "vi_du": "Dụng khắc Thể = Rò rỉ thông tin gây hậu quả lớn"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ lâm Huyền Vũ", "giai_thich": "Quan lâm Huyền Vũ tượng cho kẻ trộm tin bí mật", "cach_xem": "Quan động khắc Thế = Bị tấn công mạng", "trong_so": 75, "vi_du": "Phụ Mẫu lâm Cửu Địa vượng = Hệ thống bảo mật kiên cố"}
    },
    "Đầu Tư Chứng Khoán": {
        "muc_tieu": "Xem mua mã chứng khoán này có lời không",
        "ky_mon": {"dung_than": "Mậu + Sinh Môn + Bính/Đinh", "giai_thich": "Mậu = Vốn đầu tư. Sinh Môn = Lợi nhuận. Bính/Đinh = Biến động đỏ/xanh", "cach_xem": "Sinh Môn vượng sinh Can Ngày = Chứng khoán lên giá", "trong_so": 85, "vi_du": "Sinh Môn lâm Không = Giá chứng khoán sụt giảm mạnh"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Sàn giao dịch, vàng bạc, sự biến động giá", "cach_xem": "Đoài sinh Thể = Đầu tư chứng khoán có lãi", "trong_so": 70, "vi_du": "Đoài vượng tháng Thu = Thị trường đang sôi động"},
        "luc_hao": {"dung_than": "Hào Thê Tài", "giai_thich": "Thê Tài là giá trị cổ phiếu", "cach_xem": "Tài vượng hóa Tiến = Giá cổ phiếu sẽ còn tăng cao", "trong_so": 80, "vi_du": "Tài động hóa Thoái = Nên bán ngay kẻo lỗ"}
    },
    "Đầu Tư Tiền Điện Tử": {
        "muc_tieu": "Xem đầu tư Coin, tiền ảo có rủi ro không",
        "ky_mon": {"dung_than": "Thiên Bồng + Đinh + Sinh Môn", "giai_thich": "Thiên Bồng = Sự mạo hiểm cao. Đinh = Công nghệ số", "cach_xem": "Sinh Môn sinh Can Ngày = Đầu tư Coin có lời", "trong_so": 80, "vi_du": "Thiên Bồng lâm Tử Môn = Mất trắng vốn đầu tư ảo"},
        "mai_hoa": {"dung_than": "Quẻ Ly - HỎA", "giai_thich": "Ly = Tiền điện tử, ánh sáng ảo, sàn giao dịch số", "cach_xem": "Ly sinh Thể = Đầu tư tiền ảo gặp may", "trong_so": 65, "vi_du": "Ly quái biến Khảm = Rủi ro sập sàn cao"},
        "luc_hao": {"dung_than": "Hào Thê Tài + Đằng Xà", "giai_thich": "Đằng Xà tượng cho sự biến ảo khôn lường của Coin", "cach_xem": "Tài vượng hóa cát = Coin tăng giá phi mã", "trong_so": 70, "vi_du": "Tài lâm Đằng Xà động = Giá biến động cực mạnh trong ngày"}
    },
    "Đầu Tư Vàng": {
        "muc_tieu": "Xem mua vàng tích trữ lúc này có tốt không",
        "ky_mon": {"dung_than": "Mậu + Sinh Môn + Cung 6/7", "giai_thich": "Cung 6 (Càn)/7 (Đoài) thuộc Kim tượng cho Vàng", "cach_xem": "Cung Đoài vượng sinh Can Ngày = Mua vàng là đúng đắn", "trong_so": 75, "vi_du": "Mậu lâm cung Càn = Vàng là tài sản trú ẩn an toàn"},
        "mai_hoa": {"dung_than": "Quẻ Càn/Đoài - KIM", "giai_thich": "Tượng cho vàng bạc, kim loại quý", "cach_xem": "Kim sinh Thể (Thủy) = Đầu tư vàng sinh lời", "trong_so": 65, "vi_du": "Kim vượng tháng Thu = Giá vàng đang ở đỉnh"},
        "luc_hao": {"dung_than": "Hào Thê Tài hành Kim", "giai_thich": "Tài hành Kim tượng cho tiền vàng thực thụ", "cach_xem": "Tài Kim vượng tĩnh = Vàng giữ giá tốt", "trong_so": 70, "vi_du": "Tài Kim hóa xung = Giá vàng biến động thất thường"}
    },
    "Thành Lập Công Ty": {
        "muc_tieu": "Xem mở công ty mới có phát đạt bền vững không",
        "ky_mon": {"dung_than": "Khai Môn + Trực Phù + Can Giờ", "giai_thich": "Khai Môn = Sự khởi nghiệp. Can Giờ = Tương lai công ty", "cach_xem": "Khai Môn vượng sinh Can Ngày = Công ty phát triển mạnh", "trong_so": 85, "vi_du": "Trực Phù lâm Khai Môn = Công ty có uy tín lớn từ đầu"},
        "mai_hoa": {"dung_than": "Quẻ Chấn - MỘC", "giai_thich": "Chấn = Sự khởi đầu, hăng hái, bùng nổ kinh doanh", "cach_xem": "Chấn sinh Thể = Mở công ty gặp nhiều thuận lợi", "trong_so": 70, "vi_du": "Chấn biến Khôn = Khởi đầu mạnh sau đó đi vào ổn định"},
        "luc_hao": {"dung_than": "Hào Thế vượng động", "giai_thich": "Thế động tượng cho việc bắt đầu gây dựng sự nghiệp", "cach_xem": "Thế động hóa cát = Công ty ngày càng đi lên", "trong_so": 80, "vi_du": "Tài vượng sinh Thế = Công ty làm ăn có lãi ngay"}
    },
    "Giải Thể Công Ty": {
        "muc_tieu": "Xem đóng cửa doanh nghiệp có êm xuôi không",
        "ky_mon": {"dung_than": "Tử Môn + Khai Môn + Can Ngày", "giai_thich": "Tử Môn = Kết thúc. Khai Môn = Hình thức pháp lý công ty", "cach_xem": "Tử Môn lâm Khai Môn = Giải thể nhanh gọn", "trong_so": 75, "vi_du": "Kinh Môn lâm Khai Môn = Giải thể gặp rắc rối pháp lý cãi vã"},
        "mai_hoa": {"dung_than": "Quẻ Càn biến Khảm", "giai_thich": "Càn là công ty, biến Khảm là đi vào chỗ bế tắc/kết thúc", "cach_xem": "Quẻ suy phế = Thời điểm đóng cửa đã đến", "trong_so": 60, "vi_du": "Quẻ biến khắc Quẻ chủ = Giải thể gặp nhiều khó khăn"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ hướng tuyệt", "giai_thich": "Quan Quỷ (Công việc) đi vào tuyệt địa là kết thúc", "cach_xem": "Thế động hóa không/tuyệt = Tự nguyện đóng cửa doanh nghiệp", "trong_so": 70, "vi_du": "Tài lâm Không = Công ty hết vốn phải giải thể"}
    },
    "Tìm Người Đi Lạc": {
        "muc_tieu": "Xem người thân đi lạc đang ở hướng nào, có về không",
        "ky_mon": {"dung_than": "Lục Thân (theo vai vế) + Can Giờ", "giai_thich": "Can Giờ tượng cho người đi lạc nói chung", "cach_xem": "Can Giờ ở cung nào thì người đó ở hướng đó", "trong_so": 80, "vi_du": "Can Giờ lâm Không = Người đang ở nơi kín đáo khó tìm"},
        "mai_hoa": {"dung_than": "Quẻ hướng của Dụng Quái", "giai_thich": "Dụng Quái ứng với phương hướng người đó đang ở", "cach_xem": "Dụng sinh Thể = Người sẽ sớm quay về", "trong_so": 70, "vi_du": "Dụng khắc Thể = Người đi gặp khó khăn cản trở không về được"},
        "luc_hao": {"dung_than": "Hào tượng trưng cho người thân", "giai_thich": "Phụ Mẫu = Cha mẹ, Tử Tôn = Con cái...", "cach_xem": "Hào vượng động sinh Thế = Người sẽ tự tìm về", "trong_so": 75, "vi_du": "Hào lâm mộ = Người đang bị giữ lại hoặc ở trong nhà"}
    },
    "Thang Máy Nhà Ở": {
        "muc_tieu": "Xem lắp đặt thang máy có an toàn, vận hành tốt không",
        "ky_mon": {"dung_than": "Khai Môn + Cảnh Môn + Canh", "giai_thich": "Khai Môn = Máy móc thang máy. Canh = Kim loại/Cáp", "cach_xem": "Khai Môn vượng sinh Can Ngày = Thang máy rất bền", "trong_so": 70, "vi_du": "Canh lâm cung Chấn = Thang máy hay bị rung lắc"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Máy móc thiết bị cao cấp, sự vận hành lên xuống", "cach_xem": "Càn sinh Thể = Thang máy chạy êm và tốt", "trong_so": 60, "vi_du": "Càn khắc Thể (Mộc) = Coi chừng sự cố thang máy"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu + Tử Tôn", "giai_thich": "Phụ Mẫu = Thiết bị gắn vào nhà. Tử Tôn = Sự an toàn", "cach_xem": "Tử Tôn vượng = Thang máy vận hành an toàn tuyệt đối", "trong_so": 65, "vi_du": "Phụ Mẫu động = Thang máy đang được bảo trì/sửa chữa"}
    },
    "Tổ Chức Tiệc Cưới": {
        "muc_tieu": "Xem đám cưới có diễn ra suôn sẻ, vui vẻ không",
        "ky_mon": {"dung_than": "Lục Hợp + Cảnh Môn + Ất/Canh", "giai_thich": "Lục Hợp = Hôn lễ. Cảnh Môn = Sự náo nhiệt. Ất/Canh = Vợ chồng", "cach_xem": "Lục Hợp sinh Can Ngày = Đám cưới đại cát", "trong_so": 80, "vi_du": "Cảnh Môn vượng = Tiệc cưới rất sang trọng và đông khách"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Niềm vui, sự chúc tụng, hội hè tiệc tùng", "cach_xem": "Đoài sinh Thể = Đám cưới viên mãn", "trong_so": 65, "vi_du": "Đoài vượng sinh hợp = Khách mời đều hoan hỉ"},
        "luc_hao": {"dung_than": "Hào Thế + Ứng tương hợp", "giai_thich": "Thế Ứng hợp nhau tượng cho hôn lễ thành công", "cach_xem": "Thế Ứng vượng lâm Thanh Long = Đám cưới cực kỳ linh đình", "trong_so": 75, "vi_du": "Hào Tài Tử đều vượng = Đám cưới có nhiều quà cáp mừng"}
    },
    "Mua Sắm Nội Thất": {
        "muc_tieu": "Xem mua đồ nội thất có bền và hợp phong thủy không",
        "ky_mon": {"dung_than": "Sinh Môn + Cảnh Môn + Can Giờ", "giai_thich": "Sinh Môn = Nhà. Cảnh Môn = Đồ nội thất trang trí", "cach_xem": "Cảnh Môn sinh Sinh Môn = Đồ nội thất rất hợp với nhà", "trong_so": 70, "vi_du": "Cảnh Môn vượng = Đồ nội thất thuộc hàng cao cấp"},
        "mai_hoa": {"dung_than": "Quẻ Tốn - MỘC", "giai_thich": "Tốn = Đồ gỗ, sự sắp đặt khéo léo, thẩm mỹ nội thất", "cach_xem": "Tốn sinh Thể = Mua được đồ gỗ rất ưng ý", "trong_so": 60, "vi_du": "Tốn vượng tháng Xuân = Chất lượng gỗ rất tốt"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu tượng cho đồ dùng trong nhà", "cach_xem": "Phụ Mẫu vượng sinh Thế = Mua được món đồ bền đẹp", "trong_so": 65, "vi_du": "Phụ Mẫu lâm Thanh Long = Món đồ có giá trị thẩm mỹ cao"}
    },
    "Dự Đoán Kết Quả Xổ Số": {
        "muc_tieu": "Xem có lộc về tiền bạc bất ngờ không",
        "ky_mon": {"dung_than": "Mậu + Thiên Bồng + Thê Tài", "giai_thich": "Mậu = Tiền mặt. Thiên Bồng = May rủi. Thê Tài = Tài lộc", "cach_xem": "Thê Tài sinh Can Ngày = Có lộc trúng thưởng", "trong_so": 90, "vi_du": "Thiên Bồng lâm cung 8 = Có lộc nhỏ bất ngờ"},
        "mai_hoa": {"dung_than": "Quẻ Đoài - KIM", "giai_thich": "Đoài = Vàng bạc, tiền tài mang tính may rủi, niềm vui bất ngờ", "cach_xem": "Đoài sinh Thể = Có tin mừng về tiền bạc xổ số", "trong_so": 70, "vi_du": "Đoài vượng tháng Thu = Dễ trúng thưởng lúc này"},
        "luc_hao": {"dung_than": "Hào Thê Tài vượng động", "giai_thich": "Thê Tài là tiền lộc trời cho", "cach_xem": "Tài vượng sinh Thế = Được nhận khoản tiền lớn bất ngờ", "trong_so": 80, "vi_du": "Tài lâm Thanh Long động = Trúng số hoặc được biếu tiền"}
    },
    "Tìm Chỗ Đỗ Xe": {
        "muc_tieu": "Xem đến nơi có dễ tìm chỗ đậu xe không",
        "ky_mon": {"dung_than": "Khai Môn + Cung 2/5/8", "giai_thich": "Khai Môn = Cửa mở. Cung Thổ = Bãi đất/Bãi đỗ", "cach_xem": "Khai Môn lâm cung Thổ vượng = Rất dễ tìm chỗ đỗ", "trong_so": 60, "vi_du": "Khai Môn lâm Không = Hết chỗ đỗ xe"},
        "mai_hoa": {"dung_than": "Quẻ Cấn - THỔ", "giai_thich": "Cấn = Nơi dừng lại, bãi đất trống, bãi đỗ xe", "cach_xem": "Cấn sinh Thể = Tìm được chỗ đỗ xe lý tưởng", "trong_so": 55, "vi_du": "Cấn vượng = Bãi đỗ xe rất rộng rãi"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu tĩnh", "giai_thich": "Phụ Mẫu là nơi trú ngụ của xe", "cach_xem": "Phụ Mẫu vượng tĩnh = Có sẵn chỗ đỗ an toàn", "trong_so": 60, "vi_du": "Ứng sinh Thế = Được người khác nhường chỗ đỗ xe"}
    },
    "Kiểm Tra An Ninh": {
        "muc_tieu": "Xem hệ thống an ninh nhà xưởng có ổn không",
        "ky_mon": {"dung_than": "Trực Phù + Cảnh Môn + Huyền Vũ", "giai_thich": "Trực Phù = Bảo vệ. Cảnh Môn = Hệ thống Camera", "cach_xem": "Trực Phù vượng khắc Huyền Vũ = An ninh rất nghiêm ngặt", "trong_so": 75, "vi_du": "Huyền Vũ lâm cung Canh = Đề phòng trộm cắp đột nhập"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Sự giám sát, kỷ luật, hệ thống bảo vệ cấp cao", "cach_xem": "Càn sinh Thể = Hệ thống an ninh hoạt động tốt", "trong_so": 65, "vi_du": "Khảm (Dụng) khắc Ly (Thể) = An ninh lỏng lẻo dễ bị đột nhập"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ vượng", "giai_thich": "Quan Quỷ tượng cho người canh gác, bảo vệ", "cach_xem": "Quan vượng sinh Thế = Được bảo vệ an toàn tuyệt đối", "trong_so": 70, "vi_du": "Hào 1 lâm Câu Trần = Tường rào cổng ngõ rất kiên cố"}
    },
    "Sửa Chữa Điện Nước": {
        "muc_tieu": "Xem gọi thợ sửa điện nước có nhanh và triệt để không",
        "ky_mon": {"dung_than": "Thiên Nhuế + Khai Môn + Ất", "giai_thich": "Thiên Nhuế = Chỗ hỏng. Khai Môn = Thợ sửa. Ất = Dây điện/Ống nước", "cach_xem": "Khai Môn sinh Can Ngày = Gọi thợ đến ngay", "trong_so": 70, "vi_du": "Thiên Nhuế lâm cung Khảm = Hỏng đường ống nước"},
        "mai_hoa": {"dung_than": "Quẻ Khảm/Ly", "giai_thich": "Khảm = Nước, Ly = Điện", "cach_xem": "Dụng sinh Thể = Sửa chữa xong nhanh chóng", "trong_so": 60, "vi_du": "Khảm Ly giao nhau = Đang sửa cả điện lẫn nước"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn là thợ sửa chữa, người giải quyết sự cố", "cach_xem": "Tử Tôn vượng sinh Thế = Thợ giỏi sửa rất ưng ý", "trong_so": 65, "vi_du": "Quan Quỷ lâm hào động = Sự cố đang nổ ra cần sửa gấp"}
    },
    "Bệnh Mãn Tính": {
        "muc_tieu": "Xem bệnh mãn tính có ổn định hoặc thuyên giảm không",
        "ky_mon": {"dung_than": "Thiên Nhuế + Cửu Địa + can Ngày", "giai_thich": "Thiên Nhuế = Bệnh. Cửu Địa = Trì trệ, lâu dài", "cach_xem": "Cửu Địa sinh Can Ngày = Bệnh ổn định, sống chung an bình", "trong_so": 80, "vi_du": "Thiên Nhuế lâm Cửu Địa = Bệnh kéo dài nhưng không biến chứng đột ngột"},
        "mai_hoa": {"dung_than": "Quẻ Cấn - THỔ", "giai_thich": "Cấn = Ngưng nghỉ, tĩnh lặng, trì trệ", "cach_xem": "Cấn vượng = Bệnh duy trì trạng thái cũ, không tiến triển xấu", "trong_so": 65, "vi_du": "Cấn sinh Thể = Cơ thể thích nghi tốt với bệnh"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ tĩnh vượng", "giai_thich": "Quan Quỷ tĩnh mang tính ổn định, không bộc phát", "cach_xem": "Quan Quỷ tĩnh vượng sinh Thế = Bệnh không đáng ngại dù lâu khỏi", "trong_so": 70, "vi_du": "Hào Quan lâm Cửu Địa = Bệnh kinh niên nhưng ổn định"}
    },
    "Di Chứng Sau Bệnh": {
        "muc_tieu": "Xem sau khi khỏi bệnh có để lại di chứng gì không",
        "ky_mon": {"dung_than": "Thiên Nhuế + Tử Môn + Can Ngày", "giai_thich": "Thiên Nhuế = Gốc bệnh. Tử Môn = Chú chết, di chứng", "cach_xem": "Tử Môn khắc Can Ngày = Di chứng ảnh hưởng lâu dài", "trong_so": 75, "vi_du": "Tử Môn lâm Không = Không để lại di chứng gì"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Sự hiểm sâu, dư âm của bệnh tật", "cach_xem": "Khảm sinh Thể = Di chứng nhẹ, phục hồi dần", "trong_so": 60, "vi_du": "Dụng (Khảm) khắc Thể = Di chứng làm suy giảm sức khỏe"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ động hóa Thoái", "giai_thich": "Động là có biến, Thoái là lui đi", "cach_xem": "Quan động hóa Thoái = Di chứng sẽ tự hết theo thời gian", "trong_so": 65, "vi_du": "Quan động hóa Tiến = Di chứng ngày càng nặng"}
    },
    "Sức Khỏe Người Già": {
        "muc_tieu": "Xem sức khỏe cho cha mẹ, ông bà cao tuổi",
        "ky_mon": {"dung_than": "Can Năm + Thiên Nhuế + Cửu Địa", "giai_thich": "Can Năm = Người già. Thiên Nhuế = Bệnh. Cửu Địa = Thọ", "cach_xem": "Can Năm vượng địa = Sức khỏe bô lão vẫn rất tốt", "trong_so": 80, "vi_du": "Cửu Địa sinh Can Năm = Sống thọ, sức khỏe ổn định"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Người già, sự cứng cáp, khí lực", "cach_xem": "Càn vượng = Các cụ còn rất khỏe mạnh", "trong_so": 65, "vi_du": "Càn bị khắc = Sức khỏe người già đang suy giảm"},
        "luc_hao": {"dung_than": "Hào Phụ Mẫu", "giai_thich": "Phụ Mẫu tượng cho bậc trưởng thượng", "cach_xem": "Phụ Mẫu vượng tĩnh = Người già bình an vô sự", "trong_so": 70, "vi_du": "Hào Phụ Mẫu lâm Nhật Nguyệt = Sức khỏe cực kỳ vượng"}
    },
    "Ma quỷ": {
        "muc_tieu": "Xem có bị quấy phá bởi năng lượng âm hoặc thực thể vô hình không",
        "ky_mon": {"dung_than": "Đằng Xà + Huyền Vũ + Tử Môn", "giai_thich": "Đằng Xà = Quái dị. Huyền Vũ = Ám muội. Tử Môn = Âm khí", "cach_xem": "Hung thần lâm cung mệnh là có điềm lạ", "trong_so": 80, "vi_du": "Đằng Xà vượng = Có sự quấy phá tâm linh"},
        "mai_hoa": {"dung_than": "Quẻ Khảm - THỦY", "giai_thich": "Khảm = Hiểm trở, bóng tối, âm u", "cach_xem": "Khảm vượng khắc Thể = Bị âm khí xâm lấn", "trong_so": 60, "vi_du": "Khảm khắc Thể = Có điềm xấu về năng lượng"},
        "luc_hao": {"dung_than": "Hào Quan Quỷ", "giai_thich": "Quan Quỷ = Thực thể vô hình, ma quỷ", "cach_xem": "Quan Quỷ vượng động = Có sự tác động từ cõi âm", "trong_so": 70, "vi_du": "Quan Quỷ động mang Đằng Xà = Ma quỷ quấy nhiễu"}
    },
    "Thần thánh": {
        "muc_tieu": "Xem có được thần linh, gia tiên phù hộ hay không",
        "ky_mon": {"dung_than": "Trực Phù + Cửu Thiên + Thái Âm", "giai_thich": "Trực Phù = Thần tối cao. Cửu Thiên = Thần linh. Thái Âm = Quý nhân âm", "cach_xem": "Cát thần sinh Can Ngày = Được phù hộ", "trong_so": 80, "vi_du": "Trực Phù sinh Can Ngày = Được đại cát đại lợi"},
        "mai_hoa": {"dung_than": "Quẻ Càn - KIM", "giai_thich": "Càn = Trời, thần thánh, năng lượng cao", "cach_xem": "Càn sinh Thể = Được ơn trên che chở", "trong_so": 60, "vi_du": "Càn sinh Thể = Vạn sự hanh thông nhờ ơn trên"},
        "luc_hao": {"dung_than": "Hào Tử Tôn", "giai_thich": "Tử Tôn = Phúc thần, giải tai ương, thần linh", "cach_xem": "Tử Tôn vượng = Được thần linh giúp đỡ", "trong_so": 70, "vi_du": "Tử Tôn lâm Nhật Nguyệt = Phúc đức dồi dào, gia tiên độ trì"}
    },
}

# Hàm wrapper để sử dụng database mới
def lay_dung_than_200(chu_de):
    """Lấy thông tin Dụng Thần từ database 200 chủ đề"""
    return DUNG_THAN_200_CHU_DE.get(chu_de, None)

def hien_thi_dung_than_200(chu_de):
    """Hiển thị thông tin Dụng Thần chi tiết từ database 200 chủ đề"""
    dt_info = DUNG_THAN_200_CHU_DE.get(chu_de)
    
    if not dt_info:
        return f"""
═══════════════════════════════════════════════════════════════════════════
⚠️ CHƯA CÓ THÔNG TIN DỤNG THẦN CHO CHỦ ĐỀ: {chu_de.upper()}
═══════════════════════════════════════════════════════════════════════════

Chủ đề này chưa được bổ sung vào database 200 chủ đề.
Hiện có {len(DUNG_THAN_200_CHU_DE)} chủ đề đã hoàn thiện.
Vui lòng chọn một trong các chủ đề sau:

{chr(10).join([f"  {i}. {cd}" for i, cd in enumerate(sorted(DUNG_THAN_200_CHU_DE.keys()), 1)])}
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
    
    return "\n".join(result)

if __name__ == "__main__":
    print(f"Database có {len(DUNG_THAN_200_CHU_DE)} chủ đề")
    print("\nDanh sách các chủ đề:")
    for i, chu_de in enumerate(sorted(DUNG_THAN_200_CHU_DE.keys()), 1):
        print(f"{i}. {chu_de}")
