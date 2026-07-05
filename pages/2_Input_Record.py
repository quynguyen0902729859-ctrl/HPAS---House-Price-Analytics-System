import os
import pandas as pd
import streamlit as st
import time

if __name__ == "__main__":
    st.set_page_config(
        page_title="Input Record",
        layout="wide",
        page_icon="📈",
        initial_sidebar_state="expanded"
    )  
    st.sidebar.markdown("""
        <style>
            [data-testid="stBaseButton-primary"] {
                border-radius: 8px !important;
                border: none !important;
                transition: all 0.15s linear !important;
                height: 40px !important;-
            }
            [data-testid="stBaseButton-primary"] > div span div p {
                font-size: 20px !important;
                font-weight: bold !important;
            }
            .stAlert > div div div div p {
                font-weight: bold;
                font-size: 21px;
                margin-bottom: 8px;
                margin-left: 10px
            }
            [data-testid="stBaseButton-primary"]:hover {
                background-color: #1d4ed8 !important;
                transform: translateY(-2px) !important;
                box-shadow: 5px 5px 5px rgba(43, 108, 176, 0.4) !important;
            }
            [data-testid="stBaseButton-primary"]:active {
                transform: translateY(1.5px) !important;
            }
            * {
                font-family: Calibri, sans-serif
            }
            [data-testid="stAppDeployButton"] {
                display: none
            }
            section[data-testid="stSidebar"] {
                background-color: #242424 !important;
                color: white !important;
                width: 300px !important;
                text-align:center !important;
                padding-top: -100px;
                padding-bottom: -100px;
            }
            .esu {
                font-size: 18px;
                border-radius: 7.5px;
                padding-left: 10px;
                padding-top: 2px;
                padding-bottom: 2px;
                display: block;
                margin-bottom: 7px;
                margin-left: -3px;
                margin-right: 0px;
                transition: background-color 0.15s linear;
            }
            .esu:hover {
                background-color: #2E363A
            }
            [data-testid="stImage"] {
                margin-top: 0px;
                margin-bottom: -115px;   
            }
        </style>
        <div style="margin-top: -25px; margin-bottom: calc(100vh - 455px);">
            <a href="/" target="_self" class = "esu" style="text-decoration:none; color: white">
                Trang Chủ
            </a>
            <a href="/Market_Analysis" target="_self" class = "esu" style="text-decoration:none; color: white">
                Phân Tích Thị Trường
            </a>
            <a href="/Input_Record" target="_self" class = "esu" style="text-decoration:none; color: white; font-weight: bold; background-color: #2E363A">
                Thêm Dữ Liệu Dự Đoán
            </a>
            <a href="/Price_Prediction" target="_self" class = "esu" style="text-decoration:none; color: white">
                Phân Tích Dự Đoán
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.image("images/HPAS-7.PNG")  
    st.markdown("""
        <style>
        </style>
        <h1 style="font-size:65px; text-align:center; margin-top: -60px; line-height: 110px">
            THÊM DỮ LIỆU ĐỂ DỰ ĐOÁN
        </h1>  
        """,
        unsafe_allow_html=True
    )
    # with st.form("form"):
    col1, col2, col3 = st.columns([1,3,1])
    with col1:
        id = st.number_input(
            label="ID",
            min_value=0,
            max_value=999999,
            value=1,
            step=1,
            format="%d",
            help="Nhập ID của căn nhà để dễ dàng phân biệt giữa những căn nhà có các thuộc tính khác nhau, cũng như để biết dự đoán giá tiền của căn nhà nào",
        )
    with col2:
        region = st.selectbox(
            label="Vị trí",
            options=["Hà Nội", "Thành phố Hồ Chí Minh", "Tỉnh nhỏ", "Tỉnh lớn"],
            index=0,
            help="Do năng lực thu thập thông tin có hạn nên ta sẽ có 4 lựa chọn là Thành phố Hồ Chí Minh, Hà Nội, các tỉnh nhỏ và lớn. Hãy chọn một vị trí - nơi để đặt căn nhà của bạn - vì vị trí của căn nhà có thể ảnh hưởng ít nhiều đến giá thành của căn nhà.",
        )
    with col3:
        year = st.number_input(
            label="Năm xây",
            min_value=1900,
            max_value=2050,
            value=2000,
            step=1,
            format="%d",
            help="Hãy nhập năm mà căn nhà bạn muốn dự đoán giá được xây nên. Tính từ năm 1900 đến 2025.",
        )
    floors = st.slider(
        "Số tầng",
        min_value=1,
        max_value=10,
        value=3,
        step=1,
        help="Hãy chọn số tầng cho ngôi nhà mà bạn muốn dự đoán giá. Tối đa 10 tầng."
    )
    bedrooms = st.slider(
        "Số phòng ngủ",
        min_value=0,
        max_value=12,
        value=3,
        step=1,
        help="Hãy chọn số phòng ngủ cho ngôi nhà bạn muốn dự đoán giá. Tối đa 12 phòng ngủ."
    )
    bathrooms = st.slider(
        "Số phòng tắm",
        min_value=0,
        max_value=10,
        value=3,
        step=1,
        help="Hãy chọn số phòng tắm cho ngôi nhà bạn muốn dự đoán giá. Tối đa 10 phòng tắm."
    )
    col4, col5, col6, col7 = st.columns([1,1,1,1])
    with col5:
        frontage = st.number_input(
            label="Mặt tiền (m)",
            min_value=1.0,
            max_value=50.0,
            value=3.0,
            step=1.0,
            format="%.1f",
            help="Hãy nhập số mét mặt tiền mà bạn muốn căn nhà bạn muốn dự đoán giá có.",
        )
    with col6:
        road = st.number_input(
            "Độ rộng đường (m)", 
            min_value=1.0, 
            max_value=60.0, 
            value=4.0,  # Mặc định là 4m (đường ô tô tránh hoặc hẻm lớn)
            step=0.5, 
            format="%.1f",
            help="Hãy nhập độ rộng của đường hoặc con hẻm trước căn nhà bạn muốn dự đoán."
        )
    with col7:
        distance = st.number_input(
            label="Khoảng cách đến trung tâm (km)",
            min_value=0.0,
            max_value=100.0,
            value=10.0,
            step=1.0,
            format="%.1f",
            help="Hãy nhập khoảng cách từ căn nhà bạn muốn dự đoán giá cho đến trung tâm của vị trí căn nhà đó đang ở.",
        )
    with col4:
        area = st.number_input(
            label="Diện tích (m²)",
            min_value=20.0,
            max_value=1000.0,
            value=50.0,
            step=1.0,
            format="%.1f",
            help="Hãy nhập diện tích của căn nhà ban muốn dự đoán, vì nó ảnh hưởng rất lớn đến giá trị của một căn nhà.",
        )
    if area >= 500.0 or distance >= 50.0 or frontage >= 30.0 or bedrooms >= 5 or bathrooms >= 5 or floors > 4 or road > 10 or year < 1980 or frontage > (area/floors)**0.5:
        st.warning("⚠️ Các giá trị quá khác biệt so với dữ liệu huấn luyện có thể làm giảm độ chính xác của dự đoán.")
    sent = st.button(
        label="LƯU THÔNG TIN CĂN NHÀ",
        type="primary",
        help="Nút này khi ấn, toàn bộ thông tin bạn đã nhập trên sẽ được gửi đến mô hình để mô hình dự đoán giá nhà",
        icon="💾",
        use_container_width=True
    )
    if sent:
        df = pd.read_csv("data/test_data.csv")
        if id in df["House_ID"].values:
            st.toast(f"ID số {id} đã tồn tại!", icon = "❌")
            time.sleep(1)
            st.toast(f"Vui lòng chọn ID khác để tiếp tục!", icon = "⚠️")
        else:
            # Tạo một dòng dữ liệu từ thông tin mà người dùng cung cấp
            new = pd.DataFrame([{
                'House_ID': id,
                'Region': region,
                'Area': area,
                'Frontage': frontage,
                'w-road': road,
                'Distance': distance,
                'Floors': floors,
                'Bedrooms': bedrooms,
                'Bathrooms': bathrooms,
                'built-yr': year,
            }])
            # Thêm dòng dữ liệu trên vào file
            new.to_csv(
                "data/test_data.csv",
                mode="a",
                header=False,
                index=False
            )
            st.toast("Dữ liệu đã được lưu!", icon="🎉")
    st.markdown("""
        <h2 style="margin-top: 50px; text-align: center">LỊCH SỬ TẠO</h2>
        """,
        unsafe_allow_html=True
    )
    df = pd.read_csv("data/test_data.csv")
    st.dataframe(df, hide_index=True)
