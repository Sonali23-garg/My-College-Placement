import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import joblib 
model=joblib.load("model.joblib")

cgpa=float(st.number_input("Enter your CGPA  :  "))

if st.button("Predict PAKAGE "):
    pred=model.predict([[cgpa]])
    st.title(f"if CGPA is : {cgpa} your pakage will be  :  {pred/10} LPA")
