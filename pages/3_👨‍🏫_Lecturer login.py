#Lecturer login page here lecture can login and view attendance
#change password/add new users on line 31
import streamlit as st
import yaml
from datetime import datetime
import pandas as pd
import time 
import os
st.title("Lecturer Login")
username=st.text_input("Username")
password=st.text_input("Password", type="password")
ts = time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
exist=os.path.isfile("disp/disp_" + date + ".csv")
data = pd.read_csv("Attendance/att_" + date + ".csv")
df=pd.DataFrame(data)

def delduplicate(data, exist): # to overcome the problem of multiple values in att_csv file
 if exist:
  data_cleaned = data.drop_duplicates(subset=['NAME'])
  data_cleaned.to_csv("disp/disp_" + date + ".csv",index=False)
  
 else:
  with open("disp/disp_" + date + ".csv", "+a") as csvfile:
               data_cleaned = data.drop_duplicates(subset=['NAME'])
               data_cleaned.to_csv("disp/disp_" + date + ".csv",index=False)
               csvfile.close()


def auth(username, password):
    if username=="lecturer_id" and password=="admin": # current username and password 
     #use elif here for multiple users
     return True
    
    else:
     return False
    

if st.button("Login"):
   if auth(username, password):
      st.success(f"Login successful, Welcome back {username}")#success message with username
      delduplicate(data, exist)
      data2=pd.read_csv("disp/disp_" + date + ".csv")
      df=pd.DataFrame(data2)
      st.dataframe(data2)#displays csv file without duplicate values

else:
      st.error("Please enter Login Details.")





    
 
  







