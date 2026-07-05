import streamlit as st

if __name__ == "__main__":
    st.set_page_config(
        page_title="Home page",
        layout="wide",
        page_icon="🏠",
        initial_sidebar_state="expanded"
    )    
    st.markdown("""
        <style>
            * {
                font-family: Calibri, sans-serif
            }
            section[data-testid="stSidebar"] {
                background-color: #242424 !important;
                color: white !important;
                width: 300px !important;
                text-align:center !important;
                padding-top: -100px;
                padding-bottom: -100px;
            }
            [data-testid="stAppDeployButton"] {
                display: none
            }
            .use {
                margin-top: 11px;
                margin-bottom: 11px;
                padding-top:6px;
                padding-bottom:2px;
                padding-left:20px;
                padding-right:20px;
                border-radius:15px;
                border:1px solid #ccc;
                transition: box-shadow 0.2s linear; border 0.2s linear;
                text-align: justify;
            }
            .use:hover {
                box-shadow: 0 0 0 3px blue;
                border: 1px solid blue
            }
            .describe {
                font-size: 20px !important;
                font-weight: bold;
                line-height: 25px;
            }
            .cre {
                font-size: 25px !important;
                margin-top: -10px !important;
                display: inline
            }
        </style>
        <h1 style="font-size:100px; text-align:center; margin-top: -70px; line-height: 110px">
            House Price Analytics System
        </h1>        
        <p style="color: grey; font-size:30px; text-align:center; margin-top: 100px; line-height: 50px">
            Chào mừng đến với HPAS – một hệ thống phân tích và dự đoán giá nhà dựa trên dữ liệu thu thập được từ thực tế lẫn người dùng. Hệ thống giúp trực quan hóa dữ liệu, nhận diện xu hướng giá và cung cấp các dự đoán thông qua các biểu đồ và Machine Learning. 
        </p>
        <h1 style = "margin-top: 75px; margin-bottom:-5px; font-size: 60px">
            Chức năng
        </h1>
        <a href="/Market_Analysis" target="_self" style="text-decoration:none;">
            <div class = "use">
                <h2 style="font-weight: bolder;">📊 Phân tích thị trường</h2>
                <p class="describe">Khám phá mối quan hệ giữa giá nhà và các yếu tố ảnh hưởng, cũng như những xu hướng tăng giảm của giá nhà thông qua những biểu đồ trực quan.</p>
            </div>
        </a>
        <a href="/Input_Record" target="_self" style="text-decoration:none;">
            <div class = "use">
                <h2 style="font-weight: bolder;">📈 Thêm dữ liệu dự đoán</h2>
                <p class="describe">Phân tích sự thay đổi của giá nhà theo thời gian để nhận diện xu hướng tăng giảm của thị trường. Giúp đánh giá tốc độ biến động giá và những giai đoạn có sự thay đổi đáng chú ý.</p>
            </div>
        </a>
        <a href="/Price_Prediction" target="_self" style="text-decoration:none;">
            <div class = "use">
                <h2 style="font-weight: bolder;">🔮 Phân tích dự đoán</h2>
                <p class="describe">Nhập dữ liệu của một căn nhà để dự đoán giá nhà bằng mô hình Machine Learning. Kết quả dự đoán được xây dựng dựa trên các mẫu dữ liệu đã được nhập trước đó.</p>
            </div>
        </a>
        <h1 style = "margin-top: 80px; margin-bottom: 10px; font-size: 60px">
            Credits
        </h1>
        <p class="cre">Ứng dựng được xây dựng với</p><a class="cre" href="https://streamlit.io/" style="text-decoration:none; margin-left: 7px; font-weight: bold">streamlit</a>
        <br>
        <p class="cre">Bản quyền thuộc về <a class="cre" href="https://streamlit.io/" style="text-decoration:none; margin-left: 2px; font-weight: bold">Nguyễn Đức Thiên Quý</a></p>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("""
        <style>
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
            <a href="/" target="_self" class = "esu" style="text-decoration:none; color: white; font-weight: bold; background-color: #2E363A">
                Trang Chủ
            </a>
            <a href="/Market_Analysis" target="_self" class = "esu" style="text-decoration:none; color: white">
                    Phân Tích Thị Trường
            </a>
            <a href="/Input_Record" target="_self" class = "esu" style="text-decoration:none; color: white">
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