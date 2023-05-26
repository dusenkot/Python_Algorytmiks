def sort(T):
    n=len(T) 
    for i in range(n-1):
        k=i
        for j in range(i+1,n):
            if T[j]<T[k]:
                k = j
        T[i],T[k] =T[k],T[i]
    return T
lista=[13, 15, 2, 71, 8, 4, 6]
wynik = sort(lista)
print(wynik)