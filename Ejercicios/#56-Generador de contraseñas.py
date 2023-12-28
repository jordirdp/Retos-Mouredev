"""
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
"""

from random import *

def menu():
    longitud = int(input ("Longitud del password (4-16): "))
    if longitud < 4 or longitud > 16:
        print ("Introduce un número entre 4 y 16")
        menu()
    mayusculas = input ("¿Deseas incorporar mayúsculas? (s/n): ")
    if mayusculas == "s":
        mayusculas = True
    else:
        mayusculas = False
    numeros = input ("¿Deseas que incluya números? (s/n): ")
    if numeros == "s":
        numeros = True
    else:
        numeros = False    
    simbolos = input ("¿Deseas que incluya símbolos? (s/n): ")
    if simbolos == "s":
        simbolos = True
    else:
        simbolos = False
    
    generador (longitud, mayusculas, numeros, simbolos)

def generador(long, Caps, Numbers, Sim):
    caracters = list(range(97, 123))
    if Caps == True:
        caracters += list(range(65, 91))
    if Numbers == True:
        caracters += list(range(48,58))
    if Sim == True:
        caracters += list(range(33,48)) + list(range(58, 65)) + list(range(91, 97))
    password = []
    for n in range(long):
        password.append(chr(choice(caracters)))
        print (password[n], end="")
        

print ("\n*** GENERADOR DE CONTRASEÑAS *** \n")
menu()