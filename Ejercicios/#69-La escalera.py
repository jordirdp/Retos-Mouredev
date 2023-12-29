"""
Crea una función que dibuje una escalera según su número de escalones.
- Si el número es positivo, será ascendente de izquiera a derecha.
- Si el número es negativo, será descendente de izquiera a derecha.
- Si el número es cero, se dibujarán dos guiones bajos (__).

Ejemplo: 4
        _
      _|
    _|
  _|
_|
"""

def negativo(numero):
    numero = abs(numero)
    r=0
    print ("_")
    for n in range(numero):
        print(" "*(n+r),"|_")
        r +=1

def positivo(numero):
    r=numero
    print (" "*(numero+r), "_")
    for n in range(numero):
        print(" "*(numero+r-2), "_|")
        r -=2

def menu():
    numero = int(input("Introduce número de escalones (positivo o negativo) = "))
    if numero == 0:
        print ("__")
        exit()
    elif abs(numero) == numero:
        positivo(numero)
    else:
        negativo(numero)

menu()