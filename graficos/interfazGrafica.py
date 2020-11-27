from tkinter import *

# #existen mas
# #WxPython
# #PyQT
# #PyGTK
#si le agregamos una w al final de la extencion "pyw" windows la abrira normal 


raiz = Tk()

raiz.title("Pruebas")

raiz.iconbitmap("icono.ico")#icono


#raiz.geometry("650x350")#tamaño ventana
#la raiz siempre se va adaptar a su contenedor interno

#raiz.resizable(0,0)#Recibe dos para parametros boolean No deja redimensionar la ventana

raiz.config(bg="green")#con esto podemos hacer varias cosas en este caso cambiar el color del fondo

miFrame = Frame()#creo el frame y toca meter el frame en la raiz o sea la ventana

miFrame.pack()#con esto metemos el frame en la ventana
#miFrame.pack(side="bottom")#side sirve para ponerlo en una posicion

#miFrame.pack(side="left",anchor="n")#anchor posiciona tambien pero con los puntos cardinales su primera letra

#miFrame.pack(fill="x")#rellenado x
#miFrame.pack(fill="y",expand=1)#rellenado y
#miFrame.pack(fill="both",expand=1)#rellena proporcional a la ventana

miFrame.config(relief="groove")#borde

miFrame.config(cursor="hand2")#cursor

miFrame.config(bd=35)#tamaño borde

miFrame.config(bg="red")


miFrame.config(width = "650",height="350")

raiz.mainloop()#este metodo es para que se ejecute indefinidamente
