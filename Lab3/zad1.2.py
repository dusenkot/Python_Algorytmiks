import random
def createTwoDimArray(m,n): # n,m= wierz kolunna
    lista= []
    for i in range(m):
        pom=[]
        for j in range (n):
            pom.append(random.randint(-20,50))
        lista.append(pom)
    return lista

def createTwoDimArray2(m,n):
    lista = [[random.randint(-20, 50)for i in range(n)] for j in range(m)]
    return lista

def printTwoDimArray(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end='\t')
        print()

def FindMaxElemt(lista):
    MyMax = lista[0][0]
    for a in lista:
        for liczba in a:
            if liczba>MyMax:
                MyMax=liczba
    return MyMax

def findPozMaxElement(lista):
    myMax=lista[0][0]
    wiersz=0
    kokumna =0 
    for a in range (len(lista)):
        for j in range(len(lista[a])):
            if lista[a][j] > myMax:
                myMax = lista[a][j]
                wiersz = a 
                kokumna = j
    return myMax, wiersz , kokumna

def MultiByNumber(lista,liczba):
    for a in range (len(lista)):
        for j in range(len(lista([a]))):
            lista[a][j]=lista[a][j]*liczba
    return lista



macierz1 = createTwoDimArray2(10,10) 
macierz = createTwoDimArray(10,10) 
printTwoDimArray(macierz)
print(macierz1)
wynik = findPozMaxElement(macierz)
print(wynik)
print("Max element: ", FindMaxElemt(macierz))