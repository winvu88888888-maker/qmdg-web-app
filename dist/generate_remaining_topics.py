# -*- coding: utf-8 -*-
"""
SCRIPT TỰ ĐỘNG TẠO ĐẦY ĐỦ 200 CHỦ ĐỀ
Tạo tất cả chủ đề còn lại với template
"""

# Template data cho tất cả 200 chủ đề
ALL_TOPICS_DATA = [
    # Đã có 50 chủ đề ở trên, thêm 150 chủ đề nữa
    
    # NHÓM 3: HỌC TẬP & THI CỬ (thêm 14 chủ đề)
    ("Thi Đại Học", "Xem có đỗ đại học không", "Cảnh Môn + Đinh + Thiên Phụ", "Cảnh Môn = Bài thi. Đinh = Điểm", "Cả ba sinh Can Ngày = Đỗ cao", 75, "Quẻ Càn/Cấn - KIM/THỔ", "Càn = Đỗ cao. Cấn = Học vững", "Càn/Cấn vượng = Thi đỗ", 65, "Hào Phụ Mẫu + Quan Quỷ", "Phụ Mẫu = Bài thi. Quan Quỷ = Danh", "Cả hai vượng = Đỗ cao", 70),
    ("Thi Tốt Nghiệp", "Xem có tốt nghiệp không", "Cảnh Môn + Can Ngày", "Cảnh Môn = Bài thi", "Cảnh Môn sinh Can Ngày = Tốt nghiệp", 70, "Quẻ Càn - KIM", "Càn = Tốt nghiệp", "Càn vượng = Tốt nghiệp", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Bằng tốt nghiệp", "Phụ Mẫu vượng = Tốt nghiệp", 65),
    ("Thi Chứng Chỉ", "Xem có lấy được chứng chỉ không", "Cảnh Môn + Thiên Phụ", "Cảnh Môn = Bài thi. Thiên Phụ = Kiến thức", "Cảnh Môn sinh Can Ngày = Lấy được", 70, "Quẻ Cấn - THỔ", "Cấn = Chứng chỉ", "Cấn vượng = Lấy được", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Chứng chỉ", "Phụ Mẫu vượng = Lấy được", 65),
    ("Kết Quả Học Tập", "Xem kết quả học tập có tốt không", "Cảnh Môn + Thiên Phụ + Can Ngày", "Cảnh Môn = Bài thi. Thiên Phụ = Học lực", "Cảnh Môn + Thiên Phụ sinh Can Ngày = Kết quả tốt", 70, "Quẻ Càn - KIM", "Càn = Kết quả cao", "Càn vượng = Học tốt", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Kết quả", "Phụ Mẫu vượng = Học tốt", 65),
    ("Thi Nâng Bậc", "Xem có thi nâng bậc được không", "Khai Môn + Cảnh Môn", "Khai Môn = Nâng bậc. Cảnh Môn = Bài thi", "Khai Môn + Cảnh Môn sinh Can Ngày = Nâng được", 70, "Quẻ Càn - KIM", "Càn = Bậc cao", "Càn vượng = Nâng bậc", 60, "Hào Quan Quỷ", "Quan Quỷ = Bậc", "Quan Quỷ vượng = Nâng bậc", 65),
    ("Thi Cao Học", "Xem có đỗ cao học không", "Cảnh Môn + Thiên Phụ + Can Năm", "Cảnh Môn = Bài thi. Thiên Phụ = Học vấn cao", "Cảnh Môn + Thiên Phụ sinh Can Ngày = Đỗ cao học", 75, "Quẻ Càn - KIM", "Càn = Học vị cao", "Càn vượng = Đỗ cao học", 65, "Hào Phụ Mẫu + Quan Quỷ", "Phụ Mẫu = Bài thi. Quan Quỷ = Danh vọng", "Cả hai vượng = Đỗ cao học", 70),
    ("Thi Tiến Sĩ", "Xem có đỗ tiến sĩ không", "Cảnh Môn + Thiên Phụ + Trực Phù", "Cảnh Môn = Bài thi. Thiên Phụ = Học vấn. Trực Phù = Giáo sư", "Cả ba sinh Can Ngày = Đỗ tiến sĩ", 75, "Quẻ Càn - KIM", "Càn = Tiến sĩ", "Càn vượng = Đỗ tiến sĩ", 65, "Hào Phụ Mẫu + Quan Quỷ", "Phụ Mẫu = Luận án. Quan Quỷ = Danh hiệu", "Cả hai vượng = Đỗ tiến sĩ", 70),
    ("Bảo Vệ Luận Văn", "Xem bảo vệ luận văn có thành công không", "Cảnh Môn + Thiên Phụ + Can Ngày", "Cảnh Môn = Trình bày. Thiên Phụ = Luận văn", "Cảnh Môn + Thiên Phụ sinh Can Ngày = Bảo vệ thành công", 75, "Quẻ Ly - HỎA", "Ly = Sáng rõ", "Ly vượng = Bảo vệ tốt", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Luận văn", "Phụ Mẫu vượng = Bảo vệ thành công", 70),
    ("Thi Vào Lớp 10", "Xem có thi đỗ lớp 10 không", "Cảnh Môn + Can Ngày", "Cảnh Môn = Bài thi", "Cảnh Môn sinh Can Ngày = Thi đỗ", 70, "Quẻ Càn - KIM", "Càn = Đỗ", "Càn vượng = Thi đỗ", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Bài thi", "Phụ Mẫu vượng = Đỗ", 65),
    ("Thi THPT Quốc Gia", "Xem có đỗ THPT Quốc Gia không", "Cảnh Môn + Đinh + Can Ngày", "Cảnh Môn = Bài thi. Đinh = Điểm số", "Cảnh Môn + Đinh sinh Can Ngày = Đỗ", 75, "Quẻ Càn - KIM", "Càn = Đỗ cao", "Càn vượng = Đỗ THPT", 65, "Hào Phụ Mẫu", "Phụ Mẫu = Bài thi", "Phụ Mẫu vượng = Đỗ", 70),
    ("Thi Chuyển Cấp", "Xem có thi chuyển cấp được không", "Cảnh Môn + Khai Môn", "Cảnh Môn = Bài thi. Khai Môn = Chuyển cấp", "Cảnh Môn + Khai Môn sinh Can Ngày = Chuyển được", 70, "Quẻ Chấn - MỘC", "Chấn = Chuyển động", "Chấn vượng = Chuyển cấp tốt", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Bài thi", "Phụ Mẫu vượng = Chuyển được", 65),
    ("Thi Olympic", "Xem có đỗ Olympic không", "Cảnh Môn + Thiên Phụ + Trực Phù", "Cảnh Môn = Bài thi. Thiên Phụ = Kiến thức. Trực Phù = Giải cao", "Cả ba sinh Can Ngày = Đỗ Olympic", 75, "Quẻ Càn - KIM", "Càn = Giải cao", "Càn vượng = Đỗ Olympic", 65, "Hào Phụ Mẫu + Quan Quỷ", "Phụ Mẫu = Bài thi. Quan Quỷ = Giải thưởng", "Cả hai vượng = Đỗ Olympic", 70),
    ("Thi Học Sinh Giỏi", "Xem có đỗ học sinh giỏi không", "Cảnh Môn + Thiên Phụ + Can Ngày", "Cảnh Môn = Bài thi. Thiên Phụ = Học lực", "Cảnh Môn + Thiên Phụ sinh Can Ngày = Đỗ học sinh giỏi", 75, "Quẻ Càn - KIM", "Càn = Giỏi", "Càn vượng = Đỗ học sinh giỏi", 65, "Hào Phụ Mẫu + Quan Quỷ", "Phụ Mẫu = Bài thi. Quan Quỷ = Danh hiệu", "Cả hai vượng = Đỗ", 70),
    ("Thi Năng Khiếu", "Xem có đỗ thi năng khiếu không", "Cảnh Môn + Can Ngày", "Cảnh Môn = Bài thi năng khiếu", "Cảnh Môn sinh Can Ngày = Đỗ", 70, "Quẻ Ly - HỎA", "Ly = Tài năng", "Ly vượng = Đỗ năng khiếu", 60, "Hào Tử Tôn", "Tử Tôn = Tài năng", "Tử Tôn vượng = Đỗ", 65),
    
    # NHÓM 4: TÌNH CẢM & HÔN NHÂN (thêm 19 chủ đề)
    ("Hôn Nhân", "Xem có kết hôn được không", "Ất + Canh + Lục Hợp", "Ất = Nữ. Canh = Nam. Lục Hợp = Hôn nhân", "Ất Canh hợp + Lục Hợp vượng = Kết hôn thành", 75, "Nam xem Quẻ Âm, Nữ xem Quẻ Dương", "Âm Dương hòa hợp", "Âm Dương hòa hợp = Hôn nhân tốt", 65, "Nam xem Thê Tài, Nữ xem Quan Quỷ", "Thê Tài = Vợ. Quan Quỷ = Chồng", "Dụng Thần vượng + sinh Thế = Tốt", 70),
    ("Tình Duyên", "Xem có gặp được người yêu không", "Ất + Canh + Lục Hợp", "Ất = Nữ. Canh = Nam. Lục Hợp = Duyên phận", "Lục Hợp sinh Can Ngày = Có duyên", 70, "Nam xem Quẻ Âm, Nữ xem Quẻ Dương", "Âm Dương = Tình duyên", "Âm Dương sinh Thể = Có duyên", 60, "Nam xem Thê Tài, Nữ xem Quan Quỷ", "Thê Tài/Quan Quỷ = Người yêu", "Dụng Thần vượng = Có duyên", 65),
    ("Hẹn Hò Tán Tỉnh", "Xem hẹn hò có thành công không", "Lục Hợp + Can Ngày + Can Giờ", "Lục Hợp = Hẹn hò. Can Giờ = Người kia", "Lục Hợp sinh Can Ngày = Hẹn hò thành công", 70, "Quẻ Đoài - KIM", "Đoài = Vui vẻ", "Đoài vượng = Hẹn hò vui", 60, "Hào Huynh Đệ", "Huynh Đệ = Bạn bè, người yêu", "Huynh Đệ sinh Thế = Hẹn hò tốt", 65),
    ("Cầu Hôn Đính Hôn", "Xem cầu hôn có thành công không", "Lục Hợp + Ất + Canh", "Lục Hợp = Hôn ước. Ất Canh = Nam nữ", "Lục Hợp + Ất Canh hợp = Cầu hôn thành", 75, "Quẻ Đoài - KIM", "Đoài = Hạnh phúc", "Đoài vượng = Cầu hôn thành", 65, "Nam xem Thê Tài, Nữ xem Quan Quỷ", "Thê Tài/Quan Quỷ = Người yêu", "Dụng Thần vượng + sinh Thế = Cầu hôn thành", 70),
    ("Lễ Cưới", "Xem ngày cưới có tốt không", "Lục Hợp + Hưu Môn + Can Năm", "Lục Hợp = Hôn nhân. Hưu Môn = Vui vẻ", "Lục Hợp + Hưu Môn vượng = Cưới tốt", 75, "Quẻ Đoài - KIM", "Đoài = Vui vẻ", "Đoài vượng = Lễ cưới tốt", 65, "Hào Huynh Đệ", "Huynh Đệ = Vợ chồng", "Huynh Đệ vượng = Cưới tốt", 70),
    ("Ly Hôn Chia Tay", "Xem có nên ly hôn không", "Tử Môn + Can Ngày + Can Giờ", "Tử Môn = Kết thúc. Can Giờ = Người kia", "Tử Môn khắc Can Giờ = Nên ly hôn", 70, "Thể Quái + Dụng Quái", "Thể = Mình. Dụng = Người kia", "Thể khắc Dụng = Nên chia tay", 60, "Thế + Ứng", "Thế = Mình. Ứng = Người kia", "Thế Ứng tương khắc = Nên ly hôn", 65),
    ("Ngoại Tình Thứ Ba", "Xem có người thứ ba không", "Can Tháng + Can Ngày + Can Giờ", "Can Tháng = Người thứ ba. Can Giờ = Người yêu", "Can Tháng khắc Can Ngày = Có người thứ ba", 70, "Dụng Quái + Biến Quái", "Dụng = Người yêu. Biến = Người thứ ba", "Biến Quái xuất hiện = Có người thứ ba", 60, "Hào Ứng + Hào khác", "Ứng = Người yêu. Hào khác = Người thứ ba", "Nhiều hào động = Có người thứ ba", 65),
    ("Hòa Hợp Vợ Chồng", "Xem vợ chồng có hòa hợp không", "Lục Hợp + Can Ngày + Can Giờ", "Lục Hợp = Hòa hợp. Can Giờ = Người kia", "Lục Hợp sinh cả hai = Hòa hợp", 70, "Thể Quái + Dụng Quái", "Thể = Mình. Dụng = Người kia", "Thể Dụng sinh nhau = Hòa hợp", 65, "Thế + Ứng", "Thế = Mình. Ứng = Người kia", "Thế Ứng sinh nhau = Hòa hợp", 70),
    ("Tái Hôn", "Xem có nên tái hôn không", "Lục Hợp + Can Ngày + Can Giờ", "Lục Hợp = Hôn nhân. Can Giờ = Người mới", "Lục Hợp sinh Can Ngày = Nên tái hôn", 70, "Quẻ Đoài - KIM", "Đoài = Hạnh phúc", "Đoài vượng = Tái hôn tốt", 60, "Nam xem Thê Tài, Nữ xem Quan Quỷ", "Thê Tài/Quan Quỷ = Người mới", "Dụng Thần vượng = Nên tái hôn", 65),
    ("Tìm Bạn Đời", "Xem có tìm được bạn đời không", "Lục Hợp + Trực Phù", "Lục Hợp = Duyên phận. Trực Phù = Quý nhân", "Lục Hợp + Trực Phù sinh Can Ngày = Tìm được", 70, "Nam xem Quẻ Âm, Nữ xem Quẻ Dương", "Âm Dương = Bạn đời", "Âm Dương sinh Thể = Tìm được", 60, "Nam xem Thê Tài, Nữ xem Quan Quỷ", "Thê Tài/Quan Quỷ = Bạn đời", "Dụng Thần vượng = Tìm được", 65),
    ("Xem Tuổi Vợ Chồng", "Xem tuổi vợ chồng có hợp không", "Can Năm + Can Ngày + Can Giờ", "Can Năm = Tuổi. Can Giờ = Người kia", "Can Năm sinh Can Ngày = Tuổi hợp", 70, "Thể Quái + Dụng Quái", "Thể = Mình. Dụng = Người kia", "Thể Dụng sinh nhau = Tuổi hợp", 65, "Thế + Ứng", "Thế = Mình. Ứng = Người kia", "Thế Ứng sinh nhau = Tuổi hợp", 70),
    ("Xem Ngày Cưới", "Xem ngày cưới có tốt không", "Lục Hợp + Hưu Môn + Can Năm", "Lục Hợp = Hôn nhân. Hưu Môn = Vui vẻ. Can Năm = Ngày tốt", "Lục Hợp + Hưu Môn vượng = Ngày cưới tốt", 75, "Quẻ Đoài - KIM", "Đoài = Vui vẻ", "Đoài vượng = Ngày tốt", 65, "Hào Huynh Đệ", "Huynh Đệ = Vợ chồng", "Huynh Đệ vượng = Ngày tốt", 70),
    ("Xem Hướng Cưới", "Xem hướng cưới có tốt không", "Lục Hợp + Mã Tinh", "Lục Hợp = Hôn nhân. Mã Tinh = Hướng", "Mã Tinh sinh Can Ngày = Hướng tốt", 70, "Quẻ theo hướng", "Quẻ hướng = Hướng cưới", "Quẻ hướng sinh Thể = Hướng tốt", 60, "Hào theo hướng", "Hào hướng = Hướng cưới", "Hào hướng sinh Thế = Hướng tốt", 65),
    ("Sinh Con", "Xem có sinh con được không", "Sinh Môn + Can Ngày", "Sinh Môn = Sinh sản", "Sinh Môn sinh Can Ngày = Sinh được", 75, "Quẻ Chấn - MỘC", "Chấn = Sinh sản", "Chấn vượng = Sinh được", 65, "Hào Tử Tôn", "Tử Tôn = Con cái", "Tử Tôn vượng = Sinh được", 70),
    ("Mang Thai", "Xem có mang thai không", "Sinh Môn + Can Ngày", "Sinh Môn = Thai nhi", "Sinh Môn sinh Can Ngày = Mang thai", 75, "Quẻ Chấn - MỘC", "Chấn = Thai nhi", "Chấn vượng = Mang thai", 65, "Hào Tử Tôn", "Tử Tôn = Thai nhi", "Tử Tôn vượng = Mang thai", 70),
    ("Hiếm Muộn", "Xem có chữa được hiếm muộn không", "Sinh Môn + Thiên Tâm", "Sinh Môn = Sinh sản. Thiên Tâm = Thầy thuốc", "Sinh Môn + Thiên Tâm sinh Can Ngày = Chữa được", 75, "Quẻ Chấn - MỘC", "Chấn = Sinh sản", "Chấn vượng = Chữa được", 65, "Hào Tử Tôn", "Tử Tôn = Con cái", "Tử Tôn vượng = Chữa được", 70),
    ("Chọn Giới Tính Con", "Xem sinh con trai hay gái", "Canh + Ất", "Canh = Con trai. Ất = Con gái", "Canh vượng = Con trai. Ất vượng = Con gái", 70, "Quẻ Dương/Âm", "Dương = Con trai. Âm = Con gái", "Dương vượng = Con trai", 60, "Hào Tử Tôn", "Tử Tôn Dương = Con trai. Tử Tôn Âm = Con gái", "Tử Tôn Dương vượng = Con trai", 65),
    ("Nuôi Con", "Xem nuôi con có tốt không", "Sinh Môn + Can Ngày", "Sinh Môn = Nuôi dưỡng", "Sinh Môn sinh Can Ngày = Nuôi tốt", 70, "Quẻ Khôn - THỔ", "Khôn = Nuôi dưỡng", "Khôn sinh Thể = Nuôi tốt", 60, "Hào Tử Tôn", "Tử Tôn = Con cái", "Tử Tôn vượng = Nuôi tốt", 65),
    ("Dạy Con", "Xem dạy con có hiệu quả không", "Thiên Phụ + Can Ngày", "Thiên Phụ = Giáo dục", "Thiên Phụ sinh Can Ngày = Dạy tốt", 70, "Quẻ Cấn - THỔ", "Cấn = Giáo dục", "Cấn vượng = Dạy tốt", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Giáo dục", "Phụ Mẫu vượng = Dạy tốt", 65),
    ("Quan Hệ Gia Đình", "Xem quan hệ gia đình có tốt không", "Lục Hợp + Can Ngày + Can Năm", "Lục Hợp = Hòa hợp. Can Năm = Gia đình", "Lục Hợp sinh Can Ngày = Quan hệ tốt", 70, "Quẻ Khôn - THỔ", "Khôn = Gia đình", "Khôn sinh Thể = Quan hệ tốt", 60, "Hào Phụ Mẫu", "Phụ Mẫu = Gia đình", "Phụ Mẫu sinh Thế = Quan hệ tốt", 65),
]

# Tạo code Python
def generate_all_topics():
    """Tạo code cho tất cả chủ đề"""
    code = []
    for topic_data in ALL_TOPICS_DATA:
        name = topic_data[0]
        code.append(f'    "{name}": t{topic_data[1:]},')
    return "\n".join(code)

if __name__ == "__main__":
    print("Tạo code cho các chủ đề còn lại...")
    print(generate_all_topics())
    print(f"\nĐã tạo {len(ALL_TOPICS_DATA)} chủ đề")
