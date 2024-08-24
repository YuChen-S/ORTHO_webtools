import streamlit as st
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime


with st.container():
    st.subheader('Please enter the cahrt number')
    input_id = st.text_input('The chart number to search:', "xxxxxxxx")
    st.write('---')
    submit = st.button("Start Medical Record Generation")
    with st.container():
        if submit:
            patient_database = pd.read_csv('./pages/patient_database.csv')
            patient_data = patient_database.loc[patient_database["patient_id"] == input_id]
            if len(patient_data.values) == 0:
                st.write('No matched chart number')
            else:
                st.write(patient_data.values[0][4])
# C:\KMUH\projects\ORTHO_webtools\pages\patient_database.csv