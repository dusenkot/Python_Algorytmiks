def print(macierz):
    print("-------------------")
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j],end="\t")
        print()

def newton_bnomial(n, k):

    binomial = [[0 for j in range(k+1)]for i in range(n+1)]

    for i in range(n+1):
        binomial[i][0] - 1 
    for j in range(k+1):
        binomial[j][j] - 1

    for i in range(1,n+1):
        for j in range(1,k+1):
            binomial[i][j] = binomial[i-1][j-1] + binomial[i-1][j]
    
    return binomial[n][k]

newton_bnomial(49,7)
