# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 21:09:13 2025

@author: kolla
"""
import numpy as np
import pandas as pd
import pickle
import streamlit as st
house=pd.read_csv("BostonHousing.csv")
model=pickle.load(open("house_price.sav",'rb'))
st.title('House Price Prediction Web App')
col1 ,col2,col3 ,col4=st.columns(4)
with col1:
    crim =st.number_input("crime rate", min_value=float(house['crim'].min()),
                       max_value=float(house['crim'].max()),
                       value=float(house['crim'].mean()))
with col2:
    zn=st.number_input('land zoned', min_value=float(house['zn'].min()),
                       max_value=float(house['zn'].max()),
                       value=float(house['zn'].mean()))
with col3:
    indus=st.number_input('proportion of non-retail business acres per town', min_value=float(house['indus'].min()),
                       max_value=float(house['indus'].max()),
                       value=float(house['indus'].mean())) 
with col4:
    chas=st.number_input('Charles River dummy variable',min_value=float(house['chas'].min()),
                       max_value=float(house['chas'].max()),
                       value=float(house['chas'].mean()))
with col1:
    nox=st.number_input('nitric oxides concentration ', min_value=float(house['nox'].min()),
                       max_value=float(house['nox'].max()),
                       value=float(house['nox'].mean()))
with col2:
    rm=st.number_input (' average number of rooms per dwelling', min_value=float(house['rm'].min()),
                       max_value=float(house['rm'].max()),
                       value=float(house['rm'].mean()))
with col3:
    age=st.number_input('age', min_value=float(house['age'].min()),
                       max_value=float(house['age'].max()),
                       value=float(house['age'].mean()))
with col4:
    dis=st.number_input('weighted distances', min_value=float(house['dis'].min()),
                       max_value=float(house['dis'].max()),
                       value=float(house['dis'].mean()))
with col1:
    rad=st.number_input('radial highways', min_value=float(house['rad'].min()),
                       max_value=float(house['rad'].max()),
                       value=float(house['rad'].mean()))
with col2:
    tax=st.number_input('tax', min_value=float(house['tax'].min()),
                       max_value=float(house['tax'].max()),
                       value=float(house['tax'].mean()))
with col3:
    ptratio=st.number_input(' pupil-teacher ratio',min_value=float(house['ptratio'].min()),
                       max_value=float(house['ptratio'].max()),
                       value=float(house['ptratio'].mean())) 
with col4:
    b=st.number_input('blacks by town ', min_value=float(house['b'].min()),
                       max_value=float(house['b'].max()),
                       value=float(house['b'].mean()))
with col1:
    lstat=st.number_input('lower status of the population', min_value=float(house['lstat'].min()),
                       max_value=float(house['lstat'].max()),
                       value=float(house['lstat'].mean()))
houseresult=np.array([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax,
   ptratio, b, lstat]],dtype:=np.float64)
if st.button('House price prediction'):
    house_prediction=model.predict(houseresult)
    st.success(f"Estimated Price: ${house_prediction[0]:,.2f}")
