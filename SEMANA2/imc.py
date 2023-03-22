# Estudiante: Felipe Leal A.
# G69 - 21 / 03 / 2023
# Módulo 1 - Semana 2
# DESAFÍO GUIADO - IMC

# DESARROLLO 

import sys # Se importa librería para trabajar desde consola, tal como se solicita.

peso = sys.argv[1]
altura = sys.argv[2]

# se chequea si valores ingresados son dígitos, y de ser así, se convierten en int:
if peso.isdigit() and altura.isdigit():
    peso = int(sys.argv[1])
    altura = int(sys.argv[2])/100
# Sin no son dígitos, se entrega aviso y se sale del programa.
else:
    print("Ingrese sólo números.")
    sys.exit()

# Fórmula IMC.
imc = peso / (altura **2 )

# Parafernalia propia...
print("__________________________")
print("\nÍNDICE IMC")
print("__________________________\n")


# Se entregan resultados en consola.
print(f"- Su peso es: {peso} kg.\n- Su altura es: {altura} mt.")
print(f"Su IMC es: {imc:.2f} kg/m2.\n")

# De acuerdo a aplicación de fórmula, se aplican condicionales para saber en qué grupo clasifica.
if imc < 18.5:
    print("Usted está BAJO PESO según la OMS.")
elif imc >= 18.5 and imc < 25:
    print("Usted está en un PESO ADECUADO según la OMS.")
elif imc >= 25 and imc < 30:
    print("Usted está en SOBREPESO según la OMS.")
elif imc >= 30 and imc < 35:
    print("Usted está en OBESIDAD GRADO I según la OMS.")
elif imc >= 35 and imc < 40:
    print("Usted está en OBESIDAD GRADO II según la OMS.")
elif imc > 40:
    print("Usted está en OBESIDAD GRADO III según la OMS.")
else:
    print("Algo salió mal.\n")

print("\n__________________________")
print("\nFIN")
print("__________________________\n")

# Espero que esté bien el ejercicio. Gracias y saludos!