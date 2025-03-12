import streamlit as st
import requests


st.title('Taxi Fare Prediction')

st.markdown('''
This app predicts the fare of a taxi ride based on user input.
''')

# Inputs do usuário
date = st.date_input('Select the date:')
time = st.time_input('Select the time:')
passenger_count = st.number_input('Number of passengers:', min_value=1, step=1)
pickup_lat = st.number_input("Pickup Latitude", format="%.6f")
pickup_lon = st.number_input("Pickup Longitude", format="%.6f")
dropoff_lat = st.number_input("Dropoff Latitude", format="%.6f")
dropoff_lon = st.number_input("Dropoff Longitude", format="%.6f")

# Formatando a data e hora para o formato esperado pela API
pickup_datetime = f"{date} {time}"

# Botão para fazer a previsão
if st.button('Predict Fare'):
    url = 'https://taxifare.lewagon.ai/predict'
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_lon,
        "pickup_latitude": pickup_lat,
        "dropoff_longitude": dropoff_lon,
        "dropoff_latitude": dropoff_lat,
        "passenger_count": passenger_count
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        prediction = response.json().get("fare", "Error: No fare returned")
        st.success(f"Estimated Fare: ${prediction:.2f}")
    else:
        st.error("Error fetching prediction. Please try again.")
