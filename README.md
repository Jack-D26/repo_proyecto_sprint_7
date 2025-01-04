# repo_proyecto_sprint_7

# link a la pgina web/app.py

https://app-exploratory-analysis.onrender.com

## Análisis Exploratorio de Datos con Streamlit

### Descripción del Proyecto (Actualización)

Este proyecto ha evolucionado de su versión inicial, la cual utilizaba el dataset `vehicles_us.csv` para explorar datos sobre anuncios de venta de coches en Estados Unidos, a una herramienta interactiva enfocada en datos históricos de la Fórmula 1. La actualización incluye un nuevo dataset que permite visualizar el desempeño de los pilotos más destacados a lo largo de los años y su evolución en puntos y victorias.

### Actualización del Dataset

El proyecto ahora utiliza datos provenientes del dataset "Formula 1 World Championship (1950 - 2024)", específicamente los archivos `driver_standings.csv`, `drivers.csv` y `races.csv`. Estos datos fueron procesados y combinados para crear un nuevo archivo consolidado, `combined_driver_standings.csv`, que sirve como base para las visualizaciones.

#### Proceso de Combinación de Datos

El archivo `data_processing.py` contiene el código para combinar los datasets de la siguiente manera:

```python
import pandas as pd

def load_and_merge_data():
    # Cargar datasets
    driver_standings = pd.read_csv('./data/driver_standings.csv')
    drivers = pd.read_csv('./data/drivers.csv')
    races = pd.read_csv('./data/races.csv')

    # Seleccionar columnas relevantes para el merge
    drivers_subset = drivers[['driverId', 'driverRef']]
    races_subset = races[['raceId', 'year']]

    # Merge con nombres de los pilotos
    merged_data = driver_standings.merge(drivers_subset, on='driverId', how='left')

    # Merge con los años de las carreras
    merged_data = merged_data.merge(races_subset, on='raceId', how='left')

    return merged_data

if __name__ == "__main__":
    combined_data = load_and_merge_data()
    combined_data.to_csv('./data/combined_driver_standings.csv', index=False)
Este proceso permite enriquecer los datos con los nombres de los pilotos y los años de las carreras, facilitando el análisis visual.


#### Análisis Exploratorio (Notebook)
Antes de la implementación de las visualizaciones interactivas en Streamlit, se realizó un análisis exploratorio utilizando un notebook de Jupyter llamado EDA_F1.ipynb. Este análisis incluyó:

Inspección de Datos: Verificación de columnas, tipos de datos y valores faltantes.
Gráficos Iniciales:
Distribución de puntos acumulados por piloto.
Evolución de victorias por año.
Gráficos de dispersión y barras para identificar tendencias.
El análisis ayudó a definir las visualizaciones clave para incluir en la aplicación web.

Funcionalidades de la Aplicación (App.py)
La aplicación web está diseñada para visualizar datos interactivos relacionados con la Fórmula 1. A continuación, se describen las principales funciones:

1. Gráfico de Barras: Total de Puntos por Piloto (Top 10)
Muestra el total de puntos acumulados por los 10 pilotos más exitosos desde el año 2000.
Permite entender quiénes han dominado la Fórmula 1 en términos de puntos totales.
Etiquetas interactivas muestran los puntos exactos de cada piloto.
2. Gráfico de Barras Vertical: Victorias por Año (Top 10 Pilotos)
Segmentado por año, este gráfico permite explorar las victorias de los pilotos más destacados en un año específico.
Utiliza un control de selección interactivo (casillas de verificación) para que los usuarios elijan los años que desean visualizar.
Destaca quién tuvo mayor éxito en cada temporada.
3. Gráfico de Barras Vertical: Puntos Acumulados por Año
Muestra la acumulación progresiva de puntos de los pilotos a lo largo de los años seleccionados.
Los usuarios pueden seleccionar múltiples años para analizar la evolución de los puntos acumulados.
Proporciona una visión histórica de cómo los pilotos han acumulado puntos con el tiempo.

#### Requisitos
Para ejecutar la aplicación, necesitas tener instalado:

Python 3.10+
Las siguientes librerías de Python:
pandas
plotly
streamlit
Instalación
Clona este repositorio:

bash
Copiar código
git clone https://github.com/Jack-D26/repo_proyecto_sprint_7
cd repo_proyecto_sprint_7
Crea y activa un entorno virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate # Linux/Mac
.\venv\Scripts\activate  # Windows
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Ejecuta la aplicación:

bash
Copiar código
streamlit run app.py


#### Conclusión
Este proyecto demuestra cómo transformar un análisis exploratorio inicial en una aplicación interactiva que permite explorar datos históricos de Fórmula 1. A través de gráficos dinámicos y controles de selección intuitivos, los usuarios pueden visualizar de manera efectiva el desempeño de los pilotos a lo largo de los años.


```
