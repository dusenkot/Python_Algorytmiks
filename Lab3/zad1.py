import random
def createTwoDimArray(m,n): # n,m= wierz kolunna
    lista= []
    for i in range(m):
        pom=[]
        for j in range (n):
            pom.append(random.randint(-20,50))
        lista.append(pom)
    return lista
        
def printTwoDimArray(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end='\t')
        print()

macierz = createTwoDimArray(5,7)
printTwoDimArray(macierz)