#raise is used for launch message custom for exeptions

def evaluateAge(age):
    if age<0:
        raise ZeroDivisionError("No allow negative age")
    if age>0:
        print("no error")

evaluateAge(-10)