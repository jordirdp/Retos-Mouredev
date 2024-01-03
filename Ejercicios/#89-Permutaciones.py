"""
Crea un programa que sea capaz de generar e imprimir todas las
permutaciones disponibles formadas por las letras de una palabra.
- Las palabras generadas no tienen por qué existir.
- Deben usarse todas las letras en cada permutación.
- Ejemplo: sol, slo, ols, osl, los, lso
"""
import itertools

palabra = input("Introduce palabra : ")
lista = []

for letra in palabra:
    lista.append(letra)

permutaciones = list(itertools.permutations(lista))

for i in range(len(permutaciones)):
    for n in range(len(permutaciones[i])):
        print(permutaciones[i][n], end="")
    print(", ", end=" ")