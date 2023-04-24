import sys
from random import randint
from os import system
import datetime
import random

system("clear")
print("")
print("\033[1;31mdb    db d888888b        d8888b. d888888b d8b   db")
print("\033[1;37m`8b  d8' `~~88~~'        88  `8D   `88'   888o  88")
print("\033[1;31m `8bd8'     88           88oooY'    88    88V8o 88")
print("\033[1;37m   88       88    C8888D 88~~~b.    88    88 V8o88")
print("\033[1;31m   88       88           88   8D   .88.   88  V888")
print("\033[1;37m   YP       YP           Y8888P' Y888888P VP   V8P")
print("")
print("                   \033[1;31m𝑽.\033[1;37m1.6  \033[1;32m◎[\033[1;36m°‿\033[1;36m°\033[1;32m]◎")
print("")
print("          \033[1;36m/* Nota: \033[1;37mIntenten asociar la cc")
print("                   \033[1;37ma Canva y Tidal")
print("")
print("")
print("\033[1;33mL=O=A\033[1;34m=D=I=\033[1;31mN=G ...")
system("sleep 3")
print("")

bin_format = "424094011632xxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #1\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37m{ccv_gen()}")
main()
print("\n")

bin_format = "424094000830xxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #2\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37m{ccv_gen()}")
main()
print("\n")

bin_format = "4240940340xxxxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #3\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37m{ccv_gen()}")
main()
print("\n")

bin_format = "4240940578xxxxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #4\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37m{ccv_gen()}")
main()
print("\n")

bin_format = "424094002574xxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #5\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37m{ccv_gen()}")
main()
print("\n")

bin_format = "489504252230xxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #6\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37m{dategen()}")
 print(f"\033[1;34mCVV : \033[1;37m{ccv_gen()}")
main()
print("\n")

bin_format = "534417377434xxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #7\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37m10/24")
 print(f"\033[1;34mCVV : \033[1;37m{ccv_gen()}")
main()
print("\n")

bin_format = "542539502305xxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #8\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37m04/25")
 print(f"\033[1;34mCVV : \033[1;37m{ccv_gen()}")
main()
print("\n")

bin_format = "542539501601xxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #9\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37m10/26")
 print(f"\033[1;34mCVV : \033[1;37m{ccv_gen()}")
main()
print("\n")

bin_format = "54253950160xxxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #10\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37mgnd")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()
print("\n")

bin_format = "424094044205xxxx"

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
  month = str(randint(1, 9))
  current_year = str(now.year)
  year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
  date = month + "/" + year

  return date


def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
 cc = generar_cc(bin_format)
 print("\033[1;31m=======\033[1;32mBIN #11\033[1;31m=======")
 print(f"\033[1;34mBIN : \033[1;37m{cc}")
 print(f"\033[1;34mFECHA : \033[1;37m11/25")
 print(f"\033[1;34mCVV : \033[1;37mgnd")
main()

print("")
print("\033[1;37mPARA LA SERIE 424094 PROBAR EN")
print("YOUTUBE IP=USA, TIDAL IP=BELGICA")
print("CANVA IP=BELGICA")
print("")
print("\033[1;37mPARA LA SERIE 542939 PROBAR EN")
print("YOUTUBE IP=USA, TIDAL IP=USA")
print("CANVA IP=USA")

print("")
nombre = input("\033[1;36mDesea generar un nombre random (y/n): ")

if nombre == "y":
    system("python generador.py")
else:
    exit()

print("")
volver = input("\033[1;37mPresione Enter para volver...")

if volver == "":
    system("python Super_gens.py")
else:
    exit()

