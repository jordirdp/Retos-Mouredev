"""
Crea una función que calcule el número de la columna de una hoja de Excel
teniendo en cuenta su nombre.
- Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
- Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""

text = "AAA"
resultado = 0
multiplicador = []

for i in range(len(text)-1,-1,-1):
    orden = (ord(text[i])) % 64
    print (orden)
    multiplicador.append(orden)

print (multiplicador)

for i in range(len(multiplicador)):
    resultado += ((26**i)*multiplicador[i])
    print (resultado)