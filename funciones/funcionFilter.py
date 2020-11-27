"""
LAS FUNCIONES FILTER SON FUNCIONES DE ORDEN SUPERIOR
PARA USAR EL PARADIGMA FUNCIONAL
ESTA FUNCION : VERIFICA QUE LOS ELEMETNOS DE UNA SECUENCIA CUMPLEN UNA CONDICIION
    DEVOLVIENDO UN ITERADOR CON LOS ELEMENTOS QUE CUMPLEN DICHA CONDICION
"""
"""
def numeroPar(num):
    if num%2==0:
        return True
   """ 
numeros =[17,24,7,39,8,51,92]

print(list(filter(lambda numero:numero%2==0,numeros)))#filter nos devuelve los elementos que cumplen con lo de la funcion numeroPar