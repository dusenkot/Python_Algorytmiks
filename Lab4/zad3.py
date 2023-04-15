def sil(m,n):
    if n==1:
        return m
    elif n>0:
        return m+sil(m,n-1)
print(sil(12,12))