import random
liczba_zer = 0
l = 0
p = 1023
a=[]
x=1023
while x >0:
    a.append(random.randit(0,1))
    x-=1
while l <= p:
    s = (l + p) // 2
    if a[s] == 1:
        p = s - 1
    else:
        liczba_zer += (s - l + 1)
        l = s + 1

print(liczba_zer)
