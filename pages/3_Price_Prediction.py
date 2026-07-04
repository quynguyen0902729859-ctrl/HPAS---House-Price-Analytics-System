# import os
# import streamlit as st
# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression
# import time
# if __name__ == "__main__":
#     st.set_page_config(
#         page_title="Home page",
#         layout="wide",
#         page_icon="🏠",
#         initial_sidebar_state="expanded"
#     )  
#     st.sidebar.markdown("""
#         <style>
#             div[data-testid="stButton"] > button {
#                 border-radius: 8px !important;
#                 border: none !important;
#                 transition: all 0.15s linear !important;
#                 height: 40px !important;
#             }
#             .stAlert > div div div div p {
#                 font-weight: bold;
#                 font-size: 25px;
#                 margin-top: -6px;
#                 margin-bottom: 8px;
#                 margin-left: 10px
#             }
#             /* Chỉ text bên trong button */
#             div[data-testid="stButton"] > button p {
#                 font-size: 20px;
#                 font-weight: bold !important;
#             }
#             /* Hover */
#             div[data-testid="stButton"] > button:hover {
#                 background-color: #1d4ed8 !important;
#                 transform: translateY(-2px) !important;
#                 box-shadow: 5px 5px 5px rgba(43, 108, 176, 0.4) !important;
#             }
#             /* Click */
#             div[data-testid="stButton"] > button:active {
#                 transform: translateY(1.5px) !important;
#             }
#             .stColumn > div div div button {
#                 height: 56px !important;
#             }
#             .stColumn > div div div button div span p{
#                 font-size: 25px !important;
#             }
#             * {
#                 font-family: Calibri, sans-serif
#             }
#             [data-testid="stAppDeployButton"] {
#                 display: none
#             }
#             section[data-testid="stSidebar"] {
#                 background-color: #242424 !important;
#                 color: white !important;
#                 width: 300px !important;
#                 text-align:center !important;
#                 padding-top: -100px;
#                 padding-bottom: -100px;
#             }
#             .esu {
#                 font-size: 18px;
#                 border-radius: 7.5px;
#                 padding-left: 10px;
#                 padding-top: 2px;
#                 padding-bottom: 2px;
#                 display: block;
#                 margin-bottom: 7px;
#                 margin-left: -3px;
#                 margin-right: 0px;
#                 transition: background-color 0.15s linear;
#             }
#             .esu:hover {
#                 background-color: #2E363A
#             }
#             [data-testid="stImage"] {
#                 margin-top: 0px;
#                 margin-bottom: -100px;          
#             }
#         </style>
#         <div style="margin-top: -25px; margin-bottom: calc(100vh - 455px);">
#             <a href="http://localhost:9999" target="_self" class = "esu" style="text-decoration:none; color: white">
#                 Trang Chủ
#             </a>
#             <a href="http://localhost:9999/Market_Analysis" target="_self" class = "esu" style="text-decoration:none; color: white">
#                 Phân Tích Thị Trường
#             </a>
#             <a href="http://localhost:9999/Input_Record" target="_self" class = "esu" style="text-decoration:none; color: white">
#                 Thêm Dữ Liệu Dự Đoán
#             </a>
#             <a href="http://localhost:9999/Price_Prediction" target="_self" class = "esu" style="text-decoration:none; color: white; font-weight: bold; background-color: #2E363A">
#                 Phân Tích Dự Đoán
#             </a>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
#     if "trained" not in st.session_state:
#         st.toast("Mô hình chưa được huấn luyện!", icon="✋")
#         time.sleep(1.5)
#         st.toast("Hãy bắt đầu huấn luyện...", icon="🙏")
#     if "model" not in st.session_state:
#         st.session_state.model = None
#     if "y_test" not in st.session_state:
#         st.session_state.y_test = None
#     if "X_test" not in st.session_state:
#         st.session_state.X_test = None
#     if "trained" not in st.session_state:
#         st.session_state.trained = False
#     if "mean_squared_error" not in st.session_state:
#         st.session_state.mean_squared_error = None
#     if "mean_absolute_error" not in st.session_state:
#         st.session_state.mean_absolute_error = None
#     if "r2_score" not in st.session_state:
#         st.session_state.r2_score = None
#     if "status" not in st.session_state:
#         st.session_state.status = "error"
#     def change_state():
#         st.session_state.status = "success"
#     st.sidebar.image("images/HPAS-7.PNG")  
#     st.markdown("""
#         <h1 style="font-size:65px; text-align:center; margin-top: -60px; line-height: 110px">
#             MÔ HÌNH DỰ ĐOÁN
#         </h1>  
#         """,
#         unsafe_allow_html=True
#     )          
#     col1, col2 = st.columns([1,4])
#     with col1:
#         training = st.button(
#             label="Huấn luyện",
#             type="primary",
#             icon="🏋",
#             use_container_width=True
#         )
#     with col2:
#         if training:
#             if not st.session_state.trained:
#                 change_state()
#                 st.toast("Đang huấn luyện...", icon="🏋")
#                 from sklearn.linear_model import LinearRegression
#                 from sklearn.model_selection import train_test_split
#                 from sklearn.metrics import (
#                     mean_squared_error,
#                     mean_absolute_error,
#                     r2_score
#                 )
#                 st.session_state.mean_squared_error = mean_squared_error
#                 st.session_state.mean_absolute_error = mean_absolute_error
#                 st.session_state.r2_score = r2_score
#                 df = pd.read_csv("data/vietnam_house_prices_1000.csv")
#                 drop_cols = [col for col in ["House_ID", "Region_Factor"] if col in df.columns]
#                 df_ml = pd.get_dummies(df.drop(columns=drop_cols), columns=["Region"], drop_first=True)
                
#                 # Tách X, y
#                 X = df_ml.drop(columns=["Price"])
#                 y = df_ml["Price"]
#                 X_train, X_test, y_train, y_test = train_test_split(
#                     X,
#                     y,
#                     test_size=0.20,
#                     random_state=42
#                 )
#                 st.session_state.X_test = X_test
#                 st.session_state.y_test = y_test
#                 y_train_log = np.log(y_train)
#                 model = LinearRegression()
#                 model.fit(X_train, y_train_log)
#                 time.sleep(0.5)
#                 st.toast("Mô hình đã huấn luyện xong!", icon="✔️")
#                 st.session_state.model = model
#                 st.session_state.trained = True
#             else:
#                 st.toast("Mô hình đã được huấn luyện!", icon="⚠️")
#         if st.session_state.status == "error":
#             st.error("Chưa Huấn Luyện...", icon="🔴")
#         else:
#             st.success("Đã Huấn Luyện!", icon="✅")
#     if st.session_state.trained:
#         check = st.button(
#             label="Thẩm định",
#             type="primary",
#             icon="📝",
#             use_container_width=True
#             )
#         if check:
#             y_pred = st.session_state.model.predict(st.session_state.X_test)
#             col4, col5, col6, col7 = st.columns([1,1,1,1])
#             with col4:
#                 st.markdown(
#                     f"<h4 style='margin-bottom: -20px '>R²</h4>{st.session_state.r2_score(st.session_state.y_test, y_pred)}"
#                     ,
#                     unsafe_allow_html=True
#                 )
#             with col5:
#                 st.markdown(
#                     f"<h4 style='margin-bottom: -20px '>MAE</h4>{st.session_state.mean_absolute_error(st.session_state.y_test, y_pred)}"
#                     ,
#                     unsafe_allow_html=True
#                 )
#             with col6:
#                 st.markdown(
#                     f"<h4 style='margin-bottom: -20px '>MSE</h4>{st.session_state.mean_squared_error(st.session_state.y_test,y_pred)}"
#                     ,
#                     unsafe_allow_html=True
#                 )
#             with col7:
#                 st.markdown(
#                     f"<h4 style='margin-bottom: -20px '>RMSE</h4>{st.session_state.mean_squared_error(st.session_state.y_test,y_pred) ** 0.5}"
#                     ,
#                     unsafe_allow_html=True
#                 )
#     if st.session_state.trained:
#         st.markdown("""
#             <hr>
#             <h1 style="font-size:65px; text-align:center; margin-top: -60px; line-height: 110px">
#                 DỰ ĐOÁN
#             </h1>  
#             """,
#             unsafe_allow_html=True
#         )
#         house_id = st.number_input(
#             label="Chọn ID nhà của bạn",
#             min_value=0,
#             max_value=100000,
#             value=None,
#             step=1,
#             format="%d",
#             placeholder = "Hãy nhập ID của căn nhà mà bạn đã nhập thông tin trước đó để dự đoán",            
#             )
#         predict = st.button(
#                 label="Dự đoán",
#                 type="primary",
#                 icon="🔍",
#                 use_container_width=True
#             )
#         if predict:
#             df = pd.read_csv("data/test_data.csv")
#             test_region_map = {
#                     "Tỉnh nhỏ": 0,
#                     "Tỉnh lớn": 1,
#                     "Hà Nội": 2,
#                     "Thành phố Hồ Chí Minh": 3
#                 }
#             df["Regions"] = df["Region"].map(test_region_map)
#             selected_house = df[df["House_ID"] == house_id]
#             if selected_house.empty:
#                 if house_id == None:
#                     st.error("Hãy nhập ID căn nhà!", icon="⚠️")
#                 else:
#                     st.error("Không tìm thấy ID này!", icon="⚠️")
#             else:
#                 X_new = pd.DataFrame({
#                     "Regions": selected_house["Regions"],
#                     "Area": selected_house["Area"],
#                     "Frontage": selected_house["Frontage"],
#                     "Road_Width": selected_house["w-road"],
#                     "dist-center": selected_house["Distance"],
#                     "Floors": selected_house["Floors"],
#                     "Bedrooms": selected_house["Bedrooms"],
#                     "Bathrooms": selected_house["Bathrooms"],
#                     "yr-built": selected_house["built-yr"]
#                 })
#                 predicted_price = st.session_state.model.predict(X_new)[0]
#                 st.success(
#                     f"Giá dự đoán: {predicted_price:.2f} tỷ đồng"
#                 )
import os
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import time

if __name__ == "__main__":
    st.set_page_config(
        page_title="Price Prediction",
        layout="wide",
        page_icon="🔮",
        initial_sidebar_state="expanded"
    )  
    st.sidebar.markdown("""
        <style>
            div[data-testid="stButton"] > button {
                border-radius: 8px !important;
                border: none !important;
                transition: all 0.15s linear !important;
                height: 40px !important;
            }
            .stAlert > div div div div p {
                font-weight: bold;
                font-size: 25px;
                margin-top: -6px;
                margin-bottom: 8px;
                margin-left: 10px
            }
            /* Chỉ text bên trong button */
            div[data-testid="stButton"] > button p {
                font-size: 20px;
                font-weight: bold !important;
            }

            /* Hover */
            div[data-testid="stButton"] > button:hover {
                background-color: #1d4ed8 !important;
                transform: translateY(-2px) !important;
                box-shadow: 5px 5px 5px rgba(43, 108, 176, 0.4) !important;
            }

            /* Click */
            div[data-testid="stButton"] > button:active {
                transform: translateY(1.5px) !important;
            }
            .stColumn > div div div button {
                height: 56px !important;
            }
            .stColumn > div div div button div span p{
                font-size: 25px !important;
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
            <a href="http://localhost:9999" target="_self" class = "esu" style="text-decoration:none; color: white">
                Trang Chủ
            </a>
            <a href="http://localhost:9999/Market_Analysis" target="_self" class = "esu" style="text-decoration:none; color: white">
                Phân Tích Thị Trường
            </a>
            <a href="http://localhost:9999/Input_Record" target="_self" class = "esu" style="text-decoration:none; color: white">
                Thêm Dữ Liệu Dự Đoán
            </a>
            <a href="http://localhost:9999/Price_Prediction" target="_self" class = "esu" style="text-decoration:none; color: white; font-weight: bold; background-color: #2E363A">
                Phân Tích Dự Đoán
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if "trained" not in st.session_state:
        st.session_state.trained = False
        st.toast("Mô hình chưa được huấn luyện!", icon="✋")
        time.sleep(1.5)
        st.toast("Hãy bắt đầu huấn luyện...", icon="🙏")
        
    if "model" not in st.session_state: st.session_state.model = None
    if "y_test" not in st.session_state: st.session_state.y_test = None
    if "X_test" not in st.session_state: st.session_state.X_test = None
    if "    " not in st.session_state: st.session_state.X_column_blueprint = None
    if "status" not in st.session_state: st.session_state.status = "error"

    def change_state():
        st.session_state.status = "success"

    st.sidebar.image("images/HPAS-7.PNG")  
    st.markdown("""
        <h1 style="font-size:65px; text-align:center; margin-top: -60px; line-height: 110px">
            MÔ HÌNH DỰ ĐOÁN
        </h1>  
        """,
        unsafe_allow_html=True
    )          
    
    col1, col2 = st.columns([1,4])
    with col1:
        training = st.button(
            label="Huấn luyện",
            type="primary",
            icon="🏋",
            use_container_width=True
        )
        
    with col2:
        if training:
            if not st.session_state.trained:
                change_state()
                st.toast("Đang huấn luyện...", icon="🏋")
                
                # Đọc dữ liệu huấn luyện
                df = pd.read_csv("data/vietnam_house_prices_1000.csv")
                
                # Phân loại cột
                drop_cols = [
                    col
                    for col in ["House_ID", "Region_Factor"]
                    if col in df.columns
                ]
                df_ml = pd.get_dummies(
                        df.drop(columns=drop_cols),
                        columns=["Region"],
                        drop_first=True
                    )
                
                # Phân tách X, y
                X = df_ml.drop(columns=["Price"])
                y = df_ml["Price"]
                
                # Lưu cấu trúc cột gốc (Ví dụ: Area, Frontage, Region_HCMC, Region_Hanoi, Region_Small_Province, v.v.)
                st.session_state.X_column_blueprint = X.columns.tolist()
                
                # Chia tập dữ liệu 80/20
                X_train, X_test, y_train, y_test = train_test_split(
                        X,
                        y,
                        test_size=0.2,
                        random_state=42
                    )
                st.session_state.X_test = X_test
                st.session_state.y_test = y_test
                
                # Train với hàm Log của Price để tăng vọt R2
                y_train_log = np.log(y_train)
                model = LinearRegression()
                model.fit(X_train, y_train_log)
                
                time.sleep(0.5)
                st.toast("Mô hình đã được huấn luyện!", icon="✔️")
                
                st.session_state.model = model
                st.session_state.trained = True
            else:
                st.toast("Mô hình đã được huấn luyện!", icon="⚠️")
                
        if st.session_state.status == "error":
            st.error("Chưa Huấn Luyện...", icon="🔴")
        else:
            st.success("Đã Huấn Luyện!", icon="✅")

    # ==========================================
    # PHẦN THẨM ĐỊNH (EVALUATION)
    # ==========================================
    if st.session_state.trained:
        check = st.button(
            label="Thẩm định",
            type="primary",
            icon="📝",
            use_container_width=True
        )
        if check:
            # Tạo dự đoán và bỏ log
            y_pred_log = st.session_state.model.predict(st.session_state.X_test)
            y_pred = np.exp(y_pred_log)
                
            r2 = r2_score(st.session_state.y_test, y_pred)
            mae = mean_absolute_error(st.session_state.y_test, y_pred)
            mse = mean_squared_error(st.session_state.y_test, y_pred)
            rmse = np.sqrt(mse)
            
            col4, col5, col6, col7 = st.columns([1,1,1,1])
            with col4:
                st.markdown(f"<h4 style='margin-bottom: -20px '>R²</h4>{r2}", unsafe_allow_html=True)
            with col5:
                st.markdown(f"<h4 style='margin-bottom: -20px '>MAE</h4>{mae}", unsafe_allow_html=True)
            with col6:
                st.markdown(f"<h4 style='margin-bottom: -20px '>MSE</h4>{mse}", unsafe_allow_html=True)
            with col7:
                st.markdown(f"<h4 style='margin-bottom: -20px '>RMSE</h4>{rmse}", unsafe_allow_html=True)

    # ==========================================
    # PHẦN DỰ ĐOÁN THEO ID (PREDICTION)
    # ==========================================
    if st.session_state.trained:
        st.markdown("""
            <hr>
            <h1 style="font-size:65px; text-align:center; margin-top: -60px; line-height: 110px">
                DỰ ĐOÁN
            </h1>  
            """,
            unsafe_allow_html=True
        )
        id = st.number_input(
            label="Chọn ID nhà",
            min_value=0,
            max_value=999999,
            value=None,
            step=1,
            format="%d",
            placeholder="Hãy nhập ID căn nhà bạn đã tạo trước đó",            
        )
        predict = st.button(
            label="Dự đoán",
            type="primary",
            icon="🔍",
            use_container_width=True
        )
        if predict:
            if id is None:
                st.error("Hãy nhập ID căn nhà!", icon="⚠️")
            else:
                # Đọc file dữ liệu người dùng tạo
                df_test = pd.read_csv("data/test_data.csv")
                
                # Lấy dòng thông tin của căn nhà có ID theo người dùng nhập
                selected_house = df_test[df_test["House_ID"] == id]
                
                if selected_house.empty:
                    st.error(f"Không tìm thấy ID này!", icon="⚠️")
                else:
                    # Đổi giá trị dữ liệu cho khớp với file huấn luyện
                    region = selected_house["Region"].values[0]
                    regions = {
                        "Tỉnh nhỏ": "S-tỉnh",
                        "Tỉnh lớn": "B-tỉnh",
                        "Hà Nội": "Hanoi",
                        "Thành phố Hồ Chí Minh": "HCMC"
                    }
                    Region = regions.get(region, "B-tỉnh")
                    
                    # Đổi tên cột dữ liệu cho khớp với file huấn luyện
                    house = pd.DataFrame({
                        "Region": [Region],
                        "Area": [selected_house["Area"].values[0]],
                        "Frontage": [selected_house["Frontage"].values[0]],
                        "Road_Width": [selected_house["w-road"].values[0]],
                        "dist-center": [selected_house["Distance"].values[0]],
                        "Floors": [selected_house["Floors"].values[0]],
                        "Bedrooms": [selected_house["Bedrooms"].values[0]],
                        "Bathrooms": [selected_house["Bathrooms"].values[0]],
                        "yr-built": [selected_house["built-yr"].values[0]]
                    })
                    
                    # Giúp Machine Learning nhận diện cột giá trị "string"
                    houses = pd.get_dummies(house, columns=["Region"])
                    
                    # Bù đắp để đồng bộ cấu trúc cột theo file huấn luyện
                    for col in st.session_state.X_column_blueprint:
                        if col not in houses.columns:
                            houses[col] = 0
                            
                    # Sắp xếp đúng thứ tự các đặc trưng
                    X_new = houses[st.session_state.X_column_blueprint]
                    
                    # Dự đoán
                    predicted_price_log = st.session_state.model.predict(X_new)[0]
                    predicted_price = np.exp(predicted_price_log)
                    col18, col19 = st.columns([1,2])
                    with col18:
                        st.info(
                            f"ID: **{id}**"
                        )
                    with col19:
                        st.info(
                            f"Vị trí : **{region}**"
                        )
                    col10, col11, col12, col13, = st.columns([1,1,1,1])
                    with col10:                    
                        st.metric(label="Diện tích (m²)", value=selected_house["Area"].values[0])
                    with col11:                    
                        st.metric(label="Mặt tiền (m)", value=selected_house["Frontage"].values[0])
                    col14, col15, col16, coll7 = st.columns([1,1,1,1])
                    with col12:                    
                        st.metric(label="Độ rộng đường/hẻm (m)", value=selected_house["w-road"].values[0])
                    with col13:                    
                        st.metric(label="Khoảng cách đến trung tâm (km)", value=selected_house["Distance"].values[0])
                    with col14:                    
                        st.metric(label="Số tầng", value=selected_house["Floors"].values[0])
                    with col15:                    
                        st.metric(label="Số phòng ngủ", value=selected_house["Bedrooms"])
                    with col16:                    
                        st.metric(label="Số phòng tắm", value=selected_house["Bathrooms"].values[0])
                    with coll7:                    
                        st.metric(label="Năm xây", value=selected_house["built-yr"].values[0])
                    st.success(
                    f"$ Giá dự đoán: {predicted_price:.2f} tỷ đồng")
                    if predicted_price > 100:
                        st.warning(
                            "Giá trị dự đoán nằm trong vùng rất hiếm của dữ liệu huấn luyện. "
                            "Độ tin cậy của dự đoán có thể thấp hơn so với các trường hợp thông thường."
                            , icon="⚠️"
                            )