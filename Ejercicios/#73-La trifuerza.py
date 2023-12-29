""" 
¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 

Crea un programa que dibuje una Trifuerza de "Zelda"
formada por asteriscos.
- Debes indicarle el número de filas de los triángulos con un entero positivo (n).
- Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
Ejemplo: Trifuerza 2
   *
  ***
 *   *
*** ***
"""

filas = int(input("Introduce número de filas = "))
espacios = 2*filas-2

for repeticiones in range(filas):
    print(" "*espacios," *  "*(repeticiones+1))
    print(" "*espacios,"*** "*(repeticiones+1))
    espacios -= 2