
import math
def evaluaEdad(edad):
    if edad<0:
        raise TypeError("No se perdmiten edades negativas")#lanzar exepciones
    else:
        print("tiene ",edad," años")

#evaluaEdad(-10)


def raiz(num):
    if num<0:
        raise ValueError("NO puede ser negativo")
    else:
        return math.sqrt(num)
try:
    raiz(-12)
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)

