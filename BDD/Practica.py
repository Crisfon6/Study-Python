from tkinter import *
from tkinter import messagebox
import sqlite3
#FUNCIONES
def conexion():
    miConexion = sqlite3.connect("GestionUsuarios")
    miCursor =miConexion.cursor()
    try:
        qcreate ="""
        CREATE TABLE USUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50) UNIQUE,
            CONTRA VARCHAR(80)           

                                    
        )"""
        miCursor.execute(qcreate)
    except sqlite3.OperationalError:
        messagebox.showinfo("Conexion","Conexion Exitosa")
    miConexion.commit()
    miConexion.close()
def salir():
    desicion = messagebox.askyesno("SALIR","Desea salir")
    if desicion:
        root.destroy()
def crear(valores):
    # print(valores)
    try:
        miConexion = sqlite3.connect("GestionUsuarios")
        miCursor =miConexion.cursor()    
        # insertusuario ="INSERT INTO USUARIOS VALUES(NULL,?,?)",valores
        #insertUsuario= "INSERT INTO USUARIOS VALUES(NULL,?,?)",valores
        miCursor.execute( "INSERT INTO USUARIOS VALUES(NULL,?,?)",valores)
    except sqlite3.IntegrityError :
        messagebox.showerror("CREAR","El nombre de usuario ya existe intente con otro")
    messagebox.showinfo("CREAR","Creacion de usuario exitosa")
    miConexion.commit()
    miConexion.close()

def leer(idLeer):
    global nombreIngresado,passwordIngresado
    miConexion = sqlite3.connect("GestionUsuarios")
    miCursor =miConexion.cursor()  
#    miCursor.execute("SELECT * FROM USUARIOS WHERE ID=?",idLeer)
    miCursor.execute("SELECT * FROM USUARIOS WHERE ID='{}'".format(idLeer))
    try:
        usuarios=miCursor.fetchone()
        
    
        nombreIngresado.set(usuarios[1])
        passwordIngresado.set(usuarios[2])
        messagebox.showinfo("LECTURA","Lectura exitosa!")
    except:
        messagebox.showerror("LECTURA","El usuario no existe en la base de datos")
    
    miConexion.commit()
    miConexion.close()

def actualizar(valores):
    miConexion = sqlite3.connect("GestionUsuarios")

    miCursor =miConexion.cursor()  
  
    actualizar = miCursor.execute("UPDATE USUARIOS SET NOMBRE='"+valores[0]+"', CONTRA='"+valores[1]+"'WHERE ID='{}'".format(valores[2]))
    if actualizar:
        messagebox.showinfo("ACTUALIZAR","Actualizacion completada")
    else:
        messagebox.showerror("ACTUALIZAR","Error al actualizar")
    miConexion.commit()
    miConexion.close()
    
    
def eliminar(valores):
    miConexion = sqlite3.connect("GestionUsuarios")

    miCursor =miConexion.cursor()  
    desicion =messagebox.askyesno("ELIMINAR","Esta seguro que desea eliminar")
    if  desicion:
        qdelete= "DELETE FROM USUARIOS WHERE ID='{}'".format(valores)
        miCursor.execute(qdelete)
   
    miConexion.commit()
    miConexion.close()
#---------------ventana y menu
root = Tk()
barraMenu = Menu(root)
root.config(menu=barraMenu,width=700,height=300)
root.resizable(0,0)


#-----------menu
archivoMenu = Menu(barraMenu,tearoff=0)


crudMenu = Menu(barraMenu,tearoff=0)



borrarMenu = Menu(barraMenu,tearoff=0)
#------opciones menu


archivoMenu.add_command(label="Nueva Conexion",command=conexion)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=salir)

crudMenu.add_command(label="Crear",command=lambda:crear([str(nombreIngresado.get()),str(passwordIngresado.get())]))
crudMenu.add_command(label="Leer",command=lambda:leer(int(idIngresado.get())))
crudMenu.add_command(label="Actualizar",command=lambda:actualizar([str(nombreIngresado.get()),str(passwordIngresado.get()),int(idIngresado.get())]))
crudMenu.add_command(label="Eliminar",command=lambda:eliminar(int(idIngresado.get())))


borrarMenu.add_command(label="Limpiar casillas")

#---LOS COLOCAMOS EN LA VENTAN
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)

#------------creacion frame
miFrame = Frame(root,width=400,height=600)
miFrame.pack()
Label(miFrame,text="Bienvenido a la practica").grid(row=1,column=1,padx=4,pady=4,columnspan=4)
miImagen = PhotoImage(file="cat.gif")
Label(miFrame,image=miImagen).grid(row=2,column=1,padx=10,pady=10,columnspan=4)

#---------------------------CREACION CAMPOS DE TEXTO
Label(miFrame,text="Nombre",padx=10,pady=10).grid(row=3,column=1,columnspan=2)
nombreIngresado=StringVar()
Nombre = Entry(miFrame,textvariable=nombreIngresado)
Nombre.grid(row=3,column=2,columnspan=2)


Label(miFrame,text="Contraseña",padx=10,pady=10).grid(row=4,column=1,columnspan=2)
passwordIngresado=StringVar()
password = Entry(miFrame,textvariable=passwordIngresado)

password.grid(row=4,column=2,columnspan=2)
password.config(show="*")

Label(miFrame,text="ID",padx=10,pady=10).grid(row=5,column=1,columnspan=2)
idIngresado=IntVar()
idUser = Entry(miFrame,textvariable=idIngresado)
idUser.grid(row=5,column=2,columnspan=2)


btnCrear = Button(miFrame,text="CREAR",width=15,bg="green",command=lambda:crear([str(nombreIngresado.get()),str(passwordIngresado.get())])).grid(row=6,column=1,pady=10)
btnLeer = Button(miFrame,text="LEER",width=15,bg="yellow",command=lambda:leer(int(idIngresado.get()))).grid(row=6,column=2,pady=10)
btnActualizar = Button(miFrame,width=15,text="ACTUALIZAR",bg="blue",command=lambda:actualizar([str(nombreIngresado.get()),str(passwordIngresado.get()),int(idIngresado.get())])).grid(row=6,column=3,columnspan=1,pady=10)
btnEliminar = Button(miFrame,width=15,text="ELIMINAR",bg="red",command=lambda:eliminar(int(idIngresado.get()))).grid(row=6,column=4,pady=10)
root.mainloop()