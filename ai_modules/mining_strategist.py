import json
import random

class MiningStrategist:
    """The brain that decides what the 10 AI Miners should search for next."""
    
    def __init__(self):
        self.categories = {
            "Kỳ Môn Độn Giáp": [
                "Bát Môn chuyên sâu", "Cửu Tinh biến hóa", "Bát Thần trợ lực", 
                "Thần sát ẩn tàng", "Cấu trúc phản phục", "Ứng dụng trong kinh doanh",
                "Kỳ Môn và sức khỏe", "Pháp thuật Kỳ Môn cổ", "Thiên Cáp Thần"
            ],
            "Kinh Dịch Chuyên Sâu": [
                "64 Quẻ và biến hóa", "Lời hào bí ẩn", "Mai Hoa Dịch Số nâng cao", 
                "Lục Hào tiên đoán", "Dịch học và thuật toán AI", "Tế lễ và Kinh Dịch"
            ],
            "Lập Trình Python/AI": [
                "Agentic Frameworks", "LLM Fine-tuning", "Streamlit UI/UX", 
                "Python Performance", "AI Security", "RAG Systems"
            ],
            "Y Học Cổ Truyền": [
                "Châm cứu và huyệt đạo", "Dược liệu quý hiếm", "Âm dương ngũ hành trong tạng phủ",
                "Khí công dưỡng sinh", "Trị bệnh từ gốc"
            ],
            "Phong Thủy Địa Lý": [
                "Loan Đầu và Lý Khí", "Huyền Không Phi Tinh", "Bát Trạch Minh Cảnh",
                "Trấn trạch và hóa giải", "Long mạch toàn cầu"
            ],
            "Chiến Lược": [
                "Thập Nhị Binh Thư", "Tôn Tử Binh Pháp", "Quỷ Cốc Tử",
                "Chiến lược đàm phán", "Tâm lý học chiến tranh"
            ],
            "Công Nghệ AI Mới": [
                "Gemini 1.5/2.0 updates", "Multimodal AI", "Robotics AI",
                "Edge Computing", "AI Ethics"
            ]
        }

    def generate_research_queue(self, category=None, count=5):
        """Generates a list of deep-dive sub-topics."""
        if category and category in self.categories:
            base_topics = self.categories[category]
        else:
            # Pick a random category if none specified
            cat = random.choice(list(self.categories.keys()))
            base_topics = self.categories[cat]
            
        queue = []
        for _ in range(count):
            topic = random.choice(base_topics)
            # Add a recursive depth factor: specific angle
            angle = random.choice([
                "Mới nhất 2026", "Bí truyền cổ tịch", "Ứng dụng thực tế", 
                "Phân tích chuyên sâu", "So sánh đối chiếu", "Lỗi thường gặp"
            ])
            queue.append(f"{topic}: {angle}")
            
        return list(set(queue)) # Unique topics only

    def synthesize_mining_prompt(self, target_topic):
        """Creates a specialized system prompt for an AI agent to 'mine' this topic."""
        return f"""
Bạn là một Đặc phái viên AI thuộc 'Quân đoàn AI Khai thác 24/7'.
Nhiệm vụ của bạn: Khai thác toàn bộ thông tin TẬN CÙNG và TINH TÚY NHẤT về chủ đề: **{target_topic}**.

YÊU CẦU:
1. Đào sâu vào các chi tiết kỹ thuật, bí quyết hoặc dữ liệu hiếm.
2. Nếu là code: Phải cung cấp đoạn mã tối ưu và thực dụng.
3. Nếu là kiến thức cổ: Phải trích dẫn hoặc dịch nghĩa súc tích.
4. Cấu trúc bài nạp phải gồm: Tiêu đề, Nội dung chi tiết, Phân loại, và Nguồn tổng hợp.

Hãy tổng hợp như một chuyên gia hàng đầu, không bỏ sót một chi tiết quan trọng nào trên Internet.
"""
