import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar el dataset
data = pd.read_csv("data/combined_driver_standings.csv")

# Filtrar los años a partir del 2000
data = data[data['year'] >= 2000]

# Obtener la lista de los Top 10 pilotos por puntos totales
top_10_drivers = (
    data.groupby('driverRef')['points'].sum()
    .sort_values(ascending=False)
    .head(10)
    .index.tolist()
)

# Gráfico 1: Total de puntos por piloto (Top 10)
st.header("Total de Puntos por Piloto (Top 10)")

# Sumar puntos por piloto
points_by_driver = data.groupby('driverRef')['points'].sum().reset_index()

# Filtrar solo Top 10 pilotos
points_by_driver = points_by_driver[points_by_driver['driverRef'].isin(
    top_10_drivers)]

# Ordenar por puntos
points_by_driver = points_by_driver.sort_values('points', ascending=False)

# Crear gráfico de barras horizontal
fig1 = px.bar(
    points_by_driver,
    x='points',
    y='driverRef',
    orientation='h',
    title="Total de Puntos por Piloto (Top 10)",
    labels={'points': 'Puntos Totales', 'driverRef': 'Piloto'},
    text='points'
)
fig1.update_traces(texttemplate='%{text:.0f}', textposition='outside')
st.plotly_chart(fig1, use_container_width=True)

st.markdown(
    "Este gráfico muestra el total de puntos acumulados por los pilotos más exitosos en la Fórmula 1 desde el año 2000."
)

# Gráfico 2: Victorias por piloto en años seleccionados
st.header("Victorias por Piloto en los Años Seleccionados (Top 10)")

# Selección de años con casillas
selected_years = st.multiselect(
    "Selecciona uno o más años:",
    options=sorted(data['year'].unique()),
    default=[2022]
)

# Filtrar datos para los años seleccionados y victorias
victories_by_driver = (
    data[data['year'].isin(selected_years) & (data['wins'] > 0)]
    .groupby('driverRef')['wins'].sum()
    .reset_index()
)

# Filtrar solo Top 10 pilotos
victories_by_driver = victories_by_driver[victories_by_driver['driverRef'].isin(
    top_10_drivers)]

# Crear gráfico de barras vertical
fig2 = px.bar(
    victories_by_driver,
    x='driverRef',
    y='wins',
    color='driverRef',
    title=f"Victorias por Piloto en los Años Seleccionados (Top 10)",
    labels={'wins': 'Victorias', 'driverRef': 'Piloto'},
    text='wins'
)
fig2.update_traces(texttemplate='%{text:.0f}', textposition='outside')
st.plotly_chart(fig2, use_container_width=True)

st.markdown(
    f"Este gráfico muestra las victorias obtenidas por los pilotos más exitosos durante los años seleccionados."
)

# Gráfico 3: Puntos acumulados por piloto en un año seleccionado
st.header("Evolución Acumulada de Puntos por Año (Top 10 Pilotos)")

# Selección de año con slider
selected_year = st.slider(
    "Selecciona un año:", min_value=2000, max_value=2024, value=2022
)

# Filtrar datos hasta el año seleccionado
filtered_data = data[data['year'] <= selected_year]

# Sumar puntos acumulados progresivamente
cumulative_points = (
    filtered_data.groupby(['year', 'driverRef'])['points']
    .sum()
    .groupby(level=1).cumsum()
    .reset_index()
)

# Filtrar solo Top 10 pilotos
cumulative_points = cumulative_points[cumulative_points['driverRef'].isin(
    top_10_drivers)]

# Crear gráfico de barras vertical
fig3 = px.bar(
    cumulative_points[cumulative_points['year'] == selected_year],
    x='driverRef',
    y='points',
    color='driverRef',
    title=f"Puntos Acumulados por Piloto hasta el Año {
        selected_year} (Top 10)",
    labels={'points': 'Puntos Acumulados', 'driverRef': 'Piloto'},
    text='points'
)
fig3.update_traces(texttemplate='%{text:.0f}', textposition='outside')
st.plotly_chart(fig3, use_container_width=True)

st.markdown(
    f"Este gráfico muestra los puntos acumulados progresivamente por cada piloto hasta el año seleccionado ({
        selected_year})."
)
