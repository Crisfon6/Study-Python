import sqlite3
#----------------SE TRABAJO CON SQLITE
miConexion=sqlite3.connect("Ejemplo1")#Crea base de datos 

miCursor= miConexion.cursor()#se crea el cursor

# qCreate = "CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(15),PRECIO INTEGER,SECCION VARCHAR(20))"
# qInsert = "INSERT INTO PRODUCTOS VALUES('BALON',25000,'DEPORTES')"
# #miCursor.execute(qcreate)
# #miCursor.execute(qInsert)

# variosProductos=[
#     ("Camiseta",10,"Deportes"),
#     ("Cama",100,"Hogar"),
#     ("Camion",10,"Jugetes")
# ]
# miConexion.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)#insertar varios

# miConexion.commit()#ESto es para confirmar los cambios en la bd

#obtener registros
qSelect = "SELECT * FROM PRODUCTOS"
miCursor.execute(qSelect)
variosProductos=miCursor.fetchall()#lista con todo 

print(type(variosProductos))

print(variosProductos)

for i in variosProductos:
    print("Nombre :",i[0]," Seccion :",i[2])

miConexion.commit()


miConexion.close()