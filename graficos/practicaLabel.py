from tkinter import *

root = Tk()

miFrame = Frame(root,width=1080,height=720)

miFrame.pack()

#miLabel= Label(miFrame,text="Buenos dias estamos aprendiendo python")
#miLabel.pack()#Si dejamos el pack nos va redimensionar todo a las dimensiones del texto sustituir por place

#miLabel.place(x=100,y=200)

Label(miFrame,text="Buenos dias estamos aprendiendo python",fg="green",font=("Arial Black",18)).place(x=100,y=200)
miImagen = PhotoImage(file="cat.gif")
Label(miFrame, image=miImagen).place(x=100,y=250)

root.mainloop()