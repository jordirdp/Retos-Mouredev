"""
Los primeros dispositivos móviles tenían un teclado llamado T9
con el que se podía escribir texto utilizando únicamente su
teclado numérico (del 0 al 9).

Crea una función que transforme las pulsaciones del T9 a su
representación con letras.
- Debes buscar cuál era su correspondencia original
- Cada bloque de pulsaciones va separado por un guión.
- Si un bloque tiene más de un número, debe ser siempre el mismo.
- Ejemplo:
    Entrada: 6-666-88-777-33-3-33-888
    Salida: MOUREDEV
"""

def t9(entrada):
    codigos = [" ", ",.?!", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    texto_entrada = entrada.split("-")

    for i in range(len(texto_entrada)):
        orden = len (texto_entrada[i])-1
        tecla = int((texto_entrada[i])[0])
        cadena = (codigos[tecla])
        print (cadena[orden], end="")


texto = "6-666-88-777-33-0-3-33-888"
t9(texto)