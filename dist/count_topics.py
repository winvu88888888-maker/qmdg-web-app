# -*- coding: utf-8 -*-
"""
Script đếm và hiển thị tất cả chủ đề với số thứ tự
"""
from qmdg_data import TOPIC_INTERPRETATIONS

# Lấy danh sách tất cả chủ đề
all_topics = list(TOPIC_INTERPRETATIONS.keys())

print("=" * 80)
print(f"📊 TỔNG SỐ CHỦ ĐỀ: {len(all_topics)}")
print("=" * 80)
print()

# Nhóm theo category
categories = {}
for i, topic in enumerate(all_topics, 1):
    # Tách category từ tên topic
    parts = topic.split()
    if len(parts) > 0:
        category = parts[0]
        if category not in categories:
            categories[category] = []
        categories[category].append((i, topic))

# Hiển thị theo nhóm
print("📋 DANH SÁCH CHỦ ĐỀ THEO NHÓM:")
print()

for category, topics in sorted(categories.items()):
    print(f"\n🔹 {category.upper()} ({len(topics)} chủ đề)")
    print("-" * 80)
    for num, topic in topics[:10]:  # Hiển thị 10 chủ đề đầu mỗi nhóm
        print(f"  {num:4d}. {topic}")
    if len(topics) > 10:
        print(f"  ... và {len(topics) - 10} chủ đề khác")

# Hiển thị tất cả chủ đề với số thứ tự
print("\n" + "=" * 80)
print("📝 DANH SÁCH ĐẦY ĐỦ TẤT CẢ CHỦ ĐỀ:")
print("=" * 80)
print()

for i, topic in enumerate(all_topics, 1):
    print(f"{i:4d}. {topic}")

# Lưu ra file
with open("danh_sach_chu_de.txt", "w", encoding="utf-8") as f:
    f.write("=" * 80 + "\n")
    f.write(f"TỔNG SỐ CHỦ ĐỀ: {len(all_topics)}\n")
    f.write("=" * 80 + "\n\n")
    
    for i, topic in enumerate(all_topics, 1):
        f.write(f"{i:4d}. {topic}\n")

print(f"\n✅ Đã lưu danh sách vào file: danh_sach_chu_de.txt")
print(f"📊 Tổng cộng: {len(all_topics)} chủ đề")
