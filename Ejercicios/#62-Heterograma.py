"""
Crea 3 funciones, cada una encargada de detectar si una cadena de
texto es un heterograma, un isograma o un pangrama.
- Debes buscar la definición de cada uno de estos términos.
- Heterograma = no contiene ninguna letra repetida
- Isograma = cada letra aparece el mismo número de veces
- Pangrama = utiliza todas las letras del alfabeto
"""


def heterograma(text):
    hetero = ""
    for letra in text:
        conteo = text.count(letra)
        if conteo == 1:
            hetero = "Verdadero"
        else:
            hetero = "Falso"
            break
    return hetero

def isograma(text):
    lista = []
    iso = ""
    for letra in text:
        conteo = text.count(letra)
        lista.append (conteo)
    for orden in range(1,len(lista)):
        if lista[orden] == lista[orden-1]:
            iso = "Verdadero"
        else:
            iso = "Falso"
            break
    return iso
        
def pangrama(text):
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    pangra = ""
    for orden in range(0,len(abecedario)):
        if abecedario[orden] in text:
            pangra = "Verdadero"
        else:
            pangra = "Falso"
            break
    return pangra

pregunta = input("Escribe una frase: ")
minusculas = pregunta.lower()
texto = minusculas.replace(" ","")

print ("¿Es un heterograma?: " + heterograma (texto))
print ("¿Es un Isograma?: " + isograma (texto))
print ("¿Es un Pangrama?: " + pangrama (texto))
