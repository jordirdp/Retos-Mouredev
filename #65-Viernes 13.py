"""
Crea una función que sea capaz de detectar si existe un viernes 13
en el mes y el año indicados.
- La función recibirá el mes y el año y retornará verdadero o falso.
"""

import calendar

semana = {
    0:"Lunes",
    1:"Martes",
    2:"Miércoles",
    3:"Jueves",
    4:"Viernes",
    5:"Sábado",
    6:"Domingo"
}

def menu():
    anno = int(input("\nIntroduce el año: "))
    mes = int(input("Introduce el mes en formato número: "))
    calcula (anno, mes)

def calcula (a, m):
    if calendar.weekday(a, m, 13) == 4:
        print ("El día 13 cae en viernes")
    else:
        dia = calendar.weekday(a, m, 13)
        print ("El día 13 cae en", semana[dia])

menu()