from os import listdir
from os.path import isfile, isdir



def ls1():
    return [obj for obj in listdir() if isfile(obj)]

archivos=ls1()
archivosFinal=[]
for i in archivos:
    if "Desencriptado.txt" in i:
        1
        #print("Este no ",i)
    elif "Encriptado.txt" in i:
        1
        #        print("Este no ",i)
    elif ".txt" in i :
        archivosFinal.append(i)
#        print(i)
#    else:
#        print(i)
    #tmp=i.split(".")

for i in archivosFinal:
    print(i)
#print(archivosFinal)
