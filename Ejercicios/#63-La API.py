"""
Llamar a una API es una de las tareas más comunes en programación.

Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...

Aquí tienes un listado de posibles APIs:
https://github.com/public-apis/public-apis
"""

import requests
from datetime import datetime, timedelta

ahora = datetime.today()
delta = timedelta(days = 1)
mañana = ahora + delta
pasadomañana = mañana + delta
fecha_inicial = mañana.strftime('%Y-%m-%d')
fecha_final = pasadomañana.strftime('%Y-%m-%d')

fechas = [fecha_inicial, fecha_final]
coordenadas = [41.4706, 2.0861]
parametros = {
    "latitude" : coordenadas[0],
    "longitude" : coordenadas[1],
    "hourly" : "temperature_2m",
    "timezone" : "auto",
    "start_date" : fechas[0],
    "end_date" : fechas[1]
    }
url = "https://api.open-meteo.com/v1/forecast"

response = requests.get(url, params=parametros)
data = response.json()
horas = data["hourly"]["time"]
temperaturas = data["hourly"]["temperature_2m"]

for h in range(0,25):
    print (horas[h], "-> ", temperaturas[h])