import pandas as pd
import streamlit as st
from app.utils import set_bg, head, body, footer

ss = st.session_state
set_bg('background.png')
head()

if 'prob_click' not in ss:
    ss['prob_click'] = False

if st.button('Bring it on!'):
    ss['prob_click'] = True
    ss['report_click'] = False
    df = pd.read_csv('olympiad-problems.csv')
    choice = df.sample(1)
    ss['sample'] = choice
    body(choice)

if ss['prob_click'] and ss['report_click']:
    body(ss['sample'])
    footer()
elif ss['prob_click']:
    footer()