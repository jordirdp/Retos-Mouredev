"""
Crea un programa que encuentre y muestre todos los pares de números primos
gemelos en un rango concreto.
El programa recibirá el rango máximo como número entero positivo.

- Un par de números primos se considera gemelo si la diferencia entre
  ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)

- Ejemplo: Rango 14
  (3, 5), (5, 7), (11, 13)
"""
lista = []

def esprimo(num):
    contador = 0
    for n in range(2, num+1):
        if num%n == 0:
            contador +=1
    if contador <= 1:
        if esgemelo(num+2) == True:
            tupla=(num,num+2)
            lista.append(tupla)

def esgemelo(num):
    contador = 0
    for n in range(2, num+1):
        if num%n == 0:
            contador +=1
    if contador <= 1:
        return True
    else:
        return False

rango = int(input("Introduce el rango = "))
for n in range(2,rango):
    esprimo(n)

print (lista)