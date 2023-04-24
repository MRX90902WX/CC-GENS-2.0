import sys
from random import randint
from os import system
import datetime                              
import random

system("sleep 1")
cantidad = input(" \033[1;37mGen: ")
print("")
print(" \033[1;31m---------------------------------")
print("        \033[1;36mBIN       | FECHA | CVV |")
print(" \033[1;31m---------------------------------")

bin_format = "53915046xxxxxxxx"

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

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 16:
    for i in range(15):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc

def dategen():
  now = datetime.datetime.now()                            
  date = ""                                                                  
  month = str(randint(3, 9))
  current_year = str(now.year)                                               
  year = str(random.randint(23, 28))
  date = month + "/" + year

  return date

def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv


def main():
  for i in range(int(cantidad)):                
    cc = generar_cc(bin_format)
    f = open('LIONST1.txt', "a+")
    f.write(f'{cc} | {dategen()}  | {ccv_gen()}\n')
    f.close()
    print(f" \033[1;37m{cc} \033[1;36m| \033[1;37m{dategen()}  \033[1;36m| \033[1;37m{ccv_gen()} \033[1;36m|")
main()

print("")
print("\033[1;36m🌐IP: ARGENTINA [🇦🇷]")
print("🔖Codigo Postal: 1425")
print("")
volver = input("\033[1;37mPresione Enter para volver...")

if volver == "":
    system("python Gens_v2-0.py")
else:
    exit()
