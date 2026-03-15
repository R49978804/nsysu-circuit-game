import streamlit as st

st.set_page_config(
    page_title="中山機電偵查局",
    page_icon="🔍",
    layout="wide"
)

# ---------首頁---------
st.title("🔍 結構破案：中山機電偵查局")

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

    st.header("遊戲說明")

    st.write("""
    1️⃣ 完成實體電路  
    2️⃣ 在系統輸入答案  
    3️⃣ 解鎖下一關  
    """)

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