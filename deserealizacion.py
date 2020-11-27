import pickle
#descodificar el archivo

fichero = open("listaNombre","rb")

lista = pickle.load(fichero)

print(lista)