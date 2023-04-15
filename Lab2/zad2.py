
def funkcja(list):
    list = [100, 45, 22, 200, 68, 56, 1000, 223, 54, 12]
    minimalne = list[0]
    maximalne = list[0]
    for i in list:
        if minimalne > i:
            minimalne = i
    for i in reversed(list):
        if maximalne < i:
            maximalne = i
    roz=maximalne-minimalne
    return  roz


roz=funkcja(list)
print("roztep jest:",roz)











