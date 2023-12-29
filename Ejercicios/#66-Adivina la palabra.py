"""
Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
- El juego comienza proponiendo una palabra aleatoria incompleta
  - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
- El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
  la palabra a adivinar)
  - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
    uno al número de intentos
  - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
    al número de intentos
  - Si el contador de intentos llega a 0, el jugador pierde
- La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
  ocultando más del 60%
- Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""

from random import *

diccionario = ["ejercicios", "soluciones", "videos", "comunidades", "escondidas"]
eleccion = choice(diccionario)
intentos = 3

palabra = []
for character in eleccion:
    palabra.append(character)
palabra_oculta = palabra.copy()

escondemos = int(0.6*len(palabra))
oculto = ""
for n1 in range(escondemos):
    ocultamos = choice(palabra)
    if ocultamos in oculto:
        continue
    else:
        oculto += ocultamos
        repeticiones = palabra.count(ocultamos)
        for n2 in range(repeticiones):
            posicion = palabra_oculta.index(ocultamos)
            palabra_oculta[posicion]="-"

print ("\nAdivina la palabra escondida: ", end="")
for letra in palabra_oculta:
    print (letra, end= " ")

for i1 in range (intentos):
    letra = input ("\nElige una letra: ")
    for n3 in range(len(palabra)):
        if palabra[n3]==letra:
            palabra_oculta[n3]=letra
    for letra in palabra_oculta:
        print (letra, end= " ")
solucion = input("\nIntroduce la palabra: ")
if solucion == eleccion:
    print("************ ¡Has ganado! ************")
else:
    print("Lo siento... Has perdido...")
