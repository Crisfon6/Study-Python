import re

# cadena = "VAamos a aprender expresiones  aprender regulares"

# #print(re.search("aprender",cadena))

# textobuscar ="aprender"

# # if re.search(textobuscar,cadena) is not None:
# #     print("HE encontrado el texto")
# # else:
# #     print("no he encontrado el texto")

# textoEncontrado = re.search(textobuscar,cadena)

# print(textoEncontrado.start())
# print(textoEncontrado.end())
# print(textoEncontrado.span())
# print(re.findall(textobuscar,cadena))

listaNombre = ['Ana',"Maria Martin","Sandra Lopez","Santiago martin","Sandra Perez"]

for elemento in listaNombre:
    #if re.findall('^Sandra',elemento):#esto busca todos los que tengan de comienzo sandra
   # if re.findall('^Sandra',elemento):#esto busca todos los que tengan de comienzo sandra#esto busca todos los que tengan de Fin martin
    if re.findall('[Ppa]',elemento):#esto busca todos los que tengan la p
        print(elemento)