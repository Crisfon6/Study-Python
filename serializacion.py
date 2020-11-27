import pickle
#en la wen se vina mejor 1 y 0 asi que se serializa poner a 1 y 0 

listaNombre= ["Pedro","juan","Carlos","Mario"]

ficheroBinario = open("listaNombre","wb")#b es para binario

pickle.dump(listaNombre,ficheroBinario)#esto vuelca los datos para guardado binario

ficheroBinario.close()

del(ficheroBinario)