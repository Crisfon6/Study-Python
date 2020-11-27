def funct_decorator(funct):
    def function_inside(*args,**kwargs):
        print("Go make a calculus")
        funct(*args,**kwargs)
        print("End")
    return function_inside

@funct_decorator
def sum(num1,num2):
    print(num1+num2)
@funct_decorator
def rest(num1,num2):
    print(num1-num2)
@funct_decorator
def potent(base,exponent):
    print(pow(base,exponent))
sum(10,2)
potent(base=2,exponent=3)