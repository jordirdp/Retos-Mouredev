"""
Crea una función que reciba dos parámetros para crear una cuenta atrás.
- El primero, representa el número en el que comienza la cuenta.
- El segundo, los segundos que tienen que transcurrir entre cada cuenta.
- Sólo se aceptan números enteros positivos.
- El programa finaliza al llegar a cero.
- Debes imprimir cada número de la cuenta atrás.
"""
import time

print ("\n *** CUENTA ATRÁS PERSONALIZADA ***")
numeros = int(input(" - ¿Desde qué número quieres que empiece a contar? = "))
tiempo = int(input(" - ¿Cuántos segundos quieres que pasen entre cada número? = "))

for i in range(numeros,0,-1):
    print (i,"...")
    time.sleep(tiempo)

print ("¡¡¡ BOOM !!!")