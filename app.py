import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado principal
st.header("Análisis Exploratorio de Datos del Dataset vehicles_us.csv")

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para el histograma
hist_checkbox = st.checkbox('Mostrar histograma')

if hist_checkbox:
    # Mostrar mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
scatter_checkbox = st.checkbox('Mostrar gráfico de dispersión')

if scatter_checkbox:
    # Mostrar mensaje
    st.write(
        'Creación de un gráfico de dispersión para el precio y los kilómetros recorridos')

    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Relación entre kilómetros recorridos y precio")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)
