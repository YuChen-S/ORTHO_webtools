import streamlit as st
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from utils import *
from utils import note_dic

###### webpage settings ######
st_website_setting()

###### sidebar info ######
st_sidebar_info()

###### Main page title and user guide
st_title_info()

##### main function #####
with st.container():
    st.subheader('Please select info of patient')
    # first row
    user_col_1_1, user_col_1_2 = st.columns(2)
    with user_col_1_1:
        age = st.number_input('The age: ', value=65, step=1)
    with user_col_1_2:
        gender_list = ['male', 'female']
        gender = st.selectbox('The gender: ', gender_list, index=0)
        gender_abb = 'he' if gender == 'male' else 'she'
    st.write('---')
    # second row
    user_col_2_1, user_col_2_2 = st.columns(2)
    with user_col_2_1:
        side_list = ['right', 'left']
        side = st.selectbox('The injuryed side: ', side_list, index=0)
    with user_col_2_2:
        location_list = ['shoulder', 'upper arm', 'elbow', 'forearm', 'wrist', 'hand', 'finger', 'hip', 'thigh', 'knee', 'ankle', 'foot', 'toe']
        location = st.selectbox('The injuryed location: ', location_list, index=7)
    st.write('---')
    # third row
    user_col_3_1, user_col_3_2 = st.columns(2)
    with user_col_3_1:
        event_date = st.date_input('The event date: ', value=datetime.date(2024, 8, 31), format='YYYY/MM/DD')
        event_date = str(event_date).replace('-', '/')
    with user_col_3_2:
        event_type_list = ['a fall', 'TA (traffic accident)']
        event_type = st.selectbox('The event type: ', event_type_list, index=0)
    st.write('---')
    # third row
    user_col_3_1, user_col_3_2 = st.columns(2)
    with user_col_3_1:
        diagnosis = st.text_input('The diagnosis:', "_____ fracture")
    with user_col_3_2:
        fracture_type = st.text_input('The type of fracture:', "____ type ____")
    st.write('---')



submit = st.button("Start Medical Record Generation")
show_result = False

with st.container():
    if submit:
        my_bar = st.progress(0)
        trauma_note = f'''
        The {age}-year-old {gender} had underlying diseases of 

        . HTN (hypertension)

        . DM (diabetes mellitus) 

        The ADL (activities of daily living) was totally independent, without any catheter indwelling.

        This time, {gender_abb} suffered from {side} {location} pain after {event_type} on {event_date}. {side} {location} tenderness and limited ROM (range of movement) were noticed, with some abrasions over extremities. No initial LOC (loss of consciousness), head contusion, massive bleeding, open wound, distal paresthesia or paralysis been noticed. Due to the above condition, {gender_abb} was brought to our ED (emergency department) on {event_date}.

        Ar triage, the vital signs were generally stable. PE (physical examination) showed no open wound and distal neurovascular function was intact. The image study revealed {side} {diagnosis}. Orthopedics was consulted and surgical intervention was suggested. After SDM (Share Decision Making) and informing the risk and benefit of operation, the patient and family agreed. No recent anticoagulant nor antiplatelet was used.

        Under the impression of {side} {location} {diagnosis}, {fracture_type}, {gender_abb} was admitted on {event_date} for further evaluations and surgical managements.
        '''
        for percent_complete in range(0, 100, 10):
             time.sleep(0.02)
             my_bar.progress(percent_complete + 10)
        print(trauma_note)
        st.success('Thanks for waiting, please check your result!')
        st.write('---')
        show_result = True

###### Result block ######
if show_result:
    with st.container():
        st.markdown("# The admission note: ")
        st.write(trauma_note)
        
