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

def basic_profile():
    user_col_1_1, user_col_1_2, user_col_1_3 = st.columns(3)
    with user_col_1_1:
        id = st.text_input('Chart number:', value='xxxxxxxx', key='id')
    with user_col_1_2:
        age = st.number_input('Age: ', value=65, step=1)
    with user_col_1_3:
        gender_list = ['male', 'female']
        gender = st.selectbox('Gender: ', gender_list, index=0)
        gender_abb = 'he' if gender == 'male' else 'she'
    underlying_list = ['Nil', 'HTN', 'T2DM', 'Dyskipidemia', 'CKD', 'ESRD', 'CAD', 'Stroke', 'CVA', 'PAOD']
    underlying = st.multiselect('Underlying diseases: ', underlying_list, underlying_list[0:1])
    if underlying == ['Nil']:
        underlying_text = 'no underlying disease.'
    else:
        text = '\n\n. '.join(underlying)
        underlying_text = f'underlying diseases of \n\n. {text}'
    # underlying_text = 'no underlying disease.' if underlying == ['Nil'] else f'underlying diseases of \n\n. {'\n\n. '.join(underlying)}'
    st.write('---')
    return id, age, gender, gender_abb, underlying_text

def trauma_section():
    with st.container():
        # first row
        id, age, gender, gender_abb, underlying_text = basic_profile()
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
        # fourth row
        user_col_3_1, user_col_3_2 = st.columns(2)
        with user_col_3_1:
            diagnosis = st.text_input('The diagnosis:', "_____ fracture", key='diagnosis')
        with user_col_3_2:
            fracture_type = st.text_input('The type of fracture:', "____ type ____", key='type')
        st.write('---')
    note = f'''The {age}-year-old {gender} had {underlying_text}\n
The ADL (activities of daily living) was totally independent, without any catheter indwelling.\n
This time, {gender_abb} suffered from {side} {location} pain after {event_type} on {event_date}. {side} {location} tenderness and limited ROM (range of movement) were noticed, \
with some abrasions over extremities. No initial LOC (loss of consciousness), head contusion, massive bleeding, open wound, distal paresthesia or paralysis been noticed. \
Due to the above condition, {gender_abb} was brought to our ED (emergency department) on {event_date}.\n
At triage, the vital signs were generally stable. PE (physical examination) showed no open wound and distal neurovascular function was intact. \
The image study revealed {side} {diagnosis}. Orthopedics was consulted and surgical intervention was suggested. \
After SDM (Share Decision Making) and informing the risk and benefit of operation, the patient and family agreed. No recent anticoagulant nor antiplatelet was used.\n
Under the impression of {side} {location} {diagnosis}, {fracture_type}, {gender_abb} was admitted on {event_date} for further evaluations and surgical managements.'''
    patient_data_list = [id, age, gender, diagnosis, note]
    return patient_data_list

def anklefoot_section():
    with st.container():
        # first row
        id, age, gender, gender_abb, underlying_text = basic_profile()
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
            pe_list = ['bunion pain', 'plantar callosity', 'metatarsalgia', 'claw toe deformity']
            hv_pe = st.multiselect('PE findings: ', pe_list, pe_list[0:2])
            hv_pe_text = ', '.join(hv_pe)
        with user_col_4_2:
            passive_reduction = st.selectbox('Passive reduction of metatarsophalangeal joint: ', ['+', '-'], index=1)
            reduction_text = 'reducible' if passive_reduction == '+' else 'irreducible'
        st.write('---')
        # fifth row
        user_col_5_1, user_col_5_2 = st.columns(2)
        with user_col_5_1:
            dorsiflexion = st.number_input('Big toe dorsiflexion angle: ', value=40, step=1)
        with user_col_5_2:
            plantarflexion = st.number_input('Big toe plantarflexion angle: ', value=40, step=1)
        st.write('---')
        # sixth row
        user_col_6_1, user_col_6_2 = st.columns(2)
        with user_col_6_1:
            hv_angle = st.number_input('The Hallux valgus angle: ', value=40.0, step=0.1)
        with user_col_6_2:
            im_angle = st.number_input('The Intermetatarsal angle: ', value=15.0, step=0.1)
        st.write('---')
        # seventh row
        user_col_7_1, user_col_7_2 = st.columns(2)
        with user_col_7_1:
            diagnosis = st.text_input('The diagnosis:', "hallux valgus")
        with user_col_7_2:
            hv_op_list = ['Chevron', 'Mitchell']
            operation = st.selectbox('The operation :', hv_op_list, index=1)
        st.write('---')
    note = f'''The {age}-year-old {gender} had {underlying_text}\n
The ADL (activities of daily living) was totally independent, without any catheter indwelling.\n
This time, {gender_abb} had {side} big toe deformity for many years. The associated symptoms included mild redness and pain over {side} first MTP (metatarsophalangeal) joints. \
The pain was aggrevated by walking, wearing tight shoes and would be relieved by rest. The pain progressed rapidly recently. \
The patient denied fever, chillness, abnormal body weight loss, swelling, local heat or recent trauma history. \
Due to the above condition, the patient came to our outpatient department on {opd_date} for help.\n
At outpatient department, physical examination showed {hv_pe_text}, and mild swelling. The {side} first MTP (metatarsophalangeal) joint was {reduction_text} by passivee reduction.\
The angle of big teo dorsiflexion and plantarflexion were {dorsiflexion}° and {plantarflexion}°, respectively. \
The X-ray study revealed hallux valgus with HV (hallux valgus) anlge {hv_angle}° and IM (intermetatarsal) angle {im_angle}°. \
After discussion with the family, they decided to receive the surgery with {side} big toe {operation} osteotomy and neurolysis. \n
Under the impression of {side} {diagnosis}, {gender_abb} was admitted on {admission_date} for surgical intervention with {operation} osteotomy and further care.\n\n\n
For PE: \n
{side} foot:\n
  - bunion tenderss ({'+' if 'bunion pain' in hv_pe  else '-'}) \n
  - plantar callosity ({'+' if 'plantar callosity' in hv_pe  else '-'}) \n
  - metatarsalgia ({'+' if 'metatarsalgia' in hv_pe  else '-'}) \n
  - claw toe deformity ({'+' if 'claw toe deformity' in hv_pe  else '-'}) \n
  - passive reduction of metatarsophalangeal joint: {reduction_text}\n
  - big toe dorsiflexion/plantarflexion: {dorsiflexion} degrees / {plantarflexion} degrees \n
  - Hallux valgus angle: {hv_angle} degrees\n
  - Intermetatarsal angle: {im_angle} degrees
'''
    patient_data_list = [id, age, gender, diagnosis, note]
    return patient_data_list

def sport_knee_section():
    with st.container():
        # first row
        id, age, gender, gender_abb, underlying_text = basic_profile()
        # second row
        user_col_2_1, user_col_2_2 = st.columns(2)
        with user_col_2_1:
            side_list = ['right', 'left']
            side = st.selectbox('The injuryed side: ', side_list, index=0)
        with user_col_2_2:
            location_list = ['knee']
            location = st.selectbox('The injuryed location: ', location_list, index=0)
        st.write('---')
        # row
        user_col_injury, user_col_sport = st.columns(2)
        with user_col_injury:
            injury_type = st.selectbox('The injuryed side: ', ['sprain', 'contusion', 'fall'], index=0)
        with user_col_sport:
            sport_type_list = ['basketball', 'badminton', 'baseball', 'running']
            sport_type = st.selectbox('The event type: ', sport_type_list, index=0)
            if sport_type == 'running':
                sport_text = 'running'
            else:
                sport_text = f'playing {sport_type}'
        # third row
        user_col_3_1, user_col_3_2, user_col_3_3 = st.columns(3)
        with user_col_3_1:
            accident_date = st.date_input('The injuryed date: ', value=datetime.date(2024, 8, 31), format='YYYY/MM/DD')
            accident_date = str(accident_date).replace('-', '/')
        with user_col_3_2:
            opd_date = st.date_input('The OPD date: ', value=datetime.date(2024, 8, 31), format='YYYY/MM/DD')
            opd_date = str(opd_date).replace('-', '/')
        with user_col_3_3:
            admission_date = st.date_input('The admission date: ', value=datetime.date(2024, 8, 31), format='YYYY/MM/DD')
            admission_date = str(admission_date).replace('-', '/')
        st.write('---')
        # fourth row
        user_col_4_1, user_col_4_2, user_col_4_3 = st.columns(3)
        with user_col_4_1:
            knee_pe_list = ['Lachman Test', 'Anterior drawer test', 'Pivot shift test', 'McMurray Test', ' Posterior sag', 'Posterior drawer test']
            knee_pe = st.multiselect('PE findings: ', knee_pe_list, knee_pe_list[0:2])
            knee_pe_text = ' (+), '.join(knee_pe)
        with user_col_4_2:
            tendon_list = ['ACL partial', 'ACL complete', 'PCL partial', 'PCL complete']
            injury_tendon = st.multiselect('The injuryed tendon: ', tendon_list, tendon_list[0:1])
            tendon_text = ', '.join(injury_tendon).replace('ACL', 'ACL (anterior cruciate ligament)')
            tendon_text = tendon_text.replace('PCL', 'PCL (posterior cruciate ligament)')
        with user_col_4_3:
            injury_meniscus = st.selectbox('The injuryed meniscus: ', ['medial', 'lateral'], index=0)
        st.write('---')
        # fifth row
        user_col_5_1, user_col_5_2 = st.columns(2)
        with user_col_5_1:
            arom_start = st.number_input('Active ROM start: ', value=10, step=1)
        with user_col_5_2:
            arom_end = st.number_input('Active ROM end: ', value=130, step=1)
        st.write('---')
        # sixth row
        # seventh row
        user_col_7_1, user_col_7_2 = st.columns(2)
        with user_col_7_1:
            diagnosis = st.text_input('The diagnosis:', "ACL (anterior cruciate ligament) tear")
        st.write('---')
    note = f'''The {age}-year-old {gender} had {underlying_text}\n
The ADL (activities of daily living) was totally independent, without any catheter indwelling.\n
This time, {gender_abb} suffered from {side} {location} {injury_type} when {sport_text} on {accident_date}. \
Afterward, {gender_abb} had sudden-onset severe pain, swelling and weakness over {side} {location} when moving the joint or doing exercise.\
The patient denied fever, chillness, abnormal body weight loss, local heat, open wound nor other trauma history. Due to the above condition, {gender_abb} first visited LMD (Local medical doctor) \
then was transferred to our OPD (Outpatient Department) on {opd_date} due to highly suspected soft tissue injury.\n
At outpatient department, the physical examination showed ROM (range of movement) of {side} {location} {arom_start}~{arom_end} degress, {knee_pe_text} (+), \
and mild tenderness over {side} gastrocnemius. The MRI (magnetic resonance image) showed {side} {location} {tendon_text} tear and suspected {injury_meniscus} meniscal tear. \
Currently, {gender_abb} could not squat down deeply, but there was no knee pain in daily activity or climbing stairs. No locking sensation was noticed. \
After discussion with the patient and family, they decided to receive the surgical treatment.\n
Under the impression of {side} {location} {diagnosis} and suspected {injury_meniscus} meniscal tear, {gender_abb} was admitted on {admission_date} for \
intervention with arthroscopic surgery and further care.\n\n\n
For PE: \n
{side} knee:\n
 inspection: mild flexion contracture, no swelling or redness\n
 palpation: no obvious tenderness points\n
 active ROM (range of movement): {arom_start}~{arom_end}°\n
 special tests:\n
  Lachman Test ({'+' if 'Lachman Test' in knee_pe else '-'})\n
  Anterior drawer test ({'+' if 'Anterior drawer test' in knee_pe else '-'})\n
  Pivot shift test ({'+' if 'Pivot shift test' in knee_pe else '-'})\n
  McMurray Test ({'+' if 'McMurray Test' in knee_pe else '-'})\n
  Posterior sag ({'+' if 'Posterior sag' in knee_pe else '-'})\n
  Posterior drawer test ({'+' if 'Posterior drawer test' in knee_pe else '-'})\n
  Valgus stress (-, at both 0 and 30°)\n
  Varus  stress (-, at both 0 and 30°)
'''
    patient_data_list = [id, age, gender, diagnosis, note]
    return patient_data_list