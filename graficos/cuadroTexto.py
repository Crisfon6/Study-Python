from tkinter import *

raiz=Tk()

miFrame = Frame(raiz, width ="1200",height="800")
miFrame.pack()
Nombre = Entry(miFrame)#caudro de texto
Nombre.grid(row=1,column=1)#divde la ventana por una cuadricula

Label(miFrame,text="Nombre",padx=150).grid(row=1,column=0,sticky="e")

Apellido = Entry(miFrame).grid(row=2,column=1)
Label(miFrame,text="Apellido",pady=40).grid(row=2,column=0,sticky="e")


Edad= Entry(miFrame)
Edad.grid(row=3,column=1)
Edad.config(fg="red",justify="center")
Label(miFrame,text="Edad",padx=100,pady=100).grid(row=3,column=0,sticky="e")

Apellido = Entry(miFrame)
Apellido.grid(row=4,column=1)
Apellido.config(show="*")
Label(miFrame,text="Password",pady=40).grid(row=4,column=0,sticky="e")

Apellido = Entry(miFrame)
Apellido.grid(row=4,column=1)
Apellido.config(show="*")
Label(miFrame,text="Password",pady=40).grid(row=4,column=0,sticky="e")

raiz.mainloop()