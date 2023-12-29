"""
Crea un programa que analice texto y obtenga:
- Número total de palabras.
- Longitud media de las palabras.
- Número de oraciones del texto (cada vez que aparecen un punto).
- Encuentre la palabra más larga.

Todo esto utilizando un único bucle.
"""

texto ="""
Nos encontramos en un
periodo de guerra civil. Las
naves espaciales rebeldes,
atacando desde una base
oculta, han logrado su 
primera victoria contra
el malvado Imperio
Galáctico.

Durante la batalla, los 
espías rebeldes han
conseguido apoderarse de 
los planos secretos del
arma total y definitiva del
Imperio, la ESTRELLA
DE LA MUERTE,
una estación espacial
acorazada, llevando en sí
potencia suficiente para
destruir a un planeta
entero.

Perseguida por los 
siniestros agentes del 
Imperio, la Princesa Leia 
vuela hacia su patria, a
bordo de su nave espacial,
llevando consigo los
planos robados, que
pueden salvar a su pueblo
y devolver la libertad a la
galaxia.
"""

oraciones = texto.count(".")
palabras = texto.split()
tamaño = ["1"]
total = 0

for i in range(len(palabras)):
    total += len(palabras[i])
    if len(palabras[i]) > len(tamaño[0]):
        tamaño.insert(0,palabras[i])
media = total/len(palabras)

print ("\n- Número total de palabras =", len(palabras))
print ("- Número de oraciones =", oraciones)
print ("- Media de letras en palabras =", media)
print ("- Palabra más larga =", tamaño[0])