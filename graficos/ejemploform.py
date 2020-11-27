from tkinter import *

ventana = Tk()
ventana.resizable(0,0)
ventana.iconbitmap("icono.ico")
ventana.config(bg="#D0FA96")
miFrame = Frame(ventana,width = "1000",height="800")
miFrame.config(bg="#A9E951")
miFrame.pack()

minombre = StringVar()

nombre = Label(miFrame,text="Nombre :")
nombre.grid(row=1,column=1,sticky="e",padx=10,pady=10)
nombreUser = Entry(miFrame,width=61,textvariable=minombre)
nombreUser.grid(row=1,column=2,sticky="e",padx=10,pady=10)

contra = Label(miFrame,text="Contraseña :")
contra.grid(row=2,column=1,sticky="e",padx=10,pady=10)
contraUser = Entry(miFrame,width=61)
contraUser.grid(row=2,column=2,sticky="e",padx=10,pady=10)
contraUser.config(show="*")

cuatroText = Label(miFrame,text="Comentario :")
cuatroText.grid(row=3,column=1,sticky="e",padx=10,pady=10)
comentario = Text(miFrame,width=46,height=8)#cuadro texto
comentario.grid(row=3,column=2,padx=10,pady=10)

scrollVertical = Scrollbar(miFrame,command=comentario.yview)#construir un scroll y funciona en y 
scrollVertical.grid(row=3,column=3,sticky="nsew")#con la ultima adaptamos el scroll a todo lo escrito en el text

comentario.config(yscrollcommand=scrollVertical.set)#para que indique en todo momento el scroll donde estamos

def codigoBoton():
    minombre.set("Cristhian")


botonEnviar =Button(ventana,text="Enviar",command=codigoBoton)

#botonEnviar.grid(row=4,column=2,sticky="e",padx=10,pady=10)
botonEnviar.pack()

ventana.mainloop()


