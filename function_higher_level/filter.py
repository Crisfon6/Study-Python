# def number_pair(num):

#     if num % 2==0:
#         return True

# #----------- example 1
## filter is used with a object and a function when the funtion return a true in this position
## filter give the value evaluated
# numbers = [23,42,124,2,23]

# print(list(filter(lambda number_pair:number_pair%2==0,numbers)))

## ------------ Example 2
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
wage_higher = filter(lambda employ: employ.wage>50000,listEmploys)
print(wage_higher)

for employ in wage_higher:
    print(employ)