"""
Crea una función que reciba dos cadenas de texto casi iguales,
a excepción de uno o varios caracteres.
La función debe encontrarlos y retornarlos en formato lista/array.
- Ambas cadenas de texto deben ser iguales en longitud.
- Las cadenas de texto son iguales elemento a elemento.
- No se pueden utilizar operaciones propias del lenguaje
  que lo resuelvan directamente.

Ejemplos:
- Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
- Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
"""

def comparacion (texto1, texto2):
    cadena1 = []
    cadena2 = []
    diferencias = []

    for caracter in texto1:
        cadena1.append(caracter)
    for caracter in texto2:
        cadena2.append(caracter)       

    for i in range(len(cadena2)):
        if cadena1[i] != cadena2[i]:
            diferencias.append(cadena2[i])
    
    print (diferencias)

text1 = "Me llamo mouredev"
text2 = "Me llemo mouredov"

if len (text1) != len (text2):
    print ("No se pueden comparar frases diferentes")
else:
    comparacion (text1, text2)