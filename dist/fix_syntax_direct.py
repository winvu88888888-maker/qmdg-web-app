# -*- coding: utf-8 -*-
"""Script sửa lỗi syntax trong qmdg_data.py"""

# Đọc file
with open("qmdg_data.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Sửa dòng 152: Thêm dấu phẩy sau }
if len(lines) > 151:
    line_152 = lines[151]  # Index 151 = dòng 152
    if line_152.strip() == "},":
        print("✅ Dòng 152 đã có dấu phẩy")
    elif line_152.strip() == "}":
        lines[151] = line_152.rstrip() + ",\r\n"
        print("✅ Đã thêm dấu phẩy vào dòng 152")

# Ghi lại file
with open("qmdg_data.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("✅ Đã sửa file qmdg_data.py")

# Verify
try:
    from qmdg_data import TOPIC_INTERPRETATIONS
    print(f"✅ SUCCESS! Loaded {len(TOPIC_INTERPRETATIONS)} topics")
except SyntaxError as e:
    print(f"❌ Vẫn còn lỗi syntax: {e}")
except Exception as e:
    print(f"⚠️ Lỗi khác: {e}")
