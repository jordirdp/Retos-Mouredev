"""
Dada una URL con parámetros, crea una función que obtenga sus valores.
No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
los parámetros serían ["2023", "0"]
"""

url = "https://retosdeprogramacion.com?year=2023&challenge=0"
url2 = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"

def inicio(url):
    if "?" in url:
        punto_corte = url.index("?")
        url_cortada = url[punto_corte+1:]
        print ("\nEsta URL tiene los siguientes argumentos: ")
        parametros (url_cortada)
    else:
        print ("\nEsta URL parece que no tiene argumentos")
        exit()

def parametros (url_cortada):
    repeticiones = url_cortada.count("&")
    for n in range (repeticiones):
        argumento = url_cortada.index("=")
        print (" -",url_cortada[0:argumento], "=", end=" ")
        separador = url_cortada.index("&")
        print (url_cortada[argumento+1:separador])
        url_cortada = url_cortada[separador+1:]
    argumento = url_cortada.index("=")
    print (" -",url_cortada[0:argumento], "=", url_cortada[argumento+1:])

inicio (url)
inicio (url2)