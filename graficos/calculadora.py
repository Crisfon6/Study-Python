from tkinter import *

ventana= Tk()

miFrame =Frame(ventana)

miFrame.pack()

operacion = ""
ultimaOperacion =""
resultado = 0

#--------PANTALLA

numeroPantalla = StringVar()
pantalla = Entry(miFrame,textvariable=numeroPantalla)

pantalla.grid(row=1,column =1,padx=10,pady=10,columnspan=4)
pantalla.config(bg="black",fg="#30FF02",justify = "right")

#------------PULSIONES BOTONES
#------NUMEROS
def numeroPulsado(num):
   global operacion 
   global resultado
   global ultimaOperacion

   if operacion!="":
      numeroPantalla.set(num)
      ultimaOperacion = operacion
      
      operacion=""
      print(ultimaOperacion)
   else:
      numeroPantalla.set(numeroPantalla.get()+num)


   
def borrar():

   numeroPantalla.set("")
def suma(num):
   global operacion
   global resultado
   resultado += float(num)
   operacion ="suma"
   numeroPantalla.set(resultado)
def mult(num):
   global operacion
   global resultado
   resultado += float(num)
   operacion ="mult"
   numeroPantalla.set(resultado)
def div(num):
   global operacion
   global resultado
   resultado += float(num)
   operacion ="div"
   numeroPantalla.set(resultado)
def resta(num):
   global operacion
   global resultado
   resultado += float(num)
   operacion ="resta"
   numeroPantalla.set(resultado)
def igual():
   global resultado
   global ultimaOperacion
   if ultimaOperacion =="suma":
      numeroPantalla.set(resultado+float(numeroPantalla.get()))
   if ultimaOperacion =="resta":
      numeroPantalla.set(resultado-float(numeroPantalla.get()))
   if ultimaOperacion =="mult":
      numeroPantalla.set(resultado*float(numeroPantalla.get()))
   if ultimaOperacion =="div":
      numeroPantalla.set(resultado/float(numeroPantalla.get()))
   resultado =0
   operacion ="igual"

  

 





#------------BOTONES
#----FILA 1
boton7 = Button(miFrame,text="7",width=3,padx=10,pady=10,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8 = Button(miFrame,text="8",width=3,padx=10,pady=10,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9 = Button(miFrame,text="9",width=3,padx=10,pady=10,command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
botonDiv = Button(miFrame,text="/",width=3,padx=10,pady=10,command=lambda:div(numeroPantalla.get()))
botonDiv.grid(row=2,column=4)

#----FILA 2
boton4 = Button(miFrame,text="4",width=3,padx=10,pady=10,command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5 = Button(miFrame,text="5",width=3,padx=10,pady=10,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6 = Button(miFrame,text="6",width=3,padx=10,pady=10,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonMul = Button(miFrame,text="*",width=3,padx=10,pady=10,command=lambda:mult(numeroPantalla.get()))
botonMul.grid(row=3,column=4)

#----FILA 3
boton1 = Button(miFrame,text="1",width=3,padx=10,pady=10,command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2 = Button(miFrame,text="2",width=3,padx=10,pady=10,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3 = Button(miFrame,text="3",width=3,padx=10,pady=10,command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonRes = Button(miFrame,text="-",width=3,padx=10,pady=10,command=lambda:resta(numeroPantalla.get()))
botonRes.grid(row=4,column=4)

#----FILA 4
boton0 = Button(miFrame,text="0",width=3,padx=10,pady=10,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
botonComa = Button(miFrame,text=",",width=3,padx=10,pady=10,command=lambda:numeroPulsado("."))
botonComa.grid(row=5,column=2)



botonIgual = Button(miFrame,text="=",width=3,padx=10,pady=10,command=lambda:igual())
botonIgual.grid(row=5,column=3)


botonSuma = Button(miFrame,text="+",width=3,padx=10,pady=10,command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5,column=4)

#----FILA 5
botonBorrar= Button(miFrame,text="C",width=3,padx=10,pady=10,command=borrar)
botonBorrar.grid(row=6,column=1)
ventana.mainloop()