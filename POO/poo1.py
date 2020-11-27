class Car():
    
    def __init__(self):#constructor
        self.__longChasis = 250
        self.__widthChasis = 120
        self.__wheel = 4 #encapsule this no allow be accesed from out class
        self.__move = False

    def run(self,action):
        self.__move =action
        if(action):
            checked =  self.__check()
        if(self.__move and checked):

            print("car in movement")
        elif(self.__move and checked==False):
            print("Problem in the check")
        else:
            print("car stop")

    def status(self):
      print("The car have {} wheels".format(self.__wheel))
    
    def __check(self):
        print("Checking.....")
        return True

myCar = Car()
myCar.run(False)
# myCar.__wheel =2
# myCar.status()