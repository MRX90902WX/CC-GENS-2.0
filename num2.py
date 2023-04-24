import sys
from random import randint
from os import system
import datetime
import random

num_format = "416392xxxx"

def esValido(num_tarjeta):
  suma = 0
  num_digitos = len(num_tarjeta)
  pos_par_impar = num_digitos & 1

  for i in range(0, num_digitos):
    digito = int(num_tarjeta[i])
    if not ((i & 1) ^ pos_par_impar):
      digito = digito * 2
    if digito > 9:
      digito = digito - 9
    suma = suma + digito

  return (suma % 10 == 0)

def generar_cc(num_format):
  num = ""
  if len(num_format) == 10:
    for i in range(9):
      if num_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        num += num_format[i]
        continue
      elif num_format[i] == "x":
        num += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(num_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = num + str(i)
      if esValido(verificador):
        num = verificador
        break
      else:
        verificador = num

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return num

def main():
  for i in range(1):
    num = generar_cc(num_format)
    print(f"+1 {num}")
main()
