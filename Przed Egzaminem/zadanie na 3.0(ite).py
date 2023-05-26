def fun_iteracyjna(n):
    wynik = 1  
    
    for i in range(1, n+1):
        wynik = wynik + 2 * i
    return wynik

for n in range(5):
    wynik5 = fun_iteracyjna(n)
    print(wynik5)