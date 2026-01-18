# -*- coding: utf-8 -*-
"""
Script tạo lại qmdg_data.py với cấu trúc đúng
"""
import json

# Load topics từ JSON
with open("topics_merged_1000.json", "r", encoding="utf-8") as f:
    topics = json.load(f)

print(f"✅ Loaded {len(topics)} topics from JSON")

# Đọc phần đầu của file qmdg_data cũ (từ dòng 1 đến dòng 153)
with open("qmdg_data_backup.py", "r", encoding="utf-8") as f:
    old_lines = f.readlines()

# Lấy phần đầu (trước TRUCTU_TRANH)
header_lines = old_lines[:153]  # Dòng 1-153

# Lấy phần TRUCTU_TRANH (dòng 154-246)
tructu_lines = old_lines[153:246]

# Lấy phần cuối (sau TOPIC_INTERPRETATIONS)
# Tìm dòng kết thúc TOPIC_INTERPRETATIONS trong file cũ
end_topic_idx = None
for i in range(246, len(old_lines)):
    if old_lines[i].strip() == "}" and i > 246:
        # Kiểm tra xem đây có phải là dấu đóng của TOPIC_INTERPRETATIONS không
        if i < len(old_lines) - 1 and "PHẦN 2" in old_lines[i+2]:
            end_topic_idx = i
            break

if end_topic_idx:
    footer_lines = old_lines[end_topic_idx+1:]
else:
    # Fallback: lấy từ dòng 2302 trở đi
    footer_lines = old_lines[2301:]

# Tạo nội dung mới
new_content = []

# 1. Header
new_content.extend(header_lines)

# 2. TRUCTU_TRANH (đã có sẵn, chỉ cần đảm bảo có dấu phẩy cuối)
new_content.extend(tructu_lines)

# 3. TOPIC_INTERPRETATIONS
new_content.append("    \n")
new_content.append("    \"TOPIC_INTERPRETATIONS\": {\n")

# Thêm tất cả topics
topic_items = list(topics.items())
for i, (name, data) in enumerate(topic_items):
    dung_than = data.get("Dụng_Thần", [])
    luan_giai = data.get("Luận_Giải_Gợi_Ý", "").replace('"', '\\"').replace('\n', ' ')
    
    dung_than_str = json.dumps(dung_than, ensure_ascii=False)
    
    line = f'        "{name}": {{"Dụng_Thần": {dung_than_str}, "Luận_Giải_Gợi_Ý": "{luan_giai}"}}'
    
    # Thêm dấu phẩy nếu không phải topic cuối
    if i < len(topic_items) - 1:
        line += ","
    
    new_content.append(line + "\n")

new_content.append("    }\n")
new_content.append("}\n")

# 4. Footer
new_content.extend(footer_lines)

# Ghi file mới
with open("qmdg_data.py", "w", encoding="utf-8") as f:
    f.writelines(new_content)

print(f"✅ Đã tạo lại qmdg_data.py với {len(topics)} topics")

# Verify
try:
    from qmdg_data import TOPIC_INTERPRETATIONS
    print(f"✅ SUCCESS! Loaded {len(TOPIC_INTERPRETATIONS)} topics")
    print(f"📋 Sample: {list(TOPIC_INTERPRETATIONS.keys())[:5]}")
except Exception as e:
    print(f"❌ Error: {e}")
