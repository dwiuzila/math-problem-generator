import base64
import streamlit as st
from datetime import datetime
from google.cloud import firestore

@st.cache(allow_output_mutation=True)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def head():
    st.markdown("<h1 style='text-align: center; margin-bottom: -35px;'>Math Problem Generator</h1>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center'>by Geoclid</p>", unsafe_allow_html=True)
    st.write("Feeling overwhelmed by your daily grind? Looking for something fun to do? Click the button for a random math problem \U0001F642.")

def body(sample):
    name = sample.iloc[0, 0]
    link = sample.iloc[0, 1]
    prob = sample.iloc[0, 2]
    st.info(f'### {name}')
    st.write(prob)
    st.caption(f'[source]({link})')
    st.markdown('---')

def report():
    # Authenticate to Firestore with the JSON account key.
    db = firestore.Client.from_service_account_json("firestore-key.json")

    # Create a reference to the Google post.
    doc_ref = db.collection("defect").document(str(datetime.now()))

    # And then uploading some data to that reference
    idx = st.session_state['sample'].index.item()
    doc_ref.set({"id": idx, "status": True})
    st.session_state['report_click'] = True

def footer():
    st.caption("Support us by either reporting this problem for bad $\LaTeX$ formatting or buying a coffee!")
    col1, col2 = st.columns([1,8])
    col1.button('Report', on_click=report)
    col2.markdown("""
        <a href="https://www.buymeacoffee.com/geoclid" target="_blank">
        <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" 
            width="136" 
            height="36" 
            alt="Buy Me A Coffee">
        </a>
    """, unsafe_allow_html=True)