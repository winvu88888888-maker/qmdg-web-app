"""
Gemini AI Helper for Qi Men Dun Jia Analysis
Provides AI-powered explanations and insights
"""

import google.generativeai as genai
import os

class GeminiQMDGHelper:
    """Helper class to integrate Gemini AI for QMDG analysis"""
    
    def __init__(self, api_key):
        """Initialize Gemini with API key"""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
    def analyze_palace(self, palace_data, topic):
        """
        Analyze a specific palace with AI
        
        Args:
            palace_data: Dict with palace information
            topic: Current divination topic
            
        Returns:
            str: AI analysis in Vietnamese
        """
        prompt = f"""Bạn là chuyên gia Kỳ Môn Độn Giáp với kiến thức sâu rộng về dịch học Trung Hoa.

Hãy phân tích cung sau một cách chi tiết và dễ hiểu:

**Thông tin cung:**
- Cung số: {palace_data.get('num', 'N/A')}
- Quái tượng: {palace_data.get('qua', 'N/A')}
- Ngũ hành: {palace_data.get('hanh', 'N/A')}
- Tinh (Sao): {palace_data.get('star', 'N/A')}
- Môn (Cửa): {palace_data.get('door', 'N/A')}
- Thần: {palace_data.get('deity', 'N/A')}
- Can Thiên: {palace_data.get('can_thien', 'N/A')}
- Can Địa: {palace_data.get('can_dia', 'N/A')}

**Chủ đề đang xem:** {topic}

Hãy phân tích theo cấu trúc sau:

1. **Ý nghĩa tổng quan**: Cung này đại diện cho điều gì trong chủ đề "{topic}"?

2. **Phân tích các yếu tố**:
   - Tinh {palace_data.get('star', 'N/A')} mang ý nghĩa gì?
   - Môn {palace_data.get('door', 'N/A')} báo hiệu điều gì?
   - Thần {palace_data.get('deity', 'N/A')} ảnh hưởng như thế nào?
   - Tổ hợp Can {palace_data.get('can_thien', 'N/A')}/{palace_data.get('can_dia', 'N/A')} có ý nghĩa gì?

3. **Tương tác giữa các yếu tố**: Các yếu tố này kết hợp với nhau tạo ra thông điệp gì?

4. **Điềm báo**: Cát hay hung? Mức độ như thế nào?

5. **Lời khuyên cụ thể**: Nên làm gì? Tránh điều gì?

Trả lời bằng tiếng Việt, ngắn gọn nhưng đầy đủ ý nghĩa."""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Lỗi khi gọi AI: {str(e)}

Vui lòng kiểm tra API key hoặc thử lại."
    
    def comprehensive_analysis(self, chart_data, topic, dung_than_info=None):
        """
        Comprehensive analysis of the entire QMDG chart
        
        Args:
            chart_data: Complete chart data
            topic: Divination topic
            dung_than_info: Information about Dụng Thần
            
        Returns:
            str: Comprehensive AI analysis
        """
        # Build palace summary
        palace_summary = []
        for i in range(1, 10):
            palace_summary.append(f"""
Cung {i}:
- Tinh: {chart_data.get('thien_ban', {}).get(i, 'N/A')}
- Môn: {chart_data.get('nhan_ban', {}).get(i, 'N/A')}
- Thần: {chart_data.get('than_ban', {}).get(i, 'N/A')}
- Can: {chart_data.get('can_thien_ban', {}).get(i, 'N/A')}/{chart_data.get('dia_can', {}).get(i, 'N/A')}
""")
        
        palaces_text = "
".join(palace_summary)
        
        dung_than_text = ""
        if dung_than_info:
            dung_than_text = f"
**Dụng Thần cần chú ý:** {', '.join(dung_than_info)}"
        
        prompt = f"""Bạn là chuyên gia Kỳ Môn Độn Giáp hàng đầu.

Hãy phân tích TỔNG QUAN toàn bộ bàn Kỳ Môn sau cho chủ đề: **{topic}**

**Thông tin bàn:**
{palaces_text}
{dung_than_text}

Hãy phân tích theo cấu trúc:

1. **Tổng quan tình hình** (2-3 câu): Nhìn chung tình hình như thế nào?

2. **Các điểm mạnh**: Những cung/yếu tố nào thuận lợi? Tại sao?

3. **Các điểm yếu**: Những cung/yếu tố nào bất lợi? Cần lưu ý gì?

4. **Tương tác quan trọng**: Có tương tác đặc biệt nào giữa các cung không?

5. **Thời điểm**: Khi nào là thời điểm tốt/xấu?

6. **Lời khuyên tổng hợp**: 
   - Nên làm gì?
   - Không nên làm gì?
   - Chiến lược tổng thể?

7. **Dự đoán kết quả**: Khả năng thành công? Cần chuẩn bị gì?

Trả lời bằng tiếng Việt, cụ thể và thực tế."""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Lỗi khi gọi AI: {str(e)}"
    
    def answer_question(self, question, chart_data, topic):
        """
        Answer user's free-form question about the chart
        
        Args:
            question: User's question
            chart_data: Current chart data
            topic: Current topic
            
        Returns:
            str: AI answer
        """
        # Build context
        palace_summary = []
        for i in range(1, 10):
            palace_summary.append(
                f"Cung {i}: {chart_data.get('thien_ban', {}).get(i, 'N/A')} - "
                f"{chart_data.get('nhan_ban', {}).get(i, 'N/A')} - "
                f"{chart_data.get('than_ban', {}).get(i, 'N/A')}"
            )
        
        context = "
".join(palace_summary)
        
        prompt = f"""Bạn là chuyên gia Kỳ Môn Độn Giáp.

**Bối cảnh:**
- Chủ đề: {topic}
- Bàn Kỳ Môn hiện tại:
{context}

**Câu hỏi của người dùng:**
{question}

Hãy trả lời câu hỏi dựa trên:
1. Thông tin từ bàn Kỳ Môn
2. Kiến thức về dịch học
3. Nguyên lý Ngũ hành, Bát quái

Trả lời ngắn gọn, dễ hiểu, cụ thể và thực tế bằng tiếng Việt."""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Lỗi: {str(e)}"
    
    def explain_element(self, element_type, element_name):
        """
        Explain a specific QMDG element (Star, Door, Deity, Stem)
        
        Args:
            element_type: 'star', 'door', 'deity', or 'stem'
            element_name: Name of the element
            
        Returns:
            str: Detailed explanation
        """
        type_map = {
            'star': 'Tinh (Sao)',
            'door': 'Môn (Cửa)',
            'deity': 'Thần',
            'stem': 'Can (Thiên Can)'
        }
        
        prompt = f"""Bạn là chuyên gia Kỳ Môn Độn Giáp.

Hãy giải thích chi tiết về {type_map.get(element_type, element_type)}: **{element_name}**

Bao gồm:
1. Nguồn gốc và ý nghĩa
2. Thuộc tính (Ngũ hành, âm dương, v.v.)
3. Tính chất (cát/hung, đặc điểm)
4. Ứng dụng trong luận đoán
5. Ví dụ cụ thể

Giải thích dễ hiểu, bằng tiếng Việt."""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Lỗi: {str(e)}"
