import streamlit as st
import pandas as pd
from plotly import graph_objs as go
from datetime import date
import utils,streamlit_utils
import plotting_utils
import json 



st.set_page_config(page_title="Stockit")
TICKERS=["AAPL", "MSFT", "GOOG", "AMZN", "META", "TSLA", "NVDA", "INTC", "IBM"]
selected_ticker=st.selectbox("Select Dataset for Prediction",TICKERS)


data_load_state=st.text("Load Data ...")
test_dates,train_data,test_data,predictions=utils.get_data(selected_ticker)
# predicted_data=get_predicted_data(selected_ticker)
data_load_state.text("Loading data Done!!")

page = st.selectbox("Select the data you want to see" ,["Raw Data", "Prediction"])
if page == "Raw Data":
    st.title("Raw-data")
    st.write(train_data)
    graph_type=st.selectbox("Select the data you want to see" ,["Line Chart","Candle Sticks"])
    if graph_type=="Line Chart":
        st.plotly_chart(plotting_utils.plot_raw_data(train_data["Date"],{"train_data":train_data["Close"]},"blue"))
    elif graph_type=="Candle Sticks":
        st.plotly_chart(plotting_utils.plot_candle(train_data["Date"],train_data))
        
elif page == "Prediction":
    # st,write(predicted_data)
    st.title("Predictions")
    d={"test_data":test_data,"Predictions":predictions}
    st.write()
    st.plotly_chart(plotting_utils.plot_raw_data(test_dates,d,["red","blue"]))




