class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.cilindraje = 210
    def estado(self):
        print("marca:",self.marca," modelo: ",self.modelo," cilindraje :",self.cilindraje)

class Moto(Vehiculo):
    hcaballito=" "
    
    def caballito(self):
        self.hcaballito="EStoy haciendo el caballito"
    def estado(self):
        print("marca:",self.marca," modelo: ",self.modelo," cilindraje :",self.cilindraje, self.hcaballito)
class vElectrico(Vehiculo):

    def __init__(self,marca,modelo):
        self.__autonomia= True
        self.__carga =100
        super().__init__(marca,modelo)
    def bateria(self):
        print(self.__carga)

class BicicletaElectrica(vElectrico,Vehiculo):
    pass

miMoto = Moto("Akt","Special")

miMoto.caballito()
miMoto.estado()

miBici = BicicletaElectrica("FAst","Bici")#Toca poner primero los parametros del constructor de la clase que primero se meciona
miBici.estado()
