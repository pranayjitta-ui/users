import streamlit as st
import sqlite3

conn=sqlite3.connect("users.db",check_same_thread=False)
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(name text PRIMARY KEY,password text)""")

choice=st.sidebar.selectbox("MENU",["LOGIN","REGISTER"])
if choice=="REGISTER":
    name=st.text_input("USERNAME")
    password=st.text_input("PASSWORD",type="password")
    if st.button("REGISTER"):
       cursor.execute("""INSERT INTO users(name,password)VALUES(?,?)""",(name,password))
       conn.commit()
       st.balloons()
if choice=="LOGIN":
    name=st.text_input("USERNAME")
    password=st.text_input("PASSWORD",type="password")
    if st.button("LOGIN"):
        cursor.execute("""SELECT * FROM users WHERE name=? AND password=?""",(name,password))
        result=cursor.fetchone()
        if result:
            st.success("valid user")
            st.snow()
        else:
            st.error("invalid user")
        
    

