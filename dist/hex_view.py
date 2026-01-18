with open('qmdg_data.py', 'rb') as f:
    lines = f.readlines()

for i in range(239, 255):
    if i < len(lines):
        print(f"Line {i+1}: {lines[i].hex(' ')} | {lines[i].decode('utf-8', errors='replace').strip()}")
