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

def MultiMatrix(m1,m2):
    wm1=len(m1)
    km1=len(m1[0])
    wm2=len(m2)
    km2=len(m2[0])
    if wm1==km2 and km1==wm2:
        m3=[]
        for i in range(wm1):
            pom=[]
            w=0
            for j in range(wm1):
                for c in range(km2):
                    w+=[j][c]*m2[c][j]
                pom.append(w)
            m3.append(pom)
        return m3

a = createTwoDimArray(5,4)
b = createTwoDimArray(4,5)
