# -*- coding: utf-8 -*-
"""Script sửa lỗi syntax - thêm dấu phẩy sau TRUCTU_TRANH"""

# Đọc file
with open("qmdg_data.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Tìm và sửa dòng 246 (index 245)
if len(lines) > 245:
    line_246 = lines[245]  # Index 245 = dòng 246
    print(f"Dòng 246: {repr(line_246)}")
    
    if line_246.strip() == "},":
        print("✅ Dòng 246 đã có dấu phẩy")
    elif line_246.strip() == "}":
        lines[245] = "    },\r\n"
        print("✅ Đã thêm dấu phẩy vào dòng 246")

# Ghi lại file
with open("qmdg_data.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("✅ Đã sửa file qmdg_data.py")

# Verify
try:
    exec(compile(open("qmdg_data.py", encoding="utf-8").read(), "qmdg_data.py", "exec"))
    print("✅ Syntax OK!")
except SyntaxError as e:
    print(f"❌ Vẫn còn lỗi syntax: {e}")
    print(f"   Dòng {e.lineno}: {e.text}")
