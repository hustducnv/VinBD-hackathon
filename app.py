import streamlit as st
from shorten import shorten
from detail import get_detail
from genz import genZ_transfer


black_list = [
    'tự tin lành mạnh',
    'hạ bì',
    'mi mắt',
    'restless',
    'trương lực',
    'rbv',
    'chuyển hoá'
]


st.title('VinBigData Hackathon')
st.header('NaN Team')

with st.form(key='my_form'):
    text_input = st.text_area(label='Enter some text', height=300)
    n_sentences = st.number_input(label='Number of sentences', min_value=1, max_value=5, value=2)
    submit_button = st.form_submit_button(label="Transfer")
    
if submit_button:
    st.subheader('Short Style:')
    result = shorten(text_input, n_sentences)
    for sent in result.split('\n'):
        st.write(sent)


    st.subheader('GenZ Style:')
    short = shorten(text_input, 4)
    result = genZ_transfer(short)
    for sent in result.split('\n'):
        st.write(sent)


    st.subheader('Analytic style:')
    for sent in text_input.split('\n'):
        st.write(sent)
    st.write('---')
    for key, value in get_detail(text_input).items():
        if value != '' and key not in black_list:
            st.markdown('**{}: ** {}'.format(key, value))
            st.write('---')
            



