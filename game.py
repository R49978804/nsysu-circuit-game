import time
import streamlit as st

st.set_page_config(
    page_title="中山機電偵查局",
    page_icon="🔍",
    layout="wide"
)

# =========================
# Session State 初始化
# =========================
if "current_page" not in st.session_state:
    st.session_state.current_page = "首頁"

if "unlocked_levels" not in st.session_state:
    st.session_state.unlocked_levels = ["首頁", "第一關：LED電路"]

if "completed_levels" not in st.session_state:
    st.session_state.completed_levels = []

# =========================
# 工具函式
# =========================
def go_to(page_name: str):
    st.session_state.current_page = page_name
    st.rerun()

def unlock_level(level_name: str):
    if level_name not in st.session_state.unlocked_levels:
        st.session_state.unlocked_levels.append(level_name)

def complete_level(level_name: str):
    if level_name not in st.session_state.completed_levels:
        st.session_state.completed_levels.append(level_name)

def level_status_text(level_name: str):
    if level_name in st.session_state.completed_levels:
        return "✅ 已完成"
    elif level_name in st.session_state.unlocked_levels:
        return "🔓 已解鎖"
    else:
        return "🔒 未解鎖"

# =========================
# Sidebar
# =========================
all_pages = ["首頁", "第一關：LED電路", "第二關：RLC濾波", "第三關：溫度轉換", "系統恢復"]

st.sidebar.title("🕵️ 關卡選單")
st.sidebar.write("請依序完成任務。")

for p in all_pages:
    if p == "系統恢復":
        # 最終畫面不讓玩家手動點進去
        continue

    unlocked = p in st.session_state.unlocked_levels
    label = f"{p}　{level_status_text(p)}"
    if st.sidebar.button(label, disabled=not unlocked, key=f"nav_{p}"):
        go_to(p)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📱 玩家入口")
st.sidebar.info("掃描活動 QR Code 後，即可進入本介面開始闖關。")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🧾 目前進度")
for p in ["第一關：LED電路", "第二關：RLC濾波", "第三關：溫度轉換"]:
    st.sidebar.write(f"- {p}：{level_status_text(p)}")

# =========================
# 頁面控制
# =========================
page = st.session_state.current_page

# =========================
# 首頁
# =========================
if page == "首頁":
    st.title("🔍 中山機電偵查局")

    st.markdown("""
    <style>
    .hero-box {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        padding: 40px 30px;
        border-radius: 20px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 20px;
        color: #cbd5e1;
        line-height: 1.8;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 15px;
        color: #0f172a;
    }

    .step-card {
        background-color: #f8fafc;
        border-left: 8px solid #2563eb;
        padding: 18px 20px;
        border-radius: 14px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.06);
    }

    .step-title {
        font-size: 22px;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 8px;
    }

    .step-text {
        font-size: 18px;
        color: #334155;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-box">
        <div class="hero-title">🎬 故事背景</div>
        <div class="hero-subtitle">
            中山機電研究中心的一套「環境監測與控制系統」突然發生異常，
            系統的部分電路被破壞，導致整個監測系統停止運作。<br><br>
            研究中心懷疑有人動過電路板，因此啟動「機電偵查任務」。<br><br>
            你們將扮演中山機電偵查員，透過工程推理與電路修復，逐步修復系統。
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🕵️ 偵查提示")

    st.markdown("""
    <div class="step-card">
        <div class="step-title">1️⃣ 完成實體電路</div>
        <div class="step-text">
            根據現場的線索與元件功能，將缺失的電路拼接完成。
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="step-card">
        <div class="step-title">2️⃣ 在系統輸入答案</div>
        <div class="step-text">
            觀察燈號、濾波結果或轉換數值，將你找到的答案輸入系統。
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="step-card">
        <div class="step-title">3️⃣ 解鎖下一關</div>
        <div class="step-text">
            每成功修復一個模組，就能取得新線索，並逐步接近最終真相。
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("▶ 開始偵查", use_container_width=True):
            go_to("第一關：LED電路")
    with col2:
        if st.button("🔄 重置進度", use_container_width=True):
            st.session_state.current_page = "首頁"
            st.session_state.unlocked_levels = ["首頁", "第一關：LED電路"]
            st.session_state.completed_levels = []
            st.rerun()

# =========================
# 第一關
# =========================
elif page == "第一關：LED電路":
    st.title("💡 第一關：修復 LED 電路")

    st.write("""
    偵查員首先抵達控制室，但系統的指示電路板已經被破壞。  
    多顆 LED 指示燈應該顯示系統狀態，但目前完全沒有反應。  

    現場留下部分電路圖與元件，你們必須拼接電路，讓整個電路形成完整通路。  
    請完成桌上的電路，當電路恢復運作後，LED 指示燈將亮起。
    """)

    st.info("提示：未亮起的 LED 請輸入 0")

    st.subheader("請輸入各顏色 LED 數量")
    red = st.number_input("🔴 紅色 LED", min_value=0, max_value=10, value=0)
    green = st.number_input("🟢 綠色 LED", min_value=0, max_value=10, value=0)
    white = st.number_input("⚪ 白色 LED", min_value=0, max_value=10, value=0)
    yellow = st.number_input("🟡 黃色 LED", min_value=0, max_value=10, value=0)

    if st.button("確認第一關答案", use_container_width=True):
        if red == 3 and green == 0 and white == 1 and yellow == 2:
            st.success("第一關成功！LED 模組已恢復。")
            st.balloons()

            complete_level("第一關：LED電路")
            unlock_level("第二關：RLC濾波")

            with st.spinner("正在解鎖第二關..."):
                time.sleep(1.5)

            go_to("第二關：RLC濾波")
        else:
            st.error("LED 數量不正確，請再檢查電路。")

# =========================
# 第二關
# =========================
elif page == "第二關：RLC濾波":
    st.title("📡 第二關：訊號濾波任務")

    st.write("""
    偵查員成功恢復電源後，發現環境感測器的訊號仍然異常。  

    系統顯示：感測訊號受到雜訊干擾，導致數據不穩定。  

    工程日誌顯示，這個模組原本使用 RLC 濾波器來處理訊號。  
    但現在部分元件的數值被調整過，濾波效果失效。  

    請調整電腦中的 R、L、C 的數值，使電路達到指定的濾波效果。
    """)

    r = st.slider("R值", 1, 100, 50)
    l = st.slider("L值", 1, 100, 20)
    c = st.slider("C值", 1, 100, 10)

    if st.button("測試濾波", use_container_width=True):
        if r == 50 and l == 20 and c == 10:
            st.success("第二關成功！濾波模組已恢復。")
            st.snow()

            complete_level("第二關：RLC濾波")
            unlock_level("第三關：溫度轉換")

            with st.spinner("正在解鎖第三關..."):
                time.sleep(1.5)

            go_to("第三關：溫度轉換")
        else:
            st.warning("濾波效果不正確。")

# =========================
# 第三關
# =========================
elif page == "第三關：溫度轉換":
    st.title("🌡️ 第三關：溫度解碼")

    st.write("""
    最後，偵查員發現系統的溫度監測模組無法正常顯示。  

    原本系統會將感測到的攝氏溫度轉換為華氏溫度，並顯示在數位顯示器上。  
    然而轉換電路遭到破壞，導致顯示數值錯誤。  

    請利用提供的電路元件，完成溫度轉換電路，使系統能正確將：  

    **F = 9/5 × C + 32**  

    的計算結果輸出到顯示模組。
    """)

    celsius = st.number_input("輸入攝氏溫度", value=25)

    if st.button("執行溫度轉換", use_container_width=True):
        fahrenheit = celsius * 9 / 5 + 32
        st.success(f"華氏溫度 = {fahrenheit}")

        if fahrenheit == 77:
            st.success("系統恢復成功！")
            st.balloons()

            complete_level("第三關：溫度轉換")
            unlock_level("系統恢復")

            with st.spinner("正在載入最終結果..."):
                time.sleep(1.8)

            go_to("系統恢復")

# =========================
# 最終成功畫面
# =========================
elif page == "系統恢復":
    st.title("🎉 系統恢復成功")

    st.success("""
恭喜偵查員！

你們成功修復了中山機電研究中心的所有電路模組，
系統已恢復正常運作。
""")

    st.balloons()

    st.markdown("""
## 🏆 任務完成

✅ LED 指示系統恢復  
✅ 訊號濾波系統恢復  
✅ 溫度監測系統恢復  

### 🕵️ 中山機電偵查任務完成！
""")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 回到首頁", use_container_width=True):
            go_to("首頁")
    with col2:
        if st.button("🔄 再玩一次", use_container_width=True):
            st.session_state.current_page = "首頁"
            st.session_state.unlocked_levels = ["首頁", "第一關：LED電路"]
            st.session_state.completed_levels = []
            st.rerun()