num=int(input("Digite um número:"))
for x in range(0,num+1):
    for y in range(x):
        print(y, end=" ")
    print()