class Coche():

    def __init__(self):
        self.__largo = 250
        self.__ancho = 23
        self.__ruedas = 4#Encapsular
        self.__enMarcha= False
    #self es igual al this de java 
    def arrancar(self):
        self.__enMarcha=True
        print("el vehiculo arranco")
    def arrancar2(self, arrancamos):
        self.__enMarcha = arrancamos
        if self.__enMarcha==True:
            print("Arrancamos")
            self.__cambiarLlantas()
            print(self.__ruedas)
    
    def __cambiarLlantas(self):
        self.__ruedas = 2

miCoche = Coche()
miCoche.largo = 220
miCoche.arrancar()
print(miCoche.largo)
miCoche.arrancar2(True)

 