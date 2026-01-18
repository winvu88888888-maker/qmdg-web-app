# -*- coding: utf-8 -*-
"""
Kỳ Môn Độn Giáp - Web Server
Flask API Server for Web Interface
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from datetime import datetime
import webbrowser
import threading
import os
import sys
import socket

# Import QMDG modules
try:
    from qmdg_data import *
    from qmdg_data import load_custom_data, KY_MON_DATA, TOPIC_INTERPRETATIONS
    from mai_hoa_dich_so import tinh_qua_theo_thoi_gian, giai_qua
    from luc_hao_kinh_dich import lap_qua_luc_hao
    from super_detailed_analysis import phan_tich_sieu_chi_tiet_chu_de, tao_phan_tich_lien_mach
    from qmdg_calc import CAN as CAN_10
    import qmdg_calc
except ImportError as e:
    print(f"❌ THIẾU THƯ VIỆN: {e}")
    print("Vui lòng chạy lệnh: pip install flask flask-cors Pillow")
    input("Nhấn Enter để thoát...")
    sys.exit(1)

# Initialize Flask app
base_dir = os.path.dirname(os.path.abspath(__file__))
# Web folder is one level up from dist
parent_dir = os.path.dirname(base_dir)
web_dir = os.path.join(parent_dir, 'web')

# Debug: Print paths
print(f"Base dir: {base_dir}")
print(f"Parent dir: {parent_dir}")
print(f"Web dir: {web_dir}")
print(f"Index.html exists: {os.path.exists(os.path.join(web_dir, 'index.html'))}")

app = Flask(__name__,
            static_folder=os.path.join(web_dir, 'static'),
            template_folder=web_dir)
CORS(app)

@app.after_request
def add_header(response):
    """Thêm header đặc biệt để Ngrok không hiện trang cảnh báo/quảng cáo"""
    response.headers['ngrok-skip-browser-warning'] = '1'
    return response

# Global data
current_chart_data = None

# ===== API ENDPOINTS =====

@app.route('/')
def index():
    """Serve main HTML page"""
    index_path = os.path.join(web_dir, 'index.html')
    if not os.path.exists(index_path):
        return f"""<h1>❌ Lỗi</h1>
        <p>Không tìm thấy file 'index.html'.</p>
        <p>Web dir: {web_dir}</p>
        <p>Index path: {index_path}</p>
        <p>Files in web dir: {os.listdir(web_dir) if os.path.exists(web_dir) else 'Directory not found'}</p>""", 404
    return send_from_directory(web_dir, 'index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    if data.get('password') == "1987":
        return jsonify({"success": True, "token": "qmdg_auth_token_1987"})
    return jsonify({"success": False, "message": "Mật khẩu không chính xác"}), 401

@app.route('/api/topics')
def get_topics():
    """Get list of all available topics"""
    return jsonify(sorted(list(TOPIC_INTERPRETATIONS.keys())))

@app.route('/api/initial-data')
def get_initial_data():
    """Get initial data for dropdowns"""
    try:
        now = datetime.now()
        params = qmdg_calc.calculate_qmdg_params(now)
        
        stars = [{"value": k, "label": k} for k in KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["CUU_TINH"].keys()]
        doors = [{"value": k, "label": k} for k in BAT_MON_CO_DINH_DISPLAY.keys()]
        branches = [{"value": b, "label": b} for b in CAN_CHI_Gio]
        
        return jsonify({
            "stars": stars,
            "doors": doors,
            "branches": branches,
            "currentTime": now.strftime("%H:%M - %d/%m/%Y"),
            "ju": params['cuc'],
            "zhifu": params['truc_phu'],
            "zhishi": params['truc_su'],
            "hourBranch": params['chi_gio']
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/current-time')
def get_current_time():
    """Get current time and calculated parameters"""
    try:
        now = datetime.now()
        params = qmdg_calc.calculate_qmdg_params(now)
        
        return jsonify({
            "currentTime": now.strftime("%H:%M - %d/%m/%Y"),
            "ju": params['cuc'],
            "zhifu": params['truc_phu'],
            "zhishi": params['truc_su'],
            "hourBranch": params['chi_gio']
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/calculate', methods=['POST'])
def calculate_chart():
    """Calculate Qi Men chart"""
    global current_chart_data
    
    try:
        data = request.json
        ju = data.get('ju', 1)
        zhifu = data.get('zhifu')
        zhishi = data.get('zhishi')
        hour_branch = data.get('hourBranch')
        
        # Calculate chart
        now = datetime.now()
        params = qmdg_calc.calculate_qmdg_params(now)
        
        # Get Can Gio
        map_can_ngay = {"Giáp": 0, "Kỷ": 0, "Ất": 1, "Canh": 1, "Bính": 2, "Tân": 2, 
                        "Đinh": 3, "Nhâm": 3, "Mậu": 4, "Quý": 4}
        idx_start = map_can_ngay.get(params['can_ngay'], 0)
        idx_chi = CAN_CHI_Gio.index(hour_branch)
        can_gio_idx = (idx_start * 2 + idx_chi) % 10
        can_gio = CAN_10[can_gio_idx]
        
        # Calculate boards
        dia_can = an_bai_luc_nghi(ju, params['is_duong_don'])
        thien_ban, can_thien_ban, nhan_ban, than_ban, truc_phu_cung = lap_ban_qmdg(
            ju, zhifu, zhishi, can_gio, hour_branch, params['is_duong_don']
        )
        
        # Get special palaces
        khong_vong = tinh_khong_vong(can_gio, hour_branch)
        dich_ma = tinh_dich_ma(hour_branch)
        
        # Build palaces data
        palaces = []
        for cung_so in range(1, 10):
            palace_data = {
                "number": cung_so,
                "name": QUAI_TUONG.get(cung_so, 'N/A'),
                "element": CUNG_NGU_HANH.get(cung_so, 'N/A'),
                "star": thien_ban.get(cung_so, 'N/A'),
                "door": nhan_ban.get(cung_so, 'N/A'),
                "deity": than_ban.get(cung_so, 'N/A'),
                "stemHeaven": can_thien_ban.get(cung_so, 'N/A'),
                "stemEarth": dia_can.get(cung_so, 'N/A'),
                "isKongWang": cung_so in khong_vong,
                "isDiMa": cung_so == dich_ma,
                "auspiciousness": calculate_auspiciousness(cung_so, thien_ban, nhan_ban, than_ban)
            }
            palaces.append(palace_data)
        
        current_chart_data = {
            "ju": ju,
            "solarTerm": params['tiet_khi'],
            "isYang": params['is_duong_don'],
            "palaces": palaces,
            "thien_ban": thien_ban,
            "can_thien_ban": can_thien_ban,
            "nhan_ban": nhan_ban,
            "than_ban": than_ban,
            "dia_can": dia_can,
            "can_ngay": params['can_ngay'],
            "can_gio": can_gio
        }
        
        return jsonify(current_chart_data)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/mai-hoa', methods=['POST'])
def get_mai_hoa():
    data = request.json
    topic = data.get('topic', 'Tổng Quát')
    now = datetime.now()
    res = tinh_qua_theo_thoi_gian(now.year, now.month, now.day, now.hour)
    res['interpretation'] = giai_qua(res, topic)
    return jsonify(res)

@app.route('/api/luc-hao', methods=['POST'])
def get_luc_hao():
    data = request.json
    topic = data.get('topic', 'Tổng Quát')
    now = datetime.now()
    res = lap_qua_luc_hao(now.year, now.month, now.day, now.hour, topic)
    return jsonify(res)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        topic = data.get('topic', 'Tổng Quát')
        chu_idx = data.get('chu_idx')
        khach_idx = data.get('khach_idx')
        
        if not current_chart_data:
            return jsonify({"error": "Vui lòng lập bàn trước"}), 400
            
        def get_p_info(idx):
            p = next(p for p in current_chart_data['palaces'] if p['number'] == idx)
            return {
                'so': idx, 'ten': p['name'], 'hanh': p['element'],
                'sao': p['star'], 'cua': p['door'], 'than': p['deity'],
                'can_thien': p['stemHeaven'], 'can_dia': p['stemEarth']
            }
            
        chu = get_p_info(chu_idx)
        khach = get_p_info(khach_idx)
        now = datetime.now()
        
        res_9pp = phan_tich_sieu_chi_tiet_chu_de(topic, chu, khach, now)
        mqh = tinh_ngu_hanh_sinh_khac(chu['hanh'], khach['hanh'])
        res_lien_mach = tao_phan_tich_lien_mach(topic, chu, khach, now, res_9pp, mqh)
        
        return jsonify({**res_9pp, "lien_mach": res_lien_mach})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def calculate_auspiciousness(cung_so, thien_ban, nhan_ban, than_ban):
    """Calculate auspiciousness level (1-10)"""
    score = 5  # Base score
    
    # Check star
    star = thien_ban.get(cung_so, '')
    if star in ['Thiên Tâm', 'Thiên Phụ', 'Thiên Anh']:
        score += 2
    elif star in ['Thiên Bồng', 'Thiên Trụ', 'Thiên Nhuế']:
        score -= 2
    
    # Check door
    door = nhan_ban.get(cung_so, '')
    door_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_MON"].get(door + " Môn", {})
    cat_hung = door_data.get("Cát_Hung", "Bình")
    if cat_hung == "Đại Cát":
        score += 3
    elif cat_hung == "Cát":
        score += 1
    elif cat_hung == "Hung":
        score -= 1
    elif cat_hung == "Đại Hung":
        score -= 3
    
    return max(1, min(10, score))

@app.route('/api/palace/<int:palace_id>')
def get_palace_detail(palace_id):
    """Get detailed information for a palace"""
    try:
        if not current_chart_data:
            return jsonify({"error": "No chart calculated"}), 400
        
        palace = next((p for p in current_chart_data['palaces'] if p['number'] == palace_id), None)
        if not palace:
            return jsonify({"error": "Palace not found"}), 404
        
        # Get detailed descriptions
        star_data = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['CUU_TINH'].get(palace['star'], {})
        door_data = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['BAT_MON'].get(palace['door'] + ' Môn', {})
        deity_data = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['BAT_THAN'].get(palace['deity'], {})
        stem_data = KY_MON_DATA['CAN_CHI_LUAN_GIAI'].get(palace['stemHeaven'], {})
        
        # Get stem combination
        cach_cuc_key = palace['stemHeaven'] + palace['stemEarth']
        combination_data = KY_MON_DATA['TRUCTU_TRANH'].get(cach_cuc_key, {})
        
        # Calculate element interaction
        hanh_cung = palace['element']
        hanh_sao = star_data.get('Hành', 'N/A')
        interaction = tinh_ngu_hanh_sinh_khac(hanh_sao, hanh_cung)
        
        detail = {
            **palace,
            "starDescription": star_data.get('Tính_Chất', 'N/A'),
            "doorDescription": door_data.get('Luận_Đoán', 'N/A'),
            "doorAuspiciousness": door_data.get('Cát_Hung', 'Bình'),
            "deityDescription": deity_data.get('Tính_Chất', 'N/A'),
            "stemHeavenDescription": stem_data.get('Tính_Chất', 'N/A'),
            "elementInteraction": interaction,
            "stemCombination": f"{palace['stemHeaven']}/{palace['stemEarth']}",
            "combinationAuspiciousness": combination_data.get('Cát_Hung', 'Bình'),
            "combinationDescription": combination_data.get('Luận_Giải', 'Chưa có nội dung.'),
            "advice": generate_advice(palace, door_data, star_data)
        }
        
        return jsonify(detail)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_advice(palace, door_data, star_data):
    """Generate advice based on palace data"""
    advice = []
    
    # Based on door
    cat_hung = door_data.get('Cát_Hung', 'Bình')
    if cat_hung in ['Đại Cát', 'Cát']:
        advice.append("Đây là thời điểm tốt để hành động.")
    elif cat_hung in ['Hung', 'Đại Hung']:
        advice.append("Nên thận trọng, tránh các quyết định quan trọng.")
    
    # Based on star
    star_tinh_chat = star_data.get('Tính_Chất', '')
    if 'tài lộc' in star_tinh_chat.lower():
        advice.append("Có lợi cho việc cầu tài, kinh doanh.")
    if 'học vấn' in star_tinh_chat.lower() or 'trí tuệ' in star_tinh_chat.lower():
        advice.append("Tốt cho học tập, nghiên cứu.")
    
    return " ".join(advice) if advice else "Hãy cân nhắc kỹ trước khi hành động."

@app.route('/api/palace-topic-analysis/<int:palace_id>/<topic>')
def get_palace_topic_analysis(palace_id, topic):
    """Get detailed palace analysis for specific topic"""
    try:
        if not current_chart_data:
            return jsonify({"error": "No chart calculated"}), 400
        
        palace = next((p for p in current_chart_data['palaces'] if p['number'] == palace_id), None)
        if not palace:
            return jsonify({"error": "Palace not found"}), 404
        
        # Get basic palace info
        star_data = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['CUU_TINH'].get(palace['star'], {})
        door_data = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['BAT_MON'].get(palace['door'] + ' Môn', {})
        deity_data = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['BAT_THAN'].get(palace['deity'], {})
        
        # Get topic-specific Dụng Thần
        topic_data = TOPIC_INTERPRETATIONS.get(topic, {})
        dung_than_list = topic_data.get("Dụng_Thần", [])
        
        # Check if this palace contains Dụng Thần
        co_dung_than = []
        for dt in dung_than_list:
            if dt in [palace['star'], palace['door'], palace['deity'], palace['stemHeaven'], palace['stemEarth']]:
                co_dung_than.append(dt)
        
        # Build detailed analysis
        analysis = {
            **palace,
            "topic": topic,
            "dungThan": dung_than_list,
            "hasDungThan": len(co_dung_than) > 0,
            "dungThanFound": co_dung_than,
            "starDescription": star_data.get('Tính_Chất', 'N/A'),
            "doorDescription": door_data.get('Luận_Đoán', 'N/A'),
            "deityDescription": deity_data.get('Tính_Chất', 'N/A'),
            "topicInterpretation": topic_data.get("Giải_Thích", "Chưa có giải thích chi tiết cho chủ đề này."),
            "advice": generate_topic_advice(palace, topic, door_data, star_data, co_dung_than)
        }
        
        return jsonify(analysis)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_topic_advice(palace, topic, door_data, star_data, dung_than_found):
    """Generate topic-specific advice"""
    advice = []
    
    # If palace has Dụng Thần
    if dung_than_found:
        advice.append(f"✅ Cung này chứa Dụng Thần: {', '.join(dung_than_found)}. Đây là cung QUAN TRỌNG cho chủ đề '{topic}'.")
    else:
        advice.append(f"⚠️ Cung này không chứa Dụng Thần chính. Ảnh hưởng gián tiếp đến '{topic}'.")
    
    # Topic-specific advice
    if topic in ["Kinh Doanh", "Công Việc", "Sự Nghiệp"]:
        cat_hung = door_data.get('Cát_Hung', 'Bình')
        if cat_hung in ['Đại Cát', 'Cát']:
            advice.append("💼 Tốt cho kinh doanh, mở rộng, đầu tư.")
        else:
            advice.append("💼 Nên thận trọng trong các quyết định kinh doanh lớn.")
    
    elif topic in ["Hôn Nhân", "Tình Cảm"]:
        if palace['door'] in ['Sinh', 'Khai']:
            advice.append("💕 Tốt cho hôn nhân, tình cảm hòa hợp.")
        elif palace['door'] in ['Thương', 'Tử']:
            advice.append("💔 Cần chú ý xung đột, mâu thuẫn trong quan hệ.")
    
    elif topic in ["Kiện Tụng", "Tranh Chấp"]:
        if palace['star'] in ['Thiên Anh', 'Thiên Xung']:
            advice.append("⚖️ Có lợi thế trong tranh chấp, kiện tụng.")
        else:
            advice.append("⚖️ Nên tìm cách hòa giải thay vì đối đầu.")
    
    return " ".join(advice)

@app.route('/api/compare', methods=['POST'])
def compare_palaces():
    """Compare two palaces"""
    try:
        if not current_chart_data:
            return jsonify({"error": "No chart calculated"}), 400
        
        data = request.json
        host_id = data.get('host')
        guest_id = data.get('guest')
        
        host = next((p for p in current_chart_data['palaces'] if p['number'] == host_id), None)
        guest = next((p for p in current_chart_data['palaces'] if p['number'] == guest_id), None)
        
        if not host or not guest:
            return jsonify({"error": "Palace not found"}), 404
        
        # Calculate interaction
        interaction = tinh_ngu_hanh_sinh_khac(host['element'], guest['element'])
        
        # Determine result
        if 'sinh' in interaction.lower() and host['element'] in interaction.split()[0]:
            result = "Chủ sinh Khách - Chủ mất lợi"
            host_strength = 40
            guest_strength = 60
        elif 'sinh' in interaction.lower():
            result = "Khách sinh Chủ - Chủ được lợi"
            host_strength = 60
            guest_strength = 40
        elif 'khắc' in interaction.lower() and host['element'] in interaction.split()[0]:
            result = "Chủ khắc Khách - Chủ thắng"
            host_strength = 70
            guest_strength = 30
        elif 'khắc' in interaction.lower():
            result = "Khách khắc Chủ - Khách thắng"
            host_strength = 30
            guest_strength = 70
        else:
            result = "Hòa - Ngang sức"
            host_strength = 50
            guest_strength = 50
        
        comparison = {
            "host": host,
            "guest": guest,
            "elementInteraction": interaction,
            "result": result,
            "interpretation": f"Ngũ hành {host['element']} và {guest['element']}: {interaction}",
            "hostStrength": host_strength,
            "guestStrength": guest_strength,
            "advice": "Dựa vào kết quả này để đưa ra chiến lược phù hợp."
        }
        
        return jsonify(comparison)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===== NEW API ENDPOINTS FOR FULL FEATURES =====

@app.route('/api/search-topics')
def search_topics():
    """Tìm kiếm chủ đề theo từ khóa"""
    try:
        query = request.args.get('q', '').strip().lower()
        
        if not query:
            # Return all topics
            return jsonify(sorted(list(TOPIC_INTERPRETATIONS.keys())))
        
        # Filter topics containing query
        filtered = [
            topic for topic in TOPIC_INTERPRETATIONS.keys()
            if query in topic.lower()
        ]
        
        return jsonify(sorted(filtered))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/dung-than/<topic>')
def get_dung_than(topic):
    """Lấy Dụng Thần chi tiết cho chủ đề (200+ database)"""
    try:
        result = {
            "topic": topic,
            "has_200_data": USE_200_TOPICS,
            "ky_mon": {},
            "mai_hoa": {},
            "luc_hao": {}
        }
        
        # Get from TOPIC_INTERPRETATIONS (basic)
        topic_data = TOPIC_INTERPRETATIONS.get(topic, {})
        result["dung_than_basic"] = topic_data.get("Dụng_Thần", [])
        result["luan_giai"] = topic_data.get("Luận_Giải_Gợi_Ý", "")
        
        # Get from 200+ database if available
        if USE_200_TOPICS:
            dt_data = lay_dung_than_200(topic)
            if dt_data:
                result["ky_mon"] = dt_data.get("ky_mon", {})
                result["mai_hoa"] = dt_data.get("mai_hoa", {})
                result["luc_hao"] = dt_data.get("luc_hao", {})
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/multi-layer-analysis', methods=['POST'])
def multi_layer_analysis():
    """Phân tích đa tầng với Lục Thân"""
    try:
        if not USE_MULTI_LAYER:
            return jsonify({"error": "Module phân tích đa tầng chưa được cài đặt"}), 400
        
        data = request.json
        topic = data.get('topic', 'Tổng Quát')
        luc_than = data.get('luc_than', 'Bản thân')
        palace_num = data.get('palace', 5)
        
        # Get palace info
        if not current_chart_data:
            return jsonify({"error": "Vui lòng lập bàn trước"}), 400
        
        palace = next((p for p in current_chart_data['palaces'] if p['number'] == palace_num), None)
        if not palace:
            return jsonify({"error": "Không tìm thấy cung"}), 404
        
        # Perform multi-layer analysis
        palace_info = {
            'so': palace_num,
            'ten': palace['name'],
            'hanh': palace['element'],
            'sao': palace['star'],
            'cua': palace['door'],
            'than': palace['deity'],
            'can_thien': palace['stemHeaven'],
            'can_dia': palace['stemEarth']
        }
        
        analysis = phan_tich_toan_dien(
            topic=topic,
            cung_info=palace_info,
            doi_tuong=luc_than
        )
        
        return jsonify(analysis)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/compare-detailed', methods=['POST'])
def compare_detailed():
    """So sánh 2 cung chi tiết (như desktop app)"""
    try:
        if not USE_DETAILED_ANALYSIS:
            return jsonify({"error": "Module so sánh chi tiết chưa được cài đặt"}), 400
        
        data = request.json
        palace1_num = data.get('palace1')
        palace2_num = data.get('palace2')
        topic = data.get('topic', 'Tổng Quát')
        
        if not current_chart_data:
            return jsonify({"error": "Vui lòng lập bàn trước"}), 400
        
        # Get palace info
        def get_palace_info(num):
            p = next((p for p in current_chart_data['palaces'] if p['number'] == num), None)
            if not p:
                return None
            return {
                'so': num,
                'ten': p['name'],
                'hanh': p['element'],
                'sao': p['star'],
                'cua': p['door'],
                'than': p['deity'],
                'can_thien': p['stemHeaven'],
                'can_dia': p['stemEarth']
            }
        
        chu = get_palace_info(palace1_num)
        khach = get_palace_info(palace2_num)
        
        if not chu or not khach:
            return jsonify({"error": "Không tìm thấy cung"}), 404
        
        # Perform detailed comparison
        comparison = so_sanh_chi_tiet_chu_khach(
            chu_de=topic,
            cung_chu=chu,
            cung_khach=khach
        )
        
        return jsonify(comparison)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===== SERVER CONTROL =====

def open_browser():
    """Open browser after server starts"""
    import time
    time.sleep(2)  # Wait for server to start
    webbrowser.open('http://localhost:5000')

def get_local_ip():
    """Lấy địa chỉ IP của máy tính trong mạng nội bộ"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def run_web_server(port=5000, open_browser_flag=True):
    """Run Flask web server"""
    if open_browser_flag:
        threading.Thread(target=open_browser, daemon=True).start()
    
    local_ip = get_local_ip()
    print(f"""
    ╔══════════════════════════════════════════════════════════╗
    ║   🔮 Kỳ Môn Độn Giáp Web Server                         ║
    ║                                                          ║
    ║   1. Truy cập trên máy tính: http://localhost:{port}    ║
    ║   2. Truy cập qua Wi-Fi:     http://{local_ip}:{port}   ║
    ║                                                          ║
    ║   📢 ĐỂ DÙNG 4G (INTERNET):                              ║
    ║   - Chạy file 'CAI_DAT_TOKEN.bat' (nếu chưa làm)         ║
    ║   - Chạy file 'MO_CONG_INTERNET.bat'                     ║
    ║   - Copy link 'Forwarding' (https://...) vao dien thoai  ║
    ║                                                          ║
    ║   ⚠️ LƯU Ý: Nếu điện thoại hiện trang Ngrok, hãy tìm     ║
    ║   và nhấn nút 'Visit Site' để vào ứng dụng.              ║
    ║                                                          ║
    ║   Nhấn Ctrl+C để dừng server                            ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    try:
        app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
    except Exception as e:
        print(f"❌ LỖI KHỞI CHẠY: {e}")
        input("Nhấn Enter để đóng cửa sổ...")

if __name__ == '__main__':
    run_web_server()
