import time
import streamlit as st
import random

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
all_pages = ["首頁", "第一關：LED電路", "第二關：RC電路", "系統恢復"]

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
for p in ["第一關：LED電路", "第二關：RC電路"]:
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

    st.markdown("""
    <div class="step-card" style="text-align:center;">
        <div class="step-title">🕵️ 偵查提示</div>
        <div class="step-text" style="font-size:26px; font-weight:800;">
            🔧 組裝電路
        </div>
        <div style="font-size:28px; margin:10px 0;">⬇️</div>
        <div class="step-text" style="font-size:26px; font-weight:800;">
            📡 完成濾波
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
    st.title("💡 第一關：七段顯示器挑戰")

    col1, col2 = st.columns([1.4, 1])
    with col1:
        st.write("""
                偵查員進入控制室後發現顯示模組被破壞。
                
                系統使用 **七段顯示器 (Seven Segment Display)** 來顯示數字。

                系統會隨機抽出一個數字 **(0–9)**，  
                你需要利用桌上的元件組裝電路，
                讓七段顯示器可以成功顯示。
        """)
    with col2:
        st.image("images/level1_1.png", caption="七段顯示器示意圖", use_container_width=True)

    # 初始化
    if "target_number" not in st.session_state:
        st.session_state.target_number = None

    # 抽選按鈕
    if st.button("🎲 抽選數字"):

        with st.spinner("抽選中..."):
            time.sleep(1)

        st.session_state.target_number = random.randint(0,9)

    # 顯示抽到的數字
    if st.session_state.target_number is not None:

        st.subheader("任務數字")

        st.markdown(
            f"""
            <div style="
            font-size:90px;
            font-weight:bold;
            text-align:center;
            background:#0f172a;
            color:white;
            padding:30px;
            border-radius:15px;">
            {st.session_state.target_number}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("請讓七段顯示器顯示此數字")

        password = st.text_input("請輸入通關密碼")

        if st.button("確認答案"):

            if password == "nsysu-F35":

                st.success("第一關成功！顯示模組恢復。")
                st.balloons()

                complete_level("第一關：LED電路")
                unlock_level("第二關：RC電路")

                time.sleep(1.5)

                go_to("第二關：RC電路")

            else:

                st.error("顯示結果不正確，請重新檢查電路。")

    else:

        st.info("請先按「抽選數字」開始任務")

# =========================
# 第二關
# =========================
elif page == "第二關：RC電路":
    st.title("📡 第二關：訊號濾波任務")

    st.write("""
    現在你已經成功顯示模組，發現環境感測器的訊號有異常。
             """)
             
    st.markdown("### 💻系統顯示：感測訊號受到雜訊干擾，導致數據不穩定")

    st.write("""
    因此你查看了放在桌子旁邊的工程日誌：
    """)

    st.image("images/level2_1.png", caption="工程日誌", use_container_width=True)

    st.components.v1.iframe(
    "https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l5YCcyWrQDhAZmmA7AGxbIBMW6BY6VWALCAKySMi2YMCmAtGGAFAA3VgXpYCmWiJDpmzCAWYMoymAz4B3YfRmNEJabI279YiVNNQ+AY2lSk+ivRLoJUWPEhovacNDzw8QjBPEgYZcjc4CEg+ACcQRAVwPQSk50xmWiwYgA8ExCUSNnBIUJBQiHowAhAAGwB7AEMAEz5m4wMQcUwdfWaOADNGgFdagBcjbs68dG1DTTwSZgspixjNR2SHKR112zmQGYO9zZ1E5l2jc87r+0sNqXT97HF754tF5de966frtauSQsmwBmiwDBMr1CNVB2Ah5RccMhGSM0JemF4yLe4Icy3hdz2aJ0OM6hIYNR0+Ap83AYCxxO+Rh0lMIpLaIB41M6vRA-SGowmeXIeHKxVo+HKDEq4BqDRacSRW0VT0y2SMnPRHLAtFEjM0PB1nQ1lyEBt1mDNpPAXUUKjcalokCw0iwJlmJSKrF2rAA+ugfZAfWBwfhAwwA7gfTwfSQfbQfVg+I7nVwlphyPRMlJloH-YHHYh-eGYGAo6XY9kE0mnUqLOKapJM+U8H6A3HPEWI6Xo7GSC3E-rqpqGSjNAwUitEQD6s3pMpg1L-CwS8oan3sNhZJuN03RHwgA",
    height=600
    )
    st.link_button(
    "🔧 開啟濾波器模擬器",
    "https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l5YCcyWrQDhAZmmA7AGxbIBMW6BY6VWALCAKySMi2YMCmAtGGAFAA3VgXpYCmWiJDpmzCAWYMoymAz4B3YfRmNEJabI279YiVNNQ+AY2lSk+ivRLoJUWPEhovacNDzw8QjBPEgYZcjc4CEg+ACcQRAVwPQSk50xmWiwYgA8ExCUSNnBIUJBQiHowAhAAGwB7AEMAEz5m4wMQcUwdfWaOADNGgFdagBcjbs68dG1DTTwSZgspixjNR2SHKR112zmQGYO9zZ1E5l2jc87r+0sNqXT97HF754tF5de966frtauSQsmwBmiwDBMr1CNVB2Ah5RccMhGSM0JemF4yLe4Icy3hdz2aJ0OM6hIYNR0+Ap83AYCxxO+Rh0lMIpLaIB41M6vRA-SGowmeXIeHKxVo+HKDEq4BqDRacSRW0VT0y2SMnPRHLAtFEjM0PB1nQ1lyEBt1mDNpPAXUUKjcalokCw0iwJlmJSKrF2rAA+ugfZAfWBwfhAwwA7gfTwfSQfbQfVg+I7nVwlphyPRMlJloH-YHHYh-eGYGAo6XY9kE0mnUqLOKapJM+U8H6A3HPEWI6Xo7GSC3E-rqpqGSjNAwUitEQD6s3pMpg1L-CwS8oan3sNhZJuN03RHwgA"
    )

    c = st.slider("C值(uF)", 10, 100, 10, step=10)

    if st.button("測試濾波", use_container_width=True):
        if c == 60:
            st.success("第二關成功！恢復濾波模組。")
            unlock_level("系統恢復")

            with st.spinner("正在載入最終結果..."):
                time.sleep(1.8)
            unlock_level("系統恢復")
            st.balloons()

            go_to("系統恢復")
        else:
            st.warning("濾波效果不正確。")

# =========================
# 最終成功畫面
# =========================
elif page == "系統恢復":
    st.title("🎉 系統恢復成功")

    st.success("""
恭喜偵查員！

你成功修復了中山機電研究中心的所有電路模組，
系統已恢復正常運作。
               
""")

    st.balloons()

    st.markdown("""
## 🏆 任務完成

✅ LED 指示系統恢復  
✅ 訊號濾波系統恢復  

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