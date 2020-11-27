from tkinter import *
from tkinter import messagebox

#--------------FUNCIONES
def infoAdicional():
    messagebox.showinfo("Procesador de Cristhian","Procesador de texto 2019")
   # messagebox.showerror("procesador de texto","Procesador de texto")
    #messagebox.showwarning("procesador de texto","Procesador de texto")
def avisoLicencia():
    messagebox.showwarning("Licencia","Procesador de texto licencia expiro")
def salir():
   # valor = messagebox.askquestion("Salir","Deseas salir")#ventana emergente de pregunta si o no

    valor = messagebox.askokcancel("Salir","Deseas salir")

    # if valor=="yes":
    #     root.destroy()
    if valor==True:
        root.destroy()
def cerrarDoc():
    valor = messagebox.askretrycancel("Reintentar","No es posible cerrar el docuemnto")
    if valor ==False:
        root.destroy()
#-------------------DISEÑP
root =Tk()
barraMenu = Menu(root)

root.config(menu=barraMenu,width=700,height=300)
root.resizable(0,0)

#-----------crea la opcion de menu
archivoMenu= Menu(barraMenu,tearoff=0)
#-------------las opciones de menu archivo
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como ...")
archivoMenu.add_separator()#agrega un separador
archivoMenu.add_command(label="Cerrar",command=cerrarDoc)
archivoMenu.add_command(label="Salir",command=salir)

editarMenu= Menu(barraMenu,tearoff=0)

editarMenu.add_command(label="Copiar")
editarMenu.add_command(label="Cortar")
editarMenu.add_command(label="Pegar")


herramientasMenu= Menu(barraMenu,tearoff=0)
ayudaMenu= Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia",command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de...",command=infoAdicional)

#---------------ponemos en la ventana los menus
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Editar",menu=editarMenu)
barraMenu.add_cascade(label="Herramientas",menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)



root.mainloop()