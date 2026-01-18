# -*- coding: utf-8 -*-
"""
Script sửa lỗi syntax trong qmdg_data.py
"""

# Đọc file
with open("qmdg_data.py", "r", encoding="utf-8") as f:
    content = f.read()

# Sửa lỗi: Xóa dòng trống thừa trước dấu đóng ngoặc
content = content.replace(',\n        \n    }', '\n    }')
content = content.replace(',\n        \r\n    }', '\n    }')

# Ghi lại
with open("qmdg_data.py", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Đã sửa lỗi syntax")

# Verify
try:
    exec(open("qmdg_data.py", encoding="utf-8").read(), {})
    print("✅ Syntax OK!")
    
    from qmdg_data import TOPIC_INTERPRETATIONS
    print(f"✅ Import thành công! Tổng topics: {len(TOPIC_INTERPRETATIONS)}")
except SyntaxError as e:
    print(f"❌ Vẫn còn lỗi syntax: {e}")
except Exception as e:
    print(f"⚠️ Lỗi khác: {e}")
