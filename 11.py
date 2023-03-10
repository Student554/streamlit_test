import streamlit as st

st.write('Hello...')

num = st.number_input('Enter number of sum :')
temp = 0

for i in range(int(num)):
    temp += st.number_input(f'value {i+1}')

st.write(f'Answer : {temp}')