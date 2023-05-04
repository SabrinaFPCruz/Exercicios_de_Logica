x=0
cont=0
A=[]
while True:
    if x % 2 != 0:
        A.append(x)
        cont+=1
    x+=1
    if cont==10:
        break
print(A)