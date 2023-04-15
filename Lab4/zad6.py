def poteng(a,b):
    if (b==1):
        return a
    if b%2 ==0:
        s=poteng(a,int(b/2))
    else:
        return a * poteng(a,b-1)
print(poteng(2,50))