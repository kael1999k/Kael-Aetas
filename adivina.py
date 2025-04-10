import random

numero_secreto = random.randint(1, 10)

print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número del 1 al 10... ¿Cuál crees que es?")

intento = int(input("Escribe tu número: "))

if intento == numero_secreto:
    print("¡Correcto! Adivinaste el número.")
else:
    print("Incorrecto. El número era", numero_secreto)
