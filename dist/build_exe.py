import subprocess
import os

def build():
    # Entry point
    main_script = "qmdg_app2.py"
    app_name = "QMDG_Application"
    
    # Files to include (source;destination)
    # On Windows, the separator is ';'
    data_files = [
        ("custom_data.json", "."),
        ("qmdg_excel_full.json", "."),
        ("qmdg_advanced_knowledge.json", "."),
        ("qmdg_detailed_analysis.py", "."), # PyInstaller usually finds these, but being explicit doesn't hurt
        ("super_detailed_analysis.py", "."),
        ("qmdg_calc.py", "."),
        ("qmdg_data.py", "."),
        ("dist/tải xuống (1).jpg", ".")
    ]
    
    # --- CHUYỂN ĐỔI JPG SANG ICO CHO ICON EXE ---
    icon_name = "app_icon.ico"
    jpg_icon = "dist/tải xuống (1).jpg"
    if not os.path.exists(jpg_icon):
        jpg_icon = "tải xuống (1).jpg"

    if os.path.exists(jpg_icon):
        try:
            from PIL import Image
            img = Image.open(jpg_icon)
            img.save(icon_name, format="ICO", sizes=[(32, 32), (48, 48), (64, 64)])
            print(f"✅ Đã tạo file icon: {icon_name}")
        except Exception as e:
            print(f"⚠️ Không thể tạo icon: {e}")
            icon_name = None
    else:
        icon_name = None

    cmd = [
        "python", "-m", "PyInstaller",
        "--noconsole",
        "--onefile",
        f"--name={app_name}",
        "--clean"
    ]
    
    if icon_name and os.path.exists(icon_name):
        cmd.append(f"--icon={icon_name}")

    for src, dest in data_files:
        if os.path.exists(src):
            cmd.append(f"--add-data={src};{dest}")
    
    cmd.append(main_script)
    
    print(f"Running command: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    print("Build complete! Check the 'dist' folder.")

if __name__ == "__main__":
    build()
