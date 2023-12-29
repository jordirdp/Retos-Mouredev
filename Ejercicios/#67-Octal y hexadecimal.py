"""
Crea una función que reciba un número decimal y lo trasforme a Octal
y Hexadecimal.
- No está permitido usar funciones propias del lenguaje de programación que
realicen esas operaciones directamente.
"""

def octal(numero):
    restos = []
    while numero > 8:
        resto = numero % 8
        restos.insert(0,resto)
        numero = numero //8
    restos.insert(0,numero)
    print (" - En octal =", end=" ")
    for i in range(len(restos)):
        print (restos[i], end="")

def hexadecimal(numero):
    restos = []
    letras = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    while numero > 16:
        resto = numero % 16
        if resto > 9:
            resto = letras[resto]
        restos.insert(0,resto)
        numero = numero //16
    if numero > 9:
        numero = letras[numero]
    restos.insert(0,numero)
    print ("\n - En hexadecimal =", end=" ")
    for i in range(len(restos)):
        print (restos[i], end="") 


decimal = int(input("\nIntroduce tu número :"))
octal (decimal)
hexadecimal (decimal)