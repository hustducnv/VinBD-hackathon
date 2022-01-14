import streamlit as st
from shorten import shorten
from detail import get_detail

st.title('VinBigData Hackathon')
st.header('Team ABC')

with st.form(key='my_form'):
    text_input = st.text_area(label='Enter some text', height=300)
    n_sentences = st.number_input(label='Number of sentences (for summarization)', min_value=1, max_value=5, value=1)
    submit_button = st.form_submit_button(label="Tranfer")
    
if submit_button:
    st.subheader('Short Version:')
    result = shorten(text_input, n_sentences)
    for sent in result.split('\n'):
        st.write(sent)

    st.subheader('Detailed Version:')
    for sent in text_input.split('\n'):
        st.write(sent)
    st.write('---')
    for key, value in get_detail(text_input).items():
        if value != '':
            st.markdown('**{}: ** {}'.format(key, value))
            st.write('---')
            



