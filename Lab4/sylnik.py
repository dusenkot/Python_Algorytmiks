def pisz(tekst, n ):
    for i in range(n):
        print(tekst)
def pisz_rek(tekst, n):
    if n>0:
        print(tekst)
        pisz_rek(tekst, n-1)


def silnia_iter(n):
    s=1
    for i in range(1, n+1):
        s=s*i
    return s

def silnia_rek(n):
    if n==0 or n==1:
        return 1
    else:
        return n*silnia_rek(n-1)
    
print(silnia_iter(10))
print(silnia_rek(10))