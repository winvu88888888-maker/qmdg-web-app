import os

def patch_qmdg_data():
    source_file = 'qmdg_data.py'
    data_file = 'final_topic_insertion.txt'
    
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    with open(data_file, 'r', encoding='utf-8') as f:
        new_content = f.read()
    
    # Replacement range: line 247 to 676 (1-indexed)
    # 0-indexed: index 246 to 675
    # lines[246:676] includes line 676
    
    start_index = 246
    end_index = 676
    
    # Preserve everything before and after
    final_lines = lines[:start_index] + [new_content + '\n'] + lines[end_index:]
    
    with open(source_file, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    
    print(f"Patched {source_file} from line 247 back to {end_index}")

if __name__ == "__main__":
    patch_qmdg_data()
