#-*- coding: utf-8 -*-

def comprobar(solu, columna, fila2):


    for j in range(fila2):
        if columna == solu[j]:
            #print("Verticalmente {},{} choca".format(columna,fila2))
            return False
    for i in range(fila2):
        if solu[i]-i == columna-fila2 or solu[i]+i == columna+fila2:
            #print("La diagonal de {},{} choca con {},{}".format(solu[i],i,columna,fila2))
            return False

    return True

def imprimirTablero(solu, nDatos):
    #Formato unicamente
    print("  ", end ="")
    for k in range(1, nDatos+1):
        print("{} ".format(k), end = "")
    print("")
    #-----------------------
    for i in range(nDatos):
        print("{} ".format(i+1), end ="") #solo formato
        for j in range(nDatos):
            if solu[i] == j :
                print( "Q " , end = "")
            else:
                print("* ", end = "")
        print("{}  ({},{})".format(i+1, solu[i]+1, i+1)) #para dar formato insertando un salto de linea
    #Formato unicamente
    print("  ", end ="")
    for k in range(1, nDatos+1):
        print("{} ".format(k), end = "")
    print("")
    #-----------------------

def colocarReina(solu, fila, nReinas):

    if fila==nReinas: #caso base
        imprimirTablero(solu, nReinas)
        print("") #Para que no se vea pegada a la siguiente solucion
    for i in range(nReinas):
        if comprobar(solu, i, fila):
            solu[fila] = i
            #print("Solucion incluida: ", end = "") solo para probar
            #print(solu[0:fila+1]) solo de prueba
            colocarReina(solu, fila+1, nReinas)



#FUNCION PRINCIPAL------------
if __name__ == "__main__":
    solucion = []
    nReinas = int(input("Cuantas reinas desea colocar: "))

    for i in range(nReinas):
        solucion.append(-1)

    colocarReina(solucion, 0, nReinas)
