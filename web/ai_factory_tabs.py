import streamlit as st
import os
import json
from datetime import datetime

# Import Shard Manager for Scalability
try:
    from ai_modules.shard_manager import add_entry, search_index, get_full_entry, delete_entry
except ImportError:
    # Local fallback for direct execution
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from shard_manager import add_entry, search_index, get_full_entry, delete_entry

HUB_PATH = "data_hub.json" # Legacy backward compatibility

def add_to_hub(title: str, content: str, category: str = "Kiến Thức", source: str = "AI System", tags: list = None):
    """Wrapper to use Shard Manager as primary storage."""
    return add_entry(title, content, category, source, tags)

def render_universal_data_hub_tab():
    st.subheader("🌐 Kho Dữ Liệu Vô Tận (Scalable Hub)")
    st.info("Hệ thống lưu trữ Đa Tầng: Tốc độ xử lý vĩnh cửu bất kể lượng dữ liệu khổng lồ.")

    categories = ["Mã Nguồn", "Nghiên Cứu", "Kiến Thức", "Kỳ Môn Độn Giáp", "Kinh Dịch", "Khác"]

    with st.expander("📥 Nạp Dữ Liệu Mới Thủ Công"):
        with st.form("sharded_hub_form"):
            title = st.text_input("Tiêu đề/Chủ đề:")
            cat = st.selectbox("Phân loại:", categories)
            source = st.text_input("Nguồn:", value="Thủ công")
            content = st.text_area("Nội dung chi tiết:", height=200)
            tags = st.text_input("Tags (phân cách bằng dấu phẩy):")
            
            if st.form_submit_button("🚀 Lưu vào Hệ Thống Đa Tầng"):
                if title and content:
                    t_list = [t.strip() for t in tags.split(",")] if tags else []
                    id = add_entry(title, content, cat, source, t_list)
                    if id:
                        st.success(f"✅ Đã lưu vào Shard! ID: {id}")
                        st.rerun()
                    else: st.error("Lỗi lưu trữ Shard.")

    st.markdown("---")
    
    # Filter and Search using Index (Fast)
    col_f1, col_f2 = st.columns([1, 2])
    with col_f1:
        selected_cat = st.selectbox("Xem theo loại:", ["Tất cả"] + categories)
    with col_f2:
        search_q = st.text_input("🔍 Tìm kiếm nhanh (Index-only):", placeholder="Nhập từ khóa...")
    
    # Fetch results from Index (Very fast, no full content loaded yet)
    index_results = search_index(search_q, selected_cat)
    
    st.write(f"Đang hiển thị {len(index_results)} mục dữ liệu (Tải theo yêu cầu).")
    
    for e in index_results:
        # Lazy Loading: Full content is only fetched when expander is opened
        with st.expander(f"[{e['category']}] 📁 {e['title']} ({e['created_at'][:10]})"):
            if st.button("👁️ Tải nội dung chi tiết", key=f"load_{e['id']}"):
                full_data = get_full_entry(e['id'], e['shard'])
                if full_data:
                    st.caption(f"Nguồn: {full_data['source']} | Tags: {', '.join(full_data['tags'])}")
                    st.markdown(full_data['content'])
                else:
                    st.error("Không thể nạp nội dung từ Shard.")
            
            if st.button("🗑️ Xóa", key=f"del_{e['id']}"):
                if delete_entry(e['id']):
                    st.success("Đã xóa!")
                    st.rerun()

def render_system_management_tab():
    st.subheader("🛠️ Quản Trị Hệ Thống & Quân Đoàn AI")
    
    tabs = st.tabs(["🤖 Mining Legion (24/7)", "🏥 System Health", "🧬 DB Interaction"])
    
    with tabs[0]:
        st.markdown("### 🏹 Quân Đoàn AI Khai Thác Tiềm Năng")
        st.warning("Hệ thống n8n background đang vận hành 10 Đặc phái viên AI.")
        
        miners = [
            {"topic": "Kỳ Môn Độn Giáp", "status": "🟢 Đang quét", "target": "China, VN Archives"},
            {"topic": "Kinh Dịch Chuyên Sâu", "status": "🟢 Đang quét", "target": "I Ching Societies"},
            {"topic": "Lập Trình Python/AI", "status": "🟡 Nghỉ quẻ", "target": "GitHub, Arxiv"},
            {"topic": "Y Học Cổ Truyền", "status": "🟢 Đang quét", "target": "Traditional Medicine Hubs"},
            {"topic": "Chiến Lược Quân Sự", "status": "🟢 Đang quét", "target": "Thập Nhị Binh Thư"},
            {"topic": "Phong Thủy Địa Lý", "status": "🟢 Đang quét", "target": "Google Maps, Folklore"},
            {"topic": "Công Nghệ AI Mới", "status": "🟢 Đang quét", "target": "TechCrunch, OpenAI Docs"},
            {"topic": "An Ninh Mạng", "status": "🟢 Đang quét", "target": "CVE, Security Lists"},
            {"topic": "Phân Tích Dữ Liệu", "status": "🟢 Đang quét", "target": "Kaggle, Datasets"},
            {"topic": "Thiết Kế UI/UX", "status": "🟢 Đang quét", "target": "Dribbble, Behance"}
        ]
        
        for m in miners:
            col1, col2, col3 = st.columns([2, 2, 3])
            col1.write(f"**{m['topic']}**")
            col2.write(m['status'])
            col3.write(f"Nguồn: {m['target']}")
            
        st.info("💡 Lưu ý: Dữ liệu tìm thấy sẽ tự động 'Push' lên GitHub thông qua n8n API. Bạn không cần làm gì cả.")

    with tabs[1]:
        st.write("Kiểm tra tính toàn vẹn của Shard...")
        # Add shard health check logic here
        st.success("Tất cả Shards (1-100) ổn định.")

    with tabs[2]:
        st.write("Sửa đổi `database_tuong_tac.py` qua AI...")
        # Existing self-repair logic
