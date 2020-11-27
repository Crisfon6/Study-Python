import pickle


class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.cilindraje = 210
    def estado(self):
        print("marca:",self.marca," modelo: ",self.modelo," cilindraje :",self.cilindraje)

coche1 = Vehiculo("akt","Especial")
coche2 = Vehiculo("Honda","TTR")
coche3 = Vehiculo("BMW","1000")

coches = [coche1,coche2,coche3]

fichero = open("ListaCoches","wb")

pickle.dump(coches,fichero)

del(fichero)

ficheroApertura = open("ListaCoches","rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

print(misCoches)
for c in misCoches :
    print(c.estado())



