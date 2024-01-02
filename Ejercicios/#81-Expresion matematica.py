"""
Crea una función que reciba una expresión matemática (String)
y compruebe si es correcta. Retornará true o false.
- Para que una expresión matemática sea correcta debe poseer
  un número, una operación y otro número separados por espacios.
  Tantos números y operaciones como queramos.
- Números positivos, negativos, enteros o decimales.
- Operaciones soportadas: + - * / %

Ejemplos:
"5 + 6 / 7 - 4" -> true
"5 a 6" -> false
"""

def funcion (texto):
    argumentos = texto.split()
    operaciones = ["+", "-", "*", "/", "%"]

    if len(argumentos)%2 == 0:
      return False

    for item in argumentos:
      if argumentos.index(item) % 2 == 0:
        try:
          float(item)
        except:
          return False
      else:
        if item not in operaciones:
          return False

    return True        

text = "5 + 6 / 7 - 4"
print (funcion (text))
text2 = "5 a 6"
print (funcion (text2))