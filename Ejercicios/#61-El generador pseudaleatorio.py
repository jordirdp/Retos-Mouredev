"""
Crea un generador de números pseudoaleatorios entre 0 y 100.
- No puedes usar ninguna función "random" (o semejante) del
  lenguaje de programación seleccionado.

Es más complicado de lo que parece...
"""

from datetime import *

def generador ():
    hora = datetime.now()
    seconds= int(hora.strftime('%f'))
    random = int(seconds/10000)
    print ("El nº es = ", random)

input ("pulsa [intro] cuando quieras generar un numero aleatorio: ")
generador()