import streamlit as st
import pandas as pd

st.title('🎈 Student554_App')
st.write('Welcome to my App')

url = st.sidebar.text_input('URL','')
#st.info(f'URL of Data : {url}')



if url:
    st.header('Output')
    st.info(f'URL of Data : {url}')
    df = pd.read_csv(url)
    st.write(df)
    columns = df.columns 
    size = columns.size
    ca = [columns[size-1],columns[size-2]]


    for i in range(0,size-2):
      ca.insert(i, columns[i])

    genre = st.radio(
    "Group by :",(ca))
    
    if genre:
        gb = df.groupby(genre).mean()
        st.bar_chart(gb)

else:
    st.subheader('Enter URL!')

#url = "https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv"

#df = pd.read_csv(url)

#st.write(df)

