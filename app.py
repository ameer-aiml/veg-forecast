%%writefile app.py
import streamlit as st
import joblib
import matplotlib.pyplot as plt
st.title('Forecasting')
st.set_option('deprecation.showPyplotGlobalUse', False)

cities = ['Chennai','Delhi','Bangalore']

select = st.sidebar.selectbox('Select City',cities)
st.write(select)

days_p = st.sidebar.slider('Days to forecast',1,30) 
model = joblib.load('abc')
x = model.make_future_dataframe(periods = days_p,freq='D')
forecast = model.predict(x)
df2 = forecast[['ds','trend','yhat_lower','yhat_upper','yhat']]
# Pandas plotting
model.plot(forecast,figsize=(20,5));
st.pyplot()
