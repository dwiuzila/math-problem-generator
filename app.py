import pandas as pd
import streamlit as st
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
      background-image: url("data:image/png;base64,%s");
      background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_png_as_page_bg('background.png')

st.markdown("<h1 style='text-align: center; margin-bottom: -35px;'>Math Problem Generator</h1>", unsafe_allow_html=True)
st.caption("<p style='text-align: center'>by Geoclid</p>", unsafe_allow_html=True)
st.write("Feeling overwhelmed by your daily grind? Looking for something fun to do? Click the button for a random math problem \U0001F642.")

df = pd.read_csv('olympiad-problems.csv', index_col=0)

if st.button('Bring it on!'):
    choice = df.sample(1)
    name = choice.index.values[0]
    link = choice.iloc[0, 0]
    prob = choice.iloc[0, 1]
    st.info(f'### {name}')
    st.write(prob)
    st.caption(f'[source]({link})')
    st.markdown('---')
    st.markdown("""
    <a href="https://www.buymeacoffee.com/geoclid" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" 
        width="136" 
        height="38" 
        alt="Buy Me A Coffee">
    </a>
    """, unsafe_allow_html=True)