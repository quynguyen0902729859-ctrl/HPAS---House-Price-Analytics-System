import os
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px

if __name__ == "__main__":
    st.set_page_config(
        page_title="Market Analysis",
        layout="wide",
        page_icon="📊",
        initial_sidebar_state="expanded"
    )  
    st.sidebar.markdown("""
        <style>
            * {
                font-family: Calibri, sans-serif;
                line-height: 32px
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
            [data-testid="stAppDeployButton"] {
                display: none
            }
        </style>
        <div style="margin-top: -25px; margin-bottom: calc(100vh - 470px);">
            <a href="http://localhost:9999" target="_self" class = "esu" style="text-decoration:none; color: white">
                Trang Chủ
            </a>
            <a href="http://localhost:9999/Market_Analysis" target="_self" class = "esu" style="text-decoration:none; color: white; font-weight: bold; background-color: #2E363A">
                Phân Tích Thị Trường
            </a>
            <a href="http://localhost:9999/Input_Record" target="_self" class = "esu" style="text-decoration:none; color: white">
                Thêm Dữ Liệu Dự Đoán
            </a>
            <a href="http://localhost:9999/Price_Prediction" target="_self" class = "esu" style="text-decoration:none; color: white">
                Phân Tích Dự Đoán
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.image("images/HPAS-7.PNG")  
    st.markdown("""
        <style>
            .title {
                background-color: #242424;
                color: white !important;
                padding-left: 30px  !important;
                padding-bottom: 20px  !important;
                border-radius: 200px;
            }
            button[data-baseweb="tab"] {
                flex-grow: 1;
                justify-content: center;
            }
        </style>
        <h1 style="font-size:75px; text-align:center; margin-top: -75px; line-height: 110px">
            THỊ TRƯỜNG
        </h1>  
        <h2 class="title">
            1. Giá nhà đã trải qua nhiều biến động
        </h2>
        <h4 style="margin-top:30px; margin-bottom: 0px; text-align: justify">
            Do tác động của nhiều yếu tố môi trường mà làm cho thị trường giá nhà có nhiều biến động lớn đang kể.
        </h4>
        """,
        unsafe_allow_html=True
    )
    # df = pd.read_csv("data/price_trend.csv")
    # model = LinearRegression()
    # X = df.iloc[:, 0:1]
    # y = df.iloc[:, 1:2]
    # model.fit(X, y)
    # fig, ax = plt.subplots(figsize=(8,4))
    # ax.plot(
    #     df["Y-sell"],
    #     df["Price"],
    #     marker='o',
    #     markersize=3,
    #     label='Giá nhà trung bình (tỷ VND)'
    # )
    # ax.set_title("Xu hướng tăng giảm của trung bình giá nhà từ 2000 đến 2025")
    # ax.set_xlabel("Năm")
    # ax.set_ylabel("Giá nhà trung bình (tỷ VND)")
    # ax.legend()
    # X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    # y_line = model.intercept_ + model.coef_[0] * X_line
    # ax.plot(X_line, y_line, linestyle='--',color='red', linewidth=1 ,label='Xu hướng (tăng)')
    # ax.legend(loc='best')
    # st.pyplot(fig)
    df = pd.read_csv("data/price_trend.csv")
    model = LinearRegression()
    X = df.iloc[:, 0:1]
    y = df.iloc[:, 1:2]
    model.fit(X, y)
    X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_line = model.intercept_ + model.coef_[0] * X_line
    fig = px.line(
        df,
        x="Year",
        y="Index",
        markers=True,
    )
    fig.add_scatter(
        x=X_line.flatten(),
        y=y_line.flatten(),
        mode="lines",
        name="Xu hướng (tăng)",
        line=dict(
            color="red",
            dash="dash",
            width=2
        )
    )
    fig.update_layout(
        title={
            "text": "Xu hướng tăng giảm của giá nhà tính theo % từ 2000 đến 2025",
            "x": 0.2,
            "y": 0.93 
        },
        height=540
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.markdown("""
        <h4 style="margin-top:0px; text-align: justify">
            Dữ liệu được tổng hợp và chuẩn hóa từ các báo cáo thị trường bất động sản nhằm phản ánh xu hướng biến động giá nhà tại Việt Nam giai đoạn 2000–2025.        </h4>
        <h4 style="margin-top:0px; margin-bottom:30px; text-align: justify">
            Biểu đồ cho thấy xu hướng tăng dài hạn của giá nhà, chịu tác động bởi quá trình đô thị hóa, lạm phát và nhu cầu nhà ở gia tăng. Trong ngắn hạn, thị trường xuất hiện các giai đoạn điều chỉnh và chững lại, tiêu biểu như giai đoạn sau khủng hoảng tài chính toàn cầu 2008 và giai đoạn 2011–2013 khi thị trường bất động sản trầm lắng. Các yếu tố như đại dịch COVID-19 và chính sách siết tín dụng trong những năm gần đây cũng góp phần tạo ra biến động ngắn hạn. Tuy vậy, xu hướng tổng thể vẫn cho thấy mức tăng đáng kể của giá nhà trong suốt giai đoạn nghiên cứu.        </h4>
        <h2 class="title">
            2. Giá nhà được định hình từ rất nhiều yếu tố
        </h2>
        <h4 style="margin-top:0px; margin-bottom:0px; text-align: justify">
            Để quyết định giá một căn nhà, ta cần dựa vào rất nhiều yếu tố chính như:
        </h4>
        <h4 style="margin-top:-22.5px; margin-bottom:0px; margin-left:25px;text-align: justify">
            - Vị trí
        <br>
            - Diện tích
        <br>
            - Mặt tiền
        <br>
            - Chiều rộng đường/hẻm
        <br>
            - Số tầng
        <br>
            - Năm xây dựng
        <br>
            - Số phòng ngủ
        <br>
            - Số phòng tắm
        <br>
            - ...
        </h4>
        <h4 style="margin-top:-22.5px; margin-bottom:0px; text-align: justify">
            Do hạn chế về khả năng thu thập dữ liệu đầy đủ, nên ta chỉ có thể phân tích dựa trên bộ dữ liệu mô phỏng gồm 3000 mẫu dựa trên các đặc điểm phổ biến của thị trường nhà ở Việt Nam.
        </h4>
        """,
        unsafe_allow_html=True
    )
    df = pd.read_csv("data/vietnam_house_prices_1000.csv")
    st.dataframe(df, hide_index=True, column_config={"Region_Factor": None})
    st.markdown("""
        <hr>
        <h1 style="font-size:75px; text-align:center; margin-top: -50px; line-height: 110px">
            PHÂN TÍCH
        </h1>
        <h2 class="title">
            1. Vị trí là yếu tố quan trọng nhất đối với giá căn nhà
        </h2>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
                <h4 style="margin-top: -100px; margin-bottom: -1000px;"></h4>
            """,
            unsafe_allow_html=True
        )
        df = pd.read_csv("data/vietnam_house_prices_1000.csv")

        # # Mã hóa Region
        # region_map = {
        #     "S-tỉnh": 0,
        #     "B-tỉnh": 1,
        #     "Hanoi": 2,
        #     "HCMC": 3
        # }

        # df["Regions"] = df["Region"].map(region_map)

        # Các cột phân tích
        corr_columns = [
            "Region_Factor",
            "Area",
            "Frontage",
            "Road_Width",
            "dist-center",
            "Floors",
            "Bedrooms",
            "Bathrooms",
            "yr-built",
            "Price"
        ]

        corr_matrix = df[corr_columns].corr()

        # Heatmap Plotly
        fig = px.imshow(
            corr_matrix,
            text_auto=".3f",           # hiện số trên ô
            color_continuous_scale="RdBu_r",
            aspect="equal"
        )

        fig.update_layout(
           # margin=dict(t=20),
            title={
                "text": "Biểu đồ nhiệt của các thuộc tính",
                "x": 0.315,
                "y": 0.91    
            },
            height=550
        )

        fig.update_xaxes(tickangle=-30)

        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with col2:
        st.markdown("""
            <style>
                i {
                    text-decoration: underline;
                    text-decoration-color: transparent;
                    transition: text-decoration-color 0.2s ease-out;
                }

                i:hover {
                    text-decoration-color: currentColor;
                }
            </style>
            <h4 style="margin-top: 18px; margin-bottom: 0px; margin-right: -50px; text-align: justify">Dựa vào biểu đồ nhiệt, ta thấy:</h4>
            <h4 style="margin-top: -10px; margin-bottom: 0px; text-align: justify">- Chỉ số <i title="Vị trí / Vùng&#10[HCMC; Hà Nội; Tỉnh nhỏ; Tỉnh lớn]">Region_Factor</i> có độ tương quan lớn nhất với <i title="Giá của căn nhà&#10Đơn vị: Tỷ VNĐ">Price</i>, vậy nên vị trí của căn nhà rất quan trọng.</h4>
            <h4 style="margin-top: -10px; margin-bottom: 0px; text-align: justify">- Chỉ số <i title="Số phòng ngủ">Bedrooms</i> tương quan với <i title="Sô phòng tắm">Bathrooms</i> rất cao, chứng tỏ nhà có nhiều phòng ngủ thì cũng có nhiều phòng tắm.</h4>
            <h4 style="margin-top: -10px; margin-bottom: 0px; text-align: justify">- Chỉ số <i title="Year-Built&#10 Năm xây">yr-built</i> có tương quan thấp với tất cả chỉ số khác, nghĩa là năm xây gần như không liên quan tới bất kì điều gì.</h4>
            """,
            unsafe_allow_html=True
        )
    corr = df.corr(numeric_only=True)
    target_corr = corr["Price"].drop("Price")

    # Tạo DataFrame để Plotly dễ xử lý
    plot_df = pd.DataFrame({
        "Feature": target_corr.index,
        "Correlation": target_corr.values,
        "Color": np.where(target_corr.values < 0, "Tương quan âm", "Tương quan dương")
    })

    fig = px.bar(
        plot_df,
        x="Correlation",
        y="Feature",
        orientation="h",
        color="Color",
        color_discrete_map={
            "Tương quan âm": "#e60039",
            "Tương quan dương": "#7d8ea3"
        },    )
    fig.update_traces(
        hovertemplate=
        "<b>%{y}</b><br>"
        "Correlation: %{x:.8f}"
        "<extra></extra>"
    )
    fig.update_layout(
        title={
            "text": "Chi tiết tương quan âm/dương của từng thuộc tính đối với Price",
            "x": 0.24,
            "y": 0.93 
        },
        xaxis_title="Mức tương quan với Price",
        yaxis_title="",
        legend_title="",
        height=450
    )
    # vạch 0 giống axvline
    fig.add_vline(x=0, line_width=1, line_color="#e1e1e1")

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.markdown("""
        <h4 style="margin-top: 0px; margin-bottom: 50px;">
            Ta có thể thấy từ biểu đồ rằng <i title="Giá của căn nhà&#10Đơn vị: Tỷ VNĐ">Price</i> được tạo nên dựa trên nhiều yếu tố một cách khá bằng nhau, nhưng top 3 tương quan nhất là <i title="Vị trí / Vùng&#10[HCMC; Hà Nội; Tỉnh nhỏ; Tỉnh lớn]">Region_Factor</i>, <i title="Distance To Center&#10Khoảng cách đến trung tâm&#10Đơn vị: km">dist-center</i> (chỉ số tương quan âm duy nhất) và <i title="Diện tích&#10Đơn vị: m²">Area</i>
        </h4>
        <h2 class="title" style="margin-bottom: 50px">
            2. Biểu diễn phân phối của mọi thuộc tính
        </h2>
        """,
        unsafe_allow_html=True
    )
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(['Giá nhà','Vị trí','Diện tích','Mặt tiền','Chiều rộng đường/hẻm','Khoảng cách đến trung tâm','Số tầng','Số phòng ngủ','Số phòng tắm','Năm xây'])
    with tab1:
        fig = px.histogram(
            df,
            x="Price",
            nbins=44,
        )
        fig.update_traces(
            #marker_color="#4f81bd",
            marker_line_color="black",
            marker_line_width=1
        )
        fig.update_layout(
            xaxis_title="Giá tiền (tỷ VNĐ)",
            yaxis_title="Số nhà",
            title={
                "text": "Biểu đồ phân phối giá nhà",
                "x": 0.13,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True,
        )
    with tab2:
        fig = px.histogram(
            df,
            x="Region",
            nbins=4,
        )
        fig.update_traces(
            marker_color="tomato",
            marker_line_color="black",
            marker_line_width=1
        )
        fig.update_layout(
            xaxis_title="Vị trí",
            yaxis_title="Số nhà",
            title={
                "text": "Biểu đồ phân phối vị trí mỗi nhà",
                "x": 0.13,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab3:
        fig = px.histogram(
            df,
            x="Area",
            nbins=150,
        )
        fig.update_traces(
            marker_color="skyblue",
            marker_line_color="black",
            marker_line_width=0.5
        )
        fig.update_layout(
            xaxis_title="Diện tích (m²)",
            yaxis_title="Số nhà",
            title={
                "text": "Biểu đồ phân phối diện tích mỗi nhà",
                "x": 0.13,
                "y": 0.97
                },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab4:
        fig = px.histogram(
            df,
            x="Frontage",
            nbins=86,
        )
        fig.update_traces(
            marker_color="mediumseagreen",
            marker_line_color="black",
            marker_line_width=0.75
        )
        fig.update_layout(
            xaxis_title="Mặt tiền (m)",
            yaxis_title="Số nhà",
            title={
                "text": "Biểu đồ phân phối mặt tiền mỗi nhà",
                "x": 0.13,
                "y": 0.97
                },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab5:
        fig = px.histogram(
            df,
            x="Road_Width",
            nbins=50,
        )
        fig.update_traces(
            marker_color="grey",
            marker_line_color="black",
            marker_line_width=1
        )
        fig.update_layout(
            xaxis_title="Chiều rộng đường/hẻm (m)",
            yaxis_title="Số nhà",
            title={
                "text": "Biểu đồ phân phối chiều rộng đường/hẻm mỗi nhà",
                "x": 0.13,
                "y": 0.97
                },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab6:
        fig = px.histogram(
            df,
            x="dist-center",
            nbins=35,
        )
        fig.update_traces(
            marker_color="gold",
            marker_line_color="black",
            marker_line_width=1
        )
        fig.update_layout(
            xaxis_title="Khoảng cách đến trung tâm (km)",
            yaxis_title="Số nhà",
            title={
                "text": "Biểu đồ phân phối khoảng cách đến trung tâm mỗi nhà",
                "x": 0.13,
                "y": 0.97
                },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab7:
        fig = px.histogram(
            df,
            x="Floors",
            nbins=5,
        )
        fig.update_traces(
            marker_color="aliceblue",
            marker_line_color="black",
            marker_line_width=1
        )
        fig.update_layout(
            xaxis_title="Số tầng",
            yaxis_title="Số nhà",
            title={
                "text": "Biểu đồ phân phối số tầng mỗi nhà",
                "x": 0.13,
                "y": 0.97
                },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab8:
        fig = px.histogram(
            df,
            x="Bedrooms",
            nbins=7,
        )
        fig.update_traces(
            marker_color="tomato",
            marker_line_color="black",
            marker_line_width=1
        )
        fig.update_layout(
            xaxis_title="Số phòng ngủ",
            yaxis_title="Số nhà",
            title={
                "text": "Biểu đồ phân phối số phòng ngủ mỗi nhà",
                "x": 0.13,
                "y": 0.97
                },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab9:
        fig = px.histogram(
            df,
            x="Bathrooms",
            nbins=5,
        )
        fig.update_traces(
            marker_color="aquamarine",
            marker_line_color="black",
            marker_line_width=1
        )
        fig.update_layout(
            xaxis_title="Số phòng tắm",
            yaxis_title="Số nhà",
            title={
                "text": "Biểu đồ phân phối số phòng tắm mỗi nhà",
                "x": 0.13,
                "y": 0.97
                },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab10:
        fig = px.histogram(
            df,
            x="yr-built",
            nbins=46,
        )
        fig.update_traces(
            marker_line_color="black",
            marker_line_width=1
        )
        fig.update_layout(
            xaxis_title="Năm xây",
            yaxis_title="Số nhà",
            title={
                "text": "Biểu đồ phân phối năm xây mỗi nhà",
                "x": 0.13,
                "y": 0.97
                },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    st.markdown("""
        <h2 class="title" style="margin-bottom: 50px">
            3. Biểu diễn mối quan hệ giữa các yếu tố và giá nhà
        </h2>
        """,
        unsafe_allow_html=True
        )
    tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19 = st.tabs(['Vị trí','Diện tích','Mặt tiền','Chiều rộng đường/hẻm','Khoảng cách đến trung tâm','Số tầng','Số phòng ngủ','Số phòng tắm','Năm xây'])
    with tab11:
        df_mean = df.groupby("Region")["Price"].mean().reset_index()
        fig = px.bar(
            df_mean,
            x="Region",
            y="Price",
        )
        fig.update_layout(
            xaxis_title="Vị trí",
            yaxis_title="Giá nhà trung bình (tỷ VNĐ)",
            title={
                "text": "Biểu đồ cột mối quan hệ giữa vị trí và giá nhà",
                "x": 0.055,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab12:
        fig = px.scatter(
            df,
            x="Area",
            y="Price",
            hover_data=[
                "Region",
                "Frontage",
                "Road_Width",
                "dist-center",
                "Floors",
                "Bedrooms",
                "Bathrooms",
                "yr-built"
            ],
            labels={
                "Area": "Diện tích (m²)",
                "Price": "Giá nhà (tỷ VNĐ)"
            }
        )
        fig.update_layout(
            title={
                "text": "Biểu đồ phân tán quan hệ giữa diện tích và giá nhà",
                "x": 0.055,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab13:
        fig = px.scatter(
            df,
            x="Frontage",
            y="Price",
            hover_data=[
                "Region",
                "Area",
                "Road_Width",
                "dist-center",
                "Floors",
                "Bedrooms",
                "Bathrooms",
                "yr-built"
            ],
            labels={
                "Frontage": "Mặt tiền (m)",
                "Price": "Giá nhà (tỷ VNĐ)"
            }
        )
        fig.update_layout(
            title={
                "text": "Biểu đồ phân tán mối quan hệ giữa mặt tiền và giá nhà",
                "x": 0.055,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab14:
        fig = px.scatter(
            df,
            x="Road_Width",
            y="Price",
            hover_data=[
                "Region",
                "Area",
                "Frontage",
                "dist-center",
                "Floors",
                "Bedrooms",
                "Bathrooms",
                "yr-built"
            ],
            labels={
                "Road_Width": "Chiều rộng đường/hẻm (m)",
                "Price": "Giá nhà (tỷ VNĐ)"
            }
        )
        fig.update_layout(
            title={
                "text": "Biểu đồ phân tán mối quan hệ giữa chiều rộng đường/hẻm và giá nhà",
                "x": 0.055,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab15:
        fig = px.scatter(
            df,
            x="dist-center",
            y="Price",
            hover_data=[
                "Region",
                "Area",
                "Frontage",
                "Road_Width",
                "Floors",
                "Bedrooms",
                "Bathrooms",
                "yr-built"
            ],
            labels={
                "dist-center": "Khoảng cách đến trung tâm (km)",
                "Price": "Giá nhà (tỷ VNĐ)"
            }
        )
        fig.update_layout(
            title={
                "text": "Biểu đồ phân tán mối quan hệ giữa chiều rộng đường/hẻm và giá nhà",
                "x": 0.055,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab16:
        df_mean = df.groupby("Floors")["Price"].mean().reset_index()
        fig = px.bar(
            df_mean,
            x="Floors",
            y="Price",
        )
        fig.update_layout(
            xaxis_title="Số tầng",
            yaxis_title="Giá nhà trung bình (tỷ VNĐ)",
            title={
                "text": "Biểu đồ cột mối quan hệ giữa số tầng và giá nhà",
                "x": 0.055,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab17:
        df_mean = df.groupby("Bedrooms")["Price"].mean().reset_index()
        fig = px.bar(
            df_mean,
            x="Bedrooms",
            y="Price",
        )
        fig.update_layout(
            xaxis_title="Số phòng ngủ",
            yaxis_title="Giá nhà trung bình (tỷ VNĐ)",
            title={
                "text": "Biểu đồ cột mối quan hệ giữa số phòng ngủ và giá nhà",
                "x": 0.055,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab18:
        df_mean = df.groupby("Bathrooms")["Price"].mean().reset_index()
        fig = px.bar(
            df_mean,
            x="Bathrooms",
            y="Price",
        )
        fig.update_layout(
            xaxis_title="Số phòng tắm",
            yaxis_title="Giá nhà trung bình (tỷ VNĐ)",
            title={
                "text": "Biểu đồ cột mối quan hệ giữa số phòng tắm và giá nhà",
                "x": 0.055,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    with tab19:
        fig = px.scatter(
            df,
            x="yr-built",
            y="Price",
            hover_data=[
                "Region",
                "Area",
                "Frontage",
                "Road_Width",
                "dist-center",
                "Floors",
                "Bedrooms",
                "Bathrooms",
            ],
            labels={
                "yr-built": "Năm xây",
                "Price": "Giá nhà (tỷ VNĐ)"
            }
        )
        fig.update_layout(
            title={
                "text": "Biểu đồ phân tán quan hệ giữa năm xây và giá nhà",
                "x": 0.055,
                "y": 0.97
            },
            height=500,
            margin=dict(t=23.5)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    st.markdown("""
            <h2 class="title" style="margin-bottom: 20px">
                4. Trung bình một căn nhà
            </h2>
            """,
            unsafe_allow_html=True
            )
    col3, col4 = st.columns([1,1])
    with col3:
        st.image("images/house_image.PNG")  
    with col4:
        st.markdown("""
            <h4 style="margin-top: 40px">
                Vậy theo tập dữ liệu, một căn nhà điển hình hiện nay sẽ có:
                <br>
                - Giá: 2,3 tỷ VNĐ
                <br>
                - Vị trí: Tỉnh lớn
                <br>
                - Diện tích: 99,23 m²
                <br>
                - Mặt tiền: 5,3 m
                <br>
                - Chiều rộng đường/hẻm: 4,1 m
                <br>
                - Khoảng cách đến trung tâm: 18,3 km
                <br>
                - Số tầng: 3 tầng
                <br>
                - Số phòng ngủ: 2 phòng
                <br>
                - Số phòng tắm: 2 phòng
                <br>
                - Năm xây: 2003
            </h4>
            """,
            unsafe_allow_html=True
            )
    st.markdown("""
        <hr>
        <h1 style="font-size:75px; text-align:center; margin-top: 0px; line-height: 110px">
            KẾT LUẬN
        </h1>  
            <h4 style="margin-top: 0px; margin-bottom: 0px; text-align: justify">Qua quá trình phân tích, có thể thấy giá nhà tại Việt Nam chịu tác động đồng thời bởi nhiều yếu tố khác nhau và không phụ thuộc hoàn toàn vào một đặc điểm riêng lẻ. Dữ liệu thị trường cho thấy giá nhà có xu hướng tăng trong dài hạn từ năm 2000 đến năm 2025 mặc dù trải qua nhiều giai đoạn biến động do các yếu tố kinh tế và xã hội.</h4>
            <h4 style="margin-top: -10px; margin-bottom: 0px; text-align: justify">Kết quả phân tích tương quan cho thấy <i title="Vị trí / Vùng&#10[HCMC; Hà Nội; Tỉnh nhỏ; Tỉnh lớn]">Region_Factor</i> là yếu tố có ảnh hưởng lớn nhất đến giá nhà, tiếp theo là <i title="Distance To Center&#10Khoảng cách đến trung tâm&#10Đơn vị: km">dist-center</i> và <i title="Diện tích&#10Đơn vị: m²">Area</i>. Các yếu tố như <i title="Số phòng ngủ">Bedrooms</i>, <i title="Số phòng tắm">Bathrooms</i>, <i title="Số tầng/lầu">Floors</i>, <i title="Mặt tiền&#10Đơn vị: m">Frontage</i> và <i title="Chiều rộng đường/hẻm&#10Đơn vị: m">Road_Width</i> cũng góp phần hình thành giá trị của bất động sản nhưng với mức độ thấp hơn. Trong khi đó,  <i title="Year-Built&#10 Năm xây">yr-built</i> gần như không thể hiện mối liên hệ đáng kể với giá nhà trong bộ dữ liệu hiện tại.</h4>
            <h4 style="margin-top: -10px; margin-bottom: 0px; text-align: justify">Từ những kết quả trên, có thể kết luận rằng việc định giá nhà cần xem xét đồng thời nhiều đặc điểm của bất động sản, đặc biệt là vị trí và khả năng kết nối với khu vực trung tâm. Những phân tích này cũng là cơ sở quan trọng cho việc xây dựng mô hình dự đoán giá nhà ở các bước tiếp theo.</h4>
        """,
        unsafe_allow_html=True
    )