import streamlit as st
import pandas as pd
from plotly import graph_objs as go
from datetime import date
import utils,streamlit_utils
import plotting_utils

st.set_page_config(page_title="Stockit")
TICKERS=["AAPL","GOOG","AMZN","WIT"]
selected_ticker=st.selectbox("Select Dataset for Prediction",TICKERS)


data_load_state=st.text("Load Data ...")
train_data,test_data=utils.get_data(selected_ticker)
# predicted_data=get_predicted_data(selected_ticker)
data_load_state.text("Loading data Done!!")

page = st.selectbox("Select the data you want to see" ,["Raw Data", "Prediction"])
if page == "Raw Data":
    st.title("Raw-data")
    st.write(train_data)
    st.plotly_chart(plotting_utils.plot_raw_data(train_data,"blue"))
elif page == "Prediction":
    # st,write(predicted_data)
    st.title("Predictions")
    st.write(test_data)
    st.plotly_chart(plotting_utils.plot_raw_data(test_data,"red"))




