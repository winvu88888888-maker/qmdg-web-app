
    def tao_mai_hoa_frame(self):
        """Táº¡o Frame hiá»ƒn thá»‹ 64 Quáº» Kinh Dá»‹ch - Mai Hoa Dá»‹ch Sá»‘"""
        # Frame chÃ­nh cho Mai Hoa Dá»‹ch Sá»‘
        self.frame_mai_hoa = ttk.LabelFrame(self.master, text="ðŸ“– 64 QUáºº KINH Dá»ŠCH - MAI HOA Dá»ŠCH Sá» ðŸ“–", 
                                            padding="15")
        self.frame_mai_hoa.pack(fill='both', expand=False, padx=10, pady=10)
        
        # Frame hiá»ƒn thá»‹ quáº»
        frame_display = tk.Frame(self.frame_mai_hoa, bg='#f8f9fa', relief='sunken', bd=2)
        frame_display.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Label Báº£n Quáº»
        self.label_ban_qua = tk.Label(frame_display, text="Báº£n Quáº»: (ChÆ°a tÃ­nh)", 
                                      font=('Segoe UI', 12, 'bold'), bg='#f8f9fa', 
                                      fg='#2c3e50', anchor='w')
        self.label_ban_qua.pack(fill='x', padx=10, pady=5)
        
        # Label Quáº» Biáº¿n
        self.label_qua_bien = tk.Label(frame_display, text="Quáº» Biáº¿n: (ChÆ°a tÃ­nh)", 
                                       font=('Segoe UI', 12, 'bold'), bg='#f8f9fa', 
                                       fg='#16a085', anchor='w')
        self.label_qua_bien.pack(fill='x', padx=10, pady=5)
        
        # Label HÃ o Äá»™ng
        self.label_hao_dong = tk.Label(frame_display, text="HÃ o Äá»™ng: -", 
                                       font=('Segoe UI', 11), bg='#f8f9fa', 
                                       fg='#7f8c8d', anchor='w')
        self.label_hao_dong.pack(fill='x', padx=10, pady=5)
        
        # Text widget hiá»ƒn thá»‹ giáº£i quáº»
        frame_giai_qua = tk.Frame(frame_display, bg='#f8f9fa')
        frame_giai_qua.pack(fill='both', expand=True, padx=10, pady=5)
        
        scrollbar = tk.Scrollbar(frame_giai_qua)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_giai_qua = tk.Text(frame_giai_qua, height=8, wrap=tk.WORD, 
                                     font=('Segoe UI', 10), bg='#ffffff',
                                     yscrollcommand=scrollbar.set)
        self.text_giai_qua.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.config(command=self.text_giai_qua.yview)
        
        # Frame buttons
        frame_buttons = tk.Frame(self.frame_mai_hoa, bg='#ecf0f1')
        frame_buttons.pack(fill='x', padx=5, pady=10)
        
        # Button Tá»± Äá»™ng Theo Giá»
        btn_auto = tk.Button(frame_buttons, text="ðŸ• Tá»± Äá»™ng Theo Giá»", 
                            command=self.tinh_qua_tu_dong,
                            font=('Segoe UI', 10, 'bold'), bg='#3498db', fg='white',
                            relief='raised', bd=3, padx=15, pady=8,
                            cursor='hand2')
        btn_auto.pack(side=tk.LEFT, padx=10)
        
        # Button Ngáº«u NhiÃªn
        btn_random = tk.Button(frame_buttons, text="ðŸŽ² Ngáº«u NhiÃªn", 
                              command=self.tinh_qua_ngau_nhien_gui,
                              font=('Segoe UI', 10, 'bold'), bg='#e74c3c', fg='white',
                              relief='raised', bd=3, padx=15, pady=8,
                              cursor='hand2')
        btn_random.pack(side=tk.LEFT, padx=10)
        
        # LÆ°u trá»¯ káº¿t quáº£ quáº» hiá»‡n táº¡i
        self.ket_qua_qua_hien_tai = None
    
    def tinh_qua_tu_dong(self):
        """TÃ­nh quáº» tá»± Ä‘á»™ng theo thá»i gian hiá»‡n táº¡i"""
        try:
            # Láº¥y thá»i gian tá»« entry
            dt_str = self.entry_datetime.get()
            dt_obj = datetime.strptime(dt_str, "%H:%M - %d/%m/%Y")
            
            # TÃ­nh quáº»
            ket_qua = tinh_qua_theo_thoi_gian(dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour)
            self.ket_qua_qua_hien_tai = ket_qua
            
            # Hiá»ƒn thá»‹
            self._hien_thi_ket_qua_qua(ket_qua)
            
        except Exception as e:
            messagebox.showerror("Lá»—i", f"KhÃ´ng thá»ƒ tÃ­nh quáº»: {str(e)}")
    
    def tinh_qua_ngau_nhien_gui(self):
        """TÃ­nh quáº» ngáº«u nhiÃªn"""
        try:
            ket_qua = tinh_qua_ngau_nhien()
            self.ket_qua_qua_hien_tai = ket_qua
            self._hien_thi_ket_qua_qua(ket_qua)
        except Exception as e:
            messagebox.showerror("Lá»—i", f"KhÃ´ng thá»ƒ tÃ­nh quáº» ngáº«u nhiÃªn: {str(e)}")
    
    def _hien_thi_ket_qua_qua(self, ket_qua):
        """Hiá»ƒn thá»‹ káº¿t quáº£ quáº» lÃªn GUI"""
        ban_qua = ket_qua['ban_qua']
        qua_bien = ket_qua['qua_bien']
        hao_dong = ket_qua['hao_dong']
        qua_thuong = ket_qua['qua_thuong']
        qua_ha = ket_qua['qua_ha']
        
        # Cáº­p nháº­t labels
        self.label_ban_qua.config(
            text=f"Báº£n Quáº»: {ban_qua['ten']} {ban_qua['unicode']} ({qua_thuong['unicode']}{qua_ha['unicode']})"
        )
        
        self.label_qua_bien.config(
            text=f"Quáº» Biáº¿n: {qua_bien['ten']} {qua_bien['unicode']}"
        )
        
        self.label_hao_dong.config(
            text=f"HÃ o Äá»™ng: HÃ o thá»© {hao_dong} | Thá»i gian: {ket_qua['thoi_gian']}"
        )
        
        # Giáº£i quáº»
        giai_thich = giai_qua(ket_qua, "Tá»•ng QuÃ¡t")
        
        # Hiá»ƒn thá»‹ vÃ o text widget
        self.text_giai_qua.config(state=tk.NORMAL)
        self.text_giai_qua.delete('1.0', tk.END)
        self.text_giai_qua.insert('1.0', giai_thich)
        self.text_giai_qua.config(state=tk.DISABLED)
