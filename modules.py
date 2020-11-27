import datetime#get date

from datetime import timedelta,date

import fmath


print(datetime.date.today())

print(datetime.timedelta(minutes=80.2))

print(date.today())

print(fmath.add(1,2))

from colorama import Fore, Back, Style,init
init(convert=True)
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

one = input("Ingresa 1 :")
two = input("ingresa 2 :")
if one == two:
    print("Son iguales")
