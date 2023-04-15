list=[100,45,22,200,68,56,1000]
x=list[0]

for i in list:
    if x>i:
        x=i
print(x)
a=0
b=len(list)
for i in range(1,b):
    if list[i]<list[a]:
        a=i
print(a+1)



3



