def poteng(a,b):
    if (b==1):
        return a
    else:
        return a * poteng(a,b-1)
print(poteng(2,50))