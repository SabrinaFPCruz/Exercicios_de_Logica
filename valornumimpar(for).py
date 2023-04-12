num=int(input("Digite um número:"))
soma=0
for x in range(1,num+1):
    if x%2!=0:
        soma=soma+1
    print(soma)