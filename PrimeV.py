from os import system

system("clear")
print("")
print("     \033[1;36m   ____  ____  ______  _________")
print("       / __ \/ __ \/  _/  |/  / ____/")
print("      / /_/ / /_/ // // /|_/ / __/")   
print("     / ____/ _, _// // /  / / /___")   
print("    /_/   /_/ |_/___/_/  /_/_____/")   
print("")
print("      _    __________  __________") 
print("     | |  / /  _/ __ \/ ____/ __ \ ")
print("     | | / // // / / / __/ / / / /")
print("     | |/ // // /_/ / /___/ /_/ /")
print("     |___/___/_____/_____/\____/")  
                             

print("\033[1;37m")
print("      ⠠⣀⠀⠀⠀⠀              ⠀⠠⠴⠶⣶⡄")
print("      ⠀⠈⠛⠶⣦⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠶⠀⣿⠁")
print("      ⠀⠀⠀⠀⠈⠙⠛⠿⢿⣿⣷⣶⣶⣶⣶⣶⣿⡿⠟⠛⠉⠁⠀⠐⠁")
print("")
print("")
print(" #1. BIN AUSTRALIA")
print(" #2. BIN CANADA")
print(" #3. BIN ALBANIA")
print(" #4. BIN MEXICO")
print("") 
main = input(" \033[1;32m----> ")
print("")

if main == "1":
   system("python chk1-au.py")
elif main == "2":
   system("python chk2-ca.py")
elif main == "3":
   system("python chk3-al.py")
elif main == "4":
   system("python chk4-mx.py")    
else:
   print("\033[1;34m[X]\033[1;31mOPCIÓN INCORRECTA")

