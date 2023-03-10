import streamlit as st
import pandas as pd
import array as arr

st.header('Awirut_App')
st.subheader('Welcome To my_App')

first = ['a','b']
last = ['a','b']
age = [1,2]
point = [1,2]

num = st.number_input('Enter number of student : ')
num1 = int(num)
i=0

if num1:
    while num1>num1-1:
        first[i] = st.text_input('Enter your Firstname : ', '')
        last[i] = st.text_input('Enter your Lastname : ', '')
        age[i] = st.number_input('Enter your Age : ')
        point[i] = st.number_input('Point : ')
        if first[i] and last[i] and age[i] and point[i]:
            st.write(f'Name is : {first[i]} {last[i]}')
            st.write(f'Age : {age[i]} year old')
            st.write(f'Point : {point[i]}')
            if point[i]>=0 and point[i]<=100:
                if point[i]<50:
                    st.write('Grade : F')
                elif point[i]<55:
                    st.write('Grade : D')
                elif point[i]<60:
                    st.write('Grade : D+')
                elif point[i]<65:
                    st.write('Grade : C')
                elif point[i]<70:
                    st.write('Grade : C+')
                elif point[i]<75:
                    st.write('Grade : B')
                elif point[i]<80:
                    st.write('Grade : B+')
                else:
                    st.write('Grade : A')
            else:
                st.subheader('Point out of length')
        else:
            st.error('Awaiting of data!!!')
    i=i+1

#if first and last and age:
    #st.write(f'Name is : {first} {last}')
   # st.write(f'Age : {age} year old')