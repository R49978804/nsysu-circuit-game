import streamlit as st

st.set_page_config(
    page_title="中山機電偵查局",
    page_icon="🔍",
    layout="wide"
)

# ---------首頁---------
st.title("🔍 中山機電偵查局")

st.write("""
中山機電研究中心的監測系統遭到破壞。

三個重要電路模組失去功能，
你們是機電偵查員，必須修復電路並找出最終密碼。
""")

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
        <div class="hero-title">🔍 結構破案：中山機電偵查局</div>
        <div class="hero-subtitle">
            中山機電研究中心的監測系統遭到破壞。<br>
            三個重要電路模組失去功能，現在需要你們化身偵查員，<br>
            透過觀察、拼接與推理，逐步修復系統，找出最終密碼。
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">🎮 任務流程</div>', unsafe_allow_html=True)

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

    st.markdown("""
    <div class="hint-box">
        <div class="hint-title">🕵️ 偵查提示</div>
        <div class="hint-text">
            請從左側欄選擇關卡開始挑戰。<br>
            每一關都代表一個待修復的系統模組，請仔細觀察現象並推理答案。
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------第一關---------
elif page == "第一關：LED電路":

    st.header("第一關：修復LED電路")
    
    st.write("""
    LED 指示燈全部熄滅，
    請完成電路拼接。
    
    當電路修復後，觀察亮起的顏色與數量。
    """)

    answer = st.text_input("輸入答案，例如：red3")

    if st.button("確認答案"):

        if answer == "red3":
            st.success("第一關成功！")
            st.balloons()
        else:
            st.error("答案不正確，請再檢查電路")

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