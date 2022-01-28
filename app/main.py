"""Main program for the streamlit app"""

import streamlit as st
from utils import set_bg, head, body, footer, read_data

st.set_page_config(page_title='Math Problem Generator', page_icon='assets/icon.png')

ss = st.session_state
set_bg('assets/background.png')
head()

if 'prob_click' not in ss:
    ss['prob_click'] = False

if st.button('Bring it on!'):
    ss['prob_click'] = True
    ss['report_click'] = False
    df = read_data('data/olympiad-problems.csv')
    choice = df.sample(1)
    ss['sample'] = choice
    body(choice)

if ss['prob_click'] and ss['report_click']:
    body(ss['sample'])
    footer()
elif ss['prob_click']:
    footer()