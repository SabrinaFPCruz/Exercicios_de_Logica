num=[]
media=0
soma=0
cont=0

#Receber e adcionar valores a um vetor
for a in range(3):
        num.append(int(input("Digite um numero: ")))

#Mostrar valores pares da lista
for par in range(3):
        if num[par]%2==0:
                print(num[par], end=" ")
print()

menor=num[0]
maior=num[0]

#Mostrar o menor valor na lista
for b in num:
        if b < menor:
                menor=b

#Mostrar o maior valor na lista
for b in num:
        if b > maior:
                maior=b
print("O menor valor dentro do vetor é:",menor)
print("O maior valor dentro do vetor é:",maior)

#Fazer a média entre os valores da lista
for d in range(3):
        soma+=num[d]
        media=soma/3
print("Está é a média entre os números:",media)

#Mostrar quantos dos valores da lista são iguais ou maiores a média entre eles
for e in range(3):
        if media<=num[e]:
                cont+=1
print("Existem",cont,"valores, maiores que a media", media)