# repo_proyecto_sprint_7

# Análisis Exploratorio de Datos con Streamlit

## Descripción del Proyecto

Esta aplicación web interactiva, desarrollada con Streamlit, permite realizar un análisis exploratorio de datos de manera sencilla y visual. El proyecto utiliza el dataset `vehicles_us.csv`, que contiene información sobre anuncios de venta de coches en Estados Unidos.

Con esta herramienta, los usuarios pueden generar gráficos interactivos para explorar los datos y obtener información visual rápidamente.

## Funcionalidades

- **Visualización de Histogramas**: Permite al usuario explorar la distribución de los kilómetros recorridos (`odometer`) de los vehículos a través de un histograma interactivo.
- **Gráfico de Dispersión**: Permite visualizar la relación entre los kilómetros recorridos (`odometer`) y el precio (`price`) de los vehículos.
- **Selección Interactiva**: Los usuarios pueden seleccionar qué gráficos generar mediante casillas de verificación.

## Requisitos

Para ejecutar la aplicación, necesitas tener instalado:

- Python 3.10+
- Las siguientes librerías de Python:
  - `pandas`
  - `plotly`
  - `streamlit`

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/Jack-D26/repo_proyecto_sprint_7
   cd tu-repositorio

   ```

2. Crea y activa un entorno virtual:

3. Instala las dependencias:
   pip install -r requirements.txt

4. Ejecución
   streamlit run app.py

Dataset
El archivo "vehicles_us.csv" contiene información sobre vehículos en venta y se utiliza para generar las visualizaciones interactivas.
