"""
Crea las funciones capaces de transformar colores HEX
a RGB y viceversa.
Ejemplos:
RGB a HEX: r: 0, g: 0, b: 0 -> #000000
HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
"""

letras = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

def rgb_hex():
    r = int(input ("\nIntroduce los valores a continuación:\n- R = "))
    g = int(input ("- G = "))
    b = int(input ("- B = "))
    list_rgb = [r,g,b]
    list_hexa = []

    for numero in list_rgb:
        restos = []

        while numero > 16:
            resto = numero % 16
            if resto > 9:
                resto = letras[resto]
            restos.insert(0,resto)
            numero = numero //16
        if numero > 9:
            numero = letras[numero]
        restos.insert(0,numero)

        if len(restos)==1:
            restos.insert(0,0)

        for i in range(len(restos)):
            list_hexa.append(restos[i])
    
    print ("HEX: #", end="")
    for i in range(6):
        print (list_hexa[i], end="")



def hex_rgb():
    hexa = input("\nIntroduce los seis dígitos seguidos : #")
    list_hexa = []
    list_rgb = []

    for i in range (0, 6, 2):
        list_hexa.append(hexa[i+1]+hexa[i])
    
    for i in range(3):
        rgb = 0
        for n in range(2):
            if list_hexa[i][n].isdigit() == True:
                rgb += ((16**n) * int(list_hexa[i][n]))
            else:
                orden = list(letras.values()).index(list_hexa[i][n])
                rgb += ((16**n) * list(letras.keys())[orden])         
        list_rgb.append(rgb)

    print (f"R:{list_rgb[0]}, G:{list_rgb[1]}, B:{list_rgb[2]}")    


def menu():
    print("\n*** CONVERSOR DE COLORES ***")
    print(" 1 - RGB a HEX")
    print(" 2 - HEX A RGB")
    entrada = input("\n  Elige tu opcion = ")
    if entrada == "1":
        rgb_hex()
    elif entrada == "2":
        hex_rgb()
    else:
        print ("solo puedes introducir 1 o 2")

menu()