const app = {
    API_BASE: window.location.origin + '/api',
    currentChart: null,
    currentTopic: 'Tổng Quát',
    allTopics: [],
    currentPalaceIndex: 4, // Start at palace 5 (center)
    palaceOrder: [4, 9, 2, 3, 5, 7, 8, 1, 6], // Lạc Thư order
    dungThanExpanded: true,

    async login() {
        const password = document.getElementById('password').value;
        try {
            const response = await fetch(`${this.API_BASE}/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ password })
            });
            const data = await response.json();
            if (data.success) {
                document.getElementById('login-screen').classList.add('d-none');
                document.getElementById('main-app').classList.remove('d-none');
                this.init();
            } else {
                alert(data.message || 'Mật khẩu không chính xác');
            }
        } catch (e) {
            console.error(e);
            alert('Lỗi kết nối server. Vui lòng kiểm tra server đã chạy chưa.');
        }
    },

    async init() {
        this.showLoading(true);
        await this.loadTopics();
        await this.calculate();
        this.setupEventListeners();
        this.startClock();
        this.showLoading(false);
    },

    setupEventListeners() {
        // Topic search
        const searchInput = document.getElementById('topic-search');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => this.searchTopics(e.target.value));
            searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') this.searchTopics(e.target.value);
            });
        }

        // Topic selection
        const topicSelect = document.getElementById('topic-select');
        if (topicSelect) {
            topicSelect.addEventListener('change', (e) => {
                this.currentTopic = e.target.value;
                this.updateDungThan();
                this.updateOtherTabs();
            });
        }

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') this.navigatePalace(-1);
            if (e.key === 'ArrowRight') this.navigatePalace(1);
        });
    },

    startClock() {
        const updateTime = () => {
            const now = new Date();
            const timeStr = now.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });
            const elem = document.getElementById('current-time');
            if (elem) elem.textContent = timeStr;
        };
        updateTime();
        setInterval(updateTime, 1000);
    },

    async loadTopics() {
        try {
            const response = await fetch(`${this.API_BASE}/topics`);
            this.allTopics = await response.json();
            const select = document.getElementById('topic-select');
            select.innerHTML = '<option value="Tổng Quát">Tổng Quát</option>';
            this.allTopics.forEach(t => {
                const opt = document.createElement('option');
                opt.value = t;
                opt.textContent = t;
                select.appendChild(opt);
            });
        } catch (e) {
            console.error('Lỗi tải chủ đề:', e);
        }
    },

    searchTopics(query) {
        const select = document.getElementById('topic-select');
        if (!query.trim()) {
            // Show all topics
            select.innerHTML = '<option value="Tổng Quát">Tổng Quát</option>';
            this.allTopics.forEach(t => {
                const opt = document.createElement('option');
                opt.value = t;
                opt.textContent = t;
                select.appendChild(opt);
            });
            return;
        }

        const filtered = this.allTopics.filter(t =>
            t.toLowerCase().includes(query.toLowerCase())
        );

        select.innerHTML = '<option value="Tổng Quát">Tổng Quát</option>';
        filtered.forEach(t => {
            const opt = document.createElement('option');
            opt.value = t;
            opt.textContent = t;
            select.appendChild(opt);
        });

        // Auto-select if only one result
        if (filtered.length === 1) {
            select.value = filtered[0];
            this.currentTopic = filtered[0];
            this.updateDungThan();
        }
    },

    clearSearch() {
        document.getElementById('topic-search').value = '';
        this.searchTopics('');
    },

    async calculate() {
        try {
            this.showLoading(true);
            const initRes = await fetch(`${this.API_BASE}/initial-data`);
            const initData = await initRes.json();

            const params = {
                ju: initData.ju,
                zhifu: initData.zhifu,
                zhishi: initData.zhishi,
                hourBranch: initData.hourBranch
            };

            const calcRes = await fetch(`${this.API_BASE}/calculate`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(params)
            });
            this.currentChart = await calcRes.json();
            this.updateChartInfo(initData);
            this.renderGrid();
            this.updateDungThan();
            this.updateOtherTabs();
            this.showLoading(false);
        } catch (e) {
            console.error('Lỗi tính toán:', e);
            this.showLoading(false);
            alert('Lỗi tính toán bàn. Vui lòng thử lại.');
        }
    },

    updateChartInfo(initData) {
        if (!this.currentChart) return;

        // Update chart info panel
        document.getElementById('info-ju').textContent = this.currentChart.ju || '--';
        document.getElementById('info-solar').textContent = this.currentChart.solarTerm || '--';
        document.getElementById('info-type').textContent = this.currentChart.isYang ? 'Dương Độn ☀️' : 'Âm Độn 🌙';
        document.getElementById('info-zhifu').textContent = initData.zhifu || '--';
        document.getElementById('info-zhishi').textContent = initData.zhishi || '--';
        document.getElementById('info-branch').textContent = initData.hourBranch || '--';

        // Update lunar calendar info (will be enhanced later)
        const lunarText = `Giờ ${this.currentChart.can_gio || '--'} ${initData.hourBranch || '--'} | Ngày ${this.currentChart.can_ngay || '--'} | Cục ${this.currentChart.ju || '--'}`;
        document.getElementById('info-lunar').textContent = lunarText;
    },

    renderGrid() {
        const grid = document.getElementById('qimen-grid');
        if (!grid || !this.currentChart) return;

        grid.innerHTML = '';
        const layout = [[4, 9, 2], [3, 5, 7], [8, 1, 6]];

        grid.style.display = 'grid';
        grid.style.gridTemplateColumns = 'repeat(3, 1fr)';
        grid.style.gap = '8px';

        layout.forEach(row => {
            row.forEach(num => {
                const p = this.currentChart.palaces.find(x => x.number === num);
                if (!p) return;

                const div = document.createElement('div');
                div.className = 'palace-box p-2 border bg-white text-center position-relative';
                div.style.minHeight = '120px';
                div.style.fontSize = '0.85rem';
                div.style.cursor = 'pointer';
                div.style.transition = 'all 0.3s';

                // Add color based on auspiciousness
                if (p.auspiciousness >= 7) {
                    div.style.borderColor = '#27ae60';
                    div.style.backgroundColor = '#d4fc79';
                } else if (p.auspiciousness <= 4) {
                    div.style.borderColor = '#c0392b';
                    div.style.backgroundColor = '#ff9a9e';
                }

                const symbols = [];
                if (p.isKongWang) symbols.push('💀');
                if (p.isDiMa) symbols.push('🐎');

                div.innerHTML = `
                    <div class="palace-header-num" style="position: absolute; top: 2px; left: 4px; font-size: 1.2rem; font-weight: bold; color: #2c3e50;">${num}</div>
                    <div class="palace-header-name" style="text-align: center; font-weight: bold; color: #34495e; margin-top: 20px; font-size: 0.85rem;">${p.name}</div>
                    <div class="palace-element" style="text-align: center; font-size: 0.7rem; color: #7f8c8d; margin-bottom: 4px;">${p.element}</div>
                    
                    <div class="palace-star" style="color: #2980b9; font-weight: 600; font-size: 0.85rem; text-align: center;">⭐ ${p.star}</div>
                    <div class="palace-door" style="color: #27ae60; font-weight: bold; font-size: 0.85rem; text-align: center;">🚪 ${p.door}</div>
                    <div class="palace-deity" style="color: #7f8c8d; font-style: italic; font-size: 0.75rem; text-align: center;">👤 ${p.deity}</div>
                    
                    <div class="palace-stems" style="display: flex; justify-content: space-between; margin-top: 4px; padding: 0 4px;">
                        <span style="color: #8e44ad; font-weight: bold; font-size: 0.85rem;">${p.stemHeaven}</span>
                        <span style="font-size: 1rem;">${symbols.join(' ')}</span>
                        <span style="color: #c0392b; font-weight: bold; font-size: 0.85rem;">${p.stemEarth}</span>
                    </div>
                `;

                // Click to show detail
                div.addEventListener('click', () => this.showPalaceDetail(num));

                // Hover effect
                div.addEventListener('mouseenter', () => {
                    div.style.transform = 'scale(1.05)';
                    div.style.boxShadow = '0 4px 8px rgba(0,0,0,0.2)';
                });
                div.addEventListener('mouseleave', () => {
                    div.style.transform = 'scale(1)';
                    div.style.boxShadow = 'none';
                });

                grid.appendChild(div);
            });
        });
    },

    async showPalaceDetail(palaceNum) {
        try {
            this.showLoading(true);
            const topic = this.currentTopic;

            // Use new topic-specific analysis API
            const response = await fetch(`${this.API_BASE}/palace-topic-analysis/${palaceNum}/${encodeURIComponent(topic)}`);
            const analysis = await response.json();

            const modal = new bootstrap.Modal(document.getElementById('palaceModal'));
            document.getElementById('palace-modal-title').innerHTML =
                `🏰 Cung ${palaceNum} - ${analysis.name} <span class="badge bg-secondary">${analysis.element}</span>`;

            const body = document.getElementById('palace-body');

            // Build comprehensive HTML
            let html = `<div class="palace-detail">`;

            // Dụng Thần Section
            if (analysis.dungThan && analysis.dungThan.length > 0) {
                html += `
                    <div class="alert ${analysis.hasDungThan ? 'alert-success' : 'alert-warning'} mb-3">
                        <h6 class="alert-heading">🎯 Dụng Thần cho chủ đề "${topic}"</h6>
                        <p class="mb-1"><strong>Cần xem:</strong> ${analysis.dungThan.join(', ')}</p>
                        ${analysis.hasDungThan ?
                        `<p class="mb-0 text-success"><strong>✅ Cung này chứa:</strong> ${analysis.dungThanFound.join(', ')}</p>` :
                        `<p class="mb-0 text-warning">⚠️ Cung này không chứa Dụng Thần chính</p>`
                    }
                    </div>
                `;
            }

            // Basic Info
            html += `
                <h6 class="text-primary border-bottom pb-2">📊 Thông Tin Cơ Bản</h6>
                <div class="row mb-3">
                    <div class="col-6"><strong>Quái Tượng:</strong> ${analysis.name}</div>
                    <div class="col-6"><strong>Ngũ Hành:</strong> <span class="badge bg-info">${analysis.element}</span></div>
                    <div class="col-6"><strong>Cửu Tinh:</strong> ⭐ ${analysis.star}</div>
                    <div class="col-6"><strong>Bát Môn:</strong> 🚪 ${analysis.door}</div>
                    <div class="col-6"><strong>Bát Thần:</strong> 👤 ${analysis.deity}</div>
                    <div class="col-6"><strong>Can Thiên/Địa:</strong> ${analysis.stemHeaven}/${analysis.stemEarth}</div>
                </div>
            `;

            // Detailed Descriptions
            html += `
                <h6 class="text-success border-bottom pb-2 mt-3">🌟 Đặc Điểm Chi Tiết</h6>
                <div class="mb-3">
                    <p class="small"><strong>⭐ ${analysis.star}:</strong> ${analysis.starDescription}</p>
                    <p class="small"><strong>🚪 ${analysis.door}:</strong> ${analysis.doorDescription}</p>
                    <p class="small"><strong>👤 ${analysis.deity}:</strong> ${analysis.deityDescription}</p>
                </div>
            `;

            // Topic Interpretation
            if (analysis.topicInterpretation) {
                html += `
                    <h6 class="text-info border-bottom pb-2 mt-3">📖 Giải Thích Theo Chủ Đề</h6>
                    <div class="alert alert-light mb-3">
                        <p class="small mb-0">${analysis.topicInterpretation}</p>
                    </div>
                `;
            }

            // Advice
            if (analysis.advice) {
                html += `
                    <h6 class="text-warning border-bottom pb-2 mt-3">💡 Lời Khuyên</h6>
                    <div class="alert alert-warning mb-3">
                        <p class="small mb-0">${analysis.advice}</p>
                    </div>
                `;
            }

            // Special Markers
            const markers = [];
            if (analysis.isKongWang) markers.push('💀 Không Vong');
            if (analysis.isDiMa) markers.push('🐎 Dịch Mã');
            if (markers.length > 0) {
                html += `
                    <div class="alert alert-secondary mt-3">
                        <strong>Đặc điểm:</strong> ${markers.join(' | ')}
                    </div>
                `;
            }

            html += `</div>`;
            body.innerHTML = html;

            modal.show();
            this.showLoading(false);
        } catch (e) {
            console.error('Lỗi chi tiết cung:', e);
            this.showLoading(false);
            alert('Lỗi tải chi tiết cung');
        }
    },

    navigatePalace(direction) {
        this.currentPalaceIndex = (this.currentPalaceIndex + direction + this.palaceOrder.length) % this.palaceOrder.length;
        const palaceNum = this.palaceOrder[this.currentPalaceIndex];

        const info = document.getElementById('current-palace-info');
        if (info) {
            const palace = this.currentChart?.palaces.find(p => p.number === palaceNum);
            info.textContent = palace ? `Cung ${palaceNum} - ${palace.name}` : `Cung ${palaceNum}`;
        }

        this.showPalaceDetail(palaceNum);
    },

    async updateDungThan() {
        const content = document.getElementById('dung-than-content');
        if (!content) return;

        try {
            const response = await fetch(`${this.API_BASE}/topics`);
            const topics = await response.json();

            // For now, show a placeholder
            content.innerHTML = `
                <div class="small">
                    <div class="mb-2"><strong>🔮 Kỳ Môn:</strong> Xem Cửu Tinh, Bát Môn theo chủ đề "${this.currentTopic}"</div>
                    <div class="mb-2"><strong>📖 Mai Hoa:</strong> Xem quẻ chính và quẻ biến</div>
                    <div><strong>☯️ Lục Hào:</strong> Xem hào động và Lục Thân</div>
                </div>
            `;
        } catch (e) {
            console.error('Lỗi cập nhật Dụng Thần:', e);
        }
    },

    toggleDungThan() {
        this.dungThanExpanded = !this.dungThanExpanded;
        const content = document.getElementById('dung-than-content');
        const toggle = document.getElementById('dung-than-toggle');

        if (this.dungThanExpanded) {
            content.style.display = 'block';
            toggle.textContent = '▼';
        } else {
            content.style.display = 'none';
            toggle.textContent = '▶';
        }
    },

    async updateOtherTabs() {
        try {
            // Mai Hoa
            const mhRes = await fetch(`${this.API_BASE}/mai-hoa`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: this.currentTopic })
            });
            const mhData = await mhRes.json();
            document.getElementById('maihoa-content').innerHTML =
                `<pre style="white-space: pre-wrap; font-size: 0.9rem;">${mhData.interpretation || 'Đang tải...'}</pre>`;

            // Lục Hào
            const lhRes = await fetch(`${this.API_BASE}/luc-hao`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: this.currentTopic })
            });
            const lhData = await lhRes.json();
            document.getElementById('luchao-content').innerHTML =
                `<pre style="white-space: pre-wrap; font-size: 0.9rem;">${lhData.giai_thich || 'Đang tải...'}</pre>`;
        } catch (e) {
            console.error('Lỗi cập nhật tabs:', e);
        }
    },

    async showAnalysis() {
        if (!this.currentChart) {
            alert('Vui lòng lập bàn trước');
            return;
        }

        try {
            this.showLoading(true);
            const findPalace = (stem) => this.currentChart.palaces.find(p => p.stemHeaven === stem)?.number || 1;
            const chu_idx = findPalace(this.currentChart.can_ngay);
            const khach_idx = findPalace(this.currentChart.can_gio);

            const res = await fetch(`${this.API_BASE}/analyze`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    topic: this.currentTopic,
                    chu_idx,
                    khach_idx
                })
            });
            const data = await res.json();

            const body = document.getElementById('analysis-body');
            let html = `<div class="analysis-result">`;

            if (data.do_tin_cay_tong) {
                html += `<div class="alert alert-info">
                    <strong>📊 Độ tin cậy:</strong> ${data.do_tin_cay_tong}%
                </div>`;
            }

            if (data.phan_tich_9_phuong_phap?.ky_mon?.ket_luan) {
                html += `<h6 class="text-primary">🔮 Vị Thế Chủ - Khách</h6>
                <p>${data.phan_tich_9_phuong_phap.ky_mon.ket_luan}</p>`;
            }

            if (data.lien_mach) {
                html += `<hr><h6 class="text-success">⏰ Dòng Chảy Thời Gian</h6>`;
                if (data.lien_mach.qua_khu) html += `<p><strong>Quá khứ:</strong> ${data.lien_mach.qua_khu}</p>`;
                if (data.lien_mach.hien_tai) html += `<p><strong>Hiện tại:</strong> ${data.lien_mach.hien_tai}</p>`;
                if (data.lien_mach.tuong_lai) html += `<p><strong>Tương lai:</strong> ${data.lien_mach.tuong_lai}</p>`;
                if (data.lien_mach.ket_luan_tong_hop) {
                    html += `<div class="alert alert-success mt-3">
                        <strong>📝 Kết luận:</strong> ${data.lien_mach.ket_luan_tong_hop}
                    </div>`;
                }
            }

            html += `</div>`;
            body.innerHTML = html;

            const modal = new bootstrap.Modal(document.getElementById('analysisModal'));
            modal.show();
            this.showLoading(false);
        } catch (e) {
            console.error('Lỗi phân tích:', e);
            this.showLoading(false);
            alert('Lỗi phân tích chi tiết. Vui lòng thử lại.');
        }
    },

    showLoading(show) {
        const overlay = document.getElementById('loading-overlay');
        if (overlay) {
            overlay.classList.toggle('d-none', !show);
        }
    }
};

// Auto-login on Enter key
document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password');
    if (passwordInput) {
        passwordInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') app.login();
        });
        passwordInput.focus();
    }
});
