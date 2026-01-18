# -*- coding: utf-8 -*-
"""
Script cập nhật qmdg_data.py với 1059 chủ đề đã merge
"""
import json

# Đọc topics đã merge
with open("topics_merged_1000.json", "r", encoding="utf-8") as f:
    merged_topics = json.load(f)

print(f"✅ Đã load {len(merged_topics)} chủ đề từ JSON")

# Đọc file qmdg_data.py
with open("qmdg_data.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Tìm vị trí bắt đầu và kết thúc của TOPIC_INTERPRETATIONS
start_idx = None
end_idx = None
brace_count = 0
found_topic_interp = False

for i, line in enumerate(lines):
    if '"TOPIC_INTERPRETATIONS":' in line:
        start_idx = i
        found_topic_interp = True
        continue
    
    if found_topic_interp:
        brace_count += line.count('{') - line.count('}')
        if brace_count == 0 and '}' in line:
            end_idx = i
            break

if start_idx is None or end_idx is None:
    print("❌ Không tìm thấy TOPIC_INTERPRETATIONS")
    exit(1)

print(f"📍 Tìm thấy TOPIC_INTERPRETATIONS từ dòng {start_idx} đến {end_idx}")

# Tạo nội dung mới
new_lines = []
new_lines.append('    "TOPIC_INTERPRETATIONS": {\n')

for i, (topic_name, topic_data) in enumerate(merged_topics.items()):
    dung_than = topic_data.get("Dụng_Thần", [])
    luan_giai = topic_data.get("Luận_Giải_Gợi_Ý", "")
    
    # Escape quotes trong string
    luan_giai_escaped = luan_giai.replace('"', '\\"').replace('\n', ' ')
    
    # Format dòng
    dung_than_str = json.dumps(dung_than, ensure_ascii=False)
    line = f'        "{topic_name}": {{"Dụng_Thần": {dung_than_str}, "Luận_Giải_Gợi_Ý": "{luan_giai_escaped}"}}'
    
    # Thêm dấu phẩy nếu không phải topic cuối
    if i < len(merged_topics) - 1:
        line += ','
    
    new_lines.append(line + '\n')

new_lines.append('    }\n')

# Thay thế nội dung
new_content = lines[:start_idx] + new_lines + lines[end_idx+1:]

# Ghi lại file
with open("qmdg_data.py", "w", encoding="utf-8") as f:
    f.writelines(new_content)

print(f"✅ Đã cập nhật qmdg_data.py với {len(merged_topics)} chủ đề!")
print("📝 File qmdg_data.py đã được cập nhật thành công")

# Verify
print("\n🔍 Đang verify...")
try:
    from qmdg_data import TOPIC_INTERPRETATIONS
    print(f"✅ Verify thành công! Tổng số topics: {len(TOPIC_INTERPRETATIONS)}")
    print(f"📋 Mẫu 5 topics: {list(TOPIC_INTERPRETATIONS.keys())[:5]}")
except Exception as e:
    print(f"❌ Lỗi verify: {e}")
