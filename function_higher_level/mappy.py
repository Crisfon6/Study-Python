#function map apply a function a each object of a interable
#

class Employ:
    def __init__(self,name,level,wage):
        self.name = name
        self.level = level
        self.wage  = wage
    def __str__(self):
        return "{} work like {} won a wage of ${}".format(self.name,self.level,self.wage)

listEmploys = [
    Employ("CRisthian","master",50000),
    Employ("Prometeo","CEO",20000),
    Employ("POLO","CTO",80000),
    Employ("Mid","master",45000)

]
def commision(employ):
    employ.wage = employ.wage*1.03
    return employ

listEmploysCommision = map(commision,filter(lambda employ: employ.wage>=50000,listEmploys))
for i in listEmploysCommision:
    print(i)