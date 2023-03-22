# Estudiante: Felipe Leal A.
# G69 - 21 / 03 / 2023
# Módulo 1 - Semana 2
# DESAFÍO GUIADO - CACHIPUN

# DESARROLLO 


import sys
import random

opciones = ['piedra', 'papel','tijera']
jugador_humano = sys.argv[1] # Usuario ingresa alguna de las opciones desde a terminal.
jugador_computador = random.choice(opciones) # Computador escoge alguna opción al azar

# Parafernalia propia...
print("__________________________")
print("\nJUEGO DEL CACHIPÚN")
print("__________________________\n")


print(f"- Tú jugada, humano: {jugador_humano.upper()}\n- La jugada del computador: {jugador_computador.upper()}\n")


# 1. opción GANAR
if jugador_humano == 'piedra' and jugador_computador == 'tijera':
    print(f"GANASTE HUMANO!")
elif jugador_humano == 'tijera' and jugador_computador == 'papel':
    print(f"GANASTE HUMANO!")
elif jugador_humano == 'papel' and jugador_computador == 'piedra':
    print(f"GANASTE HUMANO!")
# 2. opción PERDER
elif jugador_humano == 'piedra' and jugador_computador == 'papel':
    print(f"GANÓ LA MÁQUINA :(")
elif jugador_humano == 'tijera' and jugador_computador == 'piedra':
    print(f"GANÓ LA MÁQUINA :(")
elif jugador_humano == 'papel' and jugador_computador == 'tijera':
    print(f"GANÓ LA MÁQUINA :(")
# 3. opción EMPATE
elif jugador_humano == jugador_computador: 
    print(f"WOW, EMPATE!")
# 4. Aviso por si hay algo inesperado    
else: 
    print("Algo salió mal. Asegúrate de escribir bien y con minúsculas tu opción: papel, piedra o tijera.")


print("\n__________________________")
print("\nFIN")
print("__________________________\n")

# Espero que esté bien el ejercicio. Gracias y saludos!