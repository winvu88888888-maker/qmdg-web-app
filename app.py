import streamlit as st
import sys
import os
from datetime import datetime
from zoneinfo import ZoneInfo
from PIL import Image

# Add dist directory to Python path
dist_path = os.path.join(os.path.dirname(__file__), 'dist')
if dist_path not in sys.path:
    sys.path.insert(0, dist_path)

# Import modules from dist directory
try:
    from qmdg_data import *
    from qmdg_data import load_custom_data, save_custom_data
    from qmdg_data import KY_MON_DATA, TOPIC_INTERPRETATIONS
    import qmdg_calc
    from qmdg_detailed_analysis import phan_tich_chi_tiet_cung, so_sanh_chi_tiet_chu_khach
    from super_detailed_analysis import phan_tich_sieu_chi_tiet_chu_de, tao_phan_tich_lien_mach
    from integrated_knowledge_base import (
        get_comprehensive_palace_info, 
        format_info_for_display,
        get_qua_info,
        get_sao_info,
        get_mon_info,
        get_can_info
    )
    from mai_hoa_dich_so import tinh_qua_theo_thoi_gian, tinh_qua_ngau_nhien, giai_qua
    from luc_hao_kinh_dich import lap_qua_luc_hao
    
    # Import Gemini AI helper
    try:
        from gemini_helper import GeminiQMDGHelper
        GEMINI_AVAILABLE = True
    except ImportError:
        GEMINI_AVAILABLE = False
    
    try:
        from dung_than_200_chu_de_day_du import (
            DUNG_THAN_200_CHU_DE,
            hien_thi_dung_than_200,
            lay_dung_than_200
        )
        USE_200_TOPICS = True
    except ImportError:
        USE_200_TOPICS = False
    
    try:
        from database_tuong_tac import (
            LUC_THAN_MAPPING,
            SINH_KHAC_MATRIX,
            TUONG_TAC_SAO_MON,
            QUY_TAC_CHON_DUNG_THAN,
            ANH_HUONG_MUA,
            TRONG_SO_PHAN_TICH,
            TRONG_SO_YEU_TO,
            LUC_THAN_THEO_CHU_DE,
            goi_y_doi_tuong_theo_chu_de
        )
        from phan_tich_da_tang import (
            chon_dung_than_theo_chu_de,
            xac_dinh_luc_than,
            phan_tich_sinh_khac_hop,
            phan_tich_tuong_tac_trong_cung,
            phan_tich_tuong_tac_giua_cac_cung,
            phan_tich_yeu_to_thoi_gian,
            tinh_diem_tong_hop,
            phan_tich_toan_dien
        )
        USE_MULTI_LAYER_ANALYSIS = True
    except ImportError:
        USE_MULTI_LAYER_ANALYSIS = False

    CAN_10 = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    SAO_9 = list(KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["CUU_TINH"].keys())
    THAN_8 = list(KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_THAN"].keys())
    CUA_8 = list(BAT_MON_CO_DINH_DISPLAY.keys())

except ImportError as e:
    st.error(f"❌ Lỗi: Thiếu file dữ liệu hoặc module: {e}")
    st.stop()

# ======================================================================
# STREAMLIT PAGE CONFIG
# ======================================================================
st.set_page_config(
    page_title="🔮 Kỳ Môn Độn Giáp 🔮",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================================
# ZOOM FUNCTIONALITY
# ======================================================================
# Initialize zoom level in session state
if 'zoom_level' not in st.session_state:
    st.session_state.zoom_level = 100  # Default 100%

# Inject custom CSS for zoom
def apply_zoom():
    zoom_scale = st.session_state.zoom_level / 100
    st.markdown(f"""
        <style>
        .main .block-container {{
            transform: scale({zoom_scale});
            transform-origin: top center;
            transition: transform 0.3s ease;
        }}
        
        /* Adjust container to prevent cutoff */
        .main {{
            overflow-x: hidden;
        }}
        
        /* Zoom control styling */
        .zoom-controls {{
            position: fixed;
            top: 10px;
            right: 10px;
            z-index: 999999;
            background: rgba(255, 255, 255, 0.95);
            padding: 8px 12px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
            display: flex;
            gap: 8px;
            align-items: center;
        }}
        
        .zoom-btn {{
            background: #667eea;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.2s;
        }}
        
        .zoom-btn:hover {{
            background: #5568d3;
            transform: translateY(-1px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }}
        
        .zoom-btn:active {{
            transform: translateY(0);
        }}
        
        .zoom-display {{
            font-weight: 600;
            color: #2c3e50;
            min-width: 50px;
            text-align: center;
        }}
        </style>
    """, unsafe_allow_html=True)

apply_zoom()

# ======================================================================
# AUTHENTICATION
# ======================================================================
def check_password():
    """Returns True if the user had the correct password."""
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == "1987":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.markdown("### 🔐 Xác Thực Truy Cập - Kỳ Môn Độn Giáp")
        st.text_input(
            "Vui lòng nhập mật khẩu để sử dụng:",
            type="password",
            on_change=password_entered,
            key="password",
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.markdown("### 🔐 Xác Thực Truy Cập - Kỳ Môn Độn Giáp")
        st.text_input(
            "Vui lòng nhập mật khẩu để sử dụng:",
            type="password",
            on_change=password_entered,
            key="password",
        )
        st.error("❌ Mật khẩu không chính xác! Vui lòng liên hệ tác giả Vũ Việt Cường.")
        return False
    else:
        # Password correct.
        return True

if not check_password():
    st.stop()

# ======================================================================
# ZOOM CONTROLS (Floating)
# ======================================================================
# Create zoom controls using columns at the top
zoom_col1, zoom_col2, zoom_col3, zoom_col4, zoom_col5 = st.columns([1, 1, 1, 1, 6])

with zoom_col1:
    if st.button("🔍−", key="zoom_out", help="Thu nhỏ (Zoom Out)"):
        st.session_state.zoom_level = max(50, st.session_state.zoom_level - 10)
        st.rerun()

with zoom_col2:
    if st.button(f"{st.session_state.zoom_level}%", key="zoom_reset", help="Đặt lại 100%"):
        st.session_state.zoom_level = 100
        st.rerun()

with zoom_col3:
    if st.button("🔍+", key="zoom_in", help="Phóng to (Zoom In)"):
        st.session_state.zoom_level = min(200, st.session_state.zoom_level + 10)
        st.rerun()

with zoom_col4:
    st.markdown(f"<div style='padding: 8px; color: #666; font-size: 12px;'>Zoom: {st.session_state.zoom_level}%</div>", unsafe_allow_html=True)

# ======================================================================
# INITIALIZE SESSION STATE
# ======================================================================
if 'chu_de_hien_tai' not in st.session_state:
    st.session_state.chu_de_hien_tai = "Tổng Quát"
if 'all_topics_full' not in st.session_state:
    st.session_state.all_topics_full = sorted(list(TOPIC_INTERPRETATIONS.keys()))
if 'current_view' not in st.session_state:
    st.session_state.current_view = "ky_mon"  # ky_mon, mai_hoa, luc_hao

# ======================================================================
# HEADER
# ======================================================================
col_header1, col_header2, col_header3 = st.columns([1, 3, 1])

with col_header1:
    # Try to load avatar image
    img_path = os.path.join(os.path.dirname(__file__), "dist", "tải xuống (1).jpg")
    if os.path.exists(img_path):
        try:
            img = Image.open(img_path)
            st.image(img, width=100)
        except:
            pass

with col_header2:
    st.markdown("<h1 style='text-align: center; color: #f1c40f;'>🔮 KỲ MÔN ĐỘN GIÁP 🔮</h1>", unsafe_allow_html=True)

with col_header3:
    st.markdown("**Tác giả**")
    st.markdown("**Vũ Việt Cường**")

st.markdown("---")

# ======================================================================
# SIDEBAR - CONTROLS
# ======================================================================
with st.sidebar:
    st.markdown("### ⚙️ Điều Khiển")
    
    # View selection
    view_option = st.radio(
        "Chọn Phương Pháp:",
        ["🔮 Kỳ Môn Độn Giáp", "📖 Mai Hoa 64 Quẻ", "☯️ Lục Hào Kinh Dịch"],
        index=0
    )
    
    if view_option == "🔮 Kỳ Môn Độn Giáp":
        st.session_state.current_view = "ky_mon"
    elif view_option == "📖 Mai Hoa 64 Quẻ":
        st.session_state.current_view = "mai_hoa"
    else:
        st.session_state.current_view = "luc_hao"
    
    
    st.markdown("---")
    
    # Gemini AI Assistant Configuration
    if GEMINI_AVAILABLE:
        st.markdown("### 🤖 AI Assistant (Gemini)")
        
        gemini_api_key = st.text_input(
            "Gemini API Key:",
            type="password",
            help="Lấy API key miễn phí tại: https://makersuite.google.com/app/apikey",
            key="gemini_api_key"
        )
        
        if gemini_api_key:
            try:
                if 'gemini_helper' not in st.session_state or st.session_state.get('gemini_key') != gemini_api_key:
                    st.session_state.gemini_helper = GeminiQMDGHelper(gemini_api_key)
                    st.session_state.gemini_key = gemini_api_key
                st.success("✅ AI đã sẵn sàng!")
                st.info("💡 Click nút '🤖 Hỏi AI' ở mỗi cung để được giải thích chi tiết")
            except Exception as e:
                st.error(f"❌ Lỗi kết nối AI: {str(e)}")
        else:
            st.warning("⚠️ Nhập API key để sử dụng AI")
            with st.expander("📖 Hướng dẫn lấy API key"):
                st.markdown("""
                **Bước 1:** Truy cập https://makersuite.google.com/app/apikey
                
                **Bước 2:** Đăng nhập Google
                
                **Bước 3:** Click "Create API Key"
                
                **Bước 4:** Copy và paste vào ô trên
                
                **Miễn phí:** 60 requests/phút
                """)
    
    st.markdown("---")
    
    # Time controls (for Ky Mon)
    if st.session_state.current_view == "ky_mon":
        st.markdown("### 🕐 Thời Gian")
        
        use_current_time = st.checkbox("Sử dụng giờ hiện tại", value=True)
        
        if use_current_time:
            # Use Vietnam timezone (UTC+7)
            vn_tz = ZoneInfo("Asia/Ho_Chi_Minh")
            now = datetime.now(vn_tz)
            selected_datetime = now
        else:
            vn_tz = ZoneInfo("Asia/Ho_Chi_Minh")
            now_vn = datetime.now(vn_tz)
            selected_date = st.date_input("Chọn ngày:", now_vn.date())
            selected_time = st.time_input("Chọn giờ:", now_vn.time())
            selected_datetime = datetime.combine(selected_date, selected_time, tzinfo=vn_tz)
        
        # Calculate QMDG parameters
        try:
            params = qmdg_calc.calculate_qmdg_params(selected_datetime)
            
            st.info(f"""
            **Thời gian:** {selected_datetime.strftime("%H:%M - %d/%m/%Y")}
            
            **Âm lịch:**
            - Giờ: {params['can_gio']} {params['chi_gio']}
            - Ngày: {params['can_ngay']} {params['chi_ngay']}
            - Tháng: {params['can_thang']} {params['chi_thang']}
            - Năm: {params['can_nam']} {params['chi_nam']}
            
            **Cục:** {params['cuc']} ({'Dương' if params.get('is_duong_don', True) else 'Âm'} Độn)
            
            **Tiết khí:** {params['tiet_khi']}
            
            **Trực Phù:** {params['truc_phu']}
            
            **Trực Sử:** {params['truc_su']}
            """)
            
        except Exception as e:
            st.error(f"Lỗi tính toán: {e}")
            params = None
    
    st.markdown("---")
    
    # Topic selection
    st.markdown("### 🎯 Chủ Đề Chính")
    
    # Search box
    search_term = st.text_input("🔍 Tìm kiếm chủ đề:", "")
    
    if search_term:
        filtered_topics = [t for t in st.session_state.all_topics_full if search_term.lower() in t.lower()]
    else:
        filtered_topics = st.session_state.all_topics_full
    
    selected_topic = st.selectbox(
        "Chọn chủ đề:",
        filtered_topics,
        index=0 if "Tổng Quát" not in filtered_topics else filtered_topics.index("Tổng Quát")
    )
    
    st.session_state.chu_de_hien_tai = selected_topic
    
    st.info(f"📌 Đã chọn: **{selected_topic}**")
    
    # Multi-layer analysis (if available)
    if USE_MULTI_LAYER_ANALYSIS:
        st.markdown("---")
        st.markdown("### 🎯 Đối Tượng (Lục Thân)")
        
        doi_tuong_options = [
            "🧑 Bản thân",
            "👨‍👩‍👧 Anh chị em",
            "👴👵 Bố mẹ",
            "👶 Con cái",
            "🤝 Người ngoài (Quan)",
            "💰 Người ngoài (Tài)"
        ]
        
        selected_doi_tuong = st.selectbox("Chọn đối tượng:", doi_tuong_options, index=0)

# ======================================================================
# MAIN CONTENT
# ======================================================================

if st.session_state.current_view == "ky_mon":
    st.markdown("## 🔮 BẢNG KỲ MÔN ĐỘN GIÁP")
    
    if params:
        # Calculate full chart
        try:
            # Get Can Gio
            map_can_ngay = {"Giáp": 0, "Kỷ": 0, "Ất": 1, "Canh": 1, "Bính": 2, "Tân": 2, 
                            "Đinh": 3, "Nhâm": 3, "Mậu": 4, "Quý": 4}
            idx_start = map_can_ngay.get(params['can_ngay'], 0)
            idx_chi = CAN_CHI_Gio.index(params['chi_gio'])
            can_gio_idx = (idx_start * 2 + idx_chi) % 10
            can_gio = CAN_10[can_gio_idx]
            
            # Calculate boards
            from qmdg_data import an_bai_luc_nghi, lap_ban_qmdg, tinh_khong_vong, tinh_dich_ma
            
            dia_can = an_bai_luc_nghi(params['cuc'], params['is_duong_don'])
            thien_ban, can_thien_ban, nhan_ban, than_ban, truc_phu_cung = lap_ban_qmdg(
                params['cuc'], params['truc_phu'], params['truc_su'], 
                can_gio, params['chi_gio'], params['is_duong_don']
            )
            
            # Calculate special palaces
            khong_vong = tinh_khong_vong(can_gio, params['chi_gio'])
            dich_ma = tinh_dich_ma(params['chi_gio'])
            
            # Store in session state
            if 'chart_data' not in st.session_state:
                st.session_state.chart_data = {}
            
            st.session_state.chart_data = {
                'thien_ban': thien_ban,
                'can_thien_ban': can_thien_ban,
                'nhan_ban': nhan_ban,
                'than_ban': than_ban,
                'dia_can': dia_can,
                'khong_vong': khong_vong,
                'dich_ma': dich_ma,
                'can_gio': can_gio,
                'can_ngay': params['can_ngay']
            }
            
        except Exception as e:
            st.error(f"Lỗi tính toán bàn: {e}")
            st.session_state.chart_data = None
        
        # Display 9 palaces grid with full information
        if st.session_state.chart_data:
            st.markdown("### 📊 Chín Cung Kỳ Môn")
            
            chart = st.session_state.chart_data
            
            # Palace layout: 4-9-2 / 3-5-7 / 8-1-6
            palace_layout = [
                [4, 9, 2],
                [3, 5, 7],
                [8, 1, 6]
            ]
            
            # Create 3x3 grid
            for row in palace_layout:
                cols = st.columns(3)
                for col_idx, palace_num in enumerate(row):
                    with cols[col_idx]:
                        # Get palace data
                        sao = chart['thien_ban'].get(palace_num, 'N/A')
                        cua = chart['nhan_ban'].get(palace_num, 'N/A')
                        than = chart['than_ban'].get(palace_num, 'N/A')
                        can_thien = chart['can_thien_ban'].get(palace_num, 'N/A')
                        can_dia = chart['dia_can'].get(palace_num, 'N/A')
                        hanh = CUNG_NGU_HANH.get(palace_num, 'N/A')
                        
                        # Check if palace has Dụng Thần
                        topic_data = TOPIC_INTERPRETATIONS.get(selected_topic, {})
                        dung_than_list = topic_data.get("Dụng_Thần", [])
                        has_dung_than = any(dt in [sao, cua, than, can_thien, can_dia] for dt in dung_than_list)
                        
                        # Determine color based on auspiciousness
                        door_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_MON"].get(cua + " Môn", {})
                        cat_hung = door_data.get("Cát_Hung", "Bình")
                        
                        if cat_hung in ["Đại Cát", "Cát"]:
                            bg_color = "#d4edda"  # Light green
                            border_color = "#28a745"
                        elif cat_hung in ["Hung", "Đại Hung"]:
                            bg_color = "#f8d7da"  # Light red
                            border_color = "#dc3545"
                        else:
                            bg_color = "#fff3cd"  # Light yellow
                            border_color = "#ffc107"
                        
                        # Highlight if has Dụng Thần
                        if has_dung_than:
                            border_color = "#007bff"
                            border_width = "3px"
                        else:
                            border_width = "2px"
                        
                        # Special markers
                        markers = []
                        if palace_num in chart['khong_vong']:
                            markers.append("🌑 Không Vong")
                        if palace_num == chart['dich_ma']:
                            markers.append("🐎 Dịch Mã")
                        marker_text = " ".join(markers) if markers else ""
                        
                        # Display palace card with enhanced design
                        st.markdown(f"""
                        <div style="
                            background: linear-gradient(135deg, {bg_color} 0%, {bg_color}ee 100%);
                            border: {border_width} solid {border_color};
                            border-radius: 15px;
                            padding: 16px;
                            margin: 8px;
                            min-height: 240px;
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1), 0 1px 3px rgba(0,0,0,0.08);
                            transition: all 0.3s ease;
                            position: relative;
                            overflow: hidden;
                        ">
                            <div style="
                                position: absolute;
                                top: -50px;
                                right: -50px;
                                width: 100px;
                                height: 100px;
                                background: rgba(255,255,255,0.1);
                                border-radius: 50%;
                            "></div>
                            <div style="text-align: center; font-weight: 700; font-size: 20px; color: #1a1a2e; margin-bottom: 4px; text-shadow: 0 1px 2px rgba(0,0,0,0.1);">
                                Cung {palace_num} - {QUAI_TUONG.get(palace_num, '')}
                            </div>
                            <div style="text-align: center; font-size: 13px; color: #555; margin-bottom: 12px; font-weight: 600;">
                                {hanh} {marker_text}
                            </div>
                            <div style="height: 2px; background: linear-gradient(90deg, transparent, {border_color}, transparent); margin: 10px 0;"></div>
                            <div style="font-size: 14px; line-height: 2; font-family: 'Segoe UI', Arial, sans-serif;">
                                <div style="display: flex; align-items: center; margin: 4px 0;">
                                    <span style="min-width: 110px; font-weight: 600; color: #444;">⭐ Tinh:</span>
                                    <span style="color: #2c3e50; font-weight: 500;">{sao}</span>
                                </div>
                                <div style="display: flex; align-items: center; margin: 4px 0;">
                                    <span style="min-width: 110px; font-weight: 600; color: #444;">🚪 Môn:</span>
                                    <span style="color: #2c3e50; font-weight: 500;">{cua}</span>
                                </div>
                                <div style="display: flex; align-items: center; margin: 4px 0;">
                                    <span style="min-width: 110px; font-weight: 600; color: #444;">👤 Thần:</span>
                                    <span style="color: #2c3e50; font-weight: 500;">{than}</span>
                                </div>
                                <div style="display: flex; align-items: center; margin: 4px 0;">
                                    <span style="min-width: 110px; font-weight: 600; color: #444;">☁️ Can Thiên:</span>
                                    <span style="color: #2c3e50; font-weight: 500;">{can_thien}</span>
                                </div>
                                <div style="display: flex; align-items: center; margin: 4px 0;">
                                    <span style="min-width: 110px; font-weight: 600; color: #444;">🌍 Can Địa:</span>
                                    <span style="color: #2c3e50; font-weight: 500;">{can_dia}</span>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Expander for detailed analysis
                        with st.expander(f"📖 Chi tiết Cung {palace_num}"):
                            # Basic info
                            st.markdown(f"**Quái tượng:** {QUAI_TUONG.get(palace_num, 'N/A')}")
                            st.markdown(f"**Ngũ hành:** {hanh}")
                            st.markdown(f"**Cát/Hung:** {cat_hung}")
                            
                            # Check Dụng Thần
                            if has_dung_than:
                                found_dt = [dt for dt in dung_than_list if dt in [sao, cua, than, can_thien, can_dia]]
                                st.success(f"✅ Cung này chứa Dụng Thần: **{', '.join(found_dt)}**")
                                st.info(f"Đây là cung QUAN TRỌNG cho chủ đề **'{selected_topic}'**")
                            else:
                                st.warning("⚠️ Cung này không chứa Dụng Thần chính")
                            
                            # Star description
                            star_data = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['CUU_TINH'].get(sao, {})
                            if star_data:
                                col_sao_1, col_sao_2 = st.columns([3, 1])
                                with col_sao_1:
                                    st.markdown(f"**⭐ {sao}:** {star_data.get('Tính_Chất', 'N/A')}")
                                with col_sao_2:
                                    if 'gemini_helper' in st.session_state:
                                        if st.button(f"🤖 Giải thích {sao}", key=f"ai_star_{palace_num}_{sao}"):
                                            with st.spinner(f"AI đang giải thích về sao {sao}..."):
                                                explanation = st.session_state.gemini_helper.explain_element('star', sao)
                                                st.info(explanation)
                            
                            # Door description
                            if door_data:
                                col_door_1, col_door_2 = st.columns([3, 1])
                                with col_door_1:
                                    st.markdown(f"**🚪 {cua} Môn:** {door_data.get('Luận_Đoán', 'N/A')}")
                                with col_door_2:
                                    if 'gemini_helper' in st.session_state:
                                        if st.button(f"🤖 Giải thích {cua}", key=f"ai_door_{palace_num}_{cua}"):
                                            with st.spinner(f"AI đang giải thích về cửa {cua}..."):
                                                explanation = st.session_state.gemini_helper.explain_element('door', cua)
                                                st.info(explanation)
                            
                            # Deity description
                            deity_data = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['BAT_THAN'].get(than, {})
                            if deity_data:
                                col_than_1, col_than_2 = st.columns([3, 1])
                                with col_than_1:
                                    st.markdown(f"**👤 {than}:** {deity_data.get('Tính_Chất', 'N/A')}")
                                with col_than_2:
                                    if 'gemini_helper' in st.session_state:
                                        if st.button(f"🤖 Giải thích {than}", key=f"ai_than_{palace_num}_{than}"):
                                            with st.spinner(f"AI đang giải thích về thần {than}..."):
                                                explanation = st.session_state.gemini_helper.explain_element('deity', than)
                                                st.info(explanation)
                            
                            # Stem combination
                            cach_cuc_key = can_thien + can_dia
                            combination_data = KY_MON_DATA['TRUCTU_TRANH'].get(cach_cuc_key, {})
                            if combination_data:
                                col_can_1, col_can_2 = st.columns([3, 1])
                                with col_can_1:
                                    st.markdown(f"**🔗 {can_thien}/{can_dia}:** {combination_data.get('Luận_Giải', 'Chưa có nội dung')}")
                                    st.caption(f"Cát/Hung: {combination_data.get('Cát_Hung', 'Bình')}")
                                with col_can_2:
                                    if 'gemini_helper' in st.session_state:
                                        if st.button(f"🤖 Giải thích {can_thien}/{can_dia}", key=f"ai_can_{palace_num}_{can_thien}_{can_dia}"):
                                            with st.spinner(f"AI đang giải thích về tổ hợp {can_thien}/{can_dia}..."):
                                                explanation = st.session_state.gemini_helper.explain_element('stem', f"{can_thien}/{can_dia}")
                                                st.info(explanation)
                            
                            # AI Analysis Button
                            if 'gemini_helper' in st.session_state:
                                st.markdown("---")
                                if st.button(f"🤖 Hỏi AI về Cung {palace_num}", key=f"ai_palace_{palace_num}", type="primary"):
                                    with st.spinner("🤖 AI đang phân tích..."):
                                        palace_data = {
                                            'num': palace_num,
                                            'qua': QUAI_TUONG.get(palace_num, 'N/A'),
                                            'hanh': hanh,
                                            'star': sao,
                                            'door': cua,
                                            'deity': than,
                                            'can_thien': can_thien,
                                            'can_dia': can_dia
                                        }
                                        try:
                                            analysis = st.session_state.gemini_helper.analyze_palace(
                                                palace_data,
                                                selected_topic
                                            )
                                            st.markdown("### 🤖 Phân Tích AI")
                                            st.markdown(analysis)
                                        except Exception as e:
                                            st.error(f"❌ Lỗi: {str(e)}")

        
        # Display Dụng Thần info
        st.markdown("---")
        st.markdown("### 🎯 THÔNG TIN DỤNG THẦN")
        
        topic_data = TOPIC_INTERPRETATIONS.get(selected_topic, {})
        dung_than_list = topic_data.get("Dụng_Thần", [])
        luan_giai = topic_data.get("Luận_Giải_Gợi_Ý", "")
        
        if dung_than_list:
            st.success(f"**Dụng Thần cần xem:** {', '.join(dung_than_list)}")
        
        if luan_giai:
            st.info(f"**Gợi ý luận giải:** {luan_giai}")
        
        # Display detailed Dụng Thần from 200+ database
        if USE_200_TOPICS:
            dt_data = lay_dung_than_200(selected_topic)
            if dt_data and 'ky_mon' in dt_data:
                km = dt_data['ky_mon']
                st.markdown("#### 🔮 Dụng Thần Kỳ Môn Chi Tiết")
                st.write(f"**Dụng Thần:** {km.get('dung_than', 'N/A')}")
                st.write(f"**Giải thích:** {km.get('giai_thich', 'N/A')}")
                st.write(f"**Cách xem:** {km.get('cach_xem', 'N/A')}")
                if 'vi_du' in km:
                    st.write(f"**Ví dụ:** {km['vi_du']}")
        
        # ===== PALACE COMPARISON SECTION =====
        if st.session_state.chart_data:
            st.markdown("---")
            st.markdown("### ⚖️ SO SÁNH CHỦ - KHÁCH")
            
            col1, col2, col3 = st.columns([2, 2, 1])
            
            with col1:
                chu_cung = st.selectbox(
                    "Chọn Cung Chủ (Bản thân):",
                    options=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                    format_func=lambda x: f"Cung {x} - {QUAI_TUONG.get(x, '')}",
                    key="chu_cung_select"
                )
            
            with col2:
                khach_cung = st.selectbox(
                    "Chọn Cung Khách (Đối phương):",
                    options=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                    index=1,
                    format_func=lambda x: f"Cung {x} - {QUAI_TUONG.get(x, '')}",
                    key="khach_cung_select"
                )
            
            with col3:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("🔍 So Sánh", type="primary", use_container_width=True):
                    st.session_state.show_comparison = True
            
            # Display comparison results
            if st.session_state.get('show_comparison', False):
                try:
                    chart = st.session_state.chart_data
                    
                    # Get palace info
                    def get_palace_info(cung_num):
                        return {
                            'so': cung_num,
                            'ten': QUAI_TUONG.get(cung_num, 'N/A'),
                            'hanh': CUNG_NGU_HANH.get(cung_num, 'N/A'),
                            'sao': chart['thien_ban'].get(cung_num, 'N/A'),
                            'cua': chart['nhan_ban'].get(cung_num, 'N/A'),
                            'than': chart['than_ban'].get(cung_num, 'N/A'),
                            'can_thien': chart['can_thien_ban'].get(cung_num, 'N/A'),
                            'can_dia': chart['dia_can'].get(cung_num, 'N/A')
                        }
                    
                    chu = get_palace_info(chu_cung)
                    khach = get_palace_info(khach_cung)
                    
                    # Use detailed comparison if available
                    try:
                        from qmdg_detailed_analysis import so_sanh_chi_tiet_chu_khach
                        comparison_result = so_sanh_chi_tiet_chu_khach(selected_topic, chu, khach)
                        
                        st.markdown("#### 📊 KẾT QUẢ SO SÁNH CHI TIẾT")
                        
                        # Display palace info side by side
                        col_chu, col_khach = st.columns(2)
                        
                        with col_chu:
                            st.markdown(f"""
                            **🏠 CUNG CHỦ - Cung {chu['so']} ({chu['ten']})**
                            - Ngũ Hành: {chu['hanh']}
                            - ⭐ Tinh: {chu['sao']}
                            - 🚪 Môn: {chu['cua']}
                            - 👤 Thần: {chu['than']}
                            - Can: {chu['can_thien']}/{chu['can_dia']}
                            """)
                        
                        with col_khach:
                            st.markdown(f"""
                            **👥 CUNG KHÁCH - Cung {khach['so']} ({khach['ten']})**
                            - Ngũ Hành: {khach['hanh']}
                            - ⭐ Tinh: {khach['sao']}
                            - 🚪 Môn: {khach['cua']}
                            - 👤 Thần: {khach['than']}
                            - Can: {khach['can_thien']}/{khach['can_dia']}
                            """)
                        
                        # Element interaction
                        st.markdown("---")
                        st.markdown("**🔄 PHÂN TÍCH NGŨ HÀNH:**")
                        interaction = comparison_result.get('ngu_hanh_sinh_khac', 'N/A')
                        st.info(f"**{chu['hanh']}** và **{khach['hanh']}**: {interaction}")
                        
                        # Strength comparison
                        if 'diem_chu' in comparison_result and 'diem_khach' in comparison_result:
                            st.markdown("**💪 ĐIỂM SỐ LỰC LƯỢNG:**")
                            col_score1, col_score2 = st.columns(2)
                            
                            with col_score1:
                                chu_score = comparison_result['diem_chu']
                                st.metric("Chủ", f"{chu_score}/100", delta=None)
                                st.progress(chu_score / 100)
                            
                            with col_score2:
                                khach_score = comparison_result['diem_khach']
                                st.metric("Khách", f"{khach_score}/100", delta=None)
                                st.progress(khach_score / 100)
                        
                        # Advantages and disadvantages
                        if 'uu_diem_chu' in comparison_result:
                            st.success(f"**✅ Ưu điểm Chủ:** {comparison_result['uu_diem_chu']}")
                        
                        if 'nhuoc_diem_chu' in comparison_result:
                            st.warning(f"**⚠️ Nhược điểm Chủ:** {comparison_result['nhuoc_diem_chu']}")
                        
                        # Advice
                        if 'loi_khuyen' in comparison_result:
                            st.markdown("**💡 LỜI KHUYÊN:**")
                            st.info(comparison_result['loi_khuyen'])
                        
                        # Timing prediction
                        if 'du_doan_thoi_gian' in comparison_result:
                            with st.expander("⏰ Dự Đoán Thời Gian"):
                                st.write(comparison_result['du_doan_thoi_gian'])
                        
                        # AI Comparison Analysis
                        if 'gemini_helper' in st.session_state:
                            st.markdown("---")
                            if st.button("🤖 AI Phân Tích So Sánh", key="ai_compare_btn", type="primary"):
                                with st.spinner("🤖 AI đang phân tích so sánh..."):
                                    try:
                                        prompt = f"""Bạn là chuyên gia Kỳ Môn Độn Giáp. Hãy phân tích so sánh giữa 2 cung sau cho chủ đề '{selected_topic}':
                                        
                                        **Cung Chủ (Cung {chu['so']}):** Sao {chu['sao']}, Môn {chu['cua']}, Thần {chu['than']}, Can {chu['can_thien']}/{chu['can_dia']}
                                        **Cung Khách (Cung {khach['so']}):** Sao {khach['sao']}, Môn {khach['cua']}, Thần {khach['than']}, Can {khach['can_thien']}/{khach['can_dia']}
                                        **Mối quan hệ ngũ hành:** {interaction}
                                        
                                        Hãy giải thích rõ:
                                        1. Vị thế bên nào mạnh hơn?
                                        2. Thuận lợi và khó khăn của mỗi bên.
                                        3. Kết quả dự đoán và lời khuyên cụ thể.
                                        
                                        Trả lời ngắn gọn, thực tế bằng tiếng Việt."""
                                        
                                        analysis = st.session_state.gemini_helper.model.generate_content(prompt).text
                                        st.markdown("### 🤖 Phân Tích So Sánh AI")
                                        st.markdown(analysis)
                                    except Exception as e:
                                        st.error(f"❌ Lỗi: {str(e)}")
                        
                    except ImportError:
                        # Fallback to simple comparison
                        st.markdown("#### 📊 KẾT QUẢ SO SÁNH CƠ BẢN")
                        
                        col_chu, col_khach = st.columns(2)
                        
                        with col_chu:
                            st.markdown(f"**🏠 Cung Chủ {chu['so']}**")
                            st.write(f"Ngũ Hành: {chu['hanh']}")
                            st.write(f"Sao: {chu['sao']}")
                            st.write(f"Môn: {chu['cua']}")
                        
                        with col_khach:
                            st.markdown(f"**👥 Cung Khách {khach['so']}**")
                            st.write(f"Ngũ Hành: {khach['hanh']}")
                            st.write(f"Sao: {khach['sao']}")
                            st.write(f"Môn: {khach['cua']}")
                        
                        # Simple element interaction
                        interaction = tinh_ngu_hanh_sinh_khac(chu['hanh'], khach['hanh'])
                        st.info(f"**Ngũ hành:** {interaction}")
                        
                except Exception as e:
                    st.error(f"Lỗi so sánh: {e}")
        
        # ===== INTEGRATED ANALYSIS SECTION =====
        if st.session_state.chart_data:
            st.markdown("---")
            st.markdown("### 📋 BÁO CÁO TỔNG HỢP")
            
            with st.expander("🔍 Xem Phân Tích Tổng Hợp (Kỳ Môn + Mai Hoa + Lục Hào)"):
                if st.button("🎯 Tạo Báo Cáo Tổng Hợp", type="primary"):
                    try:
                        chart = st.session_state.chart_data
                        
                        # Find host palace (Can Ngay)
                        chu_idx = 5  # Default to center
                        for cung, can in chart['can_thien_ban'].items():
                            if can == chart['can_ngay']:
                                chu_idx = cung
                                break
                        
                        # Use selected guest palace or default
                        khach_idx = st.session_state.get('khach_cung_select', 1)
                        
                        def get_p_info(idx):
                            return {
                                'so': idx,
                                'ten': QUAI_TUONG.get(idx, 'N/A'),
                                'hanh': CUNG_NGU_HANH.get(idx, 'N/A'),
                                'sao': chart['thien_ban'].get(idx, 'N/A'),
                                'cua': chart['nhan_ban'].get(idx, 'N/A'),
                                'than': chart['than_ban'].get(idx, 'N/A'),
                                'can_thien': chart['can_thien_ban'].get(idx, 'N/A'),
                                'can_dia': chart['dia_can'].get(idx, 'N/A')
                            }
                        
                        chu = get_p_info(chu_idx)
                        khach = get_p_info(khach_idx)
                        now = datetime.now()
                        
                        # Super detailed analysis
                        from super_detailed_analysis import phan_tich_sieu_chi_tiet_chu_de, tao_phan_tich_lien_mach
                        
                        with st.spinner("Đang phân tích toàn diện..."):
                            res_9pp = phan_tich_sieu_chi_tiet_chu_de(selected_topic, chu, khach, now)
                            mqh = tinh_ngu_hanh_sinh_khac(chu['hanh'], khach['hanh'])
                            res_lien_mach = tao_phan_tich_lien_mach(selected_topic, chu, khach, now, res_9pp, mqh)
                        
                        st.success("✅ Đã tạo báo cáo tổng hợp!")
                        
                        # Display 9 aspects analysis
                        st.markdown("#### 📊 PHÂN TÍCH 9 PHƯƠNG DIỆN")
                        
                        aspects = [
                            ('thai_at', '⚖️ Thái Ất'),
                            ('thanh_cong', '🎯 Thành Công'),
                            ('tai_loc', '💰 Tài Lộc'),
                            ('quan_he', '🤝 Quan Hệ'),
                            ('suc_khoe', '❤️ Sức Khỏe'),
                            ('tranh_chap', '⚔️ Tranh Chấp'),
                            ('di_chuyen', '🚗 Di Chuyển'),
                            ('hoc_van', '📚 Học Vấn'),
                            ('tam_linh', '🔮 Tâm Linh')
                        ]
                        
                        for key, label in aspects:
                            if key in res_9pp:
                                data = res_9pp[key]
                                with st.expander(f"{label} - Điểm: {data.get('diem', 'N/A')}/10"):
                                    st.write(f"**Thái độ:** {data.get('thai_do', 'N/A')}")
                                    st.write(f"**Phân tích:** {data.get('phan_tich', 'N/A')}")
                        
                        # Overall score
                        if 'tong_ket' in res_9pp:
                            st.markdown("---")
                            st.markdown("#### 🎯 TỔNG KẾT")
                            tong_ket = res_9pp['tong_ket']
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                st.metric("Điểm Tổng Hợp", f"{tong_ket.get('diem_tong', 'N/A')}/100")
                            with col2:
                                st.metric("Thái Độ", tong_ket.get('thai_do_chung', 'N/A'))
                            
                            if 'loi_khuyen_tong_quat' in tong_ket:
                                st.info(f"**💡 Lời khuyên:** {tong_ket['loi_khuyen_tong_quat']}")
                        
                        # Coherent analysis
                        if res_lien_mach:
                            st.markdown("---")
                            st.markdown("#### 🔗 PHÂN TÍCH LIÊN MẠCH")
                            st.write(res_lien_mach)
                        
                        # Download report
                        report_text = f"""
BÁO CÁO PHÂN TÍCH KỲ MÔN ĐỘN GIÁP
Chủ đề: {selected_topic}
Thời gian: {now.strftime('%H:%M - %d/%m/%Y')}

THÔNG TIN CUNG CHỦ (Cung {chu['so']}):
- Quái: {chu['ten']}
- Ngũ Hành: {chu['hanh']}
- Sao: {chu['sao']}
- Môn: {chu['cua']}
- Thần: {chu['than']}
- Can: {chu['can_thien']}/{chu['can_dia']}

THÔNG TIN CUNG KHÁCH (Cung {khach['so']}):
- Quái: {khach['ten']}
- Ngũ Hành: {khach['hanh']}
- Sao: {khach['sao']}
- Môn: {khach['cua']}
- Thần: {khach['than']}
- Can: {khach['can_thien']}/{khach['can_dia']}

PHÂN TÍCH LIÊN MẠCH:
{res_lien_mach}
                        """
                        
                        st.download_button(
                            label="📥 Tải Báo Cáo (TXT)",
                            data=report_text,
                            file_name=f"bao_cao_qmdg_{selected_topic}_{now.strftime('%Y%m%d_%H%M')}.txt",
                            mime="text/plain"
                        )
                        
                    except Exception as e:
                        st.error(f"Lỗi tạo báo cáo: {e}")
                        import traceback
                        st.code(traceback.format_exc())

            # AI Comprehensive Analysis
            if 'gemini_helper' in st.session_state and st.session_state.chart_data:
                st.markdown("---")
                st.markdown("### 🤖 PHÂN TÍCH TỔNG HỢP BẰNG AI")
                
                if st.button("💬 Phân Tích Toàn Bàn Bằng AI", type="primary", key="ai_comprehensive"):
                    with st.spinner("🤖 AI đang phân tích toàn bộ bàn..."):
                        try:
                            # Get Dụng Thần info
                            topic_data = TOPIC_INTERPRETATIONS.get(selected_topic, {})
                            dung_than_list = topic_data.get("Dụng_Thần", [])
                            
                            analysis = st.session_state.gemini_helper.comprehensive_analysis(
                                st.session_state.chart_data,
                                selected_topic,
                                dung_than_list
                            )
                            
                            st.success("**🤖 Phân Tích Tổng Hợp:**")
                            st.markdown(analysis)
                        except Exception as e:
                            st.error(f"❌ Lỗi: {str(e)}")
            
            # AI Q&A Section
            if 'gemini_helper' in st.session_state and st.session_state.chart_data:
                st.markdown("---")
                st.markdown("### ❓ HỎI AI VỀ BÀN NÀY")
                
                user_question = st.text_area(
                    "Câu hỏi của bạn:",
                    placeholder="Ví dụ: Tôi nên làm gì để tăng vận may? Thời điểm nào tốt nhất?",
                    key="ai_question"
                )
                
                if st.button("🤖 Hỏi AI", key="ai_ask", type="primary"):
                    if user_question:
                        with st.spinner("🤖 AI đang suy nghĩ..."):
                            try:
                                answer = st.session_state.gemini_helper.answer_question(
                                    user_question,
                                    st.session_state.chart_data,
                                    selected_topic
                                )
                                st.info(f"**🤖 Trả lời:**

{answer}")
                            except Exception as e:
                                st.error(f"❌ Lỗi: {str(e)}")
                    else:
                        st.warning("⚠️ Vui lòng nhập câu hỏi")



elif st.session_state.current_view == "mai_hoa":
    st.markdown("## 📖 MAI HOA DỊCH SỐ - 64 QUẺ KINH DỊCH")
    
    st.markdown(f"### 🎯 Chủ đề: **{selected_topic}**")
    st.caption("Mai Hoa Dịch Số sẽ phân tích theo chủ đề đã chọn")
    
    st.markdown("### Chọn phương pháp tính quẻ:")
    
    method = st.radio("", ["Theo thời gian", "Ngẫu nhiên"], key="mai_hoa_method")
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
    
    with col_btn1:
        btn_time = st.button("🎲 Lập Quẻ Theo Thời Gian", use_container_width=True) if method == "Theo thời gian" else False
    
    with col_btn2:
        btn_random = st.button("🎲 Lập Quẻ Ngẫu Nhiên", use_container_width=True) if method == "Ngẫu nhiên" else False
    
    if btn_time or btn_random:
        try:
            now = datetime.now()
            
            if btn_time:
                qua_result = tinh_qua_theo_thoi_gian(now.year, now.month, now.day, now.hour)
            else:
                qua_result = tinh_qua_ngau_nhien()
            
            # Get interpretation for selected topic
            giai_qua_result = giai_qua(qua_result, selected_topic)
            qua_result['interpretation'] = giai_qua_result
            
            # Store in session state
            st.session_state.mai_hoa_result = qua_result
            
        except Exception as e:
            st.error(f"Lỗi lập quẻ: {e}")
            import traceback
            st.code(traceback.format_exc())
    
    # Display results if available
    if 'mai_hoa_result' in st.session_state:
        qua_result = st.session_state.mai_hoa_result
        
        st.success("✅ Đã lập quẻ thành công!")
        
        # Display hexagrams visually
        st.markdown("### 📊 Quẻ Tượng")
        
        col_ban, col_ho, col_bien = st.columns(3)
        
        # Helper function to display hexagram
        def display_hexagram(qua_name, title, column):
            with column:
                st.markdown(f"**{title}**")
                st.markdown(f"<div style='text-align: center; font-size: 24px; font-weight: bold; color: #2c3e50;'>{qua_name}</div>", unsafe_allow_html=True)
                
                # Display trigrams (simplified)
                st.markdown("<div style='text-align: center; font-size: 14px; color: #7f8c8d;'>☰☷☲☳☴☵☶☱</div>", unsafe_allow_html=True)
        
        if 'ban_qua' in qua_result:
            display_hexagram(qua_result['ban_qua'], "🎯 Bản Quẻ", col_ban)
        
        if 'ho_qua' in qua_result:
            display_hexagram(qua_result['ho_qua'], "🤝 Hỗ Quẻ", col_ho)
        
        if 'bien_qua' in qua_result:
            display_hexagram(qua_result['bien_qua'], "🔄 Biến Quẻ", col_bien)
        
        # Display detailed information
        st.markdown("---")
        st.markdown("### 📋 Thông Tin Chi Tiết")
        
        info_col1, info_col2 = st.columns(2)
        
        with info_col1:
            if 'thuong_qua' in qua_result:
                st.info(f"**Thượng Quái:** {qua_result['thuong_qua']}")
            if 'ha_qua' in qua_result:
                st.info(f"**Hạ Quái:** {qua_result['ha_qua']}")
        
        with info_col2:
            if 'dong_hao' in qua_result:
                st.warning(f"**Động Hào:** {qua_result['dong_hao']}")
            if 'ngu_hanh' in qua_result:
                st.success(f"**Ngũ Hành:** {qua_result['ngu_hanh']}")
        
        # Display interpretation
        st.markdown("---")
        st.markdown(f"### 📜 Giải Quẻ Theo Chủ Đề: **{selected_topic}**")
        
        if 'interpretation' in qua_result:
            st.markdown(qua_result['interpretation'])
        else:
            st.write("Chưa có giải quẻ chi tiết.")
        
        # Display raw data in expander
        with st.expander("🔍 Xem Dữ Liệu Thô"):
            st.json(qua_result)


elif st.session_state.current_view == "luc_hao":
    st.markdown("## ☯️ LỤC HÀO KINH DỊCH")
    
    st.markdown(f"### 🎯 Chủ đề: **{selected_topic}**")
    st.caption("Lục Hào Kinh Dịch sẽ phân tích theo chủ đề đã chọn")
    
    if st.button("🎲 Lập Quẻ Lục Hào", type="primary", use_container_width=False):
        try:
            now = datetime.now()
            luc_hao_result = lap_qua_luc_hao(now.year, now.month, now.day, now.hour, selected_topic)
            
            # Store in session state
            st.session_state.luc_hao_result = luc_hao_result
            
        except Exception as e:
            st.error(f"Lỗi lập quẻ: {e}")
            import traceback
            st.code(traceback.format_exc())
    
    # Display results if available
    if 'luc_hao_result' in st.session_state:
        luc_hao_result = st.session_state.luc_hao_result
        
        st.success("✅ Đã lập quẻ thành công!")
        
        # Display hexagram visually
        st.markdown("### 📊 Quẻ Tượng")
        
        col_ban, col_bien = st.columns(2)
        
        with col_ban:
            st.markdown("**🎯 Bản Quẻ**")
            if 'ban_qua_ten' in luc_hao_result:
                st.markdown(f"<div style='text-align: center; font-size: 24px; font-weight: bold; color: #2c3e50;'>{luc_hao_result['ban_qua_ten']}</div>", unsafe_allow_html=True)
            
            # Display hexagram lines (visual representation)
            if 'ban_qua_lines' in luc_hao_result:
                st.markdown("<div style='text-align: center; font-family: monospace; font-size: 16px;'>", unsafe_allow_html=True)
                for line in luc_hao_result['ban_qua_lines']:
                    if line == 1:  # Yang line
                        st.markdown("━━━━━━", unsafe_allow_html=True)
                    else:  # Yin line
                        st.markdown("━━  ━━", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
        
        with col_bien:
            st.markdown("**🔄 Biến Quẻ**")
            if 'bien_qua_ten' in luc_hao_result:
                st.markdown(f"<div style='text-align: center; font-size: 24px; font-weight: bold; color: #2c3e50;'>{luc_hao_result['bien_qua_ten']}</div>", unsafe_allow_html=True)
            
            if 'bien_qua_lines' in luc_hao_result:
                st.markdown("<div style='text-align: center; font-family: monospace; font-size: 16px;'>", unsafe_allow_html=True)
                for line in luc_hao_result['bien_qua_lines']:
                    if line == 1:
                        st.markdown("━━━━━━", unsafe_allow_html=True)
                    else:
                        st.markdown("━━  ━━", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
        
        # Display detailed information
        st.markdown("---")
        st.markdown("### 📋 Thông Tin Chi Tiết")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if 'the_ung' in luc_hao_result:
                st.info(f"**Thế Ứng:** {luc_hao_result['the_ung']}")
            if 'dong_hao' in luc_hao_result:
                st.warning(f"**Động Hào:** {luc_hao_result['dong_hao']}")
        
        with col2:
            if 'luc_than' in luc_hao_result:
                st.success(f"**Lục Thân:** {luc_hao_result['luc_than']}")
            if 'luc_thu' in luc_hao_result:
                st.info(f"**Lục Thú:** {luc_hao_result['luc_thu']}")
        
        with col3:
            if 'vuong_suy' in luc_hao_result:
                st.success(f"**Vượng Suy:** {luc_hao_result['vuong_suy']}")
            if 'dong_tinh' in luc_hao_result:
                st.warning(f"**Động Tĩnh:** {luc_hao_result['dong_tinh']}")
        
        # Display interpretation
        st.markdown("---")
        st.markdown(f"### 📜 Giải Quẻ Theo Chủ Đề: **{selected_topic}**")
        
        if 'giai_qua' in luc_hao_result:
            st.markdown(luc_hao_result['giai_qua'])
        elif 'interpretation' in luc_hao_result:
            st.markdown(luc_hao_result['interpretation'])
        else:
            st.write("Chưa có giải quẻ chi tiết.")
        
        # Detailed analysis by lines
        if 'phan_tich_tung_hao' in luc_hao_result:
            with st.expander("🔍 Phân Tích Từng Hào"):
                for hao_info in luc_hao_result['phan_tich_tung_hao']:
                    st.markdown(f"**{hao_info.get('ten', 'N/A')}:** {hao_info.get('y_nghia', 'N/A')}")
        
        # Display raw data in expander
        with st.expander("🔍 Xem Dữ Liệu Thô"):
            st.json(luc_hao_result)


# ======================================================================
# FOOTER
# ======================================================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #7f8c8d;'>
    <p>© 2026 Vũ Việt Cường - Kỳ Môn Độn Giáp Web Application</p>
    <p>🌐 Chạy 24/7 trên Streamlit Cloud</p>
</div>
""");
