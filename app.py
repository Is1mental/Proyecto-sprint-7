import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.title("Análisis de Anuncios de Coches")

# Botón para construir un histograma
if st.button("Mostrar Histograma"):
    st.write("Histograma del odómetro:")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)

# Botón para construir un gráfico de dispersión
if st.button("Mostrar Gráfico de Dispersión"):
    st.write("Relación entre el odómetro y el precio:")
    scatter_fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(scatter_fig)