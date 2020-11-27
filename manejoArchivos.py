from io import  open

# archivo_text =  open("archivo.txt","w")#w crea el archivo puede escribir pero solo una unica vez

# frase = "EStupendo dia para estudiar python \nEl jueves"

# archivo_text.write(frase)

#archivo_text =  open("archivo.txt","r")#te permite leer un archivo

#texto = archivo_text.read()#te lo almacena en un string
#lineasTexto  = archivo_text.readlines()#te lo almacena en una lista


#archivo_text.close()
#print(texto)
#print(lineasTexto)

# archivo = open("archivo.txt","a")#abre en mode append para agregar

# archivo.write("\nnuevo dia para seguir aprendiendo")
# archivo.write("\nnuevo dia para seguir aprendiendo")
# archivo.close()

#archivo = open("archivo.txt","r")
#print(archivo.read())#esto deja el puntero en la ultima posicion
#archivo.seek(8)#ME deja desplazar el puntero a una posicion en este caso la posicion 0
#print(archivo.read(3))#lee desde hasta la posciion del puntero en este caso hasta la 3


archivo = open("archivo.txt","r+")#lectura y escrituras

lineasTexto = archivo.readlines()

lineasTexto[2] = "ESto es agregado\n"

archivo.seek(0)

archivo.writelines(lineasTexto)

archivo.close()