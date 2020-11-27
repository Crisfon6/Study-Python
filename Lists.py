deoList = [1,"hello",1.35,True,[1,2,3]]
colors = ['red']
listas = list((1,2,3,4))
print(deoList)
print(listas)

r =list(range(1,11))
print(r)
print(len(deoList))
print(deoList[1])

print(2 in deoList)# si existe en la list
deoList[len(deoList)-1] = "nuevo"
print(deoList)

colors.append("RED")
colors.extend(["green", "coffe"])
colors.extend(("green", "coffe"))
print(colors)

colors.insert(3,"agregado")
print(colors)

colors.pop()#quita el ultimo
colors.pop(0)
print(colors)

colors.remove("agregado")
print(colors)

#colors.clear()#limpia la lista
#print(colors)
colors.sort(reverse=True)
print(colors)

print(colors.index("RED"))#INDICE

print(colors.count('RED'))