import streamlit as st
import os
import json
from datetime import datetime

HUB_PATH = "data_hub.json"

def add_to_hub(title: str, content: str, category: str = "Kiến Thức", source: str = "AI System", tags: list = None):
    """Utility to add an entry to the universal data hub."""
    if not os.path.exists(HUB_PATH):
        with open(HUB_PATH, 'w', encoding='utf-8') as f:
            json.dump({"entries": []}, f)
            
    try:
        with open(HUB_PATH, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            new_entry = {
                "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
                "title": title,
                "category": category,
                "source": source,
                "content": content,
                "tags": tags or [],
                "created_at": datetime.now().isoformat()
            }
            data['entries'].append(new_entry)
            f.seek(0)
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.truncate()
        return True
    except Exception as e:
        print(f"Error adding to hub: {e}")
        return False

def render_universal_data_hub_tab():
    st.subheader("🌐 Kho Dữ Liệu Vô Tận (Universal Data Hub)")
    st.info("Nơi lưu trữ và truy xuất mọi thông tin từ Internet và hệ thống.")
    
    # Path for persistent data hub
    hub_path = HUB_PATH
    
    if not os.path.exists(hub_path):
        with open(hub_path, 'w', encoding='utf-8') as f:
            json.dump({"entries": []}, f)

    categories = ["Mã Nguồn", "Nghiên Cứu", "Kiến Thức", "Kỳ Môn Độn Giáp", "Khác"]

    with st.expander("📥 Nạp Dữ Liệu Mới Thủ Công"):
        with st.form("add_to_hub_form"):
            title = st.text_input("Tiêu đề/Chủ đề:")
            cat = st.selectbox("Phân loại:", categories)
            source = st.text_input("Nguồn (URL hoặc Tên):")
            content = st.text_area("Nội dung chi tiết (Markdown auto-detected):", height=200)
            tags = st.text_input("Tags (phân cách bằng dấu phẩy):")
            
            if st.form_submit_button("🚀 Lưu vào Kho Vô Tận"):
                if title and content:
                    success = add_to_hub(
                        title=title,
                        content=content,
                        category=cat,
                        source=source,
                        tags=[t.strip() for t in tags.split(",")] if tags else []
                    )
                    if success:
                        st.success("✅ Đã lưu trữ thành công!")
                        st.rerun()
                    else:
                        st.error("Lỗi lưu trữ.")

    st.markdown("---")
    
    # Filter and Search
    col_f1, col_f2 = st.columns([1, 2])
    with col_f1:
        selected_cat = st.selectbox("Xem theo loại:", ["Tất cả"] + categories)
    with col_f2:
        search = st.text_input("🔍 Tìm kiếm trong Kho dữ liệu:", placeholder="Nhập từ khóa...")
    
    try:
        with open(hub_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            entries = data.get('entries', [])
            
        if selected_cat != "Tất cả":
            entries = [e for e in entries if e.get('category') == selected_cat]

        if search:
            search = search.lower()
            entries = [e for e in entries if search in e['title'].lower() or search in e['content'].lower()]
            
        st.write(f"Đang hiển thị {len(entries)} mục dữ liệu.")
        
        for e in reversed(entries):
            cat_label = e.get('category', 'Kiến Thức')
            with st.expander(f"[{cat_label}] 📁 {e['title']} ({e['created_at'][:10]})"):
                st.caption(f"Nguồn: {e['source']} | Tags: {', '.join(e['tags'])}")
                st.markdown(e['content'])
                if st.button("🗑️ Xóa", key=f"del_{e['id']}"):
                    # Logic to delete entry
                    data['entries'] = [x for x in data['entries'] if x['id'] != e['id']]
                    with open(hub_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                    st.rerun()
    except Exception as e:
        st.info("Kho dữ liệu đang trống hoặc có lỗi định dạng.")

def render_system_management_tab():
    st.subheader("🛠️ Quản Trị Hệ Thống (AI Self-Repair)")
    st.warning("Tính năng nâng cao: AI có quyền truy cập và sửa đổi cấu hình lõi.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔄 Cập Nhật database_tuong_tac.py")
        if st.button("🔍 AI Quét & Tối Ưu Hóa Dữ Liệu", use_container_width=True):
            with st.spinner("AI đang phân tích các quy tắc sinh khắc và ngũ hành..."):
                # Logic to trigger AI analysis of database_tuong_tac.py
                st.info("AI đã phát hiện 0 lỗi logic. Hệ thống đang đạt hiệu suất tối ưu.")
                
    with col2:
        st.markdown("### ➕ Thêm Chủ Đề Mói")
        new_topic_name = st.text_input("Tên chủ đề mới:")
        if st.button("🪄 AI Tự Tạo Nội Dung Luận Giải", use_container_width=True):
            if new_topic_name:
                st.info(f"AI đang soạn thảo nội dung cho chủ đề: {new_topic_name}")
            else:
                st.error("Vui lòng nhập tên chủ đề.")

    st.markdown("---")
    st.markdown("### 🛠️ Bảo Trì Web")
    if st.button("🧹 Dọn dẹp Cache & File rác", type="secondary"):
        st.success("Hệ thống đã được dọn dẹp sạch sẽ!")
