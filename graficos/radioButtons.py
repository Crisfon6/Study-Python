from tkinter import *

root = Tk()

varOpcion = IntVar()

def imprimir():
    if  varOpcion.get() == 1:
        print("Eres un hombre")
        etiqueta.config(text="Eres macho")
    else:
        print("Eres una mujer")
        etiqueta.config(text="Eres hembra")

Label(root,text="Genero").pack()

Radiobutton(root,text="Masculino",variable=varOpcion,value=1,command=imprimir).pack()

Radiobutton(root,text="Femenino",variable=varOpcion,value=0,command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()