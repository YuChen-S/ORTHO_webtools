import streamlit as st
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
# from streamlit_gsheets import GSheetsConnection
from utils import *
from utils import note_dic



###### webpage settings ######
st_website_setting()

###### sidebar info ######
st_sidebar_info()

###### Main page title and user guide
st_title_info()

##### main function #####
st.subheader('Please select subspecialty')
subspecialty_list = ['trauma', 'anklefoot', 'tka', 'spine', 'ped', 'scope', 'hand']
subspecialty = st.selectbox('The subspecialty: ', subspecialty_list, index=0)
st.write('---')

if subspecialty == 'trauma':
    age, gender, gender_abb, side, location, event_date, event_type, diagnosis, fracture_type = trauma_section()
    note = f'''
        The {age}-year-old {gender} had underlying diseases of 

        . HTN (hypertension)

        . DM (diabetes mellitus) 

        The ADL (activities of daily living) was totally independent, without any catheter indwelling.

        This time, {gender_abb} suffered from {side} {location} pain after {event_type} on {event_date}. {side} {location} tenderness and limited ROM (range of movement) were noticed, with some abrasions over extremities. No initial LOC (loss of consciousness), head contusion, massive bleeding, open wound, distal paresthesia or paralysis been noticed. Due to the above condition, {gender_abb} was brought to our ED (emergency department) on {event_date}.

        Ar triage, the vital signs were generally stable. PE (physical examination) showed no open wound and distal neurovascular function was intact. The image study revealed {side} {diagnosis}. Orthopedics was consulted and surgical intervention was suggested. After SDM (Share Decision Making) and informing the risk and benefit of operation, the patient and family agreed. No recent anticoagulant nor antiplatelet was used.

        Under the impression of {side} {location} {diagnosis}, {fracture_type}, {gender_abb} was admitted on {event_date} for further evaluations and surgical managements.
        '''
elif subspecialty == 'anklefoot':
    age, gender, gender_abb, side, location, opd_date, admission_date, pe, deformity, hv_angle, im_angle, diagnosis, disease_type = anklefoot_section()
    note = f'''
        The {age}-year-old {gender} had underlying diseases of 

        . HTN (hypertension)

        . DM (diabetes mellitus) 

        The ADL (activities of daily living) was totally independent, without any catheter indwelling.

        This time, {gender_abb} had {side} big toe deformity for many years, but {gender_abb} did not pay much attention to it. However, {gender_abb} suffered from progressive bunion pain recently. The pain aggravated when wearing tight shoes or walking, and it relieved after rest. Assoicated symptoms included metatarsalgia, redness, and callosity formation. No fever, body weight loss, swelling, or local heat was noticed. {gender_abb} came to our outpatient department on {opd_date} for help.
        
        At outpatient department, physical examination showed {side} hallux valgus deformity with bunion tenderness, {pe}, and {deformity}. X ray showed {side} hallux valgus, with HV (hallux valgus) anlge {hv_angle}° and IM (intermetatarsal) angle {im_angle}°. After discussion with the family, they decided to receive the surgery with {side} big toe Mitchell osteotomy and neurolysis. 
        
        Under the diagnosis of {side} hallux valgus, {gender_abb} was admitted on {admission_date} for surgical intervention and further care.
        '''
else:
    note = 'empty'

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
    with st.container():
        st.markdown("# The admission note: ")
        st.write(note)
        
