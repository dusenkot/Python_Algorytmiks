def znajdz_pierwsza_parzysta(A):
    for liczba in A:
        if liczba % 2 == 0:
            return liczba
    return None
n = 10
A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]
w = znajdz_pierwsza_parzysta(A)
print(w)  # powinno wypisać 4
