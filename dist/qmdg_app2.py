import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import threading
from datetime import datetime
import json
import os
import sys
from PIL import Image, ImageTk

# ======================================================================
# PHẦN 1: IMPORT DỮ LIỆU VÀ LOGIC
# ======================================================================
try:
    from qmdg_data import *
    from qmdg_data import load_custom_data, save_custom_data
    from qmdg_data import KY_MON_DATA, TOPIC_INTERPRETATIONS
    
    # NEW: Import module tính toán thời gian thực
    import qmdg_calc
    
    # NEW: Import tất cả chủ đề và phân tích chi tiết
    # from qmdg_all_topics import ALL_QMDG_TOPICS # Đã chuyển sang TOPIC_INTERPRETATIONS
    from qmdg_detailed_analysis import phan_tich_chi_tiet_cung, so_sanh_chi_tiet_chu_khach
    
    # NEW: Import siêu hệ thống dự đoán (Đã được hợp nhất trong super_detailed_analysis)
    # from sieu_du_doan_module import SieuDuDoan 
    
    # NEW: Import phân tích siêu chi tiết 4 PHƯƠNG PHÁP CHUẨN (KM, LN, TA, BZ)
    from super_detailed_analysis import phan_tich_sieu_chi_tiet_chu_de, tao_phan_tich_lien_mach
    
    # NEW: Import module tổng hợp tri thức từ tất cả nguồn (Excel, JSON, PDF)
    from integrated_knowledge_base import (
        get_comprehensive_palace_info, 
        format_info_for_display,
        get_qua_info,
        get_sao_info,
        get_mon_info,
        get_can_info
    )
    
    # NEW: Import module Mai Hoa Dịch Số - 64 Quẻ Kinh Dịch
    from mai_hoa_dich_so import tinh_qua_theo_thoi_gian, tinh_qua_ngau_nhien, giai_qua
    
    # NEW: Import module Lục Hào Kinh Dịch - Hệ thống hoàn chỉnh
    from luc_hao_kinh_dich import lap_qua_luc_hao
    
    # NEW: Import module vẽ quẻ NÂNG CẤP - Gạch âm dương TO, RÕ NÉT
    try:
        from ve_qua_am_duong_enhanced import (
            tao_hien_thi_qua_chi_tiet_to,
            tao_hien_thi_3_qua_to,
            ve_hao_to,
            xac_dinh_hao_am_duong
        )
        USE_ENHANCED_VISUAL = True
    except ImportError:
        from ve_qua_am_duong import (
            tao_hien_thi_qua_chi_tiet,
            tao_hien_thi_3_qua
        )
        USE_ENHANCED_VISUAL = False
    
    # NEW: Import module Tổng hợp 3 hệ thống
    try:
        from tong_hop_3_he_thong import tong_hop_3_he_thong, tao_bao_cao_tong_hop
        HAS_TONG_HOP_3 = True
    except ImportError:
        HAS_TONG_HOP_3 = False
    
    # NEW: Import module Dụng Thần nâng cấp với so sánh tác động
    # Ưu tiên: Sử dụng TOPIC_INTERPRETATIONS với 1059 chủ đề
    try:
        from dung_than_200_chu_de_day_du import (
            DUNG_THAN_200_CHU_DE,
            hien_thi_dung_than_200,
            lay_dung_than_200
        )
        USE_200_TOPICS = True
        print("✅ Đã tải database Dụng Thần 200+ chủ đề")
    except ImportError:
        USE_200_TOPICS = False
        try:
            from dung_than_enhanced import (
                DUNG_THAN_DATABASE,
                hien_thi_dung_than_chi_tiet,
                so_sanh_tac_dong_dung_than
            )
            USE_ENHANCED_DUNG_THAN = True
            print("⚠️ Dùng database Enhanced (5 chủ đề)")
        except ImportError:
            from dung_than_chi_tiet_200_chu_de import hien_thi_dung_than
            USE_ENHANCED_DUNG_THAN = False
            print("⚠️ Dùng database cũ (3 chủ đề)")
    
    # NEW: Import module Phân Tích Đa Tầng - Dụng Thần làm trung tâm
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
        print("✅ Đã tải module Phân Tích Đa Tầng")
    except ImportError as e:
        USE_MULTI_LAYER_ANALYSIS = False
        print(f"⚠️ Không tải được module Phân Tích Đa Tầng: {e}")

    CAN_10 = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    SAO_9 = list(KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["CUU_TINH"].keys())
    THAN_8 = list(KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_THAN"].keys())
    CUA_8 = list(BAT_MON_CO_DINH_DISPLAY.keys())

except ImportError as e:
    messagebox.showerror("Lỗi Liên Kết File", f"Thiếu file dữ liệu hoặc module: {e}")
    exit()

# ======================================================================
# PHẦN 1.5: HỆ THỐNG BẢO MẬT (LOGIN)
# ======================================================================

class LoginManager:
    def __init__(self, master):
        self.master = master
        self.master.title("🔐 Xác Thực Truy Cập - Kỳ Môn Độn Giáp")
        self.master.geometry("400x250")
        self.master.resizable(False, False)
        self.master.configure(bg="#2c3e50")

        # Căn giữa cửa sổ login
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - 200
        y = (screen_height // 2) - 125
        self.master.geometry(f"+{x}+{y}")

        self.create_widgets()

    def create_widgets(self):
        # Tiêu đề
        tk.Label(self.master, text="HỆ THỐNG BẢO MẬT", font=('Segoe UI', 14, 'bold'), 
                 bg="#2c3e50", fg="#f1c40f", pady=20).pack()

        tk.Label(self.master, text="Vui lòng nhập mật khẩu để sử dụng:", font=('Segoe UI', 10), 
                 bg="#2c3e50", fg="#ecf0f1").pack(pady=5)

        # Ô nhập mật khẩu
        self.password_entry = tk.Entry(self.master, show="*", font=('Segoe UI', 12), 
                                      justify='center', width=20, bd=3)
        self.password_entry.pack(pady=10)
        self.password_entry.focus_set()
        self.password_entry.bind('<Return>', lambda e: self.check_password())

        # Nút Đăng nhập
        btn_login = tk.Button(self.master, text="MỞ ỨNG DỤNG 🔑", command=self.check_password,
                             font=('Segoe UI', 10, 'bold'), bg='#27ae60', fg='white',
                             padx=20, pady=5, cursor='hand2', relief='raised')
        btn_login.pack(pady=15)

    def check_password(self):
        entered_password = self.password_entry.get()
        if entered_password == "1987":
            # Xóa cửa sổ login và mở ứng dụng chính
            for widget in self.master.winfo_children():
                widget.destroy()
            
            # Khởi tạo ứng dụng chính ngay trên root
            QMDG_App(self.master)
        else:
            messagebox.showerror("Lỗi Truy Cập", "Mật khẩu không chính xác!\nVui lòng liên hệ tác giả Vũ Việt Cường.")
            self.password_entry.delete(0, tk.END)

# ======================================================================
# PHẦN 2: LỚP ỨNG DỤNG QMDG_App (GUI)
# ======================================================================

class QMDG_App:
    def __init__(self, master):
        self.master = master
        
        self.master.state('zoomed') # Tự động phóng to cửa sổ khi khởi động
        
        # --- THIẾT LẬP ẢNH ĐẠI DIỆN & ICON ---
        self._setup_app_icon()
        
        # --- TẢI DỮ LIỆU TÙY CHỈNH ---
        self.custom_data = load_custom_data()
        self._merge_custom_data()
        
        # Dữ liệu điều hướng cung
        self.palace_list = [1, 8, 3, 4, 9, 2, 7, 6, 5] # Thứ tự di chuyển (vòng Lạc Thư)
        self.current_palace_nav_idx = -1
        self.palace_detail_window = None

        # --- Cấu hình Font (NÂNG CẤP - Lớn hơn, đẹp hơn) ---
        self.font_main = ('Segoe UI', 11, 'bold')
        self.font_cung_info = ('Segoe UI', 10, 'bold')          
        self.font_cung_so = ('Segoe UI', 16, 'bold')     
        self.font_can = ('Segoe UI', 15, 'bold')       
        self.font_than = ('Segoe UI', 12, 'bold', 'italic')
        self.font_tinh = ('Segoe UI', 14, 'bold')          
        self.font_mon_chay = ('Segoe UI', 13, 'bold')    
        self.font_mon_co_dinh = ('Segoe UI', 10, 'bold')          
        
        # Dữ liệu Bàn (Khởi tạo)
        self.is_duong_don = True # Mặc định
        self.can_gio = "Giáp"
        self.can_ngay = "Giáp" 
        self.can_thang = "Giáp"
        self.can_nam = "Giáp"
        self.dia_can = an_bai_luc_nghi(1, True) 
        self.thien_ban, self.can_thien_ban, self.nhan_ban, self.than_ban, self.truc_phu_cung_so = {}, {}, {}, {}, 0
        self.ket_qua_tranh = {}
        self.khong_vong_cung = []
        self.dich_ma_cung = None
        
        self.is_running = False 
        
        # Dữ liệu đã TÍNH TOÁN TRƯỚC
        self.danh_sach_giai_thich = {} 
        self.detail_window = None 
        self.data_input_window = None 
        self.cung_input_window = None 
        
        self.manual_cung_data = {} 

        # --- Tạo Giao Diện (NÂNG CẤP - Màu đẹp hơn) ---
        # Tạo Vùng Cuộn (Scrollable Area) cho toàn bộ ứng dụng để tránh mất cung dưới
        self.main_canvas = tk.Canvas(master, bg="#ecf0f1")
        self.main_scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_frame = tk.Frame(self.main_canvas, bg="#ecf0f1")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))
        )

        self.canvas_window = self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=self.main_scrollbar.set)

        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.main_scrollbar.pack(side="right", fill="y")
        
        # NEW: Đảm bảo frame bên trong luôn rộng bằng canvas để có thể căn giữa nội dung
        self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.itemconfig(self.canvas_window, width=e.width))

        # ======================================================================
        # ZOOM FUNCTIONALITY - Phóng to/Thu nhỏ toàn bộ giao diện
        # ======================================================================
        self.zoom_level = 1.0  # Mức zoom mặc định (100%)
        
        # Bind phím tắt zoom
        self.master.bind('<Control-plus>', lambda e: self.zoom_in())
        self.master.bind('<Control-equal>', lambda e: self.zoom_in())  # Ctrl + = (không cần Shift)
        self.master.bind('<Control-minus>', lambda e: self.zoom_out())
        self.master.bind('<Control-0>', lambda e: self.reset_zoom())


        # Header với gradient effect (Nâng cao chiều cao để chứa ảnh to)
        header_frame = tk.Frame(self.scrollable_frame, bg="#2c3e50", height=120)
        header_frame.pack(fill='x')

        # --- HIỂN THỊ ẢNH ĐẠI DIỆN & TÊN TÁC GIẢ BÊN PHẢI ---
        right_container = tk.Frame(header_frame, bg="#2c3e50")
        right_container.pack(side=tk.RIGHT, padx=30, pady=5)

        if hasattr(self, 'avatar_header_img'):
            # Text Tác giả (Chữ nổi, bóng)
            author_frame = tk.Frame(right_container, bg="#2c3e50")
            author_frame.pack(side=tk.LEFT, padx=15)
            
            # Hiệu ứng chữ bóng (Layer labels)
            tk.Label(author_frame, text="Tác giả", font=('Segoe UI', 10, 'italic'), 
                     bg="#2c3e50", fg="#bdc3c7").pack(anchor='e')
            
            # Chữ nổi "Vũ Việt Cường"
            lbl_name = tk.Label(author_frame, text="Vũ Việt Cường", 
                                font=('Segoe UI', 16, 'bold'), 
                                bg="#2c3e50", fg="#f1c40f", 
                                relief='raised', padx=10, pady=2)
            lbl_name.pack(anchor='e')

            self.label_avatar = tk.Label(right_container, image=self.avatar_header_img, 
                                         bg="#2c3e50", bd=2, relief='ridge')
            self.label_avatar.pack(side=tk.LEFT)

        header_label = tk.Label(header_frame, text="🔮 KỲ MÔN ĐỘN GIÁP 🔮", 
                               font=('Segoe UI', 24, 'bold'), 
                               bg="#2c3e50", fg="#ecf0f1", pady=35)
        header_label.pack(side=tk.LEFT, padx=(100, 50)) # Tăng padx trái để đẩy vào giữa hơn
        
        # ======================================================================
        # ZOOM CONTROLS - Nút điều khiển phóng to/thu nhỏ
        # ======================================================================
        zoom_frame = tk.Frame(header_frame, bg="#2c3e50")
        zoom_frame.pack(side=tk.LEFT, padx=20)
        
        tk.Label(zoom_frame, text="🔍 Zoom:", font=('Segoe UI', 9, 'bold'), 
                bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        
        self.btn_zoom_out = tk.Button(zoom_frame, text="−", font=('Segoe UI', 14, 'bold'),
                                      command=self.zoom_out, bg='#34495e', fg='white',
                                      width=3, cursor='hand2', relief='raised')
        self.btn_zoom_out.pack(side=tk.LEFT, padx=2)
        
        self.lbl_zoom_percent = tk.Label(zoom_frame, text="100%", font=('Segoe UI', 10, 'bold'),
                                         bg="#2c3e50", fg="#f1c40f", width=5, cursor='hand2')
        self.lbl_zoom_percent.pack(side=tk.LEFT, padx=2)
        self.lbl_zoom_percent.bind('<Button-1>', lambda e: self.reset_zoom())
        
        self.btn_zoom_in = tk.Button(zoom_frame, text="+", font=('Segoe UI', 14, 'bold'),
                                     command=self.zoom_in, bg='#34495e', fg='white',
                                     width=3, cursor='hand2', relief='raised')
        self.btn_zoom_in.pack(side=tk.LEFT, padx=2)

        
        self.frame_input = ttk.Frame(self.scrollable_frame, padding="15"); 
        self.frame_input.pack(anchor='center', padx=10, pady=10)
        
        # NEW: Tạo Frame chứa 3 nút chuyển đổi - Căn giữa
        self.frame_toggle = tk.Frame(self.scrollable_frame, bg="#34495e", pady=10)
        self.frame_toggle.pack(anchor='center', padx=10)
        
        # Button hiển thị Kỳ Môn
        self.btn_show_qimen = tk.Button(self.frame_toggle, text="🔮 BẢNG KỲ MÔN", 
                                        command=self.hien_thi_ky_mon,
                                        font=('Segoe UI', 10, 'bold'), bg='#2980b9', fg='white',
                                        relief='sunken', bd=4, padx=15, pady=10,
                                        cursor='hand2', activebackground='#2980b9')
        self.btn_show_qimen.pack(side=tk.LEFT, padx=10, expand=True)
        
        # Button hiển thị 64 Quẻ Mai Hoa
        self.btn_show_64qua = tk.Button(self.frame_toggle, text="📖 MAI HOA 64 QUẺ", 
                                        command=self.hien_thi_64_qua,
                                        font=('Segoe UI', 10, 'bold'), bg='#e74c3c', fg='white',
                                        relief='raised', bd=4, padx=15, pady=10,
                                        cursor='hand2', activebackground='#c0392b')
        self.btn_show_64qua.pack(side=tk.LEFT, padx=10, expand=True)
        
        # Button hiển thị Lục Hào Kinh Dịch
        self.btn_show_luchao = tk.Button(self.frame_toggle, text="☯️ LỤC HÀO KINH DỊCH", 
                                         command=self.hien_thi_luc_hao,
                                         font=('Segoe UI', 10, 'bold'), bg='#16a085', fg='white',
                                         relief='raised', bd=4, padx=15, pady=10,
                                         cursor='hand2', activebackground='#138d75')
        self.btn_show_luchao.pack(side=tk.LEFT, padx=10, expand=True)
        
        # Frame cho Kỳ Môn (sẽ ẩn/hiện) - Căn giữa
        self.frame_grid = tk.Frame(self.scrollable_frame, bg="#ecf0f1", padx=20, pady=20); 
        self.frame_grid.pack(anchor='center', padx=10, pady=10) 
        
        self.tao_input_fields()
        self.tao_grid_layout()
        
        # NEW: Tạo Frame Mai Hoa Dịch Số - 64 Quẻ Kinh Dịch (ẩn ban đầu)
        self.tao_mai_hoa_frame()
        self.frame_mai_hoa.pack_forget()  # Ẩn frame 64 quẻ ban đầu
        
        # NEW: Tạo Frame Lục Hào Kinh Dịch (ẩn ban đầu)
        self.tao_luc_hao_frame()
        self.frame_luc_hao.pack_forget()  # Ẩn frame Lục Hào ban đầu

        # Tự động cập nhật
        self.cap_nhat_thoi_gian_thuc()
        self.lap_va_hien_thi_ban(is_default=True)
        self._cap_nhat_chu_de_toan_cuc() # Khởi tạo Dụng Thần info
        self.master.after(60000, self.auto_reload_time)

    def _setup_app_icon(self):
        """Tải ảnh đại diện và thiết lập Icon cho toàn bộ ứng dụng."""
        img_name = "tải xuống (1).jpg"
        # Thử nhiều đường dẫn để tìm ảnh (dev và build)
        paths_to_try = [
            os.path.join(os.getcwd(), "dist", img_name),
            os.path.join(os.getcwd(), img_name),
        ]
        
        if hasattr(sys, '_MEIPASS'):
            paths_to_try.append(os.path.join(sys._MEIPASS, img_name))

        img_path = None
        for p in paths_to_try:
            if os.path.exists(p):
                img_path = p
                break

        if img_path:
            try:
                # Load ảnh gốc
                self.pil_img = Image.open(img_path)
                
                # Setup avatar cho Header (100x100) - PHÓNG TO THEO YÊU CẦU
                header_pil = self.pil_img.resize((100, 100), Image.Resampling.LANCZOS)
                self.avatar_header_img = ImageTk.PhotoImage(header_pil)
                
                # Biểu tượng icon nhỏ (giữ nguyên)
                icon_pil = self.pil_img.resize((32, 32), Image.Resampling.LANCZOS)
                self.app_icon = ImageTk.PhotoImage(icon_pil)
                self.master.iconphoto(False, self.app_icon)
                
                # Dự phòng cho biến cũ nếu có dùng ở nơi khác
                self.avatar_img = self.avatar_header_img 
                
                print(f"✅ Đã thiết lập ảnh đại diện: {img_path}")
            except Exception as e:
                print(f"Lỗi thiết lập icon: {e}")
    
    def _merge_custom_data(self):
        global KY_MON_DATA
        if not self.custom_data: return
        custom_tranh = self.custom_data.get("TRUCTU_TRANH", {})
        if custom_tranh:
            KY_MON_DATA["TRUCTU_TRANH"].update(custom_tranh)

    def _get_all_can_pairs(self):
        can_list_non_giap = [c for c in CAN_10 if c != "Giáp"]
        all_pairs = []
        for can_thien in can_list_non_giap:
            for can_dia in can_list_non_giap:
                key_lien_nhau = can_thien + can_dia
                display_format = f"{can_thien}/{can_dia}"
                all_pairs.append((key_lien_nhau, display_format))
        return all_pairs

    def auto_reload_time(self):
        current_dia_chi_gio_combo = self.combo_dia_chi.get()
        now = datetime.now()
        new_dia_chi_gio = tinh_dia_chi_gio(now.hour) 
        
        self.cap_nhat_thoi_gian_thuc() 

        if new_dia_chi_gio != current_dia_chi_gio_combo:
            # Tự động lập lại bàn khi đổi giờ (Chi Giờ thay đổi)
            self.lap_va_hien_thi_ban(is_default=False)
            # Thông báo nhỏ (tùy chọn, có thể bỏ qua để không làm phiền)
            # print(f"Đã tự động cập nhật sang giờ {new_dia_chi_gio}")
        
        self.master.after(10000, self.auto_reload_time) # Check mỗi 10s để chính xác hơn

    def cap_nhat_thoi_gian_thuc(self):
        now = datetime.now()
        current_date_time_str = now.strftime("%H:%M - %d/%m/%Y")
        
        # NEW: Sử dụng qmdg_calc để tính toán thông số
        try:
            params = qmdg_calc.calculate_qmdg_params(now)
            
            # Cập nhật GUI
            self.entry_datetime.config(state=tk.NORMAL)
            self.entry_datetime.delete(0, tk.END)
            self.entry_datetime.insert(0, current_date_time_str)
            self.entry_datetime.config(state='readonly') 

            self.entry_cuc.delete(0, tk.END)
            self.entry_cuc.insert(0, str(params['cuc']))
            
            self.combo_truc_phu.set(params['truc_phu'])
            self.combo_truc_su.set(params['truc_su'])
            self.combo_dia_chi.set(params['chi_gio'])
            
            self.is_duong_don = params.get('is_duong_don', True)
            can_chi_str = f"Giờ {params['can_gio']} {params['chi_gio']} | Ngày {params['can_ngay']} {params['chi_ngay']} | Tháng {params['can_thang']} {params['chi_thang']} | Năm {params['can_nam']} {params['chi_nam']}"
            self.lbl_can_chi_full.config(text=can_chi_str)
            
            self.master.title(f"🔮 Bàn Cung Kỳ Môn Độn Giáp - {params['tiet_khi']} - Cục {params['cuc']} ({'Dương' if self.is_duong_don else 'Âm'} Độn) 🔮")
            
        except Exception as e:
            print(f"Lỗi tính toán thời gian thực: {e}")

    def tao_input_fields(self):
        catinh_keys = list(KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["CUU_TINH"].keys())
             
        tk.Label(self.frame_input, text="Giờ/Ngày Hiện Tại:", font=self.font_main).grid(row=0, column=0, padx=5, pady=2, sticky='w')
        self.entry_datetime = tk.Entry(self.frame_input, width=15, state='readonly', fg='blue', font=self.font_cung_info); self.entry_datetime.grid(row=0, column=1, padx=5, pady=2, sticky='w')
        tk.Label(self.frame_input, text="Cục (1-18):", font=self.font_main).grid(row=0, column=2, padx=5, pady=2, sticky='w')
        self.entry_cuc = tk.Entry(self.frame_input, width=5, font=self.font_cung_info); self.entry_cuc.grid(row=0, column=3, padx=5, pady=2, sticky='w')
        
        tk.Label(self.frame_input, text="Sao Trực Phù:", font=self.font_main).grid(row=1, column=0, padx=5, pady=2, sticky='w')
        self.combo_truc_phu = ttk.Combobox(self.frame_input, values=catinh_keys, width=15, state='readonly', font=self.font_cung_info); self.combo_truc_phu.grid(row=1, column=1, padx=5, pady=2, sticky='w')
        
        tk.Label(self.frame_input, text="Cửa Trực Sử:", font=self.font_main).grid(row=1, column=2, padx=5, pady=2, sticky='w')
        self.combo_truc_su = ttk.Combobox(self.frame_input, values=list(BAT_MON_CO_DINH_DISPLAY.keys()), width=5, state='readonly', font=self.font_cung_info); self.combo_truc_su.grid(row=1, column=3, padx=5, pady=2, sticky='w')

        tk.Label(self.frame_input, text="Địa Chi Giờ:", font=self.font_main).grid(row=2, column=0, padx=5, pady=2, sticky='w')
        self.combo_dia_chi = ttk.Combobox(self.frame_input, values=CAN_CHI_Gio, width=10, state='readonly', font=self.font_cung_info); self.combo_dia_chi.grid(row=2, column=1, padx=5, pady=2, sticky='w')

        self.button_lap_ban = ttk.Button(self.frame_input, text="Lập Bàn 🔮", command=lambda: self.lap_va_hien_thi_ban(is_default=False))
        self.button_lap_ban.grid(row=0, column=4, rowspan=2, padx=15, pady=2, sticky='ns')
        self.button_tai_lai = ttk.Button(self.frame_input, text="Tải Giờ Thực 🔄", command=self.tai_lai_gio_va_lap_ban)
        self.button_tai_lai.grid(row=2, column=4, padx=15, pady=2, sticky='s')
        
        # Row 3: Lịch Âm (Can Chi)
        tk.Label(self.frame_input, text="Âm Lịch (Can Chi):", font=self.font_main).grid(row=3, column=0, padx=5, pady=2, sticky='w')
        self.lbl_can_chi_full = tk.Label(self.frame_input, text="Đang tính toán...", font=self.font_main, fg='#d35400')
        self.lbl_can_chi_full.grid(row=3, column=1, columnspan=4, padx=5, pady=2, sticky='w')

        # Hàng 4: Nhóm nút điều khiển Dữ liệu & So sánh
        frame_data_btns = tk.Frame(self.frame_input)
        frame_data_btns.grid(row=4, column=0, columnspan=5, pady=5, sticky='w')

        self.button_cap_nhat_data = ttk.Button(frame_data_btns, text="Cập Nhật Dữ Liệu Luận Giải ✍️", command=self._mo_cua_so_nhap_lieu)
        self.button_cap_nhat_data.pack(side=tk.LEFT, padx=2)
        
        self.button_cap_nhat_cung = ttk.Button(frame_data_btns, text="Sửa Cung Thủ Công ✏️", command=self._mo_cua_so_nhap_lieu_cung_thuc_te)
        self.button_cap_nhat_cung.pack(side=tk.LEFT, padx=2)

        self.button_so_sanh = ttk.Button(frame_data_btns, text="So Sánh 2 Cung ⚖️", command=self._mo_cua_so_so_sanh)
        self.button_so_sanh.pack(side=tk.LEFT, padx=2)

        self.button_xem_chu_de = ttk.Button(frame_data_btns, text="Xem Chi Tiết 📖", command=lambda: self._hien_thi_luan_giai_chu_de(None))
        self.button_xem_chu_de.pack(side=tk.LEFT, padx=2)

        # NEW: Nút di chuyển lên xuống 9 cung
        self.btn_prev_palace = ttk.Button(frame_data_btns, text="▲ Cung Trước", width=12, command=lambda: self._navigate_palace(-1))
        self.btn_prev_palace.pack(side=tk.LEFT, padx=2)
        
        self.btn_next_palace = ttk.Button(frame_data_btns, text="▼ Cung Sau", width=12, command=lambda: self._navigate_palace(1))
        self.btn_next_palace.pack(side=tk.LEFT, padx=2)
        
        # Hàng 5: CHỦ ĐỀ CHÍNH - Điều khiển toàn bộ ứng dụng
        frame_chu_de = tk.Frame(self.frame_input, bg='#f4f6f7', pady=5)
        frame_chu_de.grid(row=5, column=0, columnspan=5, pady=5, sticky='ew')
        
        tk.Label(frame_chu_de, text="🎯 CHỦ ĐỀ CHÍNH:", font=('Segoe UI', 11, 'bold'), fg='#e74c3c', bg='#f4f6f7').pack(side=tk.LEFT, padx=5)
        
        
        # Lấy TẤT CẢ 1059 chủ đề từ TOPIC_INTERPRETATIONS
        self.all_topics_full = sorted(list(TOPIC_INTERPRETATIONS.keys()))
        print(f"Tổng số chủ đề: {len(self.all_topics_full)}")  # Debug: hiển thị số lượng topics
        
        
        # Ô tìm kiếm chủ đề
        tk.Label(frame_chu_de, text="🔍 Tìm:", font=('Segoe UI', 9), bg='#f4f6f7').pack(side=tk.LEFT, padx=(10, 2))
        
        self.entry_tim_chu_de = tk.Entry(frame_chu_de, width=20, font=('Segoe UI', 9))
        self.entry_tim_chu_de.pack(side=tk.LEFT, padx=2)
        self.entry_tim_chu_de.bind('<Return>', lambda e: self._thuc_hien_tim_kiem_manual())
        
        btn_tim = ttk.Button(frame_chu_de, text="🔍", width=3, command=self._thuc_hien_tim_kiem_manual)
        btn_tim.pack(side=tk.LEFT, padx=2)
        
        self.combo_chu_de_chinh = ttk.Combobox(frame_chu_de, values=self.all_topics_full, width=35, state='readonly', font=('Segoe UI', 10, 'bold'))
        self.combo_chu_de_chinh.pack(side=tk.LEFT, padx=5)
        self.combo_chu_de_chinh.set("Tổng Quát")
        self.combo_chu_de_chinh.bind("<<ComboboxSelected>>", self._cap_nhat_chu_de_toan_cuc)
        
        btn_xoa_tim = ttk.Button(frame_chu_de, text="✖", width=3, command=self._xoa_tim_kiem_chu_de)
        btn_xoa_tim.pack(side=tk.LEFT, padx=2)
        
        self.chu_de_hien_tai = "Tổng Quát"
        
        # NEW: Hàng 5.5 - Dropdown chọn đối tượng (Lục Thân)
        if USE_MULTI_LAYER_ANALYSIS:
            frame_doi_tuong = tk.Frame(self.frame_input, bg='#e8f5e9', pady=5)
            frame_doi_tuong.grid(row=5, column=5, columnspan=2, pady=5, sticky='ew', padx=(10, 0))
            
            tk.Label(frame_doi_tuong, text="🎯 Đối Tượng:", font=('Segoe UI', 10, 'bold'), 
                    fg='#2e7d32', bg='#e8f5e9').pack(side=tk.LEFT, padx=5)
            
            self.doi_tuong_var = tk.StringVar(value="Bản thân")
            doi_tuong_options = [
                "🧑 Bản thân",
                "👨‍👩‍👧 Anh chị em",
                "👴👵 Bố mẹ",
                "👶 Con cái",
                "🤝 Người ngoài (Quan)",
                "💰 Người ngoài (Tài)"
            ]
            
            self.combo_doi_tuong = ttk.Combobox(
                frame_doi_tuong,
                textvariable=self.doi_tuong_var,
                values=doi_tuong_options,
                state='readonly',
                width=20,
                font=('Segoe UI', 9)
            )
            self.combo_doi_tuong.pack(side=tk.LEFT, padx=5)
            self.combo_doi_tuong.bind('<<ComboboxSelected>>', self._cap_nhat_phan_tich_luc_than)
        else:
            # Nếu không có module, tạo biến mặc định
            self.doi_tuong_var = tk.StringVar(value="Bản thân")

        # Hàng 6: Panel hiển thị nhanh Dụng Thần
        self.lbl_frame_dt_quick = ttk.LabelFrame(self.frame_input, text="🎯 THÔNG TIN DỤNG THẦN (3 PHƯƠNG PHÁP)", padding="5")
        self.lbl_frame_dt_quick.grid(row=6, column=0, columnspan=5, sticky='ew', pady=5)
        
        self.text_dt_quick = tk.Text(self.lbl_frame_dt_quick, height=4, font=('Segoe UI', 10), wrap=tk.WORD, bg='#fdfefe')
        self.text_dt_quick.pack(side=tk.LEFT, fill='x', expand=True)
        
        sb_dt = tk.Scrollbar(self.lbl_frame_dt_quick, command=self.text_dt_quick.yview)
        sb_dt.pack(side=tk.RIGHT, fill='y')
        self.text_dt_quick.config(yscrollcommand=sb_dt.set)
        
        self.text_dt_quick.insert('1.0', "Chọn chủ đề bên trên để xem Dụng Thần cho Kỳ Môn, Mai Hoa và Lục Hào.")
        self.text_dt_quick.config(state=tk.DISABLED)
    
    def _thuc_hien_tim_kiem_manual(self):
        """Thực hiện tìm kiếm khi nhấn nút hoặc Enter"""
        tu_khoa = self.entry_tim_chu_de.get().strip()
        
        # Nếu rỗng, hiển thị tất cả
        if not tu_khoa:
            self.combo_chu_de_chinh['values'] = self.all_topics_full
            print("✅ Hiển thị tất cả chủ đề")
            return
        
        tu_khoa_lower = tu_khoa.lower()
        
        # Lọc các chủ đề chứa từ khóa
        ket_qua_tim = [
            chu_de for chu_de in self.all_topics_full 
            if tu_khoa_lower in chu_de.lower()
        ]
        
        # Cập nhật dropdown
        self.combo_chu_de_chinh['values'] = ket_qua_tim
        
        # Nếu chỉ có 1 kết quả, tự động chọn
        if len(ket_qua_tim) == 1:
            self.combo_chu_de_chinh.set(ket_qua_tim[0])
            print(f"✅ Tìm thấy 1 chủ đề: {ket_qua_tim[0]}")
        elif len(ket_qua_tim) > 0:
            print(f"🔍 Tìm thấy {len(ket_qua_tim)} chủ đề với từ khóa '{tu_khoa}'")
        else:
            print(f"⚠️ Không tìm thấy chủ đề nào với từ khóa '{tu_khoa}'")
    
    def _cap_nhat_phan_tich_luc_than(self, event=None):
        """Callback khi thay đổi đối tượng Lục Thân"""
        if USE_MULTI_LAYER_ANALYSIS:
            doi_tuong_full = self.doi_tuong_var.get()
            doi_tuong = doi_tuong_full.split(" ", 1)[1] if " " in doi_tuong_full else "Bản thân"
            print(f"✅ Đã chọn đối tượng: {doi_tuong}")
            # Phân tích sẽ được cập nhật khi so sánh
    
    def _cap_nhat_chu_de_toan_cuc(self, event=None):
        """Callback khi thay đổi chủ đề - Tự động cập nhật đối tượng Lục Thân"""
        chu_de_moi = self.combo_chu_de_chinh.get()
        self.chu_de_hien_tai = chu_de_moi
        print(f"✅ Đã chuyển sang chủ đề: {chu_de_moi}")
        
        # Tự động gợi ý đối tượng dựa trên chủ đề
        if USE_MULTI_LAYER_ANALYSIS:
            try:
                doi_tuong_goi_y = goi_y_doi_tuong_theo_chu_de(chu_de_moi)
                
                # Tìm option phù hợp trong dropdown
                for option in self.combo_doi_tuong['values']:
                    if doi_tuong_goi_y in option:
                        self.doi_tuong_var.set(option)
                        print(f"💡 Tự động chọn đối tượng: {doi_tuong_goi_y}")
                        break
            except Exception as e:
                print(f"⚠️ Lỗi tự động chọn đối tượng: {e}")
    
    
    
    
    
    def _xoa_tim_kiem_chu_de(self):
        """Xóa ô tìm kiếm và hiển thị lại tất cả chủ đề"""
        self.entry_tim_chu_de.delete(0, tk.END)
        self.combo_chu_de_chinh['values'] = self.all_topics_full
        print("✅ Đã xóa tìm kiếm, hiển thị tất cả chủ đề")
    
    def _hien_thi_dien_giai_cung_theo_chu_de(self, cung_so):
        """
        Hiển thị diễn giải cung theo chủ đề khi click vào cung trên lưới
        """
        # Lấy chủ đề hiện tại
        chu_de = self.chu_de_hien_tai
        
        # Lấy thông tin cung
        manual = self.manual_cung_data.get(cung_so, {})
        sao = manual.get('Sao', self.thien_ban.get(cung_so, 'N/A'))
        cua = manual.get('Cua', self.nhan_ban.get(cung_so, 'N/A'))
        than = manual.get('Than', self.than_ban.get(cung_so, 'N/A'))
        can_thien = manual.get('Can_Thien', self.can_thien_ban.get(cung_so, 'N/A'))
        can_dia = manual.get('Can_Dia', self.dia_can.get(cung_so, 'N/A'))
        hanh = CUNG_NGU_HANH.get(cung_so, 'N/A')
        
        # NEW: Tái sử dụng cửa sổ hiển thị để tránh mở quá nhiều cửa sổ khi di chuyển
        if self.palace_detail_window and self.palace_detail_window.winfo_exists():
            window = self.palace_detail_window
            for child in window.winfo_children(): child.destroy()
        else:
            window = tk.Toplevel(self.master)
            self.palace_detail_window = window
            
        window.title(f"Luận Đoán Cung {cung_so} - {QUAI_TUONG.get(cung_so, '')} - Chủ Đề: {chu_de}")
        window.geometry("900x700")
        
        # Frame chính với scrollbar
        main_frame = ttk.Frame(window)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(main_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget = tk.Text(main_frame, wrap=tk.WORD, font=('Segoe UI', 10), 
                             yscrollcommand=scrollbar.set)
        text_widget.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.config(command=text_widget.yview)
        
        # Tạo nội dung diễn giải
        noi_dung = []
        noi_dung.append("="*90)
        noi_dung.append(f"🔮 LUẬN ĐOÁN CUNG {cung_so} - {QUAI_TUONG.get(cung_so, '')}")
        noi_dung.append(f"📌 CHỦ ĐỀ: {chu_de}")
        noi_dung.append("="*90)
        noi_dung.append("")
        
        # PHẦN 1: Thông tin cơ bản
        noi_dung.append("📊 THÔNG TIN CUNG:")
        noi_dung.append(f"   • Cửu Tinh: {sao}")
        noi_dung.append(f"   • Bát Môn: {cua}")
        noi_dung.append(f"   • Bát Thần: {than}")
        noi_dung.append(f"   • Can Thiên: {can_thien}")
        noi_dung.append(f"   • Can Địa: {can_dia}")
        noi_dung.append(f"   • Ngũ Hành: {hanh}")
        noi_dung.append("")
        
        # PHẦN 2: Phân tích theo chủ đề
        noi_dung.append(f"🎯 PHÂN TÍCH THEO CHỦ ĐỀ '{chu_de}':")
        noi_dung.append("")
        
        # NEW: Tích hợp Dụng Thần chi tiết từ database 200+
        if USE_200_TOPICS:
            dt_data = lay_dung_than_200(chu_de)
            if dt_data and 'ky_mon' in dt_data:
                km = dt_data['ky_mon']
                noi_dung.append("🔮 DỤNG THẦN KỲ MÔN CHI TIẾT (TỪ DATABASE 200+):")
                noi_dung.append(f"   • Dụng Thần: {km.get('dung_than', 'N/A')}")
                noi_dung.append(f"   • Giải thích: {km.get('giai_thich', 'N/A')}")
                noi_dung.append(f"   • Cách xem: {km.get('cach_xem', 'N/A')}")
                if 'vi_du' in km: noi_dung.append(f"   • Ví dụ: {km['vi_du']}")
                noi_dung.append("-" * 45)
                noi_dung.append("")

        # Lấy Dụng Thần của chủ đề
        topic_data = TOPIC_INTERPRETATIONS.get(chu_de, {})
        dung_than_list = topic_data.get("Dụng_Thần", [])
        
        if dung_than_list:
            noi_dung.append(f"   🎯 Dụng Thần cần xem: {', '.join(dung_than_list)}")
            noi_dung.append("")
            
            # Kiểm tra cung này có chứa Dụng Thần không
            co_dung_than = []
            for dt in dung_than_list:
                if dt in [sao, cua, than, can_thien, can_dia]:
                    co_dung_than.append(dt)
                elif dt.replace(" Môn", "") == cua or dt.replace("Cửa ", "") == cua:
                    co_dung_than.append(dt)
            
            if co_dung_than:
                noi_dung.append(f"   ✅ Cung này chứa Dụng Thần: {', '.join(co_dung_than)}")
                noi_dung.append(f"   → Đây là cung QUAN TRỌNG cho chủ đề '{chu_de}'")
            else:
                noi_dung.append(f"   ⚠️ Cung này KHÔNG chứa Dụng Thần chính")
                noi_dung.append(f"   → Ảnh hưởng gián tiếp đến '{chu_de}'")
            noi_dung.append("")
        
        # PHẦN 3: Diễn giải cụ thể theo chủ đề
        noi_dung.append("💡 DIỄN GIẢI CỤ THỂ:")
        noi_dung.append("")

        # NEW: Tích hợp phân tích thám tử (Nhân dạng, Số lượng, Thời gian) khi click cung
        try:
            def find_palace_local(stem_name):
                for c, s in self.can_thien_ban.items():
                    if s == stem_name: return c
                return 1
            chu_idx = find_palace_local(self.can_ngay)
            
            def get_info(c):
                m = self.manual_cung_data.get(c, {})
                return {
                    'so': c, 'ten': QUAI_TUONG.get(c, 'N/A'), 'hanh': CUNG_NGU_HANH.get(c, 'N/A'),
                    'sao': m.get('Sao', self.thien_ban.get(c, 'N/A')),
                    'cua': m.get('Cua', self.nhan_ban.get(c, 'N/A')),
                    'than': m.get('Than', self.than_ban.get(c, 'N/A')),
                    'can_thien': m.get('Can_Thien', self.can_thien_ban.get(c, 'N/A')),
                    'can_dia': m.get('Can_Dia', self.dia_can.get(c, 'N/A'))
                }
            
            chu_info_local = get_info(chu_idx)
            current_info_local = get_info(cung_so)
            
            try:
                dt_str = self.entry_datetime.get()
                dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
            except: dt_obj = datetime.now()
            
            analysis = phan_tich_sieu_chi_tiet_chu_de(chu_de, chu_info_local, current_info_local, dt_obj)
            if 'chi_tiet_tung_khia_canh' in analysis:
                for key in ['nhan_dang_tuong_so', 'dong_chay_thoi_gian']:
                    if key in analysis['chi_tiet_tung_khia_canh']:
                        data = analysis['chi_tiet_tung_khia_canh'][key]
                        noi_dung.append(f"🔍 {data.get('tieu_de', key)}:")
                        for line in data.get('noi_dung', []):
                            noi_dung.append(f"   {line}")
                noi_dung.append("")
        except Exception as e:
            print(f"Lỗi phân tích thám tử tại cung {cung_so}: {e}")
        
        if chu_de in ["Kinh Doanh", "Công Việc", "Sự Nghiệp"]:
            noi_dung.append("   💼 Về Kinh Doanh/Công Việc:")
            noi_dung.append(f"   • Sao {sao}:")
            if "Thiên" in sao:
                noi_dung.append("     - Cát tinh, tốt cho kinh doanh")
                noi_dung.append("     - Có quý nhân giúp đỡ")
            noi_dung.append(f"   • Môn {cua}:")
            if cua == "Sinh":
                noi_dung.append("     - Môn Sinh: Tốt cho khởi nghiệp, phát triển")
            elif cua == "Khai":
                noi_dung.append("     - Môn Khai: Tốt cho mở rộng, khai trương")
            noi_dung.append(f"   • Ngũ Hành {hanh}:")
            if hanh == "Kim":
                noi_dung.append("     - Kim: Liên quan đến tiền bạc, tài chính")
            elif hanh == "Mộc":
                noi_dung.append("     - Mộc: Phát triển, mở rộng")
            
        elif chu_de in ["Hôn Nhân", "Tình Cảm", "Gia Đình"]:
            noi_dung.append("   💑 Về Hôn Nhân/Tình Cảm:")
            noi_dung.append(f"   • Sao {sao}:")
            if "Thiên" in sao:
                noi_dung.append("     - Quan hệ tốt đẹp, hòa hợp")
            noi_dung.append(f"   • Môn {cua}:")
            if cua == "Sinh":
                noi_dung.append("     - Môn Sinh: Tình cảm phát triển tốt")
            noi_dung.append(f"   • Ngũ Hành {hanh}:")
            if hanh == "Hỏa":
                noi_dung.append("     - Hỏa: Tình cảm nồng nhiệt")
            elif hanh == "Thủy":
                noi_dung.append("     - Thủy: Tình cảm sâu sắc nhưng có trở ngại")
        
        elif chu_de in ["Sức Khỏe", "Bệnh Tật"]:
            noi_dung.append("   🏥 Về Sức Khỏe:")
            noi_dung.append(f"   • Sao {sao}:")
            if "Thiên" in sao:
                noi_dung.append("     - Sức khỏe tốt")
            noi_dung.append(f"   • Môn {cua}:")
            if cua == "Sinh":
                noi_dung.append("     - Môn Sinh: Bệnh sẽ khỏi")
            noi_dung.append(f"   • Ngũ Hành {hanh}:")
            noi_dung.append(f"     - {hanh}: Liên quan đến cơ quan tương ứng")
        
        else:
            noi_dung.append(f"   🌟 Về {chu_de}:")
            noi_dung.append("   • Xem Dụng Thần để biết ảnh hưởng cụ thể")
            noi_dung.append("   • Cung này có vai trò hỗ trợ hoặc cản trở")
        
        noi_dung.append("")
        noi_dung.append("="*90)
        
        # Hiển thị
        text_widget.insert('1.0', '\n'.join(noi_dung))
        text_widget.config(state=tk.DISABLED)
        
        # Nút đóng
        ttk.Button(window, text="Đóng", command=window.destroy).pack(pady=10)
    
        # Tạo event giả để tương thích
        class FakeEvent:
            pass
        fake_event = FakeEvent()
        
        # Gọi hàm xử lý (đã được merge logic vào đây)
        # Bỏ qua phần set combo_chon_cung cũ
    
    def _navigate_palace(self, direction):
        """Điều hướng qua 9 cung theo thứ tự Lạc Thư"""
        self.hien_thi_ky_mon() # Chuyển về tab Kỳ Môn nếu đang ở tab khác

        if self.current_palace_nav_idx == -1:
            self.current_palace_nav_idx = 0
        else:
            self.current_palace_nav_idx = (self.current_palace_nav_idx + direction) % 9
            
        cung_so = self.palace_list[self.current_palace_nav_idx]
        
        # Cập nhật highlight trên grid để người dùng biết đang xem cung nào
        self.cap_nhat_cung_buttons()
        frame = self.cung_frames.get(cung_so)
        if frame:
            frame.config(highlightbackground="#f1c40f", highlightthickness=6)
            
        # Tự động hiển thị diễn giải cho cung đó
        self._hien_thi_dien_giai_cung_theo_chu_de(cung_so)

    def _hien_thi_giai_thich_chi_tiet(self, cung_so):
        if self.detail_window and self.detail_window.winfo_exists():
            self.detail_window.destroy()

        self.detail_window = Toplevel(self.master)
        self.detail_window.title(f"Chi Tiết Luận Giải Cung {cung_so}: {QUAI_TUONG.get(cung_so, 'N/A')}")
        self.detail_window.transient(self.master)

        text_content = self.danh_sach_giai_thich.get(cung_so, "Không có nội dung giải thích cho cung này.")

        text_area = tk.Text(self.detail_window, wrap=tk.WORD, width=70, height=25, font=('Arial', 10), padx=10, pady=10)
        text_area.insert(tk.END, text_content)
        text_area.config(state=tk.DISABLED)

        scrollbar = ttk.Scrollbar(self.detail_window, command=text_area.yview)
        text_area.config(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def tao_grid_layout(self):
        self.cung_frames = {}
        self.vi_tri_in = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
        
        for i in range(3):
            self.frame_grid.grid_rowconfigure(i, weight=1, minsize=220)  # Tăng kích thước thêm nữa
            for j in range(3):
                self.frame_grid.grid_columnconfigure(j, weight=1, minsize=220)  # Tăng kích thước thêm nữa
                cung_so = self.vi_tri_in[i][j]
                # Màu nền đẹp hơn với gradient effect (simulated)
                cung_frame = tk.Frame(self.frame_grid, borderwidth=3, relief="raised", 
                                     bg='#ffffff', highlightbackground="#3498db", 
                                     highlightthickness=2, cursor="hand2")  # Thêm cursor
                cung_frame.grid(row=i, column=j, padx=8, pady=8, sticky="nsew")
                self.create_cung_elements(cung_frame, cung_so)
                self.cung_frames[cung_so] = cung_frame
                
                # Thêm event click để hiển thị diễn giải theo chủ đề
                cung_frame.bind("<Button-1>", lambda e, c=cung_so: self._hien_thi_dien_giai_cung_theo_chu_de(c))
    
    def tao_mai_hoa_frame(self):
        """Tạo Frame hiển thị 64 Quẻ Kinh Dịch - Mai Hoa Dịch Số"""
        # Frame chính cho Mai Hoa Dịch Số
        self.frame_mai_hoa = ttk.LabelFrame(self.scrollable_frame, text="📖 64 QUẺ KINH DỊCH - MAI HOA DỊCH SỐ 📖", 
                                            padding="15")
        self.frame_mai_hoa.pack(fill='both', expand=False, padx=10, pady=10)
        
        # Frame hiển thị quẻ
        frame_display = tk.Frame(self.frame_mai_hoa, bg='#f8f9fa', relief='sunken', bd=2)
        frame_display.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Label Bản Quẻ
        self.label_ban_qua = tk.Label(frame_display, text="Bản Quẻ: (Chưa tính)", 
                                      font=('Segoe UI', 12, 'bold'), bg='#f8f9fa', 
                                      fg='#2c3e50', anchor='w')
        self.label_ban_qua.pack(fill='x', padx=10, pady=5)
        
        # Label Quẻ Biến
        self.label_qua_bien = tk.Label(frame_display, text="Quẻ Biến: (Chưa tính)", 
                                       font=('Segoe UI', 12, 'bold'), bg='#f8f9fa', 
                                       fg='#16a085', anchor='w')
        self.label_qua_bien.pack(fill='x', padx=10, pady=5)
        
        # Label Hào Động
        self.label_hao_dong = tk.Label(frame_display, text="Hào Động: -", 
                                       font=('Segoe UI', 11), bg='#f8f9fa', 
                                       fg='#7f8c8d', anchor='w')
        self.label_hao_dong.pack(fill='x', padx=10, pady=5)
        
        # Text widget hiển thị giải quẻ - Tập trung vào DIỄN GIẢI CHI TIẾT
        frame_giai_qua = tk.Frame(frame_display, bg='#f8f9fa')
        frame_giai_qua.pack(fill='both', expand=True, padx=10, pady=5)
        
        scrollbar = tk.Scrollbar(frame_giai_qua)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Giảm height để tập trung vào nội dung diễn giải
        self.text_giai_qua = tk.Text(frame_giai_qua, height=18, wrap=tk.NONE, 
                                     font=('Courier New', 9), bg='#ffffff',
                                     yscrollcommand=scrollbar.set)
        self.text_giai_qua.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.config(command=self.text_giai_qua.yview)
        
        # Thêm horizontal scrollbar
        scrollbar_h = tk.Scrollbar(frame_giai_qua, orient=tk.HORIZONTAL)
        scrollbar_h.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_giai_qua.config(xscrollcommand=scrollbar_h.set)
        scrollbar_h.config(command=self.text_giai_qua.xview)
        
        # Frame buttons
        frame_buttons = tk.Frame(self.frame_mai_hoa, bg='#ecf0f1')
        frame_buttons.pack(fill='x', padx=5, pady=10)
        
        # Button Tự Động Theo Giờ
        btn_auto = tk.Button(frame_buttons, text="🕐 Tự Động Theo Giờ", 
                            command=self.tinh_qua_tu_dong,
                            font=('Segoe UI', 10, 'bold'), bg='#3498db', fg='white',
                            relief='raised', bd=3, padx=15, pady=8,
                            cursor='hand2')
        btn_auto.pack(side=tk.LEFT, padx=10)
        
        # Button Ngẫu Nhiên
        btn_random = tk.Button(frame_buttons, text="🎲 Ngẫu Nhiên", 
                              command=self.tinh_qua_ngau_nhien_gui,
                              font=('Segoe UI', 10, 'bold'), bg='#e74c3c', fg='white',
                              relief='raised', bd=3, padx=15, pady=8,
                              cursor='hand2')
        btn_random.pack(side=tk.LEFT, padx=10)
        
        # Lưu trữ kết quả quẻ hiện tại
        self.ket_qua_qua_hien_tai = None
    
    def tinh_qua_tu_dong(self):
        """Tính quẻ tự động theo thời gian hiện tại"""
        try:
            # Lấy thời gian từ entry
            dt_str = self.entry_datetime.get()
            dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
            
            # Tính quẻ
            ket_qua = tinh_qua_theo_thoi_gian(dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour)
            self.ket_qua_qua_hien_tai = ket_qua
            
            # Hiển thị
            self._hien_thi_ket_qua_qua(ket_qua)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tính quẻ: {str(e)}")
    
    def tinh_qua_ngau_nhien_gui(self):
        """Tính quẻ ngẫu nhiên"""
        try:
            ket_qua = tinh_qua_ngau_nhien()
            self.ket_qua_qua_hien_tai = ket_qua
            self._hien_thi_ket_qua_qua(ket_qua)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tính quẻ ngẫu nhiên: {str(e)}")
    
    def _hien_thi_ket_qua_qua(self, ket_qua):
        """Hiển thị kết quả quẻ lên GUI"""
        ban_qua = ket_qua['ban_qua']
        qua_bien = ket_qua['qua_bien']
        hao_dong = ket_qua['hao_dong']
        qua_thuong = ket_qua['qua_thuong']
        qua_ha = ket_qua['qua_ha']
        
        # Cập nhật labels
        self.label_ban_qua.config(
            text=f"Bản Quẻ: {ban_qua['ten']} {ban_qua['unicode']} ({qua_thuong['unicode']}{qua_ha['unicode']})"
        )
        
        self.label_qua_bien.config(
            text=f"Quẻ Biến: {qua_bien['ten']} {qua_bien['unicode']}"
        )
        
        self.label_hao_dong.config(
            text=f"Hào Động: Hào thứ {hao_dong} | Thời gian: {ket_qua['thoi_gian']}"
        )
        
        # Giải quẻ theo CHỦ ĐỀ TOÀN CỤC
        chu_de = self.chu_de_hien_tai  # Sử dụng chủ đề đã chọn
        giai_thich = giai_qua(ket_qua, chu_de)
        
        # Tạo visualization quẻ nhỏ gọn
        try:
            # Chuyển đổi dữ liệu Mai Hoa sang format Lục Hào để vẽ
            from mai_hoa_dich_so import BAT_QUAI
            
            # Tìm số quẻ từ tên
            qua_thuong_so = None
            qua_ha_so = None
            for so, info in BAT_QUAI.items():
                if info['ten'] == qua_thuong['ten']:
                    qua_thuong_so = so
                if info['ten'] == qua_ha['ten']:
                    qua_ha_so = so
            
            if qua_thuong_so is not None and qua_ha_so is not None:
                # Tạo dict giả lập cho visualization
                chinh_quai_visual = {
                    'quai_info': ban_qua,
                    'quai_thuong': qua_thuong_so,
                    'quai_ha': qua_ha_so
                }
                
                # Vẽ quẻ nhỏ gọn
                try:
                    from ve_qua_am_duong_enhanced import tao_hien_thi_qua_chi_tiet_to
                    visual_text = tao_hien_thi_qua_chi_tiet_to(
                        chinh_quai_visual,
                        f"Bản Quẻ: {ban_qua['ten']}"
                    )
                    giai_thich_full = visual_text + "\n\n" + giai_thich
                except:
                    giai_thich_full = giai_thich
            else:
                giai_thich_full = giai_thich
        except Exception as e:
            print(f"Lỗi visualization: {e}")
            giai_thich_full = giai_thich
        
        # Hiển thị vào text widget
        self.text_giai_qua.config(state=tk.NORMAL)
        self.text_giai_qua.delete('1.0', tk.END)
        
        # Thêm thông tin chủ đề đang sử dụng
        header = f"📌 CHỦ ĐỀ: {chu_de}\n{'='*90}\n\n"
        
        # NEW: Tích hợp Dụng Thần chi tiết cho Mai Hoa
        dung_than_text = ""
        if USE_200_TOPICS:
            dt_data = lay_dung_than_200(chu_de)
            if dt_data and 'mai_hoa' in dt_data:
                mh = dt_data['mai_hoa']
                dung_than_text = f"🎯 DỤNG THẦN MAI HOA:\n"
                dung_than_text += f"   • Dụng Thần: {mh.get('dung_than', 'N/A')}\n"
                dung_than_text += f"   • Giải thích: {mh.get('giai_thich', 'N/A')}\n"
                dung_than_text += f"   • Cách xem: {mh.get('cach_xem', 'N/A')}\n"
                if 'vi_du' in mh: dung_than_text += f"   • Ví dụ: {mh['vi_du']}\n"
                dung_than_text += f"{'-'*90}\n\n"

        self.text_giai_qua.insert('1.0', header + dung_than_text + giai_thich_full)
        self.text_giai_qua.config(state=tk.DISABLED)
    
    def hien_thi_ky_mon(self):
        """Hiển thị bảng Kỳ Môn, ẩn 64 Quẻ"""
        # Ẩn frame 64 quẻ
        self.frame_mai_hoa.pack_forget()
        self.frame_luc_hao.pack_forget()
        
        # Hiện frame Kỳ Môn
        self.frame_grid.pack(padx=10, pady=10, fill='both', expand=True)
        
        # Cập nhật màu nút (nút Kỳ Môn sáng hơn)
        self.btn_show_qimen.config(bg='#2980b9', relief='sunken')
        self.btn_show_64qua.config(bg='#e74c3c', relief='raised')
        self.btn_show_luchao.config(bg='#16a085', relief='raised')
    
    def hien_thi_64_qua(self):
        """Hiển thị 64 Quẻ Mai Hoa, ẩn bảng Kỳ Môn và Lục Hào"""
        # Ẩn frame Kỳ Môn và Lục Hào
        self.frame_grid.pack_forget()
        self.frame_luc_hao.pack_forget()
        
        # Hiện frame 64 quẻ Mai Hoa
        self.frame_mai_hoa.pack(fill='both', expand=False, padx=10, pady=10)
        
        # Cập nhật màu nút (nút 64 Quẻ sáng hơn)
        self.btn_show_qimen.config(bg='#3498db', relief='raised')
        self.btn_show_64qua.config(bg='#c0392b', relief='sunken')
        self.btn_show_luchao.config(bg='#16a085', relief='raised')
        
        # Tự động tính quẻ theo thời gian hiện tại nếu chưa có
        if self.ket_qua_qua_hien_tai is None:
            self.tinh_qua_tu_dong()
    
    def hien_thi_luc_hao(self):
        """Hiển thị Lục Hào Kinh Dịch, ẩn bảng Kỳ Môn và Mai Hoa"""
        # Ẩn frame Kỳ Môn và Mai Hoa
        self.frame_grid.pack_forget()
        self.frame_mai_hoa.pack_forget()
        
        # Hiện frame Lục Hào
        self.frame_luc_hao.pack(fill='both', expand=False, padx=10, pady=10)
        
        # Cập nhật màu nút (nút Lục Hào sáng hơn)
        self.btn_show_qimen.config(bg='#3498db', relief='raised')
        self.btn_show_64qua.config(bg='#e74c3c', relief='raised')
        self.btn_show_luchao.config(bg='#138d75', relief='sunken')
        
        # Tự động tính quẻ theo thời gian hiện tại nếu chưa có
        if not hasattr(self, 'ket_qua_luc_hao_hien_tai') or self.ket_qua_luc_hao_hien_tai is None:
            self.tinh_luc_hao_tu_dong()
    
    def tao_luc_hao_frame(self):
        """Tạo Frame hiển thị Lục Hào Kinh Dịch - 3 Quẻ"""
        # Frame chính cho Lục Hào
        self.frame_luc_hao = ttk.LabelFrame(self.scrollable_frame, text="☯️ LỤC HÀO KINH DỊCH - 3 QUẺ ☯️", 
                                            padding="15")
        
        # Text widget hiển thị kết quả
        frame_display = tk.Frame(self.frame_luc_hao, bg='#f8f9fa')
        frame_display.pack(fill='both', expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(frame_display)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Tập trung vào DIỄN GIẢI CHI TIẾT
        self.text_luc_hao = tk.Text(frame_display, height=22, wrap=tk.NONE, 
                                    font=('Courier New', 9), bg='#ffffff',
                                    yscrollcommand=scrollbar.set)
        self.text_luc_hao.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.config(command=self.text_luc_hao.yview)
        
        # Thêm horizontal scrollbar
        scrollbar_h = tk.Scrollbar(frame_display, orient=tk.HORIZONTAL)
        scrollbar_h.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_luc_hao.config(xscrollcommand=scrollbar_h.set)
        scrollbar_h.config(command=self.text_luc_hao.xview)
        
        # Frame buttons
        frame_buttons = tk.Frame(self.frame_luc_hao, bg='#ecf0f1')
        frame_buttons.pack(fill='x', padx=5, pady=10)
        
        # Button Tự Động Theo Giờ
        btn_auto = tk.Button(frame_buttons, text="🕐 Tự Động Theo Giờ", 
                            command=self.tinh_luc_hao_tu_dong,
                            font=('Segoe UI', 10, 'bold'), bg='#3498db', fg='white',
                            relief='raised', bd=3, padx=15, pady=8,
                            cursor='hand2')
        btn_auto.pack(side=tk.LEFT, padx=10)
        
        # Combobox chọn chủ đề
        tk.Label(frame_buttons, text="Chủ đề:", font=('Segoe UI', 10), 
                bg='#ecf0f1').pack(side=tk.LEFT, padx=5)
        
        self.combo_chu_de_luchao = ttk.Combobox(frame_buttons, 
            values=["Tổng Quát", "Kinh Doanh", "Hôn Nhân", "Sức Khỏe", 
                    "Học Tập", "Công Việc", "Tài Lộc", "Quan Tụng"],
            state='readonly', width=15, font=('Segoe UI', 9))
        self.combo_chu_de_luchao.set("Tổng Quát")
        self.combo_chu_de_luchao.pack(side=tk.LEFT, padx=10)
        
        # Lưu trữ kết quả
        self.ket_qua_luc_hao_hien_tai = None
    
    def tinh_luc_hao_tu_dong(self):
        """Tính Lục Hào tự động theo thời gian hiện tại"""
        try:
            # Lấy thời gian từ entry
            dt_str = self.entry_datetime.get()
            dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
            
            # Lấy chủ đề TOÀN CỤC
            chu_de = self.chu_de_hien_tai
            
            # Tính quẻ Lục Hào
            ket_qua = lap_qua_luc_hao(dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour, chu_de)
            self.ket_qua_luc_hao_hien_tai = ket_qua
            
            # Hiển thị
            self._hien_thi_ket_qua_luc_hao(ket_qua)
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tính Lục Hào: {str(e)}")
    
    def _hien_thi_ket_qua_luc_hao(self, ket_qua):
        """Hiển thị kết quả Lục Hào lên GUI"""
        # Lưu kết quả
        self.ket_qua_luc_hao_hien_tai = ket_qua
        
        # Lấy chủ đề toàn cục
        chu_de = self.chu_de_hien_tai
        
        # Hiển thị vào text widget
        self.text_luc_hao.config(state=tk.NORMAL)
        self.text_luc_hao.delete('1.0', tk.END)
        
        # Thêm header với chủ đề
        header = f"📌 CHỦ ĐỀ: {chu_de}\n{'='*90}\n\n"
        
        # NEW: Tích hợp Dụng Thần chi tiết cho Lục Hào
        dung_than_text = ""
        if USE_200_TOPICS:
            dt_data = lay_dung_than_200(chu_de)
            if dt_data and 'luc_hao' in dt_data:
                lh = dt_data['luc_hao']
                dung_than_text = f"🎯 DỤNG THẦN LỤC HÀO:\n"
                dung_than_text += f"   • Dụng Thần: {lh.get('dung_than', 'N/A')}\n"
                dung_than_text += f"   • Giải thích: {lh.get('giai_thich', 'N/A')}\n"
                dung_than_text += f"   • Cách xem: {lh.get('cach_xem', 'N/A')}\n"
                if 'vi_du' in lh: dung_than_text += f"   • Ví dụ: {lh['vi_du']}\n"
                dung_than_text += f"{'-'*90}\n\n"
        
        # Lấy giải thích (đã có trong ket_qua)
        giai_thich = ket_qua.get('giai_thich', '')
        
        self.text_luc_hao.insert('1.0', header + dung_than_text + giai_thich)
        self.text_luc_hao.config(state=tk.DISABLED)
    

    def create_cung_elements(self, parent_frame, cung_so):
        parent_frame.grid_rowconfigure(0, weight=1); parent_frame.grid_rowconfigure(1, weight=1); parent_frame.grid_rowconfigure(2, weight=1)
        parent_frame.grid_columnconfigure(0, weight=1); parent_frame.grid_columnconfigure(1, weight=1); parent_frame.grid_columnconfigure(2, weight=1)

        self.label_than = tk.Label(parent_frame, text="Thần", font=self.font_than, anchor='center', fg='#7f8c8d', bg='#FFFFFF') 
        self.label_than.grid(row=0, column=1, sticky='ew')
        
        self.label_sao = tk.Label(parent_frame, text="Tinh", font=self.font_tinh, anchor='w', fg='#2980b9', bg='#FFFFFF')
        self.label_sao.grid(row=0, column=0, padx=5, sticky='nw')
        
        self.label_can_thien = tk.Label(parent_frame, text="CT", font=self.font_can, fg='#8e44ad', anchor='e', bg='#FFFFFF')
        self.label_can_thien.grid(row=0, column=2, padx=5, sticky='ne')

        sub_frame_center = tk.Frame(parent_frame, bg='#FFFFFF')
        sub_frame_center.grid(row=1, column=0, columnspan=3, sticky='nsew')
        ten_cung = QUAI_TUONG.get(cung_so, 'N/A')
        self.label_cung_info = tk.Label(sub_frame_center, text=ten_cung, font=self.font_cung_info, anchor='center', fg='#2c3e50', bg='#FFFFFF') 
        self.label_cung_info.pack(fill='x', pady=2)
        self.label_mon_co_dinh = tk.Label(sub_frame_center, text="Môn Cố Định", font=self.font_mon_co_dinh, anchor='center', fg='#95a5a6', bg='#FFFFFF') 
        self.label_mon_co_dinh.pack(fill='x')
        
        self.label_cua = tk.Label(parent_frame, text="Môn Chạy", font=self.font_mon_chay, anchor='center', fg='#27ae60', bg='#FFFFFF')
        self.label_cua.grid(row=2, column=1, sticky='ew')
        
        self.label_cung_so = tk.Label(parent_frame, text=str(cung_so), font=self.font_cung_so, anchor='w', fg='#34495e', bg='#FFFFFF')
        self.label_cung_so.grid(row=2, column=0, padx=5, sticky='sw')

        self.label_can_dia = tk.Label(parent_frame, text="ĐC", font=self.font_can, fg='#c0392b', anchor='e', bg='#FFFFFF')
        self.label_can_dia.grid(row=2, column=2, padx=5, sticky='se')
        
        parent_frame.labels = {
            'sao': self.label_sao, 'cua': self.label_cua, 'can_thien': self.label_can_thien,
            'can_dia': self.label_can_dia, 'than': self.label_than, 'cung_info': self.label_cung_info,
            'mon_co_dinh': self.label_mon_co_dinh, 'sub_frame_center': sub_frame_center,
            'cung_so': self.label_cung_so
        }
        
        for child in parent_frame.winfo_children():
             child.bind("<Button-1>", lambda event, c=cung_so: self._hien_thi_giai_thich_chi_tiet(c))
             for sub_child in child.winfo_children():
                sub_child.bind("<Button-1>", lambda event, c=cung_so: self._hien_thi_giai_thich_chi_tiet(c))

    def lap_va_hien_thi_ban(self, is_default):
        if self.is_running: return
        self.is_running = True
        self.master.config(cursor="wait") 
        self.button_lap_ban.config(state=tk.DISABLED)
        self.button_tai_lai.config(state=tk.DISABLED)
        
        if self.detail_window and self.detail_window.winfo_exists():
            self.detail_window.destroy()
            self.detail_window = None
        if self.cung_input_window and self.cung_input_window.winfo_exists():
            self.cung_input_window.destroy()
            self.cung_input_window = None

        thread = threading.Thread(target=self._lap_ban_logic, args=(is_default,)); thread.start()

    def _lap_ban_logic(self, is_default):
        try:
            cuc = int(self.entry_cuc.get())
            truc_phu = self.combo_truc_phu.get()
            truc_su = self.combo_truc_su.get()
            dia_chi_gio = self.combo_dia_chi.get()
            
            # Lấy thông tin Can Chi từ qmdg_calc dựa trên entry_datetime
            try:
                dt_str = self.entry_datetime.get()
                dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
            except:
                dt_obj = datetime.now()
                
            params = qmdg_calc.calculate_qmdg_params(dt_obj)
            self.can_gio = params['can_gio']
            self.can_ngay = params['can_ngay']
            self.can_nam = params['can_nam']
            self.can_thang = params['can_thang']
            
            # Cập nhật nhãn âm lịch trong logic lập bàn
            can_chi_str = f"Giờ {self.can_gio} {params['chi_gio']} | Ngày {self.can_ngay} {params['chi_ngay']} | Tháng {self.can_thang} {params['chi_thang']} | Năm {self.can_nam} {params['chi_nam']}"
            self.master.after(0, lambda: self.lbl_can_chi_full.config(text=can_chi_str))
            
            # Cập nhật tiêu đề cửa sổ chính
            self.master.after(0, lambda: self.master.title(f"🔮 Bàn Cung Kỳ Môn Độn Giáp - {params['tiet_khi']} - Cục {cuc} ({'Dương' if self.is_duong_don else 'Âm'} Độn) - [{can_chi_str}] 🔮"))

            dia_can_moi = an_bai_luc_nghi(cuc, self.is_duong_don) 
            thien_ban, can_thien_ban, nhan_ban, than_ban, cung_dich_truc_phu = lap_ban_qmdg(cuc, truc_phu, truc_su, self.can_gio, dia_chi_gio, self.is_duong_don)
            khong_vong_cung = tinh_khong_vong(self.can_gio, dia_chi_gio) 
            dich_ma_cung = tinh_dich_ma(dia_chi_gio)
            ket_qua_tranh = kiem_tra_cau_truc_tranh(can_thien_ban, dia_can_moi)
            
            self.thien_ban = thien_ban
            self.can_thien_ban = can_thien_ban
            self.nhan_ban = nhan_ban
            self.than_ban = than_ban
            self.truc_phu_cung_so = cung_dich_truc_phu
            self.dia_can = dia_can_moi
            self.khong_vong_cung = khong_vong_cung
            self.dich_ma_cung = dich_ma_cung
            self.ket_qua_tranh = ket_qua_tranh
            
            self._tinh_toan_truoc_giai_thich() 
            self.master.after(0, self._cap_nhat_gui_sau_tinh_toan)
            
        except Exception as e:
            self.master.after(0, lambda: messagebox.showerror("Lỗi Lập Bàn", f"Đã xảy ra lỗi khi tính toán: {e}"))
            self.master.after(0, self._hoan_tat_lap_ban)

    def _tinh_toan_truoc_giai_thich(self):
        self.danh_sach_giai_thich = {} 
        self.danh_sach_giai_thich[5] = "--- TRUNG CUNG (CUNG 5) ---\n\nTrung cung thường không xét Sao, Môn, Thần (trừ Thiên Cầm)."

        for cung_so in [1, 2, 3, 4, 6, 7, 8, 9]:
            manual_data = self.manual_cung_data.get(cung_so, {})
            
            sao = manual_data.get('Sao', self.thien_ban.get(cung_so, 'N/A'))
            cua_chay = manual_data.get('Cua', self.nhan_ban.get(cung_so, 'N/A'))
            can_thien = manual_data.get('Can_Thien', self.can_thien_ban.get(cung_so, 'N/A'))
            can_dia = manual_data.get('Can_Dia', self.dia_can.get(cung_so, 'N/A'))
            than = manual_data.get('Than', self.than_ban.get(cung_so, 'N/A'))
            
            hanh_cung = CUNG_NGU_HANH.get(cung_so, 'N/A')
            hanh_can_thien = KY_MON_DATA["CAN_CHI_LUAN_GIAI"].get(can_thien, {}).get('Hành', 'N/A') 
            hanh_sao = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['CUU_TINH'].get(sao, {}).get('Hành', 'N/A')

            cach_cuc_key_tu_cung = can_thien + can_dia
            ket_hop_can = KY_MON_DATA["TRUCTU_TRANH"].get(cach_cuc_key_tu_cung, {})

            ket_hop_sao_cung = tinh_ngu_hanh_sinh_khac(hanh_sao, hanh_cung)
            ket_hop_can_cung = tinh_ngu_hanh_sinh_khac(hanh_can_thien, hanh_cung)

            sao_detail = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['CUU_TINH'].get(sao, {})
            can_thien_detail = KY_MON_DATA['CAN_CHI_LUAN_GIAI'].get(can_thien, {})
            mon_detail = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['BAT_MON'].get(cua_chay + ' Môn', {})
            than_detail = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['BAT_THAN'].get(than, {})
            
            header = f"--- CHI TIẾT CUNG {cung_so}: {QUAI_TUONG.get(cung_so, 'N/A')} ({hanh_cung}) ---"
            if manual_data: header += " [DỮ LIỆU ĐƯỢC CHỈNH SỬA THỦ CÔNG]"

            noidung = [
                header,
                "\n*** 1. THIÊN BÀN (Cửu Tinh và Can Thiên) ***",
                f"- Cửu Tinh: **{sao}**", f"  - Hành: {sao_detail.get('Hành', 'N/A')}", f"  - Tính Chất: {sao_detail.get('Tính_Chất', 'N/A')}",
                f"- Can Thiên: **{can_thien}**", f"  - Tính Chất: {can_thien_detail.get('Tính_Chất', 'N/A')}",
                "\n*** 2. NHÂN BÀN (Bát Môn) ***",
                f"- Bát Môn: **{cua_chay} Môn**", f"  - Cát/Hung: {mon_detail.get('Cát_Hung', 'N/A')}", f"  - Luận Đoán: {mon_detail.get('Luận_Đoán', 'N/A')}",
                "\n*** 3. ĐỊA BÀN (Can Địa và Cung) ***",
                f"- Can Địa (Lục Nghi): **{can_dia}**", f"- Ngũ Hành Cung Vị: {hanh_cung}",
                f"- Can {can_thien} / Cung {hanh_cung}: **{ket_hop_can_cung}**", f"- Sao {sao} / Cung {hanh_cung}: **{ket_hop_sao_cung}**",
                "\n*** 4. THẦN BÀN (Bát Thần) ***",
                f"- Bát Thần: **{than}**", f"  - Tính Chất: {than_detail.get('Tính_Chất', 'N/A')}",
                "\n*** 5. CÁCH CỤC KẾT HỢP CAN/CAN ***",
                f"- Cách Cục: **{can_thien}/{can_dia}**", f"- Cát/Hung: {ket_hop_can.get('Cát_Hung', 'Bình')}", f"- Luận Giải: {ket_hop_can.get('Luận_Giải', 'Chưa có nội dung.')}"
            ]
            self.danh_sach_giai_thich[cung_so] = "\n".join(noidung)
    
    def _cap_nhat_gui_sau_tinh_toan(self):
        try:
            self.cap_nhat_cung_buttons()
        finally: self._hoan_tat_lap_ban()

    def tai_lai_gio_va_lap_ban(self):
        self.manual_cung_data = {} # Xóa dữ liệu chỉnh sửa thủ công để cập nhật hoàn toàn theo giờ
        self.cap_nhat_thoi_gian_thuc()
        self.lap_va_hien_thi_ban(is_default=False)

    def _hoan_tat_lap_ban(self):
        self.is_running = False
        self.master.config(cursor="")
        self.button_lap_ban.config(state=tk.NORMAL)
        self.button_tai_lai.config(state=tk.NORMAL)

    def cap_nhat_cung_buttons(self):
        dung_than_chon = self.chu_de_hien_tai
        for c, frame in self.cung_frames.items():
            sao_calc = self.thien_ban.get(c, 'N/A')
            cua_chay_calc = self.nhan_ban.get(c, 'N/A')
            can_thien_calc = self.can_thien_ban.get(c, 'N/A')
            can_dia_calc = self.dia_can.get(c, 'N/A')
            than_calc = self.than_ban.get(c, 'N/A')
            
            manual_data = self.manual_cung_data.get(c, {})
            sao = manual_data.get('Sao', sao_calc)
            cua_chay = manual_data.get('Cua', cua_chay_calc)
            can_thien = manual_data.get('Can_Thien', can_thien_calc)
            can_dia = manual_data.get('Can_Dia', can_dia_calc)
            than = manual_data.get('Than', than_calc)
            
            is_manually_edited = bool(manual_data)
            
            # MÀU NỀN THEO HÌNH MẪU - NHẠT VÀ TINH TẾ HƠN
            ngu_hanh_cung = CUNG_NGU_HANH.get(c, "Thổ")
            cat_hung_cua = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_MON"].get(cua_chay + " Môn", {}).get("Cát_Hung", "Bình")
            
            # Màu nền theo hình mẫu
            if c in [3, 4, 8]:  # Cung 3, 4, 8: Xanh lá nhạt
                sao_nen_color = '#c8f0d4'  # Xanh lá rất nhạt (như hình)
                border_color = '#2ecc71'   # Xanh lá
                shadow_color = '#27ae60'   # Bóng đổ xanh
            elif c == 9:  # Cung 9: Xám nhạt
                sao_nen_color = '#e8e8e8'  # Xám nhạt
                border_color = '#95a5a6'   # Xám
                shadow_color = '#7f8c8d'   # Bóng đổ xám
            elif c == 2:  # Cung 2: Xám nhạt
                sao_nen_color = '#e8e8e8'  # Xám nhạt
                border_color = '#95a5a6'   # Xám
                shadow_color = '#7f8c8d'   # Bóng đổ xám
            elif c in [6, 7]:  # Cung 6, 7: Xám trắng
                sao_nen_color = '#f5f5f5'  # Xám trắng nhạt
                border_color = '#bdc3c7'   # Xám nhạt
                shadow_color = '#95a5a6'   # Bóng đổ xám
            elif c == 1:  # Cung 1: Xanh dương nhạt
                sao_nen_color = '#d6eaf8'  # Xanh dương rất nhạt
                border_color = '#3498db'   # Xanh dương
                shadow_color = '#2980b9'   # Bóng đổ xanh đậm
            elif c == 5:  # Cung 5: Vàng
                sao_nen_color = '#fff9c4'  # Vàng nhạt
                border_color = '#f9ca24'   # Vàng
                shadow_color = '#f39c12'   # Bóng đổ vàng đậm
            else:
                sao_nen_color = '#ffffff'  # Trắng
                border_color = '#bdc3c7'
                shadow_color = '#95a5a6'
            
            # LOGIC DỤNG THẦN ĐỘNG
            is_dung_than = False
            if dung_than_chon != "Không":
                topic_data = TOPIC_INTERPRETATIONS.get(dung_than_chon, {})
                dung_than_targets = topic_data.get("Dụng_Thần", [])
                
                # Danh sách các giá trị có trong cung hiện tại
                palace_elements = [
                    sao, cua_chay, than, can_thien, can_dia,
                    f"{cua_chay} Môn", # Khớp với "Sinh Môn"
                    f"Cửa {cua_chay}", # Khớp với "Cửa Sinh"
                    f"Sao {sao}"
                ]
                
                # Thêm các Can đặc biệt nếu khớp
                if can_thien == self.can_ngay or can_dia == self.can_ngay:
                    palace_elements.append("Can Ngày")
                    palace_elements.append("Ri Gan")
                if can_thien == self.can_gio or can_dia == self.can_gio:
                    palace_elements.append("Can Giờ")
                    palace_elements.append("Shi Gan")
                if can_thien == self.can_nam or can_dia == self.can_nam:
                    palace_elements.append("Can Năm")
                    palace_elements.append("Nian Gan")
                if can_thien == self.can_thang or can_dia == self.can_thang:
                    palace_elements.append("Can Tháng")
                    palace_elements.append("Yue Gan")

                for target in dung_than_targets:
                    if target in palace_elements:
                        is_dung_than = True
                        break
                    # Khớp trực tiếp Can (ví dụ: "Mậu", "Canh")
                    if target in [can_thien, can_dia]:
                        is_dung_than = True
                        break

            # Cài đặt ban đầu cho cung
            relief_val, border_val, highlight_color, highlight_thickness = "flat", 2, border_color, 2
            border_width = 2
            
            is_khong_vong = c in self.khong_vong_cung
            is_dich_ma = c == self.dich_ma_cung

            # Ghi đè màu nếu có điều kiện đặc biệt - HIỆU ỨNG 3D MẠNH
            if is_manually_edited:
                relief_val, border_val, highlight_color, highlight_thickness = "ridge", 5, "#FF6F00", 4
                sao_nen_color = '#ffd699'  # Cam ĐẬM cho chỉnh sửa thủ công
                shadow_color = '#cc5700'
            elif is_dich_ma and is_khong_vong:
                relief_val, border_val, highlight_color, highlight_thickness = "groove", 5, "#FFB300", 4
                sao_nen_color = '#fff59d'  # Vàng ĐẬM cho Dịch Mã + Không Vong
                shadow_color = '#cc8f00'
            elif is_khong_vong:
                relief_val, border_val, highlight_color, highlight_thickness = "solid", 4, "#757575", 3
                sao_nen_color = '#d6d6d6'  # Xám ĐẬM cho Không Vong
                shadow_color = '#4a4a4a'
            elif is_dich_ma:
                relief_val, border_val, highlight_color, highlight_thickness = "groove", 4, "#2E7D32", 3
                sao_nen_color = '#c8e6c9'  # Xanh lá ĐẬM cho Dịch Mã
                shadow_color = '#1b5e20'
            elif is_dung_than:
                relief_val, border_val, highlight_color, highlight_thickness = "raised", 5, "#e74c3c", 4
                sao_nen_color = '#fdedec'  # Đỏ cực nhạt cho nền
                shadow_color = '#c0392b'   # Đỏ đậm cho viền/bóng
                highlight_color = '#e74c3c'
            else:
                relief_val, border_val, highlight_color, highlight_thickness = "raised", 4, border_color, 3

            # HIỆU ỨNG 3D/4D - Thêm đổ bóng bằng cách dùng nhiều border
            frame.config(bg=sao_nen_color, relief=relief_val, borderwidth=border_val, 
                        highlightbackground=highlight_color, highlightthickness=highlight_thickness,
                        highlightcolor=shadow_color)  # Màu bóng đổ

            labels = frame.labels 
            for name in ['sao', 'cua', 'can_thien', 'can_dia', 'than', 'cung_info', 'mon_co_dinh', 'cung_so']:
                labels[name].config(bg=sao_nen_color) 
            labels['sub_frame_center'].config(bg=sao_nen_color)

            # Màu chữ cho môn (đậm hơn, dễ đọc hơn)
            if cat_hung_cua == "Đại Cát": 
                mau_chu_mon = "#155724"  # Xanh lá đậm
            elif cat_hung_cua == "Cát": 
                mau_chu_mon = "#0c5460"  # Xanh dương đậm
            elif cat_hung_cua == "Bình": 
                mau_chu_mon = "#856404"  # Vàng nâu
            elif cat_hung_cua == "Hung": 
                mau_chu_mon = "#721c24"  # Đỏ đậm
            elif cat_hung_cua == "Đại Hung": 
                mau_chu_mon = "#5a1a1f"  # Đỏ thẫm
            else: 
                mau_chu_mon = "#383d41"  # Xám đậm 
            
            kv = " 💀(KV)" if c in self.khong_vong_cung else ""
            dm = " 🐎(DM)" if c == self.dich_ma_cung else ""
            
            labels['sao'].config(text=f"{sao} (T.T)" if is_manually_edited else sao)
            labels['cua'].config(text=f"{cua_chay}{kv}{dm}", fg=mau_chu_mon)
            labels['can_thien'].config(text=can_thien)
            labels['can_dia'].config(text=can_dia)
            labels['than'].config(text=than)
            labels['mon_co_dinh'].config(text=f"Môn Gốc: {BAT_MON_CO_DINH_CUNG.get(c, 'N/A')} ({BAT_MON_CO_DINH_DISPLAY.get(BAT_MON_CO_DINH_CUNG.get(c, ''), 'N/A')})")

        self.master.update_idletasks()

    def _mo_cua_so_nhap_lieu(self):
        if self.data_input_window and self.data_input_window.winfo_exists():
            self.data_input_window.lift(); return

        window = Toplevel(self.master)
        window.title("Cập Nhật Luận Giải Cách Cục Can/Can (Master-Detail)")
        window.transient(self.master); window.resizable(False, True)
        self.data_input_window = window

        self.all_can_pairs = self._get_all_can_pairs()
        can_pairs_display = [pair[1] for pair in self.all_can_pairs] 

        main_frame = ttk.Frame(window, padding=10); main_frame.pack(fill='both', expand=True)
        main_frame.grid_columnconfigure(0, weight=1); main_frame.grid_columnconfigure(1, weight=2) 

        frame_master = ttk.LabelFrame(main_frame, text="✍️ Nhập/Cập Nhật Cách Cục", padding=10)
        frame_master.grid(row=0, column=0, padx=10, pady=5, sticky='nsw')

        tk.Label(frame_master, text="Chọn Cặp Can Thiên / Can Địa:", font=self.font_main).grid(row=0, column=0, padx=5, pady=5, sticky='w', columnspan=2)
        self.combo_cach_cuc = ttk.Combobox(frame_master, values=can_pairs_display, width=15, state='readonly', font=self.font_cung_info)
        self.combo_cach_cuc.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        self.combo_cach_cuc.bind("<<ComboboxSelected>>", self._load_selected_to_master_from_combo)
        
        tk.Label(frame_master, text="Cát/Hung:", font=self.font_main).grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.combo_cat_hung = ttk.Combobox(frame_master, values=["Đại Cát", "Cát", "Bình", "Hung", "Đại Hung"], width=10, state='readonly', font=self.font_cung_info)
        self.combo_cat_hung.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='w'); self.combo_cat_hung.set("Bình")

        tk.Label(frame_master, text="Luận Giải Chi Tiết:", font=self.font_main).grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        self.text_luan_giai = tk.Text(frame_master, height=10, width=30, font=('Arial', 9))
        self.text_luan_giai.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        frame_buttons = ttk.Frame(frame_master)
        frame_buttons.grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(frame_buttons, text="Lưu & Áp Dụng", command=self._luu_du_lieu_tuy_chinh).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="Xóa Mục Đang Chọn 🗑️", command=self._xoa_du_lieu_tuy_chinh).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="Xóa Form Nhanh", command=self._clear_master_form).pack(side=tk.LEFT, padx=5)

        frame_detail = ttk.LabelFrame(main_frame, text="📚 Các Cách Cục Đã Lưu", padding=10)
        frame_detail.grid(row=0, column=1, padx=10, pady=5, sticky='nsew')
        frame_detail.grid_rowconfigure(0, weight=1); frame_detail.grid_columnconfigure(0, weight=1)

        self.tree = ttk.Treeview(frame_detail, columns=("CachCuc", "CatHung", "LuanGiai"), show="headings", height=15)
        self.tree.heading("CachCuc", text="Cặp Can", anchor='w'); self.tree.heading("CatHung", text="Cát/Hung"); self.tree.heading("LuanGiai", text="Luận Giải")
        self.tree.column("CachCuc", width=80, anchor='w'); self.tree.column("CatHung", width=60, anchor='center'); self.tree.column("LuanGiai", width=250, anchor='w')
        self.tree.bind('<<TreeviewSelect>>', self._load_selected_to_master_from_treeview)
        self.tree.grid(row=0, column=0, sticky='nsew')
        
        scrollbar = ttk.Scrollbar(frame_detail, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set); scrollbar.grid(row=0, column=1, sticky='ns')
        self._cap_nhat_treeview_all_pairs()

    def _load_selected_to_master_from_treeview(self, event):
        selected_item = self.tree.focus()
        if not selected_item: self._clear_master_form(); return
        values = self.tree.item(selected_item, 'values')
        if values:
            cach_cuc_raw_display = values[0]
            can_thien = cach_cuc_raw_display.split('/')[0]; can_dia = cach_cuc_raw_display.split('/')[1]
            cach_cuc_key = can_thien + can_dia 
            data = KY_MON_DATA["TRUCTU_TRANH"].get(cach_cuc_key, {})
            self._clear_master_form(clear_combo=False)
            self.combo_cach_cuc.set(cach_cuc_raw_display) 
            self.combo_cat_hung.set(data.get("Cát_Hung", "Bình"))
            self.text_luan_giai.insert("1.0", data.get("Luận_Giải", ""))

    def _load_selected_to_master_from_combo(self, event):
        cach_cuc_raw_display = self.combo_cach_cuc.get()
        if not cach_cuc_raw_display: self._clear_master_form(); return
        can_thien = cach_cuc_raw_display.split('/')[0]; can_dia = cach_cuc_raw_display.split('/')[1]
        cach_cuc_key = can_thien + can_dia 
        data = KY_MON_DATA["TRUCTU_TRANH"].get(cach_cuc_key, {})
        self._clear_master_form(clear_combo=False)
        self.combo_cach_cuc.set(cach_cuc_raw_display) 
        self.combo_cat_hung.set(data.get("Cát_Hung", "Bình"))
        self.text_luan_giai.insert("1.0", data.get("Luận_Giải", ""))
        
    def _clear_master_form(self, clear_combo=True):
        if hasattr(self, 'combo_cach_cuc') and clear_combo: self.combo_cach_cuc.set("") 
        if hasattr(self, 'text_luan_giai'): self.text_luan_giai.delete("1.0", tk.END)
        if hasattr(self, 'combo_cat_hung'): self.combo_cat_hung.set("Bình")

    def _cap_nhat_treeview_all_pairs(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        all_tranh_data = KY_MON_DATA["TRUCTU_TRANH"] 
        for key_lien_nhau, display_format in self.all_can_pairs:
            data = all_tranh_data.get(key_lien_nhau, {})
            cat_hung = data.get("Cát_Hung", "Bình") 
            luan_giai = data.get("Luận_Giải", "Chưa có nội dung.") 
            luan_giai_treeview = luan_giai[:50] + "..." if len(luan_giai) > 50 and luan_giai != "Chưa có nội dung." else luan_giai
            self.tree.insert("", tk.END, values=(display_format, cat_hung, luan_giai_treeview))

    def _luu_du_lieu_tuy_chinh(self):
        cach_cuc_raw_display = self.combo_cach_cuc.get().strip()
        cat_hung = self.combo_cat_hung.get()
        luan_giai = self.text_luan_giai.get("1.0", tk.END).strip()
        if not cach_cuc_raw_display or not luan_giai: messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn Cặp Can và nhập Luận Giải."); return
        try:
            can_thien = cach_cuc_raw_display.split('/')[0]; can_dia = cach_cuc_raw_display.split('/')[1]
            cach_cuc_key = can_thien + can_dia 
        except IndexError: messagebox.showerror("Lỗi Cú Pháp", "Giá trị Can/Can không hợp lệ."); return
        
        if cach_cuc_key in KY_MON_DATA["TRUCTU_TRANH"] and cach_cuc_key not in self.custom_data.get("TRUCTU_TRANH", {}):
            if not messagebox.askyesno("Xác nhận Ghi đè", f"Cách cục **{cach_cuc_raw_display}** là mặc định. Ghi đè?", parent=self.data_input_window): return

        if "TRUCTU_TRANH" not in self.custom_data: self.custom_data["TRUCTU_TRANH"] = {}
        self.custom_data["TRUCTU_TRANH"][cach_cuc_key] = {"Cát_Hung": cat_hung, "Luận_Giải": luan_giai}
        
        if save_custom_data(self.custom_data):
            self._merge_custom_data()
            self.lap_va_hien_thi_ban(is_default=False)
            self._cap_nhat_treeview_all_pairs()
            self._clear_master_form()
            messagebox.showinfo("Thành công", f"Đã lưu cách cục {cach_cuc_raw_display}!")

    def _xoa_du_lieu_tuy_chinh(self):
        cach_cuc_raw_display = self.combo_cach_cuc.get().strip()
        if not cach_cuc_raw_display: messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn Cặp Can cần xóa."); return
        try:
            can_thien = cach_cuc_raw_display.split('/')[0]; can_dia = cach_cuc_raw_display.split('/')[1]
            cach_cuc_key = can_thien + can_dia
        except IndexError: messagebox.showerror("Lỗi Cú Pháp", "Giá trị Can/Can không hợp lệ."); return

        if "TRUCTU_TRANH" in self.custom_data and cach_cuc_key in self.custom_data["TRUCTU_TRANH"]:
            if not messagebox.askyesno("Xác nhận Xóa", f"Xóa cách cục **{cach_cuc_raw_display}** khỏi dữ liệu tùy chỉnh?", parent=self.data_input_window): return
            del self.custom_data["TRUCTU_TRANH"][cach_cuc_key]
            if save_custom_data(self.custom_data):
                self._merge_custom_data()
                self.lap_va_hien_thi_ban(is_default=False)
                self._cap_nhat_treeview_all_pairs()
                self._clear_master_form()
                messagebox.showinfo("Thành công", f"Đã xóa cách cục {cach_cuc_raw_display}.")
        else: messagebox.showwarning("Không tìm thấy", f"Cách cục **{cach_cuc_raw_display}** không có trong dữ liệu tùy chỉnh.")

    def _mo_cua_so_nhap_lieu_cung_thuc_te(self):
        if self.cung_input_window and self.cung_input_window.winfo_exists(): self.cung_input_window.lift(); return

        window = Toplevel(self.master)
        window.title("✏️ Nhập/Sửa Dữ Liệu Các Cung (Thủ Công)")
        window.transient(self.master); window.resizable(False, False)
        self.cung_input_window = window
        
        frame_main = ttk.Frame(window, padding=10); frame_main.pack(fill='both', expand=True)

        tk.Label(frame_main, text="Chọn Cung Cần Sửa (1-9):", font=self.font_main).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        self.combo_cung_sua = ttk.Combobox(frame_main, values=[f"{i} - {QUAI_TUONG.get(i, '')}" for i in [1, 2, 3, 4, 6, 7, 8, 9]], width=20, state='readonly', font=self.font_cung_info)
        self.combo_cung_sua.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        self.combo_cung_sua.bind("<<ComboboxSelected>>", self._load_cung_data_to_manual_form)
        
        row_offset = 2
        tk.Label(frame_main, text="Sao (Tinh):", font=self.font_main).grid(row=row_offset, column=0, padx=5, pady=2, sticky='w'); row_offset += 1
        self.combo_manual_sao = ttk.Combobox(frame_main, values=SAO_9, width=15, state='readonly', font=self.font_cung_info); self.combo_manual_sao.grid(row=row_offset, column=0, padx=5, pady=2, sticky='w', columnspan=2); row_offset += 1
        
        tk.Label(frame_main, text="Cửa (Môn Chạy):", font=self.font_main).grid(row=row_offset, column=0, padx=5, pady=2, sticky='w'); row_offset += 1
        self.combo_manual_cua = ttk.Combobox(frame_main, values=CUA_8, width=15, state='readonly', font=self.font_cung_info); self.combo_manual_cua.grid(row=row_offset, column=0, padx=5, pady=2, sticky='w', columnspan=2); row_offset += 1
        
        tk.Label(frame_main, text="Thần (Bát Thần):", font=self.font_main).grid(row=row_offset, column=0, padx=5, pady=2, sticky='w'); row_offset += 1
        self.combo_manual_than = ttk.Combobox(frame_main, values=THAN_8, width=15, state='readonly', font=self.font_cung_info); self.combo_manual_than.grid(row=row_offset, column=0, padx=5, pady=2, sticky='w', columnspan=2); row_offset += 1
        
        tk.Label(frame_main, text="Can Thiên:", font=self.font_main).grid(row=row_offset, column=0, padx=5, pady=2, sticky='w'); row_offset += 1
        self.combo_manual_can_thien = ttk.Combobox(frame_main, values=CAN_10, width=15, state='readonly', font=self.font_cung_info); self.combo_manual_can_thien.grid(row=row_offset, column=0, padx=5, pady=2, sticky='w', columnspan=2); row_offset += 1
        
        tk.Label(frame_main, text="Can Địa:", font=self.font_main).grid(row=row_offset, column=0, padx=5, pady=2, sticky='w'); row_offset += 1
        self.combo_manual_can_dia = ttk.Combobox(frame_main, values=CAN_10, width=15, state='readonly', font=self.font_cung_info); self.combo_manual_can_dia.grid(row=row_offset, column=0, padx=5, pady=2, sticky='w', columnspan=2); row_offset += 1
        
        frame_buttons = ttk.Frame(frame_main)
        frame_buttons.grid(row=row_offset, column=0, columnspan=2, pady=10)
        ttk.Button(frame_buttons, text="Áp Dụng", command=self._save_manual_cung_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="Khôi Phục Mặc Định", command=self._reset_manual_cung_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_buttons, text="An Các Cung Khác (Mô Phỏng) 🔄", command=self._an_cac_cung_con_lai).pack(side=tk.LEFT, padx=5)

    def _load_cung_data_to_manual_form(self, event):
        selected_text = self.combo_cung_sua.get()
        if not selected_text: return
        cung_so = int(selected_text.split(" - ")[0])
        manual_data = self.manual_cung_data.get(cung_so, {})
        
        self.combo_manual_sao.set(manual_data.get('Sao', self.thien_ban.get(cung_so, 'N/A')))
        self.combo_manual_cua.set(manual_data.get('Cua', self.nhan_ban.get(cung_so, 'N/A')))
        self.combo_manual_than.set(manual_data.get('Than', self.than_ban.get(cung_so, 'N/A')))
        self.combo_manual_can_thien.set(manual_data.get('Can_Thien', self.can_thien_ban.get(cung_so, 'N/A')))
        self.combo_manual_can_dia.set(manual_data.get('Can_Dia', self.dia_can.get(cung_so, 'N/A')))

    def _save_manual_cung_data(self):
        selected_text = self.combo_cung_sua.get()
        if not selected_text: messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn Cung cần sửa.", parent=self.cung_input_window); return
        cung_so = int(selected_text.split(" - ")[0])
        new_data = {
            'Sao': self.combo_manual_sao.get(), 'Cua': self.combo_manual_cua.get(),
            'Than': self.combo_manual_than.get(), 'Can_Thien': self.combo_manual_can_thien.get(),
            'Can_Dia': self.combo_manual_can_dia.get()
        }
        if 'N/A' in new_data.values() or '' in new_data.values(): messagebox.showerror("Lỗi Dữ Liệu", "Vui lòng chọn đầy đủ thông tin.", parent=self.cung_input_window); return
        self.manual_cung_data[cung_so] = new_data
        self._tinh_toan_truoc_giai_thich()
        self.cap_nhat_cung_buttons()
        messagebox.showinfo("Thành công", f"Đã lưu dữ liệu thủ công cho Cung {cung_so}!", parent=self.cung_input_window)

    def _reset_manual_cung_data(self):
        selected_text = self.combo_cung_sua.get()
        if not selected_text: messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn Cung cần khôi phục.", parent=self.cung_input_window); return
        cung_so = int(selected_text.split(" - ")[0])
        if cung_so in self.manual_cung_data:
            if not messagebox.askyesno("Xác nhận Khôi Phục", f"Khôi phục dữ liệu mặc định cho Cung {cung_so}?", parent=self.cung_input_window): return
            del self.manual_cung_data[cung_so]
            self._tinh_toan_truoc_giai_thich()
            self.cap_nhat_cung_buttons()
            self._load_cung_data_to_manual_form(None)
            messagebox.showinfo("Thành công", f"Đã khôi phục dữ liệu mặc định cho Cung {cung_so}!", parent=self.cung_input_window)
        else: messagebox.showinfo("Thông báo", f"Cung {cung_so} không có dữ liệu thủ công.", parent=self.cung_input_window)

    def _an_cac_cung_con_lai(self):
        """Mô phỏng an bàn các cung còn lại dựa trên cung đã nhập thủ công (Quy luật: Sao/Cửa thuận, Thần tùy Âm/Dương)."""
        selected_text = self.combo_cung_sua.get()
        if not selected_text: messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn Cung khởi điểm và Áp Dụng trước.", parent=self.cung_input_window); return

        cung_khoi_diem = int(selected_text.split(" - ")[0])
        khoi_diem_data = self.manual_cung_data.get(cung_khoi_diem)
        if not khoi_diem_data: messagebox.showwarning("Thiếu dữ liệu", f"Cung {cung_khoi_diem} chưa có dữ liệu thủ công.", parent=self.cung_input_window); return

        try:
            cuc = int(self.entry_cuc.get())
            # Quy ước: Dương Độn (Cục > 0) -> Thần đi thuận. Âm Độn (Cục < 0 hoặc logic khác) -> Thần đi nghịch.
            # Ở đây dùng logic đơn giản: Cục Lẻ = Dương, Cục Chẵn = Âm (như code cũ) HOẶC dựa vào Tiết Khí nếu có.
            # Tạm dùng: Cục 1-9 là Dương, nếu user nhập số âm thì là Âm? 
            # Code cũ: is_duong_thuan = (cuc % 2 == 0) -> Âm Độn.
            # Sửa lại cho chuẩn hơn: Dương Độn (1,7,4...) -> Thần Thuận. Âm Độn (9,3,6...) -> Thần Nghịch.
            # Tạm thời giữ logic cũ của user để tránh break, nhưng cải tiến vòng xoay không gian.
            is_duong_don = (cuc % 2 != 0) # Giả sử lẻ là Dương Độn
        except ValueError: is_duong_don = True

        # 1. Định nghĩa thứ tự vòng tròn không gian (Spatial Clockwise)
        CUNG_CLOCKWISE = [1, 8, 3, 4, 9, 2, 7, 6]
        
        # 2. Định nghĩa thứ tự các thành phần (Luôn đi thuận trong danh sách này)
        # Sao: Bồng -> Nhậm -> Xung -> Phụ -> Anh -> Nhuế -> Trụ -> Tâm
        SAO_SEQ = ["Thiên Bồng", "Thiên Nhậm", "Thiên Xung", "Thiên Phụ", "Thiên Anh", "Thiên Nhuế", "Thiên Trụ", "Thiên Tâm"]
        # Cửa: Hưu -> Sinh -> Thương -> Đỗ -> Cảnh -> Tử -> Kinh -> Khai
        CUA_SEQ = ["Hưu", "Sinh", "Thương", "Đỗ", "Cảnh", "Tử", "Kinh", "Khai"]
        # Thần: Phù -> Xà -> Âm -> Hợp -> Hổ -> Vũ -> Địa -> Thiên
        THAN_SEQ = ["Trực Phù", "Đằng Xà", "Thái Âm", "Lục Hợp", "Bạch Hổ", "Huyền Vũ", "Cửu Địa", "Cửu Thiên"]
        # Can: Mậu -> Kỷ -> Canh -> Tân -> Nhâm -> Quý -> Đinh -> Bính -> Ất (Vòng Lục Nghi - Tam Kỳ)
        CAN_SEQ = ["Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý", "Đinh", "Bính", "Ất"]

        # 3. Lấy chỉ số bắt đầu
        try:
            start_idx_cung = CUNG_CLOCKWISE.index(cung_khoi_diem)
            start_sao = khoi_diem_data['Sao']
            start_cua = khoi_diem_data['Cua']
            start_than = khoi_diem_data['Than']
            start_can_thien = khoi_diem_data['Can_Thien']
            
            idx_sao = SAO_SEQ.index(start_sao) if start_sao in SAO_SEQ else 0
            idx_cua = CUA_SEQ.index(start_cua) if start_cua in CUA_SEQ else 0
            idx_than = THAN_SEQ.index(start_than) if start_than in THAN_SEQ else 0
            idx_can = CAN_SEQ.index(start_can_thien) if start_can_thien in CAN_SEQ else 0
            
        except ValueError: return 

        # 4. Vòng lặp điền các cung còn lại
        for i in range(1, 8): # Đi tiếp 7 cung còn lại
            current_cung_idx = (start_idx_cung + i) % 8
            current_cung = CUNG_CLOCKWISE[current_cung_idx]
            
            # Sao và Cửa luôn đi thuận (Clockwise)
            next_sao = SAO_SEQ[(idx_sao + i) % 8]
            next_cua = CUA_SEQ[(idx_cua + i) % 8]
            
            # Can Thiên đi thuận theo Sao (giả định vòng Can xoay cùng vòng Sao)
            next_can = CAN_SEQ[(idx_can + i) % 9] # Lưu ý: Can có 9, Sao có 8. Logic này chỉ là tương đối.
            # Nếu muốn chính xác tuyệt đối cần biết Can nào ẩn dưới Can nào.
            # Tạm thời dùng vòng 9 Can xoay.
            
            # Thần: Dương Độn đi Thuận, Âm Độn đi Nghịch
            if is_duong_don:
                next_than = THAN_SEQ[(idx_than + i) % 8]
            else:
                next_than = THAN_SEQ[(idx_than - i) % 8]
            
            self.manual_cung_data[current_cung] = {
                'Sao': next_sao,
                'Cua': next_cua,
                'Than': next_than,
                'Can_Thien': next_can,
                'Can_Dia': self.dia_can.get(current_cung, 'N/A')
            }
            
        self._tinh_toan_truoc_giai_thich()
        self.cap_nhat_cung_buttons()
        self._load_cung_data_to_manual_form(None)
        messagebox.showinfo("Thành công", "Đã mô phỏng an bàn các cung còn lại theo quy luật!", parent=self.cung_input_window)

    def _mo_cua_so_so_sanh(self):
        """Mở cửa sổ so sánh chi tiết Chủ-Khách với phân tích sâu"""
        window = Toplevel(self.master)
        window.title("⚖️ So Sánh Chi Tiết Chủ - Khách")
        window.transient(self.master)
        window.geometry("900x700")
        
        # Main frame với scrollbar
        main_frame = ttk.Frame(window)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        
        # Frame chọn cung
        frame_chon = ttk.LabelFrame(main_frame, text="📍 Chọn Cung So Sánh", padding=15)
        frame_chon.pack(fill='x', pady=(0, 10))
        
        cung_values = [f"{i} - {QUAI_TUONG.get(i, '')} ({CUNG_NGU_HANH.get(i)})" for i in range(1, 10)]
        
        tk.Label(frame_chon, text="Cung Chủ (Bên Mình):", font=self.font_main).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.combo_cung1 = ttk.Combobox(frame_chon, values=cung_values, state='readonly', width=30, font=self.font_cung_info)
        self.combo_cung1.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_chon, text="Cung Khách (Đối Phương):", font=self.font_main).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.combo_cung2 = ttk.Combobox(frame_chon, values=cung_values, state='readonly', width=30, font=self.font_cung_info)
        self.combo_cung2.grid(row=1, column=1, padx=5, pady=5)
        
        # Hiển thị chủ đề hiện tại (từ chủ đề chính)
        tk.Label(frame_chon, text="📌 Chủ Đề Phân Tích:", font=('Segoe UI', 10, 'bold'), fg='#e74c3c').grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.label_chu_de_hien_tai = tk.Label(frame_chon, text=self.chu_de_hien_tai, font=('Segoe UI', 11, 'bold'), fg='#2980b9')
        self.label_chu_de_hien_tai.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        
        # Frame kết quả với scrollbar
        frame_ket_qua = ttk.LabelFrame(main_frame, text="📊 Kết Quả Phân Tích Chi Tiết", padding=10)
        frame_ket_qua.pack(fill='both', expand=True)
        
        # Text widget với scrollbar
        text_scroll = tk.Scrollbar(frame_ket_qua)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_ket_qua = tk.Text(frame_ket_qua, wrap=tk.WORD, font=('Segoe UI', 10), 
                               yscrollcommand=text_scroll.set, bg='#f8f9fa')
        text_ket_qua.pack(side=tk.LEFT, fill='both', expand=True)
        text_scroll.config(command=text_ket_qua.yview)
        
        # Configure text tags for formatting
        text_ket_qua.tag_config('title', font=('Segoe UI', 14, 'bold'), foreground='#2c3e50')
        text_ket_qua.tag_config('section', font=('Segoe UI', 12, 'bold'), foreground='#3498db')
        text_ket_qua.tag_config('good', font=('Segoe UI', 10, 'bold'), foreground='#27ae60')
        text_ket_qua.tag_config('bad', font=('Segoe UI', 10, 'bold'), foreground='#e74c3c')
        text_ket_qua.tag_config('highlight', font=('Segoe UI', 11, 'bold'), foreground='#8e44ad')
        text_ket_qua.tag_config('neutral', font=('Segoe UI', 10), foreground='#7f8c8d')
        
        def thuc_hien_so_sanh_chi_tiet():
            v1 = self.combo_cung1.get()
            v2 = self.combo_cung2.get()
            chu_de = self.chu_de_hien_tai  # Sử dụng chủ đề toàn cục
            
            if not v1 or not v2:
                text_ket_qua.config(state=tk.NORMAL)
                text_ket_qua.delete('1.0', tk.END)
                text_ket_qua.insert('1.0', "⚠️ Vui lòng chọn cả 2 cung để so sánh!", 'bad')
                text_ket_qua.config(state=tk.DISABLED)
                return
            
            try:
                cung1 = int(v1.split(" - ")[0])
                cung2 = int(v2.split(" - ")[0])
                
                # Lấy thông tin chi tiết từng cung
                def get_cung_info(c):
                    manual = self.manual_cung_data.get(c, {})
                    c_int = int(c)
                    return {
                        'so': c_int,
                        'ten': QUAI_TUONG.get(c_int, 'N/A'),
                        'hanh': CUNG_NGU_HANH.get(c_int, 'N/A'),
                        'sao': manual.get('Sao', self.thien_ban.get(c_int, 'N/A')),
                        'cua': manual.get('Cua', self.nhan_ban.get(c_int, 'N/A')),
                        'than': manual.get('Than', self.than_ban.get(c_int, 'N/A')),
                        'can_thien': manual.get('Can_Thien', self.can_thien_ban.get(c_int, 'N/A')),
                        'can_dia': manual.get('Can_Dia', self.dia_can.get(c_int, 'N/A')),
                        'is_khong_vong': c_int in self.khong_vong_cung,
                        'is_dich_ma': c_int == self.dich_ma_cung
                    }
                
                chu = get_cung_info(cung1)
                khach = get_cung_info(cung2)
                
                # NEW: PHÂN TÍCH ĐA TẦNG - DỤNG THẦN LÀM TRUNG TÂM
                ket_qua_da_tang = None
                if USE_MULTI_LAYER_ANALYSIS:
                    try:
                        # Lấy đối tượng được chọn
                        doi_tuong_full = self.doi_tuong_var.get()
                        doi_tuong = doi_tuong_full.split(" ", 1)[1] if " " in doi_tuong_full else "Bản thân"
                        
                        # Lấy thời gian
                        try:
                            dt_str = self.entry_datetime.get()
                            dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
                        except:
                            dt_obj = datetime.now()
                        
                        # Gọi hàm phân tích toàn diện
                        ket_qua_da_tang = phan_tich_toan_dien(chu_de, chu, khach, dt_obj, doi_tuong)
                        
                        print(f"✅ Phân tích đa tầng thành công cho đối tượng: {doi_tuong}")
                    except Exception as e:
                        print(f"⚠️ Lỗi phân tích đa tầng: {e}")
                        import traceback
                        traceback.print_exc()
                
                # NEW: Lấy phân tích tổng hợp 4 phương pháp cho bối cảnh hiện tại
                try:
                    dt_str = self.entry_datetime.get()
                    dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
                    nam, thang, ngay, gio = dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour
                except:
                    now = datetime.now()
                    nam, thang, ngay, gio = now.year, now.month, now.day, now.hour

                # NEW: Gọi hàm phân tích siêu chi tiết 4 PHƯƠNG PHÁP CHUẨN
                dt_obj = datetime(nam, thang, ngay, gio)
                ket_qua_9pp = phan_tich_sieu_chi_tiet_chu_de(chu_de, chu, khach, dt_obj)
                tong_hop_standard = ket_qua_9pp["tong_hop"]
                
                # NEW: TỔNG HỢP 3 PHƯƠNG PHÁP (KỲ MÔN + MAI HOA + KINH DỊCH)
                try:
                    from tong_hop_3_phuong_phap_chu_de import (
                        tong_hop_3_phuong_phap_cho_chu_de,
                        tao_bao_cao_tong_hop_3pp
                    )
                    
                    ket_qua_3pp = tong_hop_3_phuong_phap_cho_chu_de(chu_de, chu, khach, dt_obj)
                    co_tong_hop_3pp = True
                except Exception as e:
                    print(f"Lỗi tổng hợp 3 phương pháp: {e}")
                    co_tong_hop_3pp = False
                
                # NEW: Gọi hàm tạo phân tích liền mạch kết hợp 9 phương pháp
                mqh_chu_khach = tinh_ngu_hanh_sinh_khac(chu['hanh'], khach['hanh'])
                phan_tich_lien_mach = tao_phan_tich_lien_mach(chu_de, chu, khach, dt_obj, ket_qua_9pp, mqh_chu_khach)
                
                # Tính điểm từ hệ thống cũ để tương thích
                ket_qua_diem = self._tong_hop_diem_da_chieu(chu, khach, chu_de, dt_obj)
                diem_chu = ket_qua_diem['diem_chu']
                diem_khach = ket_qua_diem['diem_khach']
                breakdown = ket_qua_diem['breakdown']
                
                # Xác định mức độ nguy hiểm
                if diem_chu >= 71:
                    muc_do_nguy_hiem = "🔵 RẤT THUẬN LỢI"
                    mau_muc_do = 'good'
                elif diem_chu >= 55:
                    muc_do_nguy_hiem = "🟢 AN TOÀN - CÓ LỢI THẾ"
                    mau_muc_do = 'good'
                elif diem_chu >= 46:
                    muc_do_nguy_hiem = "🟡 CẨN TRỌNG - NGANG SỨC"
                    mau_muc_do = 'neutral'
                elif diem_chu >= 31:
                    muc_do_nguy_hiem = "🟠 NGUY HIỂM - BẤT LỢI"
                    mau_muc_do = 'bad'
                else:
                    muc_do_nguy_hiem = "🔴 CỰC KỲ NGUY HIỂM"
                    mau_muc_do = 'bad'
                
                # Tạo nội dung phân tích
                text_ket_qua.config(state=tk.NORMAL)
                text_ket_qua.delete('1.0', tk.END)
                
                # Tiêu đề
                text_ket_qua.insert(tk.END, "⚖️ SIÊU DỰ ĐOÁN TỔNG HỢP - CHI TIẾT MỌI CHÂN TƠ KẼ TÓC\n", 'title')
                text_ket_qua.insert(tk.END, f"Chủ đề: {chu_de}\n", 'neutral')
                text_ket_qua.insert(tk.END, f"Thời gian lập quẻ: {dt_obj.strftime('%H:%M - %d/%m/%Y')}\n", 'neutral')
                text_ket_qua.insert(tk.END, f"Độ tin cậy hệ thống: {ket_qua_9pp['do_tin_cay_tong']}%\n\n", 'highlight')
                
                # NEW: PHẦN 0 - PHÂN TÍCH ĐA TẦNG (DỤNG THẦN LÀM TRUNG TÂM)
                if ket_qua_da_tang:
                    text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                    text_ket_qua.insert(tk.END, "🎯 PHÂN TÍCH ĐA TẦNG - DỤNG THẦN LÀM TRUNG TÂM\n\n", 'section')
                    
                    # 1. Hiển thị Dụng Thần được chọn
                    dung_than_info = ket_qua_da_tang.get('dung_than', {})
                    text_ket_qua.insert(tk.END, f"🔮 DỤNG THẦN: {dung_than_info.get('ten', 'N/A')}\n", 'highlight')
                    if dung_than_info.get('dung_than_phu'):
                        text_ket_qua.insert(tk.END, f"   Dụng Thần phụ: {', '.join(dung_than_info['dung_than_phu'])}\n")
                    text_ket_qua.insert(tk.END, "\n")
                    
                    # 2. Hiển thị Lục Thân - Đối tượng
                    luc_than_info = ket_qua_da_tang.get('luc_than', {})
                    sinh_khac_info = ket_qua_da_tang.get('sinh_khac_luc_than', {})
                    
                    text_ket_qua.insert(tk.END, "👥 ĐỐI TƯỢNG PHÂN TÍCH (LỤC THÂN):\n", 'highlight')
                    text_ket_qua.insert(tk.END, f"   {luc_than_info.get('icon', '')} {luc_than_info.get('type', 'N/A')}\n")
                    text_ket_qua.insert(tk.END, f"   Mô tả: {luc_than_info.get('mo_ta', 'N/A')}\n")
                    
                    if sinh_khac_info:
                        quan_he = sinh_khac_info.get('quan_he', 'N/A')
                        loai = sinh_khac_info.get('loai', '')
                        diem = sinh_khac_info.get('diem', 0)
                        
                        # Xác định màu sắc dựa trên điểm
                        if diem >= 80:
                            mau_luc_than = 'good'
                            bieu_tuong = '✅'
                        elif diem >= 60:
                            mau_luc_than = 'neutral'
                            bieu_tuong = '⚠️'
                        else:
                            mau_luc_than = 'bad'
                            bieu_tuong = '❌'
                        
                        text_ket_qua.insert(tk.END, f"\n   {bieu_tuong} MỐI QUAN HỆ: {quan_he} ({loai})\n", mau_luc_than)
                        text_ket_qua.insert(tk.END, f"   Điểm số: {diem}/100\n", mau_luc_than)
                        text_ket_qua.insert(tk.END, f"   Ý nghĩa: {sinh_khac_info.get('y_nghia', 'N/A')}\n")
                        text_ket_qua.insert(tk.END, f"   Lời khuyên: {sinh_khac_info.get('loi_khuyen', 'N/A')}\n")
                    text_ket_qua.insert(tk.END, "\n")
                    
                    # 3. Hiển thị Điểm Tổng Hợp
                    diem_tong = ket_qua_da_tang.get('diem_tong', 0)
                    ket_luan = ket_qua_da_tang.get('ket_luan', 'N/A')
                    mau_sac = ket_qua_da_tang.get('mau_sac', '#000000')
                    
                    # Chuyển màu hex sang tag
                    if diem_tong >= 80:
                        mau_tag = 'good'
                    elif diem_tong >= 50:
                        mau_tag = 'neutral'
                    else:
                        mau_tag = 'bad'
                    
                    text_ket_qua.insert(tk.END, "📊 ĐIỂM TỔNG HỢP ĐA TẦNG:\n", 'highlight')
                    text_ket_qua.insert(tk.END, f"   🎯 Tổng điểm: {diem_tong}/100\n", mau_tag)
                    text_ket_qua.insert(tk.END, f"   • Trong cung: {ket_qua_da_tang.get('diem_trong_cung', 0)}/100\n")
                    text_ket_qua.insert(tk.END, f"   • Giữa các cung: {ket_qua_da_tang.get('diem_giua_cung', 0)}/100\n")
                    text_ket_qua.insert(tk.END, f"   • Thời gian: {ket_qua_da_tang.get('diem_thoi_gian', 0)}/100\n")
                    text_ket_qua.insert(tk.END, f"\n   💡 KẾT LUẬN: {ket_luan}\n\n", mau_tag)
                    
                    # 4. Chi tiết phân tích trong cung
                    chi_tiet = ket_qua_da_tang.get('chi_tiet', {})
                    if chi_tiet.get('chu'):
                        text_ket_qua.insert(tk.END, "🔍 CHI TIẾT PHÂN TÍCH TRONG CUNG:\n", 'highlight')
                        
                        for role, cung_data in [("CHỦ", chi_tiet.get('chu', {})), ("KHÁCH", chi_tiet.get('khach', {}))]:
                            text_ket_qua.insert(tk.END, f"\n   ▸ {role}:\n")
                            chi_tiet_cung = cung_data.get('chi_tiet', {})
                            
                            for yeu_to in ['sao', 'mon', 'than', 'ngu_hanh']:
                                if yeu_to in chi_tiet_cung:
                                    info = chi_tiet_cung[yeu_to]
                                    text_ket_qua.insert(tk.END, f"     • {yeu_to.capitalize()}: {info.get('ten', 'N/A')} ({info.get('diem', 0)}/100)\n")
                                    text_ket_qua.insert(tk.END, f"       → {info.get('y_nghia', 'N/A')}\n")
                        text_ket_qua.insert(tk.END, "\n")
                    
                    text_ket_qua.insert(tk.END, "═" * 80 + "\n\n", 'neutral')
                
                # PHẦN 1: CHIẾN LƯỢC & VỊ THẾ (KỲ MÔN + PDF ADVANCED)
                text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                text_ket_qua.insert(tk.END, "🏆 PHÂN TÍCH CHIẾN LƯỢC & TƯỢNG Ý BÍ TRUYỀN\n\n", 'section')
                
                # Cơ chế tự sửa lỗi KeyError
                analysis_key = 'phan_tich_9_phuong_phap' if 'phan_tich_9_phuong_phap' in ket_qua_9pp else 'phan_tich_chuyen_sau'
                if analysis_key in ket_qua_9pp and 'ky_mon' in ket_qua_9pp[analysis_key]:
                    text_ket_qua.insert(tk.END, ket_qua_9pp[analysis_key]['ky_mon']['ket_luan'] + "\n\n", 'highlight')

                # PHẦN 2: QUÁ KHỨ - HIỆN TẠI - TƯƠNG LAI (LIÊN MẠCH)
                text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                text_ket_qua.insert(tk.END, "🪐 DÒNG CHẢY BIẾN HÓA (TAM THỨC & BÁT TỰ HỢP NHẤT)\n\n", 'section')
                
                # Tích hợp Tương tác đặc biệt từ PDF vào dòng chảy logic
                from super_detailed_analysis import _phan_tich_tuong_tac_nang_cao
                tuong_tac_pdf = _phan_tich_tuong_tac_nang_cao(chu, khach)
                if tuong_tac_pdf:
                    text_ket_qua.insert(tk.END, "🔗 TƯƠNG TÁC ĐẶC BIỆT (BÍ TRUYỀN PDF):\n", 'highlight')
                    text_ket_qua.insert(tk.END, tuong_tac_pdf + "\n\n")
                
                # Quá khứ
                text_ket_qua.insert(tk.END, phan_tich_lien_mach['qua_khu'] + "\n\n")
                text_ket_qua.insert(tk.END, "─" * 40 + "\n\n")
                
                # Hiện tại
                text_ket_qua.insert(tk.END, phan_tich_lien_mach['hien_tai'] + "\n\n")
                text_ket_qua.insert(tk.END, "─" * 40 + "\n\n")
                
                # Tương lai
                text_ket_qua.insert(tk.END, phan_tich_lien_mach['tuong_lai'] + "\n\n")
                
                # PHẦN 3: TRUY VẾT DIỄN BIẾN (LỤC NHÂM & THÁM TỬ)
                text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                text_ket_qua.insert(tk.END, "📋 KỊCH BẢN DIỄN BIẾN CHI TIẾT\n\n", 'section')
                text_ket_qua.insert(tk.END, phan_tich_lien_mach['su_viec_se_xay_ra'] + "\n\n")
                
                # PHẦN 4: THỜI GIAN VÀ THỜI ĐIỂM CỤ THỂ
                text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                text_ket_qua.insert(tk.END, "📅 THỜI GIAN VÀ THỜI ĐIỂM ỨNG NGHIỆM\n\n", 'section')
                text_ket_qua.insert(tk.END, phan_tich_lien_mach['thoi_gian_cu_the'] + "\n\n")
                
                # PHẦN 4: THÔNG TIN CHI TIẾT KHÁC (THEO CHỦ ĐỀ)
                if ket_qua_9pp['chi_tiet_tung_khia_canh']:
                    text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                    text_ket_qua.insert(tk.END, f"🔍 HỒ SƠ THÁM TỬ & MANH MỐI {chu_de.upper()}\n\n", 'section')
                    
                    for khia_canh_key, khia_canh_data in ket_qua_9pp['chi_tiet_tung_khia_canh'].items():
                        tieu_de_hien_thi = khia_canh_data.get('tieu_de', khia_canh_key)
                        text_ket_qua.insert(tk.END, f"▸ {tieu_de_hien_thi}:\n", 'highlight')
                        for noi_dung in khia_canh_data.get('noi_dung', []):
                            text_ket_qua.insert(tk.END, f"  {noi_dung}\n")
                        text_ket_qua.insert(tk.END, "\n")
                
                # HIỂN THỊ DỮ LIỆU BỔ SUNG TỪ ẢNH (NẾU CÓ)
                advanced_kb = KY_MON_DATA.get("ADVANCED_KNOWLEDGE", {})
                image_data = advanced_kb.get("IMAGE_EXTRACTED_DATA", {})
                if chu_de in image_data:
                    text_ket_qua.insert(tk.END, "🖼️ DỮ LIỆU BỔ SUNG TỪ ẢNH/SƠ ĐỒ:\n", 'section')
                    text_ket_qua.insert(tk.END, image_data[chu_de] + "\n\n", 'highlight')
                
                # PHẦN 5: TỔNG KẾT VÀ CHỈ DẪN HÀNH ĐỘNG
                text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                text_ket_qua.insert(tk.END, phan_tich_lien_mach['ket_luan_tong_hop'] + "\n\n")
                
                # PHẦN 6: KẾT LUẬN TỔNG HỢP TỪ ENGINE DỰ ĐOÁN CHÍNH XÁC
                if 'tong_hop' in ket_qua_9pp and ket_qua_9pp['tong_hop']:
                    text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                    text_ket_qua.insert(tk.END, "🎯 KẾT LUẬN TỔNG HỢP CHUYÊN SÂU\n\n", 'section')
                    
                    tong_hop = ket_qua_9pp['tong_hop']
                    
                    # Hiển thị kết luận cuối cùng nếu có
                    if 'ket_luan_cuoi_cung' in tong_hop and tong_hop['ket_luan_cuoi_cung']:
                        text_ket_qua.insert(tk.END, tong_hop['ket_luan_cuoi_cung'] + "\n\n")
                    else:
                        # Hiển thị từng phần nếu không có kết luận tổng hợp
                        if 'qua_khu' in tong_hop:
                            text_ket_qua.insert(tk.END, tong_hop['qua_khu'] + "\n")
                        
                        if 'hien_tai' in tong_hop:
                            text_ket_qua.insert(tk.END, tong_hop['hien_tai'] + "\n")
                        
                        if 'tuong_lai' in tong_hop:
                            text_ket_qua.insert(tk.END, tong_hop['tuong_lai'] + "\n")
                        
                        # Hành động nên làm
                        if 'hanh_dong_nen_lam' in tong_hop and tong_hop['hanh_dong_nen_lam']:
                            text_ket_qua.insert(tk.END, "\nHÀNH ĐỘNG NÊN LÀM:\n", 'highlight')
                            for i, hanh_dong in enumerate(tong_hop['hanh_dong_nen_lam'], 1):
                                text_ket_qua.insert(tk.END, f"{i}. {hanh_dong}\n", 'good')
                        
                        # Hành động nên tránh
                        if 'hanh_dong_tranh' in tong_hop and tong_hop['hanh_dong_tranh']:
                            text_ket_qua.insert(tk.END, "\nHÀNH ĐỘNG NÊN TRÁNH:\n", 'highlight')
                            for i, hanh_dong in enumerate(tong_hop['hanh_dong_tranh'], 1):
                                text_ket_qua.insert(tk.END, f"{i}. {hanh_dong}\n", 'bad')
                        
                        # Thời gian ứng nghiệm
                        if 'thoi_gian_ung_nghiem' in tong_hop:
                            text_ket_qua.insert(tk.END, f"\nTHỜI GIAN ỨNG NGHIỆM: {tong_hop['thoi_gian_ung_nghiem']}\n\n", 'highlight')
                
                # PHẦN 7: TỔNG HỢP 3 PHƯƠNG PHÁP (KỲ MÔN + MAI HOA + KINH DỊCH)
                if co_tong_hop_3pp:
                    text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                    text_ket_qua.insert(tk.END, "🔮 TỔNG HỢP 3 PHƯƠNG PHÁP: KỲ MÔN + MAI HOA + KINH DỊCH\n\n", 'section')
                    
                    # Hiển thị kết luận từ 3 phương pháp
                    text_ket_qua.insert(tk.END, ket_qua_3pp['ket_luan_tong_hop'] + "\n\n", 'highlight')
                    
                    # Thêm nút xem chi tiết
                    text_ket_qua.insert(tk.END, "💡 Nhấn nút 'Xem Chi Tiết 3 Phương Pháp' bên dưới để xem phân tích đầy đủ từ Mai Hoa và Lục Hào\n\n", 'neutral')
                
                
                # Bổ sung thông tin kỹ thuật (nếu cần xem sâu)
                text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                text_ket_qua.insert(tk.END, "📊 DỮ LIỆU KỸ THUẬT BỔ TRỢ & TRA CỨU CHI TIẾT\n\n", 'section')
                text_ket_qua.insert(tk.END, f"Mức Độ: {muc_do_nguy_hiem} | Điểm Chủ: {diem_chu}/100\n", mau_muc_do)
                text_ket_qua.insert(tk.END, f"Nhận định tổng hợp (Refined): {tong_hop_standard['nhan_dinh']}\n\n")

                # NEW: Hiển thị thuộc tính chi tiết từ Excel cho cả 2 phía
                for role, palace_info in [("CHỦ (BÊN MÌNH)", chu), ("KHÁCH (ĐỐI PHƯƠNG)", khach)]:
                    from super_detailed_analysis import _get_enriched_info
                    text_ket_qua.insert(tk.END, f"🔹 THUỘC TÍNH CHI TIẾT - {role}\n", 'highlight')
                    
                    # Tra cứu các thành phần
                    for label, name in [("Môn", palace_info['cua']), ("Sao", palace_info['sao']), ("Can", palace_info['can_thien'])]:
                        info = _get_enriched_info(name)
                        if info:
                            traits = []
                            if info.get('KHÁI NIỆM'): traits.append(f"Khái niệm: {info['KHÁI NIỆM']}")
                            if info.get('TÍNH TÌNH'): traits.append(f"Tính tình: {info['TÍNH TÌNH']}")
                            if info.get('NHÂN VẬT'): traits.append(f"Nhân vật: {info['NHÂN VẬT']}")
                            if info.get('HÌNH THÁI'): traits.append(f"Hình thái: {info['HÌNH THÁI']}")
                            
                            if traits:
                                text_ket_qua.insert(tk.END, f"  • {label} {name}:\n")
                                for t in traits:
                                    text_ket_qua.insert(tk.END, f"    - {t}\n")
                    text_ket_qua.insert(tk.END, "\n")
                
                # NEW: PHẦN PHÂN TÍCH TƯỢNG Ý SÂU SẮC TỪ TẤT CẢ NGUỒN
                text_ket_qua.insert(tk.END, "═" * 80 + "\n", 'neutral')
                text_ket_qua.insert(tk.END, "🎭 PHÂN TÍCH TƯỢNG Ý SÂU SẮC (TỪ LỤC HÀO, MAI HOA DỊCH SỐ)\n\n", 'section')
                
                for role, palace_info in [("CHỦ (BÊN MÌNH)", chu), ("KHÁCH (ĐỐI PHƯƠNG)", khach)]:
                    text_ket_qua.insert(tk.END, f"▸ {role}\n", 'highlight')
                    
                    # Lấy thông tin tổng hợp
                    try:
                        comprehensive_info = get_comprehensive_palace_info(palace_info)
                        
                        # 1. Phân tích Quẻ Tượng
                        qua_info = comprehensive_info['qua']
                        if qua_info and qua_info.get('khai_niem'):
                            text_ket_qua.insert(tk.END, f"\n  🔮 QUẺ {qua_info['ten']} (Cung {palace_info['so']}):\n")
                            if qua_info.get('khai_niem'):
                                text_ket_qua.insert(tk.END, f"    📖 Khái niệm: {qua_info['khai_niem'][:200]}...\n")
                            if qua_info.get('nhan_vat'):
                                text_ket_qua.insert(tk.END, f"    👥 Nhân vật: {qua_info['nhan_vat'][:150]}...\n")
                            if qua_info.get('dia_ly'):
                                text_ket_qua.insert(tk.END, f"    🗺️ Địa lý: {qua_info['dia_ly'][:150]}...\n")
                        
                        # 2. Phân tích Sao (Cửu Tinh)
                        sao_info = comprehensive_info['sao']
                        if sao_info and sao_info.get('khai_niem'):
                            text_ket_qua.insert(tk.END, f"\n  ⭐ SAO {sao_info['ten']}:\n")
                            if sao_info.get('khai_niem'):
                                text_ket_qua.insert(tk.END, f"    💫 Khái niệm: {sao_info['khai_niem'][:200]}...\n")
                            if sao_info.get('nhan_vat'):
                                text_ket_qua.insert(tk.END, f"    🧑 Nhân vật: {sao_info['nhan_vat'][:150]}...\n")
                            if sao_info.get('dong_vat'):
                                text_ket_qua.insert(tk.END, f"    🐾 Động vật: {sao_info['dong_vat']}\n")
                        
                        # 3. Phân tích Môn (Bát Môn)
                        mon_info = comprehensive_info['mon']
                        if mon_info and mon_info.get('khai_niem'):
                            text_ket_qua.insert(tk.END, f"\n  🚪 MÔN {mon_info['ten']}:\n")
                            if mon_info.get('khai_niem'):
                                text_ket_qua.insert(tk.END, f"    📚 Khái niệm: {mon_info['khai_niem'][:200]}...\n")
                            if mon_info.get('dia_ly'):
                                text_ket_qua.insert(tk.END, f"    📍 Địa lý: {mon_info['dia_ly'][:150]}...\n")
                        
                        # 4. Phân tích Can Thiên & Can Địa
                        can_thien_info = comprehensive_info['can_thien']
                        can_dia_info = comprehensive_info['can_dia']
                        
                        if can_thien_info and can_thien_info.get('khai_niem'):
                            text_ket_qua.insert(tk.END, f"\n  📜 CAN THIÊN {can_thien_info['ten']}:\n")
                            if can_thien_info.get('khai_niem'):
                                text_ket_qua.insert(tk.END, f"    ✨ Khái niệm: {can_thien_info['khai_niem'][:200]}...\n")
                        
                        if can_dia_info and can_dia_info.get('khai_niem'):
                            text_ket_qua.insert(tk.END, f"\n  📜 CAN ĐỊA {can_dia_info['ten']}:\n")
                            if can_dia_info.get('khai_niem'):
                                text_ket_qua.insert(tk.END, f"    ✨ Khái niệm: {can_dia_info['khai_niem'][:200]}...\n")
                        
                        # 5. Tổng hợp Tượng Ý cho Chủ Đề
                        text_ket_qua.insert(tk.END, f"\n  🎯 ÁP DỤNG VÀO CHỦ ĐỀ '{chu_de.upper()}':\n")
                        
                        # Kết hợp tất cả tượng ý để đưa ra kết luận cụ thể
                        tuong_y_lines = []
                        
                        # Từ Quẻ
                        if qua_info.get('nhan_vat'):
                            tuong_y_lines.append(f"    • Nhân vật liên quan: {qua_info['nhan_vat'][:100]}...")
                        if qua_info.get('dia_ly'):
                            tuong_y_lines.append(f"    • Địa điểm: {qua_info['dia_ly'][:100]}...")
                        
                        # Từ Sao
                        if sao_info.get('dong_vat'):
                            tuong_y_lines.append(f"    • Biểu tượng động vật: {sao_info['dong_vat']}")
                        if sao_info.get('thuc_vat'):
                            tuong_y_lines.append(f"    • Biểu tượng thực vật: {sao_info['thuc_vat']}")
                        
                        # Từ Môn
                        if mon_info.get('tinh_vat'):
                            tuong_y_lines.append(f"    • Vật phẩm liên quan: {mon_info['tinh_vat'][:100]}...")
                        
                        # Hiển thị
                        if tuong_y_lines:
                            for line in tuong_y_lines:
                                text_ket_qua.insert(tk.END, line + "\n")
                        else:
                            text_ket_qua.insert(tk.END, "    (Đang tổng hợp dữ liệu...)\n")
                    
                    except Exception as e:
                        text_ket_qua.insert(tk.END, f"    ⚠️ Lỗi khi tải dữ liệu tượng ý: {str(e)}\n")
                    
                    text_ket_qua.insert(tk.END, "\n")

                text_ket_qua.config(state=tk.DISABLED)
            except Exception as e:
                import traceback
                error_details = traceback.format_exc()
                text_ket_qua.config(state=tk.NORMAL)
                text_ket_qua.delete('1.0', tk.END)
                text_ket_qua.insert(tk.END, f"❌ LỖI HỆ THỐNG:\n\n{str(e)}\n\nChi tiết kỹ thuật:\n{error_details}", 'bad')
                text_ket_qua.config(state=tk.DISABLED)
        
        ttk.Button(frame_chon, text="🔍 Phân Tích Chi Tiết", command=thuc_hien_so_sanh_chi_tiet, 
                  style='Accent.TButton').grid(row=3, column=0, columnspan=2, pady=15)
    
    # ======================================================================
    # CÁC PHƯƠNG THỨC TÍNH ĐIỂM ĐA CHIỀU CHO SO SÁNH CHỦ-KHÁCH
    # ======================================================================
    
    def _tinh_diem_ngu_hanh_chi_tiet(self, chu, khach, thoi_gian_hien_tai):
        """
        Tính điểm Ngũ Hành chi tiết (30% tổng điểm)
        Bao gồm: Sinh khắc trực tiếp, sinh khắc gián tiếp, vượng suy theo mùa
        """
        diem_chu = 50  # Điểm gốc
        diem_khach = 50
        chi_tiet = []
        
        # 1. Sinh khắc trực tiếp Cung vs Cung
        mqh = tinh_ngu_hanh_sinh_khac(chu['hanh'], khach['hanh'])
        
        v_chu = chu.get('vai_tro', 'Chủ')
        v_khach = khach.get('vai_tro', 'Khách')
        
        if "Sinh" in mqh and chu['hanh'] in mqh.split()[0]:
            # Chủ sinh Khách - mất lợi
            diem_chu -= 15
            diem_khach += 15
            chi_tiet.append(f"❌ {v_chu} ({chu['hanh']}) sinh {v_khach} ({khach['hanh']}) → {v_chu} mất năng lượng")
        elif "Sinh" in mqh:
            # Khách sinh Chủ - được lợi
            diem_chu += 15
            diem_khach -= 15
            chi_tiet.append(f"✅ {v_khach} ({khach['hanh']}) sinh {v_chu} ({chu['hanh']}) → {v_chu} được bồi bổ")
        elif "Khắc" in mqh and chu['hanh'] in mqh.split()[0]:
            # Chủ khắc Khách - chiếm ưu thế
            diem_chu += 25
            diem_khach -= 25
            chi_tiet.append(f"✅ {v_chu} ({chu['hanh']}) khắc {v_khach} ({khach['hanh']}) → {v_chu} áp đảo cục diện")
        elif "Khắc" in mqh:
            # Khách khắc Chủ - bị áp đảo
            diem_chu -= 25
            diem_khach += 25
            chi_tiet.append(f"❌ {v_khach} ({khach['hanh']}) khắc {v_chu} ({chu['hanh']}) → {v_chu} bị khống chế")
        else:
            chi_tiet.append(f"⚖️ {v_chu} và {v_khach} hòa khí → Ngang sức")
        
        # 2. Sinh khắc gián tiếp: Sao vs Cung
        sao_chu_hanh = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['CUU_TINH'].get(chu['sao'], {}).get('Hành', 'N/A')
        sao_khach_hanh = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['CUU_TINH'].get(khach['sao'], {}).get('Hành', 'N/A')
        
        mqh_sao_chu = tinh_ngu_hanh_sinh_khac(sao_chu_hanh, chu['hanh'])
        if "Sinh" in mqh_sao_chu and sao_chu_hanh in mqh_sao_chu.split()[0]:
            diem_chu += 5
            chi_tiet.append(f"  • Sao {chu['sao']} ({sao_chu_hanh}) sinh Cung → +5 điểm Chủ")
        elif "Khắc" in mqh_sao_chu and chu['hanh'] in mqh_sao_chu.split()[0]:
            diem_chu -= 5
            chi_tiet.append(f"  • Cung khắc Sao {chu['sao']} → -5 điểm Chủ")
        
        # 3. Vượng suy theo mùa (dựa vào tháng hiện tại)
        thang_hien_tai = thoi_gian_hien_tai.month
        
        # Mùa Xuân (1-3): Mộc vượng, Hỏa tướng, Thủy hưu, Kim tù, Thổ tử
        # Mùa Hạ (4-6): Hỏa vượng, Thổ tướng, Mộc hưu, Thủy tù, Kim tử
        # Mùa Thu (7-9): Kim vượng, Thủy tướng, Thổ hưu, Hỏa tù, Mộc tử
        # Mùa Đông (10-12): Thủy vượng, Mộc tướng, Kim hưu, Thổ tù, Hỏa tử
        
        VUONG_SUY = {
            1: {"Mộc": 10, "Hỏa": 5, "Thủy": 0, "Kim": -5, "Thổ": -10},
            2: {"Mộc": 10, "Hỏa": 5, "Thủy": 0, "Kim": -5, "Thổ": -10},
            3: {"Mộc": 10, "Hỏa": 5, "Thủy": 0, "Kim": -5, "Thổ": -10},
            4: {"Hỏa": 10, "Thổ": 5, "Mộc": 0, "Thủy": -5, "Kim": -10},
            5: {"Hỏa": 10, "Thổ": 5, "Mộc": 0, "Thủy": -5, "Kim": -10},
            6: {"Hỏa": 10, "Thổ": 5, "Mộc": 0, "Thủy": -5, "Kim": -10},
            7: {"Kim": 10, "Thủy": 5, "Thổ": 0, "Hỏa": -5, "Mộc": -10},
            8: {"Kim": 10, "Thủy": 5, "Thổ": 0, "Hỏa": -5, "Mộc": -10},
            9: {"Kim": 10, "Thủy": 5, "Thổ": 0, "Hỏa": -5, "Mộc": -10},
            10: {"Thủy": 10, "Mộc": 5, "Kim": 0, "Thổ": -5, "Hỏa": -10},
            11: {"Thủy": 10, "Mộc": 5, "Kim": 0, "Thổ": -5, "Hỏa": -10},
            12: {"Thủy": 10, "Mộc": 5, "Kim": 0, "Thổ": -5, "Hỏa": -10}
        }
        
        diem_vuong_chu = VUONG_SUY.get(thang_hien_tai, {}).get(chu['hanh'], 0)
        diem_vuong_khach = VUONG_SUY.get(thang_hien_tai, {}).get(khach['hanh'], 0)
        
        diem_chu += diem_vuong_chu
        diem_khach += diem_vuong_khach
        
        if diem_vuong_chu > 0:
            chi_tiet.append(f"  • {chu['hanh']} đang vượng (tháng {thang_hien_tai}) → +{diem_vuong_chu} điểm Chủ")
        elif diem_vuong_chu < 0:
            chi_tiet.append(f"  • {chu['hanh']} đang suy (tháng {thang_hien_tai}) → {diem_vuong_chu} điểm Chủ")
        
        return {
            'diem_chu': diem_chu,
            'diem_khach': diem_khach,
            'chi_tiet': chi_tiet
        }
    
    def _tinh_diem_sao_mon_than(self, chu, khach):
        """
        Tính điểm Sao-Môn-Thần (25% tổng điểm)
        """
        diem_chu = 50
        diem_khach = 50
        chi_tiet = []
        
        # 1. Điểm Môn (Bát Môn)
        cua_chu_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_MON"].get(chu['cua'] + " Môn", {})
        cua_khach_data = KY_MON_DATA["DU_LIEU_DUNG_THAN_PHU_TRO"]["BAT_MON"].get(khach['cua'] + " Môn", {})
        
        cat_hung_chu = cua_chu_data.get("Cát_Hung", "Bình")
        cat_hung_khach = cua_khach_data.get("Cát_Hung", "Bình")
        
        DIEM_MON = {"Đại Cát": 25, "Cát": 15, "Bình": 0, "Hung": -15, "Đại Hung": -25}
        
        v_chu = chu.get('vai_tro', 'Chủ')
        v_khach = khach.get('vai_tro', 'Khách')
        
        diem_mon_chu = DIEM_MON.get(cat_hung_chu, 0)
        diem_mon_khach = DIEM_MON.get(cat_hung_khach, 0)
        diem_chu += diem_mon_chu
        diem_khach += diem_mon_khach
        
        chi_tiet.append(f"🚪 Môn {v_chu}: {chu['cua']} ({cat_hung_chu}) → {'+' if diem_mon_chu >= 0 else ''}{diem_mon_chu} điểm")
        chi_tiet.append(f"🚪 Môn {v_khach}: {khach['cua']} ({cat_hung_khach}) → {'+' if diem_mon_khach >= 0 else ''}{diem_mon_khach} điểm")
        
        # 2. Điểm Thần (Bát Thần)
        THAN_TOT = ["Trực Phù", "Lục Hợp", "Cửu Thiên", "Thái Âm"]
        THAN_XAU = ["Bạch Hổ", "Huyền Vũ", "Đằng Xà"]
        THAN_BINH = ["Cửu Địa"]
        
        v_khach = khach.get('vai_tro', 'Khách')
        
        # Thần Chủ
        if chu['than'] in THAN_TOT:
            diem_chu += 10
            chi_tiet.append(f"  • Thần {chu['than']} hỗ trợ {v_chu} → +10 điểm")
        elif chu['than'] in THAN_XAU:
            diem_chu -= 10
            chi_tiet.append(f"  • Thần {chu['than']} gây trở ngại cho {v_chu} → -10 điểm")
        
        # Thần Khách
        if khach['than'] in THAN_TOT:
            diem_khach += 10
            chi_tiet.append(f"  • Thần {khach['than']} hỗ trợ {v_khach} → +10 điểm")
        elif khach['than'] in THAN_XAU:
            diem_khach -= 10
            chi_tiet.append(f"  • Thần {khach['than']} gây trở ngại cho {v_khach} → -10 điểm")
        
        # Sao Chủ
        sao_chu_data = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['CUU_TINH'].get(chu['sao'], {})
        tinh_chat_chu = sao_chu_data.get('Tính_Chất', '')
        if "Cát" in tinh_chat_chu or "Tốt" in tinh_chat_chu:
            diem_chu += 5
            chi_tiet.append(f"  • Sao {chu['sao']} cát → +5 điểm cho {v_chu}")
        elif "Hung" in tinh_chat_chu or "Xấu" in tinh_chat_chu:
            diem_chu -= 5
            chi_tiet.append(f"  • Sao {chu['sao']} hung → -5 điểm cho {v_chu}")
            
        # Sao Khách
        sao_khach_data = KY_MON_DATA['DU_LIEU_DUNG_THAN_PHU_TRO']['CUU_TINH'].get(khach['sao'], {})
        tinh_chat_khach = sao_khach_data.get('Tính_Chất', '')
        if "Cát" in tinh_chat_khach or "Tốt" in tinh_chat_khach:
            diem_khach += 5
            chi_tiet.append(f"  • Sao {khach['sao']} cát → +5 điểm cho {v_khach}")
        elif "Hung" in tinh_chat_khach or "Xấu" in tinh_chat_khach:
            diem_khach -= 5
            chi_tiet.append(f"  • Sao {khach['sao']} hung → -5 điểm cho {v_khach}")
        
        return {
            'diem_chu': diem_chu,
            'diem_khach': diem_khach,
            'chi_tiet': chi_tiet
        }
    
    def _tinh_diem_can_chi(self, chu, khach):
        """
        Tính điểm Can Chi (20% tổng điểm)
        """
        diem_chu = 50
        diem_khach = 50
        chi_tiet = []
        
        # 1. Cách cục Can Thiên/Can Địa
        cach_cuc_chu = chu['can_thien'] + chu['can_dia']
        cach_cuc_khach = khach['can_thien'] + khach['can_dia']
        
        ket_hop_chu = KY_MON_DATA["TRUCTU_TRANH"].get(cach_cuc_chu, {})
        ket_hop_khach = KY_MON_DATA["TRUCTU_TRANH"].get(cach_cuc_khach, {})
        
        cat_hung_cach_cuc_chu = ket_hop_chu.get("Cát_Hung", "Bình")
        cat_hung_cach_cuc_khach = ket_hop_khach.get("Cát_Hung", "Bình")
        
        DIEM_CACH_CUC = {"Đại Cát": 20, "Cát": 12, "Bình": 0, "Hung": -12, "Đại Hung": -20}
        
        diem_chu += DIEM_CACH_CUC.get(cat_hung_cach_cuc_chu, 0)
        diem_khach += DIEM_CACH_CUC.get(cat_hung_cach_cuc_khach, 0)
        
        v_chu = chu.get('vai_tro', 'Chủ')
        v_khach = khach.get('vai_tro', 'Khách')
        
        chi_tiet.append(f"📜 Cách cục {v_chu}: {chu['can_thien']}/{chu['can_dia']} ({cat_hung_cach_cuc_chu})")
        chi_tiet.append(f"📜 Cách cục {v_khach}: {khach['can_thien']}/{khach['can_dia']} ({cat_hung_cach_cuc_khach})")
        
        # 2. Không Vong và Dịch Mã
        # Cung Chủ
        if chu['so'] in self.khong_vong_cung:
            diem_chu -= 10
            chi_tiet.append(f"  • Cung {v_chu} gặp Không Vong → -10 điểm")
        
        if chu['so'] == self.dich_ma_cung:
            diem_chu += 8
            chi_tiet.append(f"  • Cung {v_chu} có Dịch Mã → +8 điểm (linh hoạt)")

        # Cung Khách
        if khach['so'] in self.khong_vong_cung:
            diem_khach -= 10
            chi_tiet.append(f"  • Cung {v_khach} gặp Không Vong → -10 điểm")
        
        if khach['so'] == self.dich_ma_cung:
            diem_khach += 8
            chi_tiet.append(f"  • Cung {v_khach} có Dịch Mã → +8 điểm (linh hoạt)")
        
        return {
            'diem_chu': diem_chu,
            'diem_khach': diem_khach,
            'chi_tiet': chi_tiet
        }
    
    def _tinh_diem_dung_than(self, chu, khach, chu_de):
        """
        Tính điểm Dụng Thần (15% tổng điểm)
        """
        diem_chu = 50
        diem_khach = 50
        chi_tiet = []
        
        if chu_de in TOPIC_INTERPRETATIONS:
            topic_data = TOPIC_INTERPRETATIONS[chu_de]
            dung_than_list = topic_data.get("Dụng_Thần", [])
            
            # Kiểm tra Chủ có Dụng Thần không
            chu_co_dung_than = any(dt in [chu['sao'], chu['cua'], chu['than'], chu['can_thien'], chu['can_dia']] 
                                   for dt in dung_than_list)
            khach_co_dung_than = any(dt in [khach['sao'], khach['cua'], khach['than'], khach['can_thien'], khach['can_dia']] 
                                     for dt in dung_than_list)
            
            v_chu = chu.get('vai_tro', 'Chủ')
            v_khach = khach.get('vai_tro', 'Khách')
            
            if chu_co_dung_than:
                diem_chu += 15
                chi_tiet.append(f"✅ {v_chu} nắm Dụng Thần ({', '.join(dung_than_list)}) → +15 điểm")
            
            if khach_co_dung_than:
                diem_khach += 15
                chi_tiet.append(f"  • {v_khach} cũng có Dụng Thần → +15 điểm")
            
            if not chu_co_dung_than and not khach_co_dung_than:
                chi_tiet.append(f"  • Không bên nào có Dụng Thần rõ ràng")
        
        return {
            'diem_chu': diem_chu,
            'diem_khach': diem_khach,
            'chi_tiet': chi_tiet
        }
    
    def _tinh_diem_thoi_gian(self, chu, khach, thoi_gian_hien_tai):
        """
        Tính điểm Thời Gian (10% tổng điểm)
        """
        diem_chu = 50
        diem_khach = 50
        chi_tiet = []
        
        # Lấy Can Chi giờ hiện tại
        gio_hien_tai = thoi_gian_hien_tai.hour
        chi_gio_idx = (gio_hien_tai // 2) % 12
        CHI_GIO = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        chi_gio = CHI_GIO[chi_gio_idx]
        
        # Kiểm tra Can Thiên Chủ có hợp với thời gian không
        # (Logic đơn giản - có thể mở rộng)
        
        # Kiểm tra Ngũ Hành của giờ có hợp với Chủ không
        NGU_HANH_CHI = {
            "Tý": "Thủy", "Sửu": "Thổ", "Dần": "Mộc", "Mão": "Mộc",
            "Thìn": "Thổ", "Tỵ": "Hỏa", "Ngọ": "Hỏa", "Mùi": "Thổ",
            "Thân": "Kim", "Dậu": "Kim", "Tuất": "Thổ", "Hợi": "Thủy"
        }
        
        hanh_gio = NGU_HANH_CHI.get(chi_gio, "Thổ")
        
        v_chu = chu.get('vai_tro', 'Chủ')
        v_khach = khach.get('vai_tro', 'Khách')

        # MQH với Chủ
        mqh_chu = tinh_ngu_hanh_sinh_khac(hanh_gio, chu['hanh'])
        if "Sinh" in mqh_chu and hanh_gio in mqh_chu.split()[0]:
            diem_chu += 10
            chi_tiet.append(f"⏰ Giờ {chi_gio} ({hanh_gio}) sinh {v_chu} ({chu['hanh']}) → +10 điểm")
        elif "Khắc" in mqh_chu and chu['hanh'] in mqh_chu.split()[0]:
            diem_chu -= 10
            chi_tiet.append(f"⏰ Giờ {chi_gio} ({hanh_gio}) bị {v_chu} khắc → -10 điểm")
        else:
            chi_tiet.append(f"⏰ Giờ {chi_gio} ({hanh_gio}) trung lập với {v_chu}")

        # MQH với Khách
        v_khach = khach.get('vai_tro', 'Khách')
        mqh_khach = tinh_ngu_hanh_sinh_khac(hanh_gio, khach['hanh'])
        if "Sinh" in mqh_khach and hanh_gio in mqh_khach.split()[0]:
            diem_khach += 10
            chi_tiet.append(f"⏰ Giờ {chi_gio} ({hanh_gio}) sinh {v_khach} ({khach['hanh']}) → +10 điểm")
        elif "Khắc" in mqh_khach and khach['hanh'] in mqh_khach.split()[0]:
            diem_khach -= 10
            chi_tiet.append(f"⏰ Giờ {chi_gio} ({hanh_gio}) bị {v_khach} khắc → -10 điểm")
        else:
            chi_tiet.append(f"⏰ Giờ {chi_gio} ({hanh_gio}) trung lập với {v_khach}")
        
        return {
            'diem_chu': diem_chu,
            'diem_khach': diem_khach,
            'chi_tiet': chi_tiet
        }
    
    def _tong_hop_diem_da_chieu(self, chu, khach, chu_de, thoi_gian):
        """
        Tổng hợp điểm từ 5 chiều với trọng số
        """
        advanced_kb = KY_MON_DATA.get("ADVANCED_KNOWLEDGE", {})
        # Tính điểm từng chiều
        ngu_hanh = self._tinh_diem_ngu_hanh_chi_tiet(chu, khach, thoi_gian)
        sao_mon_than = self._tinh_diem_sao_mon_than(chu, khach)
        can_chi = self._tinh_diem_can_chi(chu, khach)
        dung_than = self._tinh_diem_dung_than(chu, khach, chu_de)
        thoi_gian_diem = self._tinh_diem_thoi_gian(chu, khach, thoi_gian)
        
        # Trọng số
        TRONG_SO = {
            'ngu_hanh': 0.30,
            'sao_mon_than': 0.25,
            'can_chi': 0.20,
            'dung_than': 0.15,
            'thoi_gian': 0.10
        }
        
        # Tính điểm thưởng/phạt từ tương tác bí truyền (PDF)
        bonus_chu = 0
        key_sao = f"{chu['sao']}_{khach['sao']}"
        if key_sao in advanced_kb.get("PALACE_INTERACTIONS", {}):
            # Nếu có tương tác đặc biệt trong sách cổ, tăng trọng số tin cậy
            bonus_chu += 7
        
        # Tính điểm tổng hợp
        diem_chu_tong = (
            ngu_hanh['diem_chu'] * TRONG_SO['ngu_hanh'] +
            sao_mon_than['diem_chu'] * TRONG_SO['sao_mon_than'] +
            can_chi['diem_chu'] * TRONG_SO['can_chi'] +
            dung_than['diem_chu'] * TRONG_SO['dung_than'] +
            thoi_gian_diem['diem_chu'] * TRONG_SO['thoi_gian'] +
            bonus_chu
        )
        
        diem_khach_tong = (
            ngu_hanh['diem_khach'] * TRONG_SO['ngu_hanh'] +
            sao_mon_than['diem_khach'] * TRONG_SO['sao_mon_than'] +
            can_chi['diem_khach'] * TRONG_SO['can_chi'] +
            dung_than['diem_khach'] * TRONG_SO['dung_than'] +
            thoi_gian_diem['diem_khach'] * TRONG_SO['thoi_gian']
        )
        
        # Chuẩn hóa về thang 0-100
        diem_chu_final = max(0, min(100, diem_chu_tong))
        diem_khach_final = max(0, min(100, diem_khach_tong))
        
        return {
            'diem_chu': int(diem_chu_final),
            'diem_khach': int(diem_khach_final),
            'breakdown': {
                'ngu_hanh': ngu_hanh,
                'sao_mon_than': sao_mon_than,
                'can_chi': can_chi,
                'dung_than': dung_than,
                'thoi_gian': thoi_gian_diem
            }
        }
    
    # ======================================================================
    # KẾT THÚC CÁC PHƯƠNG THỨC TÍNH ĐIỂM ĐA CHIỀU
    # ======================================================================
    
    def _tao_loi_khuyen_theo_chu_de(self, chu_de, diem_chu, diem_khach, chu, khach, uu_the):
        """Tạo lời khuyên cụ thể theo từng chủ đề"""
        loi_khuyen = ""
        v_chu = chu.get('vai_tro', 'Chủ')
        v_khach = khach.get('vai_tro', 'Khách')
        
        # Kiểm tra xem chủ đề có trong TOPIC_INTERPRETATIONS không
        if chu_de in TOPIC_INTERPRETATIONS:
            topic_data = TOPIC_INTERPRETATIONS[chu_de]
            dung_than_list = topic_data.get("Dụng_Thần", [])
            goi_y = topic_data.get("Luận_Giải_Gợi_Ý", "")
            
            # Phân tích dựa trên Dụng Thần của chủ đề
            loi_khuyen += f"📋 Dụng Thần Chính: {', '.join(dung_than_list)}\n"
            loi_khuyen += f"💭 Nguyên Tắc: {goi_y}\n\n"
            
            # Kiểm tra Chủ có Dụng Thần không
            chu_co_dung_than = any(dt in [chu['sao'], chu['cua'], chu['than'], chu['can_thien'], chu['can_dia']] for dt in dung_than_list)
            khach_co_dung_than = any(dt in [khach['sao'], khach['cua'], khach['than'], khach['can_thien'], khach['can_dia']] for dt in dung_than_list)
            
            v_chu = chu.get('vai_tro', 'Chủ')
            v_khach = khach.get('vai_tro', 'Khách')
            
            if chu_co_dung_than and not khach_co_dung_than:
                loi_khuyen += f"✅ LỢI THẾ LỚN CHO {v_chu.upper()}:\n"
                loi_khuyen += f"   • {v_chu} nắm giữ Dụng Thần chính của chủ đề\n"
                loi_khuyen += "   • Đây là lợi thế quyết định, hãy tận dụng\n"
                loi_khuyen += "   • Chủ động hành động, không do dự\n"
            elif khach_co_dung_than and not chu_co_dung_than:
                loi_khuyen += f"⚠️ {v_khach.upper()} CÓ LỢI THẾ:\n"
                loi_khuyen += f"   • {v_khach} nắm Dụng Thần chính\n"
                loi_khuyen += "   • Cần tìm cách hợp tác hoặc đợi thời cơ\n"
                loi_khuyen += "   • Không nên đối đầu trực tiếp\n"
            elif chu_co_dung_than and khach_co_dung_than:
                loi_khuyen += "⚖️ CẢ HAI ĐỀU MẠNH:\n"
                loi_khuyen += "   • Cả hai đều có lợi thế riêng\n"
                loi_khuyen += "   • Kết quả phụ thuộc vào Ngũ Hành sinh khắc\n"
                loi_khuyen += "   • Hợp tác sẽ tốt hơn cạnh tranh\n"
            else:
                loi_khuyen += "💡 KHÔNG CÓ DỤNG THẦN RÕ RÀNG:\n"
                loi_khuyen += "   • Cần xem xét các yếu tố khác\n"
                loi_khuyen += "   • Dựa vào Ngũ Hành và Cát/Hung\n"
        
        # Lời khuyên theo các chủ đề tổng quát
        if chu_de == "Kinh Doanh":
            if diem_chu > diem_khach:
                loi_khuyen += "\n✅ CHIẾN LƯỢC KINH DOANH:\n"
                loi_khuyen += "   • Đây là thời điểm tốt để chủ động đàm phán giá cả\n"
                loi_khuyen += "   • Có thể yêu cầu điều khoản có lợi hơn\n"
                loi_khuyen += "   • Nên mạnh dạn mở rộng hợp tác\n"
            else:
                loi_khuyen += "\n⚠️ THẬN TRỌNG TRONG KINH DOANH:\n"
                loi_khuyen += "   • Nên thận trọng, không vội vàng ký kết\n"
                loi_khuyen += "   • Cân nhắc đợi thời điểm thuận lợi hơn\n"
                loi_khuyen += "   • Có thể cần người trung gian hỗ trợ\n"
        
        elif chu_de == "Đàm Phán":
            if diem_chu > diem_khach:
                loi_khuyen += "\n✅ CHIẾN LƯỢC ĐÀM PHÁN:\n"
                loi_khuyen += "   • Bạn có thể chủ động đưa ra yêu cầu trước\n"
                loi_khuyen += "   • Giữ vững lập trường, không nhượng bộ dễ dàng\n"
                loi_khuyen += "   • Thời điểm tốt để gây áp lực hợp lý\n"
            else:
                loi_khuyen += "\n⚠️ CHIẾN LƯỢC PHÒNG THỦ:\n"
                loi_khuyen += "   • Nên lắng nghe nhiều, nói ít\n"
                loi_khuyen += "   • Tìm điểm chung thay vì đối đầu\n"
                loi_khuyen += "   • Chuẩn bị phương án dự phòng\n"
        
        elif chu_de == "Kiện Tụng":
            if diem_chu > diem_khach:
                loi_khuyen += f"\n✅ KHẢ NĂNG THẮNG CAO CHO {v_chu.upper()}:\n"
                loi_khuyen += f"   • Bằng chứng của {v_chu} có sức thuyết phục tuyệt đối\n"
                loi_khuyen += "   • Có thể chủ động trong phiên tòa\n"
                loi_khuyen += "   • Thời điểm tốt để đẩy nhanh tiến độ\n"
            else:
                loi_khuyen += "\n⚠️ CẦN THẬN TRỌNG:\n"
                loi_khuyen += "   • Nên cân nhắc hòa giải thay vì kiện tụng\n"
                loi_khuyen += "   • Chuẩn bị kỹ càng hơn nữa\n"
                loi_khuyen += "   • Có thể cần luật sư giỏi hơn\n"
        
        elif chu_de == "Hôn Nhân":
            if abs(diem_chu - diem_khach) < 20:
                loi_khuyen += "\n💑 TƯƠNG HỢP TỐT:\n"
                loi_khuyen += "   • Hai bên cân bằng, dễ hòa hợp\n"
                loi_khuyen += "   • Nên trân trọng và thấu hiểu lẫn nhau\n"
                loi_khuyen += "   • Thời điểm tốt để tiến tới hôn nhân\n"
            else:
                loi_khuyen += "\n⚠️ CẦN CÂN BẰNG:\n"
                loi_khuyen += "   • Một bên mạnh hơn, cần nhường nhịn\n"
                loi_khuyen += "   • Tránh áp đặt ý kiến\n"
                loi_khuyen += "   • Cần thời gian để hiểu nhau hơn\n"
        
        elif chu_de == "Thi Đấu/Cạnh Tranh":
            if diem_chu > diem_khach:
                loi_khuyen += "\n🏆 KHẢ NĂNG THẮNG CAO:\n"
                loi_khuyen += "   • Phát huy thế mạnh, tấn công chủ động\n"
                loi_khuyen += "   • Tự tin vào khả năng của mình\n"
                loi_khuyen += "   • Đây là thời điểm vàng để thi đấu\n"
            else:
                loi_khuyen += "\n⚠️ GẶP ĐỐI THỦ MẠNH:\n"
                loi_khuyen += "   • Tập trung phòng thủ, chờ cơ hội\n"
                loi_khuyen += "   • Tìm điểm yếu của đối thủ\n"
                loi_khuyen += "   • Chuẩn bị kỹ lưỡng, không chủ quan\n"
        
        elif chu_de == "Tổng Quát" or not loi_khuyen:
            if diem_chu > diem_khach:
                loi_khuyen += f"\n✅ {v_chu.upper()} CÓ LỢI THẾ TỔNG QUAN:\n"
                loi_khuyen += "   • Chủ động trong mọi tương tác\n"
                loi_khuyen += "   • Thời điểm tốt để đưa ra quyết định\n"
                loi_khuyen += "   • Tận dụng lợi thế để đạt mục tiêu\n"
            else:
                loi_khuyen += "\n⚠️ CẦN THẬN TRỌNG:\n"
                loi_khuyen += f"   • {v_chu} nên quan sát và học hỏi nhiều hơn\n"
                loi_khuyen += "   • Không nên hành động vội vàng\n"
                loi_khuyen += "   • Tìm cách cải thiện vị thế\n"
        
        return loi_khuyen
    
    def _phan_tich_thoi_gian(self, chu, khach):
        """Phân tích thời gian tốt/xấu dựa trên Can Chi"""
        thoi_gian = ""
        
        # Phân tích theo Can Thiên
        can_chu = chu['can_thien']
        can_khach = khach['can_thien']
        
        thoi_gian += "🕐 Thời Điểm Tốt Cho Chủ:\n"
        thoi_gian += f"   • Ngày/Giờ có Can {can_chu} (tương hợp với Can Thiên)\n"
        thoi_gian += f"   • Ngày/Giờ thuộc hành {chu['hanh']}\n"
        
        if chu['cua'] in ["Khai", "Sinh", "Hưu"]:
            thoi_gian += f"   • Khi Môn {chu['cua']} đang vượng\n"
        
        thoi_gian += "\n⏰ Thời Điểm Nên Tránh:\n"
        thoi_gian += f"   • Ngày/Giờ có Can {can_khach} (lợi cho Khách)\n"
        
        if khach['hanh'] == "Kim" and chu['hanh'] == "Mộc":
            thoi_gian += "   • Mùa Thu (Kim vượng, khắc Mộc)\n"
        elif khach['hanh'] == "Hỏa" and chu['hanh'] == "Kim":
            thoi_gian += "   • Mùa Hè (Hỏa vượng, khắc Kim)\n"
        
        thoi_gian += "\n🧭 Phương Hướng Tốt:\n"
        phuong_huong_map = {
            1: "Bắc", 2: "Tây Nam", 3: "Đông", 4: "Đông Nam",
            5: "Trung Tâm", 6: "Tây Bắc", 7: "Tây", 8: "Đông Bắc", 9: "Nam"
        }
        thoi_gian += f"   • Hướng {phuong_huong_map.get(chu['so'], 'N/A')} (Cung Chủ)\n"
        
        return thoi_gian
    
    def _cap_nhat_chu_de_toan_cuc(self, event=None):
        """
        Cập nhật chủ đề toàn cục cho tất cả các phần
        Hàm này được gọi khi người dùng chọn chủ đề mới từ dropdown chính
        """
        chu_de_moi = self.combo_chu_de_chinh.get()
        self.chu_de_hien_tai = chu_de_moi
        
        if hasattr(self, 'text_dt_quick'):
            self.text_dt_quick.config(state=tk.NORMAL)
            self.text_dt_quick.delete('1.0', tk.END)
            
            if USE_200_TOPICS:
                dt_info = DUNG_THAN_200_CHU_DE.get(chu_de_moi)
                if dt_info:
                    msg = f"📌 CHỦ ĐỀ: {chu_de_moi.upper()}\n"
                    msg += f"🎯 MỤC TIÊU: {dt_info['muc_tieu']}\n"
                    msg += f"----------------------------------------------------------------------\n"
                    msg += f"🔮 KỲ MÔN: {dt_info['ky_mon']['dung_than']} - {dt_info['ky_mon']['giai_thich']}\n"
                    msg += f"📖 MAI HOA: {dt_info['mai_hoa']['dung_than']} - {dt_info['mai_hoa']['giai_thich']}\n"
                    msg += f"☯️ LỤC HÀO: {dt_info['luc_hao']['dung_than']} - {dt_info['luc_hao']['giai_thich']}\n"
                    msg += f"----------------------------------------------------------------------\n"
                    
                    # THÊM PHẦN PHÂN TÍCH THỰC TẾ (CHI TIẾT DIỄN GIẢI)
                    try:
                        def find_palace(stem_name):
                            for c, s in self.can_thien_ban.items():
                                if s == stem_name: return c
                            return 1
                        chu_idx = find_palace(self.can_ngay)
                        khach_idx = find_palace(self.can_gio)
                        
                        def get_cung_info_local(c):
                            manual = self.manual_cung_data.get(c, {})
                            return {
                                'so': c, 'ten': QUAI_TUONG.get(c, 'N/A'), 'hanh': CUNG_NGU_HANH.get(c, 'N/A'),
                                'sao': manual.get('Sao', self.thien_ban.get(c, 'N/A')),
                                'cua': manual.get('Cua', self.nhan_ban.get(c, 'N/A')),
                                'than': manual.get('Than', self.than_ban.get(c, 'N/A')),
                                'can_thien': manual.get('Can_Thien', self.can_thien_ban.get(c, 'N/A')),
                                'can_dia': manual.get('Can_Dia', self.dia_can.get(c, 'N/A'))
                            }
                        chu_info = get_cung_info_local(chu_idx)
                        khach_info = get_cung_info_local(khach_idx)
                        
                        try:
                            dt_str = self.entry_datetime.get()
                            dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
                        except: dt_obj = datetime.now()
                        
                        ket_qua_9pp = phan_tich_sieu_chi_tiet_chu_de(chu_de_moi, chu_info, khach_info, dt_obj)
                        msg += f"🔍 PHÂN TÍCH THỰC TẾ: {ket_qua_9pp['tong_hop']['nhan_dinh']}\n"
                        
                        # NEW: Thêm tóm tắt thám tử vào quick view
                        if 'chi_tiet_tung_khia_canh' in ket_qua_9pp:
                            for key in ['nhan_dang_tuong_so', 'dong_chay_thoi_gian']:
                                if key in ket_qua_9pp['chi_tiet_tung_khia_canh']:
                                    data = ket_qua_9pp['chi_tiet_tung_khia_canh'][key]
                                    first_line = data.get('noi_dung', [''])[0]
                                    msg += f"▸ {data.get('tieu_de', key)}: {first_line}\n"

                        msg += f"🚩 {ket_qua_9pp['phan_tich_9_phuong_phap']['ky_mon']['ket_luan'].split('.')[0]}..."
                    except:
                        msg += "💡 MẸO: Nhấn 'Lập Bàn' để xem phân tích thực tế trên quẻ hiện tại."

                    self.text_dt_quick.insert('1.0', msg)
                else:
                    self.text_dt_quick.insert('1.0', f"Chủ đề '{chu_de_moi}' chưa có dữ liệu chi tiết.")
            else:
                self.text_dt_quick.insert('1.0', "Database 200+ chủ đề chưa được tải.")

            self.text_dt_quick.config(state=tk.DISABLED)
        
        # Cập nhật label trong cửa sổ So Sánh nếu đang mở
        if hasattr(self, 'label_chu_de_hien_tai'):
            try:
                if self.label_chu_de_hien_tai.winfo_exists():
                    self.label_chu_de_hien_tai.config(text=chu_de_moi)
            except tk.TclError:
                pass # Widget đã bị hủy
        
        # Hiển thị thông báo
        print(f"✅ Đã chuyển sang chủ đề: {chu_de_moi}")
        
        # Tự động hiển thị luận giải chủ đề
        self._hien_thi_luan_giai_chu_de(None)
        
        # TỰ ĐỘNG TÍNH LẠI MAI HOA nếu đã có kết quả
        if hasattr(self, 'ket_qua_qua_hien_tai') and self.ket_qua_qua_hien_tai is not None:
            try:
                # Tính lại với chủ đề mới
                self._hien_thi_ket_qua_qua(self.ket_qua_qua_hien_tai)
                print(f"   → Đã cập nhật Mai Hoa theo chủ đề: {chu_de_moi}")
            except Exception as e:
                print(f"   ⚠️ Lỗi cập nhật Mai Hoa: {e}")
        
        # TỰ ĐỘNG TÍNH LẠI LỤC HÀO nếu đã có kết quả
        if hasattr(self, 'ket_qua_luc_hao_hien_tai') and self.ket_qua_luc_hao_hien_tai is not None:
            try:
                # Lấy thời gian từ kết quả cũ hoặc từ entry
                dt_str = self.entry_datetime.get()
                dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
                
                # Tính lại với chủ đề mới
                ket_qua_moi = lap_qua_luc_hao(dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour, chu_de_moi)
                self._hien_thi_ket_qua_luc_hao(ket_qua_moi)
                print(f"   → Đã cập nhật Lục Hào theo chủ đề: {chu_de_moi}")
            except Exception as e:
                print(f"   ⚠️ Lỗi cập nhật Lục Hào: {e}")
    
    
    
    def _hien_thi_luan_giai_chu_de(self, event):
        """Hiển thị luận giải chi tiết về Dụng Thần của chủ đề"""
        chu_de = self.chu_de_hien_tai
        
        # Tạo cửa sổ mới
        window = tk.Toplevel(self.master)
        window.title(f"📚 DỤNG THẦN CHI TIẾT: {chu_de}")
        window.geometry("1000x750")
        
        # Frame chính
        main_frame = tk.Frame(window, bg='#f5f5f5')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Tiêu đề
        title_label = tk.Label(main_frame, text=f"🎯 CHỦ ĐỀ: {chu_de}", 
                               font=('Segoe UI', 16, 'bold'), bg='#f5f5f5', fg='#e74c3c')
        title_label.pack(pady=10)
        
        # Text widget với scrollbar
        text_frame = tk.Frame(main_frame)
        text_frame.pack(fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget = tk.Text(text_frame, wrap=tk.WORD, font=('Courier New', 9),
                             yscrollcommand=scrollbar.set, bg='#ffffff')
        text_widget.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.config(command=text_widget.yview)
        
        # THỰC HIỆN PHÂN TÍCH ĐỘNG THEO PHONG CÁCH THẦY BÓI
        try:
            # 1. Lấy thời gian
            try:
                dt_str = self.entry_datetime.get()
                dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
            except:
                dt_obj = datetime.now()

            # 2. Lấy thông tin cung Chủ/Khách
            def find_palace(stem_name):
                for c, s in self.can_thien_ban.items():
                    if s == stem_name: return c
                return 1
            
            chu_idx = find_palace(self.can_ngay)
            khach_idx = find_palace(self.can_gio)

            def get_cung_info_local(c):
                manual = self.manual_cung_data.get(c, {})
                return {
                    'so': c,
                    'ten': QUAI_TUONG.get(c, 'N/A'),
                    'hanh': CUNG_NGU_HANH.get(c, 'N/A'),
                    'sao': manual.get('Sao', self.thien_ban.get(c, 'N/A')),
                    'cua': manual.get('Cua', self.nhan_ban.get(c, 'N/A')),
                    'than': manual.get('Than', self.than_ban.get(c, 'N/A')),
                    'can_thien': manual.get('Can_Thien', self.can_thien_ban.get(c, 'N/A')),
                    'can_dia': manual.get('Can_Dia', self.dia_can.get(c, 'N/A'))
                }

            chu_info = get_cung_info_local(chu_idx)
            khach_info = get_cung_info_local(khach_idx)

            # 3. Gọi siêu phân tích
            ket_qua_9pp = phan_tich_sieu_chi_tiet_chu_de(chu_de, chu_info, khach_info, dt_obj)

            # 4. Xây dựng nội dung báo cáo
            noi_dung = f"✨ ĐỘ TIN CẬY HỆ THỐNG: {ket_qua_9pp['do_tin_cay_tong']}% ✨\n"
            noi_dung += "═" * 90 + "\n\n"
            
            # PHẦN CHI TIẾT (Kỳ Môn) - Phân tích thực tế vào quẻ/cung
            noi_dung += "🔮 PHÂN TÍCH CHI TIẾT THẾ TRẬN (KỲ MÔN):\n"
            noi_dung += f"{ket_qua_9pp['phan_tich_9_phuong_phap']['ky_mon']['ket_luan']}\n\n"

            # NEW: Hiển thị các khía cạnh chi tiết (Thám tử: Nhân dạng, Số lượng, Thời gian)
            if 'chi_tiet_tung_khia_canh' in ket_qua_9pp:
                noi_dung += "🔍 CHI TIẾT MANH MỐI (NHÂN DẠNG, SỐ LƯỢNG, THỜI GIAN):\n"
                for key, data in ket_qua_9pp['chi_tiet_tung_khia_canh'].items():
                    noi_dung += f"▸ {data.get('tieu_de', key)}:\n"
                    for line in data.get('noi_dung', []):
                        noi_dung += f"  {line}\n"
                    noi_dung += "\n"
            
            # Thêm phần Dụng Thần tra cứu nếu có
            if USE_200_TOPICS:
                dt_info = hien_thi_dung_than_200(chu_de)
                noi_dung += "📚 TRA CỨU DỤNG THẦN CƠ BẢN:\n"
                noi_dung += dt_info

        except Exception as e:
            noi_dung = f"⚠️ 'Thầy' đang bận bấm quẻ, vui lòng lập bàn trước khi xem chi tiết!\n(Lỗi: {e})"
        
        # Hiển thị
        text_widget.insert('1.0', noi_dung)
        text_widget.config(state=tk.DISABLED)
        
        # Nút đóng & Nút xem 3 phương pháp
        btn_frame = tk.Frame(main_frame, bg='#f5f5f5')
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="✖ Đóng", command=window.destroy).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="☯️ Xem Chi Tiết 3 Phương Pháp", 
                   command=self._mo_cua_so_tong_hop_4_phuong_phap).pack(side=tk.LEFT, padx=5)
    
    # ======================================================================
    # PHẦN MỚI: TỔNG HỢP 4 PHƯƠNG PHÁP DỰ ĐOÁN
    # ======================================================================
    
    def _mo_cua_so_tong_hop_4_phuong_phap(self):
        """Mở cửa sổ phân tích tổng hợp từ 9 phương pháp (Siêu Dự Đoán)"""
        
        # Tạo cửa sổ mới
        window = Toplevel(self.master)
        window.title("🔮 SIÊU DỰ ĐOÁN TỔNG HỢP 9 PHƯƠNG PHÁP 🔮")
        window.geometry("900x700")
        window.transient(self.master)
        
        # Frame chính
        main_frame = ttk.Frame(window, padding=10)
        main_frame.pack(fill='both', expand=True)
        
        # Frame nhập liệu
        input_frame = ttk.LabelFrame(main_frame, text="📋 Thông Tin Phân Tích", padding=10)
        input_frame.pack(fill='x', padx=5, pady=5)
        
        # Chọn chủ đề
        tk.Label(input_frame, text="Chủ đề:", font=self.font_main).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        all_topics_list = sorted(list(TOPIC_INTERPRETATIONS.keys()))
        combo_chu_de_tong_hop = ttk.Combobox(
            input_frame, 
            values=all_topics_list,
            width=20,
            state='readonly',
            font=self.font_cung_info
        )
        combo_chu_de_tong_hop.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        combo_chu_de_tong_hop.set("Sự nghiệp")
        
        # Ngày sinh (cho Tử Vi)
        tk.Label(input_frame, text="Ngày sinh (cho Tử Vi):", font=self.font_main).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        
        frame_ngay_sinh = ttk.Frame(input_frame)
        frame_ngay_sinh.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        tk.Label(frame_ngay_sinh, text="Năm:").pack(side=tk.LEFT, padx=2)
        entry_nam_sinh = ttk.Entry(frame_ngay_sinh, width=6)
        entry_nam_sinh.pack(side=tk.LEFT, padx=2)
        entry_nam_sinh.insert(0, "1990")
        
        tk.Label(frame_ngay_sinh, text="Tháng:").pack(side=tk.LEFT, padx=2)
        entry_thang_sinh = ttk.Entry(frame_ngay_sinh, width=4)
        entry_thang_sinh.pack(side=tk.LEFT, padx=2)
        entry_thang_sinh.insert(0, "5")
        
        tk.Label(frame_ngay_sinh, text="Ngày:").pack(side=tk.LEFT, padx=2)
        entry_ngay_sinh = ttk.Entry(frame_ngay_sinh, width=4)
        entry_ngay_sinh.pack(side=tk.LEFT, padx=2)
        entry_ngay_sinh.insert(0, "15")
        
        tk.Label(frame_ngay_sinh, text="Giờ:").pack(side=tk.LEFT, padx=2)
        entry_gio_sinh = ttk.Entry(frame_ngay_sinh, width=4)
        entry_gio_sinh.pack(side=tk.LEFT, padx=2)
        entry_gio_sinh.insert(0, "10")
        
        # Frame kết quả
        result_frame = ttk.LabelFrame(main_frame, text="📊 Kết Quả Phân Tích", padding=10)
        result_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Text area hiển thị kết quả
        text_result = tk.Text(result_frame, wrap=tk.WORD, font=('Courier New', 10), padx=10, pady=10)
        text_result.pack(side=tk.LEFT, fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(result_frame, command=text_result.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_result.config(yscrollcommand=scrollbar.set)
        
        # Hàm phân tích
        def thuc_hien_phan_tich():
            try:
                # Lấy thông tin
                chu_de = combo_chu_de_tong_hop.get()
                
                # Hiển thị đang xử lý
                text_result.config(state=tk.NORMAL)
                text_result.delete('1.0', tk.END)
                text_result.insert(tk.END, "⏳ ĐANG KẾT NỐI VỚI CÁC VÌ SAO VÀ QUẺ DỊCH...\n\n", 'warning')
                text_result.insert(tk.END, "⚡ Đang hợp nhất 4 phương pháp tiên tri CHUẨN CHỈ:\n")
                text_result.insert(tk.END, "• Kỳ Môn Độn Giáp (Chiến lược & Vị thế)\n")
                text_result.insert(tk.END, "• Lục Nhâm Thần Khóa (Diễn biến & Nhân quả)\n")
                text_result.insert(tk.END, "• Thái Ất Thần Kinh (Thế trận & Thiên thời)\n")
                text_result.insert(tk.END, "• Bát Tự Can Chi (Bản chất & Năng lực)\n\n")
                text_result.insert(tk.END, "Vui lòng đợi trong giây lát...\n")
                text_result.config(state=tk.DISABLED)
                window.update()
                
                # Lấy dữ liệu 9pp
                try:
                    dt_str = self.entry_datetime.get()
                    dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
                except:
                    dt_obj = datetime.now()
                
                # Lấy cung chủ khach mặc định dựa trên can ngày/giờ nếu chưa chọn
                # Ở đây chúng ta mượn logic từ ComparisonWindow
                cung1 = self.combo_cung1.get() if hasattr(self, 'combo_cung1') and self.combo_cung1.get() else "1"
                cung2 = self.combo_cung2.get() if hasattr(self, 'combo_cung2') and self.combo_cung2.get() else "2"
                
                def get_cung_info_local(cung_str):
                    try: c = int(cung_str.split(' - ')[0])
                    except: c = 1
                    manual = self.manual_cung_data.get(c, {})
                    return {
                        'so': c,
                        'ten': QUAI_TUONG.get(c, 'N/A'),
                        'hanh': CUNG_NGU_HANH.get(c, 'N/A'),
                        'sao': manual.get('Sao', self.thien_ban.get(c, 'N/A')),
                        'cua': manual.get('Cua', self.nhan_ban.get(c, 'N/A')),
                        'than': manual.get('Than', self.than_ban.get(c, 'N/A')),
                        'can_thien': manual.get('Can_Thien', self.can_thien_ban.get(c, 'N/A')),
                        'can_dia': manual.get('Can_Dia', self.dia_can.get(c, 'N/A'))
                    }
                
                chu = get_cung_info_local(cung1)
                khach = get_cung_info_local(cung2)
                
                ket_qua_9pp = phan_tich_sieu_chi_tiet_chu_de(chu_de, chu, khach, dt_obj)
                mqh_chu_khach = tinh_ngu_hanh_sinh_khac(chu['hanh'], khach['hanh'])
                phan_tich_lien_mach = tao_phan_tich_lien_mach(chu_de, chu, khach, dt_obj, ket_qua_9pp, mqh_chu_khach)
                
                # Hiển thị báo cáo tiên tri
                text_result.config(state=tk.NORMAL)
                text_result.delete('1.0', tk.END)
                
                text_result.insert(tk.END, "🔮 BÁO CÁO TỔNG HỢP TAM THỨC & BÁT TỰ 🔮\n", 'header')
                text_result.insert(tk.END, f"Chủ đề: {chu_de.upper()} | Độ tin cậy: {ket_qua_9pp['do_tin_cay_tong']}%\n\n")

                text_result.insert(tk.END, "🏆 LUẬN GIẢI KỲ MÔN & THÁI ẤT (THIÊN THỜI)\n", 'header')
                text_result.insert(tk.END, ket_qua_9pp['phan_tich_9_phuong_phap']['ky_mon']['ket_luan'] + "\n")
                text_result.insert(tk.END, ket_qua_9pp['phan_tich_9_phuong_phap']['thai_at']['ket_luan'] + "\n\n")

                text_result.insert(tk.END, "🪐 DÒNG CHẢY BIẾN HÓA (LỤC NHÂM & BÁT TỰ)\n", 'header')
                text_result.insert(tk.END, phan_tich_lien_mach['hien_tai'] + "\n\n")
                text_result.insert(tk.END, phan_tich_lien_mach['tuong_lai'] + "\n\n")
                
                text_result.insert(tk.END, "📋 CHI TIẾT DIỄN BIẾN SỰ VIỆC (SIÊU PHÂN TÍCH)\n", 'header')
                text_result.insert(tk.END, phan_tich_lien_mach['su_viec_se_xay_ra'] + "\n\n")

                text_result.insert(tk.END, "📅 THỜI GIAN ỨNG NGHIỆM\n", 'header')
                text_result.insert(tk.END, phan_tich_lien_mach['thoi_gian_cu_the'] + "\n\n")
                
                # NEW: Hiển thị các khía cạnh chi tiết (Thám tử)
                if ket_qua_9pp.get('chi_tiet_tung_khia_canh'):
                    text_result.insert(tk.END, f"🔍 CHI TIẾT MANH MỐI CHUYÊN SÂU\n", 'header')
                    for key, data in ket_qua_9pp['chi_tiet_tung_khia_canh'].items():
                        text_result.insert(tk.END, f"▸ {data['tieu_de']}:\n", 'good')
                        for line in data['noi_dung']:
                            text_result.insert(tk.END, f"  {line}\n")
                        text_result.insert(tk.END, "\n")

                text_result.insert(tk.END, "💥 LỜI SẤM CUỐI CÙNG\n", 'header')
                text_result.insert(tk.END, phan_tich_lien_mach['ket_luan_tong_hop'], 'warning')

                # Cấu hình màu sắc
                text_result.tag_config("header", foreground="#8e44ad", font=('Segoe UI', 11, 'bold'))
                text_result.tag_config("good", foreground="#27ae60", font=('Segoe UI', 10, 'bold'))
                text_result.tag_config("bad", foreground="#c0392b", font=('Segoe UI', 10, 'bold'))
                text_result.tag_config("warning", foreground="#e67e22", font=('Segoe UI', 10, 'bold'))
                
                text_result.config(state=tk.DISABLED)
                
            except Exception as e:
                text_result.config(state=tk.NORMAL)
                text_result.delete('1.0', tk.END)
                text_result.insert(tk.END, f"❌ LỖI: {str(e)}\n\n")
                text_result.insert(tk.END, "Vui lòng kiểm tra lại thông tin nhập vào.")
                text_result.config(state=tk.DISABLED)
        
        # Nút phân tích
        btn_phan_tich = ttk.Button(
            input_frame, 
            text="🔍 Phân Tích Ngay",
            command=thuc_hien_phan_tich
        )
        btn_phan_tich.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Tự động phân tích khi mở
        window.after(500, thuc_hien_phan_tich)

    # ======================================================================
    # ZOOM METHODS - Phương thức phóng to/thu nhỏ giao diện
    # ======================================================================
    
    def zoom_in(self):
        """Phóng to giao diện 10%"""
        self.zoom_level = min(self.zoom_level + 0.1, 2.0)  # Tối đa 200%
        self.apply_zoom()
    
    def zoom_out(self):
        """Thu nhỏ giao diện 10%"""
        self.zoom_level = max(self.zoom_level - 0.1, 0.5)  # Tối thiểu 50%
        self.apply_zoom()
    
    def reset_zoom(self):
        """Đặt lại zoom về 100%"""
        self.zoom_level = 1.0
        self.apply_zoom()
    
    def apply_zoom(self):
        """Áp dụng mức zoom bằng cách thay đổi DPI scaling và font sizes"""
        try:
            # Phương pháp 1: Thay đổi tk scaling (ảnh hưởng đến tất cả widget sizes)
            self.master.tk.call('tk', 'scaling', 1.33 * self.zoom_level)
            
            # Phương pháp 2: Cập nhật tất cả font sizes để thấy rõ sự thay đổi
            # Danh sách tất cả font attributes
            font_attrs = [
                'font_main', 'font_cung_info', 'font_cung_so', 
                'font_can', 'font_than', 'font_tinh', 
                'font_mon_chay', 'font_mon_co_dinh'
            ]
            
            # Base font sizes
            base_font_sizes = {
                'font_main': 11,
                'font_cung_info': 10,
                'font_cung_so': 16,
                'font_can': 15,
                'font_than': 12,
                'font_tinh': 14,
                'font_mon_chay': 13,
                'font_mon_co_dinh': 10
            }
            
            # Update each font
            for font_attr in font_attrs:
                if hasattr(self, font_attr):
                    base_size = base_font_sizes.get(font_attr, 10)
                    new_size = max(6, int(base_size * self.zoom_level))  # Minimum 6pt
                    
                    current_font = getattr(self, font_attr)
                    if isinstance(current_font, tuple) and len(current_font) >= 2:
                        # Create new font tuple with updated size
                        new_font = (current_font[0], new_size) + current_font[2:]
                        setattr(self, font_attr, new_font)
            
            # Cập nhật label hiển thị phần trăm
            zoom_percent = int(self.zoom_level * 100)
            if hasattr(self, 'lbl_zoom_percent'):
                self.lbl_zoom_percent.config(text=f"{zoom_percent}%")
            
            # Cập nhật title
            current_title = self.master.title()
            if " - Zoom:" in current_title:
                current_title = current_title.split(" - Zoom:")[0]
            self.master.title(f"{current_title} - Zoom: {zoom_percent}%")
            
            # Force update
            self.master.update_idletasks()
            
            print(f"✅ Đã zoom {zoom_percent}%")
            
            # Show message to user
            messagebox.showinfo("Zoom", 
                f"Đã áp dụng zoom {zoom_percent}%\n\n"
                "Lưu ý: Để zoom có hiệu quả tối đa,\n"
                "vui lòng KHỞI ĐỘNG LẠI ứng dụng.")
            
        except Exception as e:
            print(f"❌ Lỗi khi zoom: {e}")
            import traceback
            traceback.print_exc()


if __name__ == '__main__':
    root = tk.Tk()
    # Khởi động với màn hình login
    LoginManager(root)
    root.mainloop()
