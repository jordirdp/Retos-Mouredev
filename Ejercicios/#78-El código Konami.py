"""
Crea un programa que detecte cuando el famoso "Código Konami" se ha
introducido correctamente desde el teclado.
Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
"""

#Arriba, Arriba, Abajo, Abajo, Izquierda, Derecha, Izquierda, Derecha, B, A, Start

from pynput import keyboard

konami_code = [
    keyboard.Key.up,
    keyboard.Key.up,
    keyboard.Key.down,
    keyboard.Key.down,
    keyboard.Key.left,
    keyboard.Key.right,
    keyboard.Key.left,
    keyboard.Key.right,
    keyboard.KeyCode.from_char("b"),
    keyboard.KeyCode.from_char("a")]

key_position = 0

def tecla_pulsada(key):
    global key_position
    print("Tecla pulsada " + str(key))

    if key == keyboard.Key.esc:
        return False
    
    if key == konami_code[key_position]:
        key_position +=1
    else:
        key_position = 0

    if key_position == 10:
        print ("***** PREMIO *****")

print ("\nIntroduce tu código secreto : ")
keyboard.Listener(tecla_pulsada).run()