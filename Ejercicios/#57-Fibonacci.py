"""
Escribe un programa que, dado un número, compruebe y muestre si es primo,
fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar
"""

def esprimo(num):
    contador = 0
    for n in range(2, num+1):
        if num%n == 0:
            contador +=1
    if contador > 1:
        print ("no es primo,", end=" ")
    else:
        print ("es primo,", end=" ")
    esfibonacci(num)

def esfibonacci(fibo):
    lista=[0]
    old=0
    new=1
    suma = old + new
    lista.append(suma)
    while (suma<fibo):
        old = new
        new = suma
        suma = old + new
        lista.append(suma)
    if fibo in lista:
        print ("fibonacci", end=" ")
    else:
        print ("no es fibonacci", end=" ")         
    espar(fibo)

def espar(par):
        if par%2 == 0:
            print ("y es par")
        else:
            print ("y es impar")
        exit()


numero = int(input("Escribe un número: "))
print ("El número",numero, end=" ")
esprimo(numero)

