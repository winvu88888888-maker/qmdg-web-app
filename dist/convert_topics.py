import json
import os
import sys

# Ensure we can import from the current directory
sys.path.append(os.getcwd())

try:
    from dung_than_200_chu_de_day_du import DUNG_THAN_200_CHU_DE
except ImportError:
    print("Error: Could not find dung_than_200_chu_de_day_du.py")
    sys.exit(1)

topic_interpretations = {}

for topic, data in DUNG_THAN_200_CHU_DE.items():
    # Extract Dụng Thần for Ky Mon
    km_data = data.get("ky_mon", {})
    dt_str = km_data.get("dung_than", "")
    # Split by + or , and strip spaces
    dt_list = [d.strip() for d in dt_str.replace("+", ",").split(",") if d.strip()]
    
    # Create Luận Giải Gợi Ý
    muc_tieu = data.get("muc_tieu", "")
    giai_thich = km_data.get("giai_thich", "")
    luan_giai = f"{muc_tieu}. {giai_thich}"
    
    topic_interpretations[topic] = {
        "Dụng_Thần": dt_list,
        "Luận_Giải_Gợi_Ý": luan_giai
    }

# Generate part of the python code
output_file = "topic_output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("    \"TOPIC_INTERPRETATIONS\": {\n")
    items = list(topic_interpretations.items())
    for i, (topic, data) in enumerate(items):
        line = f"        \"{topic}\": {json.dumps(data, ensure_ascii=False)}"
        if i < len(items) - 1:
            line += ","
        f.write(line + "\n")
    f.write("    }\n")

print(f"Generated {len(topic_interpretations)} topics in {output_file}")
