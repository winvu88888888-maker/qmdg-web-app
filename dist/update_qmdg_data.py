# -*- coding: utf-8 -*-
"""
Script cập nhật qmdg_data.py với 992 chủ đề mới
"""
import json
import re

# Đọc file topics
with open("topics_1000_final.json", "r", encoding="utf-8") as f:
    new_topics = json.load(f)

print(f"✅ Đã load {len(new_topics)} chủ đề từ JSON")

# Đọc file qmdg_data.py hiện tại
with open("qmdg_data.py", "r", encoding="utf-8") as f:
    content = f.read()

# Tìm vị trí của TOPIC_INTERPRETATIONS
pattern = r'("TOPIC_INTERPRETATIONS":\s*\{)(.*?)(\n\s*\})'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("❌ Không tìm thấy TOPIC_INTERPRETATIONS trong qmdg_data.py")
    exit(1)

# Tạo nội dung mới cho TOPIC_INTERPRETATIONS
new_content_lines = []
new_content_lines.append('        # === 992 CHỦ ĐỀ TỰ ĐỘNG (AUTO-GENERATED) ===')

for topic_name, topic_data in new_topics.items():
    dung_than = topic_data["Dụng_Thần"]
    luan_giai = topic_data["Luận_Giải_Gợi_Ý"]
    
    # Format Python dict
    dung_than_str = str(dung_than).replace("'", '"')
    luan_giai_str = luan_giai.replace('"', '\\"')
    
    line = f'        "{topic_name}": {{"Dụng_Thần": {dung_than_str}, "Luận_Giải_Gợi_Ý": "{luan_giai_str}"}},'
    new_content_lines.append(line)

new_topic_content = '\n'.join(new_content_lines)

# Thay thế nội dung cũ
start_pos = match.start(2)
end_pos = match.end(2)

new_full_content = content[:start_pos] + '\n' + new_topic_content + '\n        ' + content[end_pos:]

# Ghi lại file
with open("qmdg_data.py", "w", encoding="utf-8") as f:
    f.write(new_full_content)

print(f"✅ Đã cập nhật qmdg_data.py với {len(new_topics)} chủ đề!")
print("📝 File qmdg_data.py đã được cập nhật thành công")
