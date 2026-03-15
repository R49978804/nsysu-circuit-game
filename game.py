import streamlit as st

st.set_page_config(page_title="中山機電偵查局", page_icon="🔍", layout="wide")

# -------------------------
# 初始化
# -------------------------
if "level" not in st.session_state:
    st.session_state.level = 1

# 關卡選單
level_options = {
    "第一關：修復照明電路": 1,
    "第二關：RLC 濾波器": 2,
    "第三關：溫度解碼": 3,
}

st.sidebar.title("🎮 關卡選擇")

selected_label = st.sidebar.radio(
    "請選擇要玩的關卡",
    list(level_options.keys()),
    index=st.session_state.level - 1
)

st.session_state.level = level_options[selected_label]

st.sidebar.markdown("---")
st.sidebar.write(f"目前關卡：**{selected_label}**")

# -------------------------
# 首頁資訊
# -------------------------
st.title("🔍 結構破案：中山機電偵查局")
st.write("請從左側選擇要挑戰的關卡。")

# -------------------------
# 第一關
# -------------------------
if st.session_state.level == 1:
    st.header("第一關：修復照明電路")

    st.write("""
    電路板上的 LED 指示燈全部熄滅，
    請完成電路拼接，使電流形成完整通路。
    """)

    # 如果有圖片可取消註解
    # st.image("led_board.png")

    answer1 = st.text_input("輸入亮起的顏色與數量（例如：red3）", key="q1")

    if st.button("確認第一關答案"):
        if answer1 == "red3":
            st.success("第一關成功：電路修復完成！")
        else:
            st.error("答案不正確，請再檢查電路。")

# -------------------------
# 第二關
# -------------------------
elif st.session_state.level == 2:
    st.header("第二關：RLC 濾波器")

    st.write("""
    感測器訊號受到雜訊干擾，
    請調整 R、L、C 的數值，
    讓系統達到目標濾波效果。
    """)

    r = st.slider("R", 1, 100, key="r")
    l = st.slider("L", 1, 100, key="l")
    c = st.slider("C", 1, 100, key="c")

    if st.button("測試濾波"):
        if r == 50 and l == 20 and c == 10:
            st.success("第二關成功：濾波完成！")
        else:
            st.warning("濾波效果尚未達標，請再調整。")

# -------------------------
# 第三關
# -------------------------
elif st.session_state.level == 3:
    st.header("第三關：溫度解碼")

    st.write("系統需要將攝氏溫度轉換為華氏溫度。")

    celsius = st.number_input("請輸入攝氏溫度", value=25.0, key="temp")

    if st.button("轉換"):
        f = celsius * 9 / 5 + 32
        st.success(f"華氏溫度 = {f}")

        if f == 77:
            st.balloons()
            st.success("第三關成功：系統完全恢復！")