from tkinter import *
from tkinter import filedialog


root = Tk()

def abreFichero():
    #fichero = filedialog.askopenfile(title="Abrir")#devuelve la ruta
   # fichero = filedialog.askopenfile(title="Abrir",initialdir="C:")#initialdir sirve para decirle desde donde se pparara a buscar
    fichero = filedialog.askopenfile(title="Abrir",initialdir="C:",filetypes=(("Ficheros de Excel","*.xls"),
        ("Ficheros python","*.py"),("Todos los ficheros","*.*")))
    print (fichero)

Button(root,text="Abrir fichero",command=abreFichero).pack()
root.mainloop()