import sys
from random import randint
from os import system
import datetime                              
import random

system("clear")
print("") 
print("\033[1;31mBY: \033[1;33mD³M⁰")
print("\033[1;33m≧◉◡◉≦")

print("")
system("bash logo")
print("")
system("bash coler")
system("sleep 1")
print("")
print("        \033[1;32m-----> \033[1;34mBIN 418238 \033[1;32m<------")
system("sleep 2")

cantidad = input("        \033[1;37mGen: ")
print("")
print("     \033[1;31m-------------------------------")
print("            \033[1;36mBIN       | FECHA | CVV ")
print("     \033[1;31m-------------------------------")

bin_format = "418238402xxxxxxx"

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
  month = str(randint(3, 12))
  current_year = str(now.year)                                               
  year = str(random.randint(23, 27))
  date = month + "/" + year

  return date

def main():
  for i in range(int(cantidad)):                
    cc = generar_cc(bin_format)
    f = open('Crunchy.txt', "a+")
    f.write(f'{cc} | {dategen()} | 0000\n')
    f.close()
    print(f"     \033[1;37m{cc} \033[1;36m| \033[1;37m{dategen()} \033[1;36m| \033[1;37m0000")
main()

print("")
print("     \033[1;33mPara crear una cuenta crunchyroll")
print("     \033[1;33mCon gmail nuevo, navegador limpio")
print("     \033[1;33mNo es necesario crear la cuenta con vpn")
print("     \033[1;33mA la hora de agregar la cc prende vpn")
print("")
system("sleep 2")
print("     \033[1;32m------------------")
print("     \033[1;37m    Metodo #1")
print("     \033[1;32m------------------")
print("     \033[1;37mUSAR VPN SINGAPUR (PAGO SINGAPUR)")
print("     \033[1;36mCVV  :   \033[1;37m0000")
print("     \033[1;36mZIP CODE: \033[1;37m00000")
print("")
print("")
print("     \033[1;32m------------------")
print("     \033[1;37m    Metodo #2")
print("     \033[1;32m------------------")
print("     \033[1;37mUSAR VPN ISRAEL (PAGO ISRAEL)")
print("     \033[1;36mCVV  :   \033[1;37m0000")
print("     \033[1;36mZIP CODE: \033[1;37m00000")
print("")
volver = input("     \033[1;37mPresione Enter para volver...")

if volver == "":
    system("python Super_gens.py")
else:
    exit()
