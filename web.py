import streamlit as st
st.title("Welcome to wscube tech")
st.header("Python")
st.subheader("Java")
st.markdown("I love Python")
st.code('''for i in range(1,5,1):
             print("hello")''')
import pandas as pd
dataset=pd.read_csv("D:\\vscode\\New folder\\car_price.csv")
st.dataframe(dataset)
name=st.text_input("Enter your Name :")
fname=st.text_input("Enter your father Your name :")
add=st.text_area("Enter your Address :")
classdata=st.selectbox("Enter your Class :",(1,2,3,4,5,6))
button=st.button("Done")
if button:
    st.markdown(f"""
    Name : {name}

    Father Name:{fname}
    
    address : {add}
    
    class : {classdata} """)
#live
