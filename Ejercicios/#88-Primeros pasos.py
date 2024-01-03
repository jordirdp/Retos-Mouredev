"""
Como cada año, el día 256 se celebra el "Día de la Programación".
En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos
256 regalos para seguir aprendiendo programación:
https://diadelaprogramacion.com

Para seguir ayudando, te propongo este reto:
Mostrar la sintaxis de los principales elementos de un lenguaje
en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?

En un fichero, haz lo siguiente (si el lenguaje lo soporta),
y comenta cada bloque para identificar con qué se corresponde:
- Haz un "Hola, mundo!"
- Crea variables de tipo String, numéricas (enteras y decimales)
  y Booleanas (o cualquier tipo de dato primitivo).
- Crea una constante.
- Usa un if, else if y else.
- Crea estructuras como un array, lista, tupla, set y diccionario.
- Usa un for, foreach y un while.
- Crea diferentes funciones (con/sin parámetros y con/sin retorno).
- Crea una clase.
- Muestra el control de excepciones.

Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
de sintaxis básica de muchos lenguajes.

¡Muchas gracias!
"""

#Hola mundo
print ("Hola, mundo!")

#Variables y constantes
String = str("minombre")
Numericas_enteras = int(52)
Numericas_decimales = float(70.5)
Booleanas = bool (True)
CONSTANTE = "se nombra en mayúsculas"

#Condicionales
if Numericas_enteras > Numericas_decimales:
    print ("int > float")
elif Numericas_decimales > Numericas_enteras:
    print ("float > int")
else:
    print ("Son iguales")

#Estructuras
lista = [String, Numericas_decimales, Numericas_enteras]
tupla = (String, Numericas_decimales, Numericas_enteras)
diccionario = {String : "str", Numericas_decimales : "float", Numericas_enteras : "int"}
myset = set([String, Numericas_decimales, Numericas_enteras])

#Bucles
for i in range (5):
    print (i)

for item in lista:
    print(item)

index = 0
while index < len(lista):
    print (lista[index])
    index+=1

#Funciones
def funcion():
    print("función simple")
def funcion_retorno() -> str:
    return "función con retorno"
def funcion_parametro (text):
    print (text)

funcion()
print(funcion_retorno())
funcion("parámetro")

#Clases
class MiClase():
    def __init__(self, name):
        self.name = name
    def hola(self):
        print(f"¡Hola, {self.name}!")

miclase = MiClase("Jordi")
print(miclase.name)
miclase.hola()

#Excepciones
try:
    print (0/0)
except:
    print ("no se puede dividir por cero")
finally:
    print ("siempre aparece")