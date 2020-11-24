from random import randint as azar

from os import listdir
from os.path import isfile,isdir


class RSA:
    def __init__(self,nombreArchivo):
        self.nombreDelArchivo=nombreArchivo
        self.n=0
        self.p=0
        self.q=0
        self.d=0
        self.e=0

        self.letras=[["a",1],["b",2],["c",3],["d",4],["e",5],["f",6],["g",7],["h",8],["i",9],["j",10],["k",11],["l",12],["m",13],["n",14],["ñ",15],["o",16],["p",17],["q",18],["r",19],["s",20],["t",21],["u",22],["v",23],["w",24],["x",25],["y",26],["z",27],
                ["A",28],["B",29],["C",30],["D",31],["E",32],["F",33],["G",34],["H",35],["I",36],["J",37],["K",38],["L",39],["M",40],["N",41],["Ñ",42],["O",43],["P",44],["Q",45],["R",46],["S",47],["T",48],["U",49],["V",50],["W",51],["X",52],["Y",53],["Z",54],
                [" ",55],["1",56],["2",57],["3",58],["4",59],["5",60],["6",61],["7",62],["8",63],["9",64],["10",65],["\n",66],["",67],["_",68]]

        self.numerosPrimos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,97]

        self.numero1=azar(0,len(self.numerosPrimos)-1)
        self.numerosPrimos.remove(self.numerosPrimos[self.numero1])
        self.numero2=azar(0,len(self.numerosPrimos)-1)

        self.p=self.numerosPrimos[self.numero1]

        #print(p)
        self.q=self.numerosPrimos[self.numero2]

        #print(q)
        #modulo de la llave publica y privada
        self.n=self.p*self.q

        #print(n)
        #pa sacar e
        self.phiN=(self.p-1)*(self.q-1)

#        print(self.phiN, "phin")
        self.mensajeNoAceptadoMostrado = False
        self.tengoUnSaltoDeLinea = False
        mensaje = RSA.leerArchivo(self.nombreDelArchivo+".txt")
        self.encriptar(mensaje)

    def sacarE(self,phi) -> int:
        #no puede ser 1  y tiene que ser menor que phiN
        e = 2
        while e < phi - 1:
            res = self.gcd(e, phi)
            if (res == 1):
    #            print("Comprobacion del valor de E :", gcd(a: e, b: phi)):
                return e
            e += 1


    def gcd(self,a,b)->int:
        i=1
        while(i<=a and i <=b):
            if(a%i==0 and b%i==0):
                gcdDato=i
            i=i+1
        return gcdDato


    #def sacarD()
    def calcularD(self,phiN, e):
        i = 0
        #numero entero con phiN que lo sustituye
        #PROBAR HASTA QUE NO SEA DECIMAL Y ya es la D
        #d = (k*Φ(n) + 1) / e for some integer k
        while (i<=100000000) :
             x = 1+(i*phiN)
             if(x%e == 0):
                d = x/e
                break
             i+=1
        return d

    #print(calcularD(2760,7))

    def regresarArreglo(self,palabra):
        contador=0
        for letra in palabra:
            if(contador==0):
                arreglo=[self.regresarLetra(letra)]
            else:
                arreglo.append(self.regresarLetra(letra))
    #            print(regresarLetra(letra), letra)
            contador+=1

        return (arreglo)


    def regresarLetra(self,letra):

        for i in self.letras:
            if not self.tengoUnSaltoDeLinea:
                #lo busca
                if(letra=="\\"):
                    print("encontro el /")
                    self.tengoUnSaltoDeLinea=True
                    return self.letras[len(self.letras)-2][1]
                elif (i[0] == letra):
                    return i[1]
            else:
                self.tengoUnSaltoDeLinea=False
                print("Entroo")
                if(letra=="n"):
                    return self.letras[len(self.letras)-3][1]


        if not self.mensajeNoAceptadoMostrado:
            print("El mensaje que encripta tiene caracteres no aceptados, seran remplazados por '-'")
            self.mensajeNoAceptadoMostrado=True
        return self.letras[len(self.letras)-1][1]

    def regresarNumero(self,numero):
        for i in self.letras:
            if(i[1]==numero):
                return i[0]



    def encriptar(self,mensaje):
        #llave publica
        self.e = self.sacarE(self.phiN)
        #coprimo de phiN, ambos tienen el maximo comun divisor el 1
        #d y e son congruentes
        #todo d=e^-1 mod n

        self.d=self.calcularD(self.phiN,self.e)

        arregloLetras=self.regresarArreglo(mensaje)
      #  print("e:",e, " n:",n," d:",d)
       # print("Encriptado")

        yaCreoArreglo=False
        for i in arregloLetras:
            if not yaCreoArreglo:
                #tenemos un numero i^e mod n (numeros primos)
                arregloEncriptado=[pow(i,self.e,self.n)]
                yaCreoArreglo=True
            else:

                arregloEncriptado.append(pow(i,self.e,self.n))

    #    for i in arregloEncriptado:
     #       print(i)

        #todo:subir al archivo encriptado
        stringSubirEncriptado =""
        stringSubirEncriptado+=str(self.n)+"\n"
        stringSubirEncriptado+=str(self.d)+"\n"
        print(len(arregloEncriptado))
        for i in (range(len(arregloEncriptado))):

             stringSubirEncriptado+=str(arregloEncriptado[i])+","

        try:
            subir=open(self.nombreDelArchivo+"Encriptado.txt","w",encoding="UTF-8")
        except IOError:
            print("No se puede abir ")
        else:
            subir.write(stringSubirEncriptado)
        subir.close()

        #print(stringSubirEncriptado)

        #todo leer archivo encriptado

        try:
            leerArchivo=open(self.nombreDelArchivo+"Encriptado.txt","r")
        except IOError:
            print("No se peude abrir ")
        else:
            print("leo")
            enQueLineaVamos=0
            for linea in leerArchivo:
                if(enQueLineaVamos==0):
                    n=linea.split("\n")
                    n.remove("")
                elif(enQueLineaVamos==1):
                    d=linea.split("\n")
                    d.remove("")
                else:
                    separar=linea.split(",")
                    separar.remove("")
                enQueLineaVamos+=1
            for i in range(len((separar))):
                separar[i]=int(separar[i])
            print(n[0])
            print(d[0])
            print(separar)
        #self.des(arregloEncriptado,self.n,self.d)
        dato=d[0]
        print(int(float(dato)))

        self.des(separar,int(n[0]),int(float(d[0])))





    def des(self,mensaje,llavePublicaN,llavePublicaD):
        stringMensaje=""
        for i in mensaje:
            #i^ n mod d
            stringMensaje+=self.regresarNumero((pow(i,int(llavePublicaD),int(llavePublicaN))))
      #  print(stringMensaje)
        try:
            subirDescencriptado=open(self.nombreDelArchivo+"Desencriptado.txt","w")
        except IOError:
            print("no se pudo ")
        else:
            subirDescencriptado.write(stringMensaje)
            subirDescencriptado.close()


    @staticmethod
    def leerArchivo(nombre):
        try:
            archivo=open(nombre,"r")
        except IOError:
            print("No se pudo abrir el archivo")
        else:
            stringRegreso="Archivo desencriptado\n"
            for linea in archivo:
#                print(linea)
                stringRegreso+=linea

            return stringRegreso
        archivo.close()



def buscarArchivos():
    return [obj for obj in listdir() if isfile(obj)]

def __main__():
    archivos=buscarArchivos()
    archivosFinal=[]
    for i in archivos:
        if "Desencriptado.txt" in i:
            1  # print("Este no ",i)
        elif "Encriptado.txt" in i:
            1  #        print("Este no ",i)
        elif ".txt" in i:
            archivosFinal.append(i)
    #        print(i)
    #    else:
    #        print(i)
    # tmp=i.split(".")

    for i in archivosFinal:
        print(i)
        nombre=i
        nombre=nombre.split(".")
        prueba=RSA(nombre[0])
    """
    nombre="archivo.txt"
    nombre=nombre.split(".")
    prueba =RSA(nombre[0])
    """

__main__()