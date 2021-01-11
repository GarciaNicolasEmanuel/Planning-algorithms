import random

#Algoritmo FIFO 
def fifo(numpaginas,referencias,rangomin,rangomax):
    listaRef = crearReferencias(referencias,rangomin,rangomax)
    lista = []
    fallos=0
    print("Pagina........... p1  p2  p3 p4")
    for item in listaRef:
        if item not in lista:
            if len(lista)<numpaginas: 
                lista.append(item)
                fallos = fallos+1
                print("Referencia ",item," : ",lista, "Si")
            else:
                lista.pop(0)
                lista.append(item)
                fallos = fallos+1
                print("Referencia ",item," : ",lista, "Si")            
        else:  
             print("Referencia ",item," : ",lista,"No") 
               
    print("número de fallos:", fallos)
    rendimiento(fallos,referencias)

    
#Algoritmo LRU
def lru(numpaginas,referencias,rangomin,rangomax):
    listaRef = crearReferencias(referencias,rangomin,rangomax)
    lista = []
    antiguos = []
    fallos=0
    print("Pagina........... p1  p2  p3 p4... ...")
    for item in listaRef:
        if item not in lista:
            if len(lista)<numpaginas: 
                lista.append(item)
                antiguos.append(item)
                fallos = fallos+1
                print("Referencia ",item," : ",lista, "Si")
            else:
                valorantiguo = antiguos.pop(0)
                #print("Valor más antiguo:",valorantiguo)
                lista.insert(lista.index(valorantiguo),item)
                l=lista.pop(lista.index(valorantiguo))
                antiguos.append(item)
                fallos = fallos+1
                print("Referencia ",item," : ",lista, "Si")             
        else:  
             print("Referencia ",item," : ",lista,"No") 
             antiguos.remove(item)
             antiguos.append(item)
               
    print("número de fallos:", fallos)
    rendimiento(fallos,referencias)

#Algoritmo Óptimo
def optimo(numpaginas,referencias,rangomin,rangomax):
    listaRef = crearReferencias(referencias,rangomin,rangomax)
    lista = []
    fallos=0
    contador=0
    asignado=False
    siguientes = []
    posRef=0
    
    print("Pagina........... p1  p2  p3 p4... ...")
    for item in listaRef:
        if item not in lista:
            if len(lista)<numpaginas: 
                lista.append(item)
                fallos = fallos+1
                print("Referencia ",item," : ",lista, "Si")
            else:
                siguientes = listaRef[posRef:]
                for item2 in lista:
                   
                   if ((item2 not in siguientes)or(len(siguientes)/2<siguientes.index(item2)))and(asignado==False):
                       lista.insert(contador,item)  
                       l=lista.pop(contador+1)
                       asignado=True 
                   contador=contador+1   
                contador=0
                asignado=False          
                fallos = fallos+1
                print("Referencia ",item," : ",lista, "Si")              
        else:  
             print("Referencia ",item," : ",lista,"No") 
        posRef=posRef+1  
               
    print("número de fallos:", fallos)
    rendimiento(fallos,referencias)

#Calculo de eficacia.
def rendimiento(fallos,referencias):
    probFallo = fallos / referencias
    probNoFallo = 1-probFallo
    TEF = (probNoFallo*1)+(probFallo*(10001))
    print("El tiempo de eficacia es: ","{0:.2f}".format(TEF),"ms")
    


#Método para crear las referencias.
def crearReferencias(referencias,rangomin,rangomax):
    listaRef=[]

    for i in range(referencias):
        listaRef.append(random.randint(rangomin, rangomax))
    print (listaRef)
    return  listaRef 

#MAIN
lru(4,20,1,7)
fifo(4,20,1,7)  
optimo(4,20,1,7) 