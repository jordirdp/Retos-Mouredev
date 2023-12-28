"""
Crea un programa que calcule quien gana más partidas al piedra,
papel, tijera, lagarto, spock.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
  "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
- Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
- Debes buscar información sobre cómo se juega con estas 5 posibilidades.

MODIFICADO A PIEDRA, PAPEL, TIJERA TRADICIONAL
"""

from random import *

def tirada(repeticiones):
    player = computer = 0
    for jugadas in range(repeticiones):
        opcion = int(input ("¿Qué eliges? (1, 2 o 3):  "))
        diccionario = {1:"🗿", 2:"📄", 3:"✂️"}
        pc = randint(1,3)

        if opcion == pc:
            solucion = "empate"
        elif opcion == 1 and pc == 2:
            solucion = "YO GANO"
            computer += 1
        elif opcion == 2 and pc == 3:
            solucion = "YO GANO"
            computer += 1
        elif opcion == 3 and pc == 1:
            solucion = "YO GANO"
            computer += 1
        else:
            solucion = "TU GANAS"
            player += 1

        print (nombre, "= ", diccionario[opcion], "  ||   PC = ", diccionario[pc], "  ->  ", solucion)
    jugadas += 1

    print ("\nRESULTADO: ", nombre, "= ", player, "  ||  Computer = ", computer)



print ("\n*** BIENVENIDO AL JUEGO PIEDRA 🗿, PAPEL 📄 O TIJERA ✂️  ***\n")
nombre = input("Introduce tu nombre: ")
numero = int(input ("\nHola "+nombre+ ". ¿A cuántas rondas quieres jugar?: "))
print ("Cada vez que pulses 1 🗿, 2 📄 o 3 ✂️  , estás eligiendo tu tirada")
tirada(numero)