import sys
from random import randint
from os import system
import datetime                              
import random

system("clear")
print("")
print("\033[1;32mT\033[1;37m------------------------------------------\033[1;32mT")
print("")
print(" ><<< ><<<<<<   ><<      ><<       ><<")   
print("      ><<        ><<    ><<     ><<   ><<")
print("      ><<         ><< ><<      ><<")       
print("\033[1;31m      ><<           ><<        ><<")       
print("      ><<           ><<        ><<")       
print("\033[1;34m      ><<           ><<         ><<   ><<")
print("      ><<    ><<    ><<     ><<   ><<<<")  
print("")
print("\033[1;32mT\033[1;37m------------------------------------------\033[1;32mT")
print("")
print("          \033[1;31m----------------------")
print("          \033[1;31m|   \033[1;32mBy: \033[1;36mDemo-Hacks   \033[1;31m|")
print("          \033[1;31m|   \033[1;35mTlg: \033[1;36m@Demo593    \033[1;31m|")
print("          ----------------------")
print("")
cantidad = input("\033[1;33m[•]Generar : \033[1;37m")
print("")

bin_format = "424094xxxxxxxxxx"

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
  month = str(randint(1, 12))
  current_year = str(now.year)                                               
  year = str(random.randint(23, 32))
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
    f = open('T.Y.C.txt', "a+")
    f.write(f'CARD : {cc} \nFECHA: {dategen()} \nCVV  : {ccv_gen()}\n\n')
    f.close()
    print(f"\033[1;32mCARD : \033[1;37m{cc}")
    print(f"\033[1;32mFECHA: \033[1;37m{dategen()}")
    print(f"\033[1;32mCVV  : \033[1;37m{ccv_gen()}\n")
main()

print("")
print("\033[1;36mNOTA: \033[1;37mSACAR EXTRAS <==")
print("")

nombre = input("\033[1;36mDesea generar un nombre random (y/n): ")

if nombre == "y":
    system("python generador.py")
else:
    exit()

print("")
print("\033[1;32m+\033[1;37m-----------------------------------------\033[1;32m+")
print("\033[1;35mMetodo opcional : copia los 4 numeros pares")
print("despues de \033[1;36m424094 \033[1;35m, y pegalo en un generador")
print("ej. \033[1;36m424094\033[1;33m6802\033[1;37mxxxxxx \033[1;35masi y generalo todo RND")
print("luego escoje una cc , remplaza los ultimos 4")
print("numeros por x, coje  su fecha y generala")
print("ej. \033[1;36m424094\033[1;33m6802\033[1;37m54xxxx \033[1;35m06/26 <=====")
print("por ultima vez sea gen o live para agregar en")
print("Tidal,Canva,Scribd IP=BELGICA Youtube IP=USA") 
print("\033[1;32m+\033[1;37m-----------------------------------------\033[1;32m+")

print("")
volver = input("\033[1;37mPresione Enter para volver...")

if volver == "":
    system("python Gens_v2-0.py")
else:
    exit()
