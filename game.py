import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(
    page_title="中山機電偵查局",
    page_icon="🔍",
    layout="wide"
)

# ---------首頁---------
st.title("🔍 中山機電偵查局")

# st.write("""
# 🎬 故事背景
         
# 中山機電研究中心的一套「環境監測與控制系統」突然發生異常，
# 系統的部分電路被破壞，導致整個監測系統停止運作。

# 研究中心懷疑有人動過電路板，因此啟動 「機電偵查任務」。

# 你們將扮演 中山機電偵查員，透過工程推理與電路修復，逐步修復系統。
# """)

page = st.sidebar.radio(
    "請選擇關卡",
    ["首頁", "第一關：LED電路", "第二關：RLC濾波", "第三關：溫度轉換"]
)

# ---------首頁---------
if page == "首頁":

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

    .hint-box {
        background-color: #fff7ed;
        border: 2px solid #fdba74;
        padding: 18px 20px;
        border-radius: 14px;
        margin-top: 20px;
    }

    .hint-title {
        font-size: 22px;
        font-weight: 700;
        color: #9a3412;
        margin-bottom: 8px;
    }

    .hint-text {
        font-size: 17px;
        color: #7c2d12;
        line-height: 1.7;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-box">
        <div class="hero-title">🎬 故事背景</div>
        <div class="hero-subtitle">
            中山機電研究中心的一套「環境監測與控制系統」突然發生異常，
            系統的部分電路被破壞，導致整個監測系統停止運作。<br>
             <br>
            研究中心懷疑有人動過電路板，因此啟動 「機電偵查任務」。<br>
             <br>
            你們將扮演 中山機電偵查員，透過工程推理與電路修復，逐步修復系統。
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">🕵️ 偵查提示</div>', unsafe_allow_html=True)

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

# ---------第一關---------
elif page == "第一關：LED電路":

    st.header("第一關：修復 LED 電路")
    
    st.write("""
    LED 指示燈全部熄滅，
    請完成電路拼接。
    
    當電路修復後，觀察亮起的顏色與數量。
    """)

    st.subheader("請輸入各顏色 LED 數量")

    red = st.number_input("🔴 紅色 LED", min_value=0, max_value=10, value=0)
    green = st.number_input("🟢 綠色 LED", min_value=0, max_value=10, value=0)
    white = st.number_input("⚪ 白色 LED", min_value=0, max_value=10, value=0)
    yellow = st.number_input("🟡 黃色 LED", min_value=0, max_value=10, value=0)

    if st.button("確認答案"):

        if red == 3 and green == 0 and white == 1 and yellow == 2:

            st.success("第一關成功！LED 模組已恢復。")
            url = "https://assets2.lottiefiles.com/packages/lf20_jbrw3hcz.json"
            lottie_success = load_lottie(url)

        else:

            st.error("LED 數量不正確，請再檢查電路。")

# ---------第二關---------
elif page == "第二關：RLC濾波":

    st.header("第二關：RLC濾波器")

    st.write("""
    感測訊號出現雜訊，
    請調整 R、L、C 數值。
    """)

    r = st.slider("R值",1,100,50)
    l = st.slider("L值",1,100,20)
    c = st.slider("C值",1,100,10)

    if st.button("測試濾波"):

        if r == 50 and l == 20 and c == 10:

            st.success("濾波成功！")
            st.balloons()

        else:

            st.warning("濾波效果不正確")

# ---------第三關---------
elif page == "第三關：溫度轉換":

    st.header("第三關：溫度轉換")

    st.write("""
    系統需要將攝氏轉換為華氏。
    """)

    c = st.number_input("輸入攝氏溫度",value=25)

    if st.button("轉換"):

        f = c * 9/5 + 32

        st.success(f"華氏溫度 = {f}")

        if f == 77:

            st.balloons()
            st.success("系統恢復成功！")