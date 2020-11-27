import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor= miConexion.cursor()

# miCursor.execute('''
#       CREATE TABLE PRODUCTOS(
#           ID INTEGER PRIMARY KEY AUTOINCREMENT, 
#           NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#           PRECIO INTEGER,
#           SECCION VARCHAR(50)
#       )

#  ''')
# productos= [
#     ("Computador",20000,"Tecnologia"),
#     ("Celular",200,"Tecnologia"),
#     ("Zapatos",14,"Calzado"),
#     ("Lavadora",203,"Hogar")
# ]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)

#miConexion.commit()

miCursor.execute("SELECT * FROM PRODUCTOS  WHERE PRECIO<=200")#consulta

productos=miCursor.fetchall()
print(productos)

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=45 WHERE ID=1")#UPDATE

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=2")

miConexion.commit()

miConexion.close()