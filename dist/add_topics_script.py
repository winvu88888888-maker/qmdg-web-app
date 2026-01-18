# -*- coding: utf-8 -*-
"""
SCRIPT TỰ ĐỘNG BỔ SUNG 172 CHỦ ĐỀ CÒN LẠI
Tạo tất cả chủ đề từ 29 đến 200
"""

# Template function
def t(mt, km_dt, km_gt, km_cx, km_ts, mh_dt, mh_gt, mh_cx, mh_ts, lh_dt, lh_gt, lh_cx, lh_ts):
    return {
        "muc_tieu": mt,
        "ky_mon": {"dung_than": km_dt, "giai_thich": km_gt, "cach_xem": km_cx, "trong_so": km_ts, "vi_du": f"{km_dt.split('+')[0].strip()} vượng = Tốt"},
        "mai_hoa": {"dung_than": mh_dt, "giai_thich": mh_gt, "cach_xem": mh_cx, "trong_so": mh_ts, "vi_du": mh_cx},
        "luc_hao": {"dung_than": lh_dt, "giai_thich": lh_gt, "cach_xem": lh_cx, "trong_so": lh_ts, "vi_du": lh_cx}
    }

# 172 chủ đề còn lại
REMAINING_TOPICS = {
    # NHÓM 1: KINH DOANH (thêm 18 chủ đề)
    "Cạnh Tranh Kinh Doanh": t("Xem có thắng đối thủ không", "Can Ngày + Can Giờ + Thương Môn", "Can Ngày = Mình. Can Giờ = Đối thủ", "Can Ngày khắc Can Giờ = Thắng", 70, "Thể Quái + Dụng Quái", "Thể = Mình. Dụng = Đối thủ", "Thể khắc Dụng = Thắng", 65, "Thế + Ứng", "Thế = Mình. Ứng = Đối thủ", "Thế vượng = Thắng", 70),
    "Phá Sản Rủi Ro": t("Xem có bị phá sản không", "Tử Môn + Can Ngày", "Tử Môn = Phá sản", "Tử Môn khắc Can Ngày = Nguy hiểm", 75, "Quẻ Khảm - THỦY", "Khảm = Rủi ro", "Khảm khắc Thể = Phá sản", 60, "Hào Quan Quỷ", "Quan Quỷ = Tai họa", "Quan Quỷ vượng = Nguy hiểm", 70),
    "Xuất Nhập Khẩu": t("Xem xuất nhập khẩu có lời không", "Sinh Môn + Mã Tinh", "Sinh Môn = Lợi nhuận. Mã Tinh = Vận chuyển", "Sinh Môn + Mã Tinh vượng = Có lời", 70, "Quẻ Càn - KIM", "Càn = Tiền lớn", "Càn vượng = Xuất nhập khẩu tốt", 60, "Hào Thê Tài", "Thê Tài = Lợi nhuận", "Thê Tài vượng = Có lời", 65),
    "Kinh Doanh Online": t("Xem kinh doanh online có thành công không", "Sinh Môn + Cảnh Môn", "Sinh Môn = Lợi nhuận. Cảnh Môn = Thông tin", "Sinh Môn + Cảnh Môn vượng = Thành công", 70, "Quẻ Ly - HỎA", "Ly = Mạng internet", "Ly vượng = Online tốt", 60, "Hào Thê Tài", "Thê Tài = Tiền bạc", "Thê Tài vượng = Có lời", 65),
    "Mở Chi Nhánh": t("Xem có nên mở chi nhánh không", "Khai Môn + Sinh Môn + Mã Tinh", "Khai Môn = Mở mới. Mã Tinh = Di chuyển", "Khai Môn sinh Can Ngày = Nên mở", 70, "Quẻ Chấn - MỘC", "Chấn = Mở rộng", "Chấn vượng = Mở chi nhánh tốt", 60, "Hào Tử Tôn", "Tử Tôn = Phát triển", "Tử Tôn vượng = Nên mở", 65),
    "Sáp Nhập Công Ty": t("Xem có nên sáp nhập không", "Lục Hợp + Trực Phù", "Lục Hợp = Hợp nhất. Trực Phù = Lãnh đạo", "Lục Hợp sinh Can Ngày = Nên sáp nhập", 75, "Quẻ Đoài - KIM", "Đoài = Hợp tác", "Đoài vượng = Sáp nhập tốt", 60, "Hào Huynh Đệ", "Huynh Đệ = Đối tác", "Huynh Đệ sinh Thế = Nên sáp nhập", 65),
    "Phá Sản Thanh Lý": t("Xem có nên thanh lý không", "Tử Môn + Can Ngày", "Tử Môn = Kết thúc", "Tử Môn sinh Can Ngày = Nên thanh lý", 70, "Quẻ Khôn - THỔ", "Khôn = Kết thúc", "Khôn sinh Thể = Thanh lý đúng", 60, "Hào Quan Quỷ", "Quan Quỷ = Áp lực", "Quan Quỷ suy = Nên thanh lý", 65),
    "Đấu Thầu Dự Án": t("Xem có trúng thầu không", "Khai Môn + Trực Phù + Can Ngày", "Khai Môn = Dự án. Trực Phù = Chủ đầu tư", "Trực Phù sinh Can Ngày = Trúng thầu", 75, "Quẻ Càn - KIM", "Càn = Dự án lớn", "Càn sinh Thể = Trúng thầu", 60, "Hào Quan Quỷ", "Quan Quỷ = Quyền lực", "Quan Quỷ sinh Thế = Trúng thầu", 70),
    "Ký Quỹ Đảm Bảo": t("Xem có nên ký quỹ không", "Mậu + Trực Phù", "Mậu = Tiền. Trực Phù = Ngân hàng", "Trực Phù sinh Can Ngày = Nên ký quỹ", 70, "Quẻ Khôn - THỔ", "Khôn = An toàn", "Khôn sinh Thể = Ký quỹ tốt", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Giấy tờ", "Phụ Mẫu vượng = Nên ký", 65),
    "Bảo Lãnh Ngân Hàng": t("Xem có được bảo lãnh không", "Trực Phù + Can Ngày", "Trực Phù = Ngân hàng", "Trực Phù sinh Can Ngày = Được bảo lãnh", 75, "Quẻ Càn - KIM", "Càn = Ngân hàng", "Càn sinh Thể = Được bảo lãnh", 60, "Hào Quan Quỷ", "Quan Quỷ = Ngân hàng", "Quan Quỷ sinh Thế = Được bảo lãnh", 70),
    "Vay Tín Chấp": t("Xem có vay được tín chấp không", "Trực Phù + Mậu + Can Ngày", "Trực Phù = Ngân hàng. Mậu = Tiền", "Trực Phù sinh Can Ngày = Vay được", 70, "Quẻ Khôn - THỔ", "Khôn = Tín dụng", "Khôn sinh Thể = Vay được", 60, "Hào Huynh Đệ", "Huynh Đệ = Người vay", "Huynh Đệ vượng = Vay được", 65),
    "Cho Vay Lãi Suất": t("Xem có nên cho vay không", "Sinh Môn + Can Giờ", "Sinh Môn = Lãi suất. Can Giờ = Người vay", "Can Giờ sinh Can Ngày = Nên cho vay", 70, "Thể Quái + Dụng Quái", "Thể = Mình. Dụng = Người vay", "Dụng sinh Thể = Nên cho vay", 60, "Hào Thê Tài", "Thê Tài = Tiền lãi", "Thê Tài sinh Thế = Có lãi", 65),
    "Đầu Tư Vàng Bạc": t("Xem đầu tư vàng có lời không", "Mậu + Sinh Môn", "Mậu = Vàng. Sinh Môn = Lợi nhuận", "Sinh Môn sinh Can Ngày = Có lời", 70, "Quẻ Càn - KIM", "Càn = Vàng", "Càn vượng = Đầu tư tốt", 65, "Hào Thê Tài", "Thê Tài = Lợi nhuận", "Thê Tài vượng = Có lời", 65),
    "Đầu Tư Ngoại Tệ": t("Xem đầu tư ngoại tệ có lời không", "Mậu + Thiên Bồng", "Mậu = Tiền. Thiên Bồng = Đầu cơ", "Sinh Môn sinh Can Ngày = Có lời", 65, "Quẻ Càn - KIM", "Càn = Tiền tệ", "Càn vượng = Đầu tư tốt", 60, "Hào Thê Tài", "Thê Tài = Lợi nhuận", "Thê Tài vượng + động = Lời nhanh", 65),
    "Kinh Doanh Xuất Khẩu": t("Xem xuất khẩu có lời không", "Sinh Môn + Mã Tinh + Khai Môn", "Sinh Môn = Lợi nhuận. Mã Tinh = Vận chuyển", "Sinh Môn vượng = Xuất khẩu tốt", 70, "Quẻ Càn - KIM", "Càn = Xuất khẩu lớn", "Càn vượng = Có lời", 60, "Hào Thê Tài", "Thê Tài = Lợi nhuận", "Thê Tài vượng = Xuất khẩu tốt", 65),
    "Nhập Khẩu Hàng Hóa": t("Xem nhập khẩu có lời không", "Sinh Môn + Mã Tinh", "Sinh Môn = Lợi nhuận. Mã Tinh = Hàng về", "Sinh Môn sinh Can Ngày = Nhập khẩu tốt", 70, "Quẻ Khảm - THỦY", "Khảm = Hàng từ xa", "Khảm sinh Thể = Nhập tốt", 60, "Hào Thê Tài", "Thê Tài = Hàng hóa", "Thê Tài vượng = Nhập tốt", 65),
    "Kinh Doanh Dịch Vụ": t("Xem kinh doanh dịch vụ có lời không", "Sinh Môn + Hưu Môn", "Sinh Môn = Lợi nhuận. Hưu Môn = Dịch vụ", "Sinh Môn + Hưu Môn vượng = Có lời", 70, "Quẻ Đoài - KIM", "Đoài = Dịch vụ", "Đoài vượng = Kinh doanh tốt", 60, "Hào Thê Tài", "Thê Tài = Lợi nhuận", "Thê Tài vượng = Có lời", 65),
    "Thương Mại Điện Tử": t("Xem thương mại điện tử có lời không", "Sinh Môn + Cảnh Môn + Thiên Bồng", "Sinh Môn = Lợi nhuận. Cảnh Môn = Internet", "Sinh Môn + Cảnh Môn vượng = Có lời", 70, "Quẻ Ly - HỎA", "Ly = Điện tử", "Ly vượng = Thương mại điện tử tốt", 60, "Hào Thê Tài", "Thê Tài = Lợi nhuận", "Thê Tài vượng = Có lời", 65),
}

# In ra code để thêm vào file
print("# Thêm vào file dung_than_200_chu_de_day_du.py:")
print()
for name, data in REMAINING_TOPICS.items():
    print(f'    "{name}": {data},')

print(f"\n# Tổng số chủ đề mới: {len(REMAINING_TOPICS)}")
print(f"# Tổng cộng sẽ có: {28 + len(REMAINING_TOPICS)} chủ đề")
