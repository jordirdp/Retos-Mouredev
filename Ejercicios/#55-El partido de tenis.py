"""
Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
gane cada punto del juego.

- Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
- Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
  15 - Love
  30 - Love
  30 - 15
  30 - 30
  40 - 30
  Deuce
  Ventaja P1
  Ha ganado el P1
- Si quieres, puedes controlar errores en la entrada de datos.
- Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""


# VARIABLES
i1 = 0
i2 = 0

def menu():
  opciones = ["P1","P2"]
  gana = input ("¿Quién ha metido el punto? P1/P2: ")

  if gana in opciones:
    juego(gana)    
  else:
    print ("¡ATENCION! Tienes que escribir P1 o P2")
    menu()

def juego(punto):
  global i1, i2

  if punto == "P1":
    i1 += 1          
  else:
    i2 += 1

  resultado(i1, i2)

def resultado(p1,p2):
  Jugador1 = ["Love", "15", "30", "40", "Ventaja P1", "Ha ganado P1"]
  Jugador2 = ["Love", "15", "30", "40", "Ventaja P2", "Ha ganado P2"]

  if (p1 == p2) and p1 >= 3:
    print ("Deuce")
  elif (p1 <= 3) and (p2 <= 3):
    print (Jugador1[p1], Jugador2[p2], sep=' - ')
  elif p1-p2 > 1:
    print (Jugador1[5])
    final()
  elif p2-p1 > 1:
    print (Jugador2[5])
    final()
  elif p1-p2 == 1:
    print (Jugador1[4])
  elif p2-p1 == 1:
    print (Jugador2[4])

  menu()

def final():
  global i1, i2

  reinicio = input ("\n¿Quieres jugar otro partido? (S/N): ")
  if reinicio == "S":
    i1 = i2 = 0
    menu()
  else:
    print ("Fin del partido")
    exit()
    

print ("\nPARTIDO DE TENIS: ")
menu()

