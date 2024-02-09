import utils
import streamlit as st

def drawing_raw_data(selected_ticker):
    data_load_state=st.text("Load Data ...")

    train_data,test_data=utils.get_data(selected_ticker)

    data_load_state.text("Loading data Done!!")

    st.subheader("Raw Data")
    st.write(train_data)