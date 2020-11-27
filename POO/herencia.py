class Car():
    def __init__(self,mark,model):
        self.mark=mark
        self.model = model
        self.movement = False
        self.speedUp = False
    
    def run(self,value):
        self.movement=value
    def speedUp(self,value):
        self.speedUp =value
    def status(self):
        print("model {} \nmovement {} \nmark {} \nspeedUp {}".format(self.model,self.movement,self.mark,self.speedUp))

class Motorcicle(Car):
    hack =""
    def doHack(self):
        self.hack = "doing hack"
    def status(self):
        print("model {} \nmovement {} \nmark {} \nspeedUp {} \ndo hack {}".format(self.model,self.movement,self.mark,self.speedUp,self.hack))
    
class VehicleElectric(Car):
    def __init__(self,*args):
        super().__init__(*args)

        self.charge= 100
    def chargin(self):
        self.charge = True

class BiciElectric(VehicleElectric,Car):#inherenci multiple
    pass


# c = Motorcicle("maz","da")
# c.run(True)
# c.status()

bici = BiciElectric("boom","head")
bici.status()