import random
import os
from colorama import Fore, Style

# Leer nombres y apellidos desde archivos de texto
with open("nombres.txt") as f:
    nombres = f.read().splitlines()

with open("apellidos.txt") as f:
    apellidos = f.read().splitlines()

# Generar nombres y apellidos aleatorios
resultados = []
for i in range(1):
    nombre_aleatorio = random.choice(nombres)
    apellido_aleatorio_1 = random.choice(apellidos)
    resultado = nombre_aleatorio + " " + apellido_aleatorio_1
    resultados.append(resultado)

# Mostrar resultados
for resultado in resultados:
    print(f"{Fore.CYAN}{resultado}{Style.RESET_ALL}")
