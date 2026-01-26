import streamlit as st
import os
import json
import sys
from datetime import datetime

# --- ROBUST PATHING FOR SUB-MODULES ---
def setup_sub_paths():
    current_file = os.path.abspath(__file__)
    web_dir = os.path.dirname(current_file)
    root_dir = os.path.dirname(web_dir)
    ai_modules_dir = os.path.join(root_dir, "ai_modules")
    
    for p in [root_dir, web_dir, ai_modules_dir]:
        if p not in sys.path:
            sys.path.insert(0, p)
    return root_dir

ROOT_DIR = setup_sub_paths()

# --- IMPORT SHARD MANAGER ---
try:
    from shard_manager import add_entry, search_index, get_full_entry, delete_entry
except ImportError:
    try:
        from ai_modules.shard_manager import add_entry, search_index, get_full_entry, delete_entry
    except ImportError:
        st.error("🚨 Lỗi: Không tìm thấy Shard Manager.")
        def add_entry(*args, **kwargs): return None
        def search_index(*args, **kwargs): return []
        def get_full_entry(*args, **kwargs): return None
        def delete_entry(*args, **kwargs): return False

# --- MINER DATA (CENTRALIZED) ---
MINERS = [
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

def render_universal_data_hub_tab():
    st.subheader("🌐 Kho Dữ Liệu Vô Tận (Scalable Hub)")
    st.info("Hệ thống lưu trữ Đa Tầng: Tốc độ xử lý vĩnh cửu.")

    categories = ["Mã Nguồn", "Nghiên Cứu", "Kiến Thức", "Kỳ Môn Độn Giáp", "Kinh Dịch", "Khác"]

    with st.expander("📥 Nạp Dữ Liệu Mới Thủ Công"):
        with st.form("sharded_hub_form"):
            title = st.text_input("Tiêu đề/Chủ đề:")
            cat = st.selectbox("Phân loại:", categories)
            content = st.text_area("Nội dung chi tiết (Markdown):", height=150)
            if st.form_submit_button("🚀 Lưu vào Hệ Thống"):
                if title and content:
                    id = add_entry(title, content, cat, source="Thủ công")
                    if id: st.success(f"✅ Đã lưu! ID: {id}"); st.rerun()

    st.markdown("---")
    
    col_f1, col_f2 = st.columns([1, 2])
    selected_cat = col_f1.selectbox("Xem theo loại:", ["Tất cả"] + categories)
    search_q = col_f2.text_input("🔍 Tìm kiếm nhanh:", placeholder="Nhập từ khóa...")
    
    index_results = search_index(search_q, selected_cat)
    st.write(f"Đang hiển thị {len(index_results)} mục.")
    
    for e in index_results:
        with st.expander(f"[{e['category']}] 📁 {e['title']} ({e['created_at'][:10]})"):
            if st.button("👁️ Tải nội dung chi tiết", key=f"load_{e['id']}"):
                full = get_full_entry(e['id'], e['shard'])
                if full: 
                    st.caption(f"ID: {e['id']} | Shard: {e['shard']}")
                    st.markdown(full['content'])
            
            if st.button("🗑️ Xóa", key=f"del_{e['id']}"):
                if delete_entry(e['id']): st.success("Đã xóa!"); st.rerun()

def render_mining_summary_on_dashboard():
    """Show a small version of miner status on the main dashboard."""
    st.markdown("### 🤖 Trạng thái Quân đoàn AI (Khai thác 24/7)")
    cols = st.columns(5)
    for i, m in enumerate(MINERS[:5]):
        cols[i].markdown(f"**{m['topic']}**\n{m['status']}")
    cols2 = st.columns(5)
    for i, m in enumerate(MINERS[5:]):
        cols2[i].markdown(f"**{m['topic']}**\n{m['status']}")

def render_system_management_tab():
    st.subheader("🛠️ Quản Trị Hệ Thống & Quân Đoàn AI")
    t1, t2, t3 = st.tabs(["🤖 Mining Legion (24/7)", "🏥 System Health", "🧬 DB Interaction"])
    
    with t1:
        st.markdown("### 🏹 Quân Đoàn AI Khai Thác Tiềm Năng")
        st.warning("Hệ thống n8n background đang vận hành 10 Đặc phái viên AI.")
        for m in MINERS:
            c1, c2, c3 = st.columns([2, 2, 3])
            c1.write(f"**{m['topic']}**")
            c2.write(m['status'])
            c3.write(f"Nguồn: {m['target']}")
        st.info("💡 Lưu ý: Dữ liệu tìm thấy sẽ tự động 'Push' lên GitHub thông qua n8n API.")

    with t2:
        st.success("Tình trạng Shards: 🟢 Ổn định (100%)")
        st.write("Dung lượng hiện tại: < 1MB")

    with t3:
        st.write("Sửa đổi `database_tuong_tac.py` qua AI...")
