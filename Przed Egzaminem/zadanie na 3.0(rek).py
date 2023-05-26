def function(n):
    if n == 0:
        return 1  
    return function(n - 1) + 2 * n  
for n in range(5):
    wyraz =function(n)
    print(wyraz)

