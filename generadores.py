#Estrcuturas que extraen valores de una funcion y se almacenan en objetos iterables
#Si solo lo vamos a usar esa vez 
#SE crea no mas hasta que lo use yield
def numers(limite):
    num =1
    while num < limite:
        yield num*2
        num+=1

devolver = numers(10)
#print(next(devolver))

for i in devolver:
    print(i)

#YIELD FROM 
#con for 
def devuelveCiudades(*ciudades):#recibe numero indeterminados de elementos y los coje como tupla
    
    for elements in ciudades:
        #con for se puede hacer pero yielfrom simplifica esto
    #     for subElements in elements:
    #         yield subElements
        yield from elements



ciudades = devuelveCiudades("Madrid", "valencia", "Bilbao","MAllorca")

print(next(ciudades))
print( next(ciudades))

