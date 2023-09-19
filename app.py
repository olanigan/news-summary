import streamlit as st
import os
from summary import summarize

# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())

st.title("Summarize News article")

def init_sidebar():
    # API Token Sidebar
    with st.sidebar:
        st.title('API Token')
        if 'OPENAI_API_KEY' in st.secrets:
            st.success('OpenAI key provided!', icon='✅')
            openai_api = st.secrets['OPENAI_API_KEY']
        else:
            openai_api = st.text_input('Enter OpenAI API token:', type='password')
            
            if not validate_key(openai_api):
                st.warning('Please enter your OpenAI API token!', icon='⚠️')
            else:
                st.success('Proceed to entering your article!', icon='👉')
        os.environ['OPENAI_API_KEY'] = openai_api

def validate_key(api_token):
    return (api_token.startswith('sk-') and len(api_token) == 51)

def display_form():
    url_container = st.container()
    summary_container = st.container()

    with url_container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Article:", placeholder="Paste the article URL", key='input')
            st.form_submit_button(label='Summarize')

    with summary_container:
        st.text_area(label="Summary:",value=summarize(user_input))

init_sidebar()
display_form()