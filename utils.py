import streamlit as st
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
# from streamlit_gsheets import GSheetsConnection


def st_website_setting():
    st.set_page_config(
        page_title="KMUH OrthoGen",
        page_icon="chart_with_upwards_trend",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def st_sidebar_info():
    with st.sidebar:
        st.title("About")
        st.info(
            """
            A webtool for daily routine of KMUH Orthopedic Residents。\n
            Medical Note Generation, Self-paid device consetns, Guide for daily routine, etc\n
            """
        )
        st.title("Contact")
        st.info(
            """
            Developer: 
            [Yu Chen Shen](), 
            [曾偉誠](), \n
            Director: []()
            """
        )
        st.success("Contact yuchen2690720@gmail.com if any problem was found, thanks")
        st.write('''---''')

def st_title_info():
    st.title('KMUH OrthoGen 2024')
    st.subheader(
    '''
    This application will help you to accelerate the progress of daily routine of KMUH orthopedic resident doctors.
    ''', anchor=None)
    st.markdown(''' **3 main features:** 
    1. Automated medical note generation.
    2. Organized depository for commonly used consents for self-paid medical device.
    3. Guidelines for the daily routine of KMUH orthopedic resident doctors.
    ''')
    st.write('**Please check the user guide if any question. Thanks for using our product!**')
    st.write('---')

def trauma_section():
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

    return age, gender, gender_abb, side, location, event_date, event_type, diagnosis, fracture_type

def anklefoot_section():
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
            location_list = ['foot', 'big toe']
            location = st.selectbox('The injuryed location: ', location_list, index=1)
        st.write('---')
        # third row
        user_col_3_1, user_col_3_2 = st.columns(2)
        with user_col_3_1:
            opd_date = st.date_input('The OPD date: ', value=datetime.date(2024, 8, 31), format='YYYY/MM/DD')
            opd_date = str(opd_date).replace('-', '/')
        with user_col_3_2:
            admission_date = st.date_input('The admission date: ', value=datetime.date(2024, 8, 31), format='YYYY/MM/DD')
            admission_date = str(admission_date).replace('-', '/')
        st.write('---')
        # fourth row
        user_col_4_1, user_col_4_2 = st.columns(2)
        with user_col_4_1:
            pe_list = ['plantar callosity', 'metatarsalgia']
            pe = st.selectbox('The PE finding: ', pe_list, index=0)
        with user_col_4_2:
            deformity_list = ['claw toe deformity']
            deformity = st.selectbox('The deformity: ', deformity_list, index=0)
        st.write('---')
        # fifth row
        user_col_5_1, user_col_5_2 = st.columns(2)
        with user_col_5_1:
            hv_angle = st.number_input('The Hallux valgus angle: ', value=40, step=1)
        with user_col_5_2:
            im_angle = st.number_input('The Intermetatarsal angle: ', value=15, step=1)
        st.write('---')
        # sixth row
        user_col_6_1, user_col_6_2 = st.columns(2)
        with user_col_6_1:
            diagnosis = st.text_input('The diagnosis:', "hallux valgus")
        with user_col_6_2:
            disease_type = st.text_input('The type:', "____ type ____")
        st.write('---')

    return age, gender, gender_abb, side, location, opd_date, admission_date, pe, deformity, hv_angle, im_angle, diagnosis, disease_type

note_dic = {
    'trauma':
    '''trauma''', 
    'ankle':
    '''ankle''',
    'knee':
    '''knee''', 
    'sport':
    '''sport''',
}