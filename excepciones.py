def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("no se puede dividir entre 0")
    
    except:
        print("Ha ocurrido un error")
    finally:#Se ejecuta siempre
        print("Gracias vuelve pronto")

while True:
    
        op1 = input("Inrese ")
        op2 = input("Ingrese")
        break
    

print(divide(op1,op2))

print("Finalizado")