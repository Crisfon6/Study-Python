#AGREGA FUNCIONALIDADES
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args,**kwargs):#*args para pasar varios argumentos
        #**kwargs para pasar clave valor
        #Acciones adiccionales que decora (agrega)
        print("vamos a realizar un calculo")
        funcion_parametro(*args,**kwargs)
        #Acciones adicionales que decoran despues de ejecutar la anterior funcion
        print("hemos terminado el calculo")

    return funcion_interior



@funcion_decoradora#con esto especificamos que la suma sera decorada
def suma(num1,num2):
    print  (num1+num2)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base,potencia):
    print(base**potencia)


suma(7,5)
resta(12,10)
potencia(base=5,potencia=4)
