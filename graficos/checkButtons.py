from tkinter import *

raiz = Tk()

raiz.iconbitmap("icono.ico")
raiz.title("CheckButton")

foto = PhotoImage(file="avion.gif")
Label(raiz,image=foto).pack()

frame = Frame(raiz)
frame.pack()
Label(frame,text="Elija su destino").pack()

playa = IntVar()
perritos = IntVar()
gatitos = IntVar()

def opcionesViaje():

    opcionEscogida =""
    if playa.get()==1:
        opcionEscogida+="Playa "
    if perritos.get()==1:
        opcionEscogida+="Perritos "
    if gatitos.get()==1:
        opcionEscogida+="Gatitos "

    textoFinal.config(text=opcionEscogida)
    
        


Checkbutton(frame,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Perritos",variable=perritos,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Gatitos",variable=gatitos,onvalue=1,offvalue=0,command=opcionesViaje).pack()
textoFinal = Label(raiz)
textoFinal.pack()

raiz.mainloop()