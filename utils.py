import streamlit as st
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

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