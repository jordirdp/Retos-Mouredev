"""
Crea un programa que realize el cifrado César de un texto y lo imprima.
También debe ser capaz de descifrarlo cuando así se lo indiquemos.

Te recomiendo que busques información para conocer en profundidad cómo
realizar el cifrado. Esto también forma parte del reto.
"""
import string

minusculas = list(string.ascii_lowercase)
mayusculas = list(string.ascii_uppercase)
puntuacion = list(string.punctuation)

def encriptar(text):
    respuesta = ""
    for letra in text:
        if letra == " ":
            respuesta += " "
        elif letra in puntuacion:
            respuesta += letra
        elif letra in minusculas and ord(letra)>120:
            respuesta += chr(ord(letra)-24)
        elif letra in mayusculas and ord(letra)>88:
            respuesta += chr(ord(letra)-24) 
        else:
            respuesta += chr(ord(letra)+2)
    print (respuesta)

def desencriptar(text):
    respuesta = ""
    for letra in text:
        if letra == " ":
            respuesta += " "
        elif letra in puntuacion:
            respuesta += letra
        elif letra in minusculas and ord(letra)<99:
            respuesta += chr(ord(letra)+24)
        elif letra in mayusculas and ord(letra)<67:
            respuesta += chr(ord(letra)+24) 
        else:
            respuesta += chr(ord(letra)-2)
    print (respuesta)

encriptar ("\nHola mundo, me llamo Jordi!")
desencriptar ("Jqnc owpfq, og nncoq Lqtfk!")
