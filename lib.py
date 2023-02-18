import streamlit as st
import time

def render_questions():
    with st.spinner('Processing...'):
        time.sleep(3)

        summary_text = '_Prompt engineering is a discipline within generative AI that focuses on writing intentional prompts to produce desired outputs from language models. It is similar to programming, but more abstract, and can be used to modify tasks and train models._' 

        st.subheader('Summary:')
        st.write(summary_text)

        st.subheader('Questions:')

        a = True

        if a == True:
            q1_resp = st.radio(
                "Q1: What is prompt engineering?",
                ('A) A programming language', 
                'B) A discipline within generative AI', 
                'C) A way to modify tasks'))


        if q1_resp == 'B) A discipline within generative AI':
            st.write('Correct!')
        else:
            st.write('Not really... The correct answer is "B) A discipline within generative AI"')