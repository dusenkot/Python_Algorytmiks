def nwd_r2(a, b):
    if a == b :
        return a
    elif a>b :
        return nwd_r2(a-b, b)
    else:
        return nwd_r2(a, b-a)
print(nwd_r2(24,36))