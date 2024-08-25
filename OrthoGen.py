import streamlit as st
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
# from streamlit_gsheets import GSheetsConnection
from utils import *



###### webpage settings ######
st_website_setting()

###### sidebar info ######
st_sidebar_info()

###### Main page title and user guide
st_title_info()

##### main function #####
st.subheader('Please select subspecialty')
def no_result():
    return ['XXXXXXXX', '65', 'male', 'diagnosis', 'note']
subspecialty_dic = {'trauma':trauma_section, 'anklefoot':anklefoot_section, 'sport_knee':sport_knee_section, 'tka':no_result, 'spine':no_result, 'ped':no_result, 'hand':no_result}
subspecialty = st.selectbox('The subspecialty: ', list(subspecialty_dic.keys()), index=0)
st.write('---')

st.subheader('Please select info of patient')
patient_data_list = subspecialty_dic[subspecialty]()
note = patient_data_list[4]

submit = st.button("Start Medical Record Generation")
show_result = False

with st.container():
    if submit:
        my_bar = st.progress(0)

        for percent_complete in range(0, 100, 10):
             time.sleep(0.02)
             my_bar.progress(percent_complete + 10)
        st.success('Thanks for waiting, please check your result!')
        st.write('---')
        show_result = True

###### Result block ######
if show_result:
    patient_database = pd.read_csv('./pages/patient_database.csv')
    if len(patient_database) > 10:
        patient_database.drop([10], inplace=True)
    new_patient_df = pd.DataFrame([patient_data_list], columns=patient_database.columns)
    merge_database = pd.concat([new_patient_df,patient_database], axis=0, ignore_index=True).reset_index(drop=True)
    merge_database.to_csv('./pages/patient_database.csv', index=False)
    with st.container():
        st.markdown("# The admission note: ")
        st.write(note)
        
