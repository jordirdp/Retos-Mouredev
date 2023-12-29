"""
Crea una función que dibuje una espiral como la del ejemplo.
- Únicamente se indica de forma dinámica el tamaño del lado.
- Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚

Ejemplo espiral de lado 5 (5 filas y 5 columnas):
════╗
╔══╗║
║╔╗║║
║╚═╝║
╚═══╝
"""

lado = int(input("Introduce el tamaño de la espiral : "))


for h in range(lado):
    espiral = ""
    horizontal = False
    for v in range(lado):
        if (h+v) == (lado-1) and v >= h:
            espiral += "╗"
            horizontal = False 
        elif (h+v) == (lado-1) and v < h:
            espiral += "╚"
            horizontal = True
        elif (h-v) == 1 and h < (lado/2):
            espiral += "╔"
            horizontal = True
        elif (h==v) and v>=(lado/2):
            espiral += "╝"
            horizontal = False
        elif h==0:
            espiral += "═"
        elif horizontal == True:
            espiral += "═" 
        else:
            espiral += "║"
        
    print (espiral)