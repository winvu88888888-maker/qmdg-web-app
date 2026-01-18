import os

def reconstruct_qmdg_data():
    backup_file = 'qmdg_data_backup.py'
    topics_file = 'topic_output.txt'
    output_file = 'qmdg_data.py'
    
    # Read topics
    with open(topics_file, 'r', encoding='utf-8') as f:
        topics_content = f.read()
    
    # Read backup to find the sections
    with open(backup_file, 'r', encoding='utf-8') as f:
        backup_lines = f.readlines()
    
    # 1. Header is fixed at lines 1-246 (TRUCTU_TRANH ends at 246)
    # Actually, let's verify where TRUCTU_TRANH ends in backup
    header_end_idx = 0
    for i, line in enumerate(backup_lines):
        if '"TRUCTU_TRANH": {' in line:
            # Found start, now find the end of this dict
            continue
        if i > 150 and '    },' in line and '"TOPIC_INTERPRETATIONS"' not in backup_lines[i+1]:
             # This is a bit risky. Let's just use the known index 246 if it matches.
             pass
    
    # Better: Use lines 1-246 which we verified
    header = backup_lines[:246]
    
    # 2. Find the start of PHẦN 2
    part2_start_idx = 0
    for i, line in enumerate(backup_lines):
        if '# PHẦN 2: LOGIC TÍNH TOÁN CƠ BẢN' in line:
            part2_start_idx = i - 1 # Include the separator line if possible
            break
    
    if part2_start_idx == 0:
        print("Could not find PHẦN 2 in backup!")
        return

    footer = backup_lines[part2_start_idx:]
    
    # Construct final content
    # Note: Header ends with 246: "    }," (closing TRUCTU_TRANH)
    # We need to add a comma if it's not there, but it is a dict entry so it's fine.
    # Wait, line 246 is "    }," which is inside KY_MON_DATA.
    # So we just append the topics.
    
    final_content = "".join(header)
    final_content += "\n"
    final_content += topics_content
    final_content += "\n    }\n" # Close KY_MON_DATA
    final_content += "".join(footer)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Reconstructed {output_file} successfully.")
    print(f"Footer started at backup line {part2_start_idx + 1}")

if __name__ == "__main__":
    reconstruct_qmdg_data()
