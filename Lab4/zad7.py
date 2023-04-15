def BinToIntHorner(tekst, x):
    wynik=ord(tekst[0])-48
    n=len(tekst)
    for i in range(1,n):
        wynik=wynik*x+ord(tekst[i])-48
    return  wynik
def hornerIntto16(tekst, x):
    lista="0123456789ABCDEF"
    wynik=lista.find(tekst[0])
    n=len(tekst)
    for i in range(1, n):
        wynik=wynik*x+lista.find(tekst[i])
    return wynik
def hornerRek(tekst, x):
    if(len(tekst)==1):
        return ord(tekst[0])-48
    else:
        return x*hornerRek(tekst[0:len(tekst)-1],x)+ord(tekst[len(tekst)-1])-48
def hornerRek16(tekst, x):
    lista="0123456789ABCDEF"
    if(len(tekst)==1):
        return lista.find(tekst[0])
    else:
      return x*hornerRek16(tekst[0:len(tekst)-1],x)+lista.find(tekst[len(tekst)-1])
print(BinToIntHorner("200",4))
print(hornerIntto16("ABC",16))
print(hornerRek("200",4))
print(hornerRek16("ABC",16))