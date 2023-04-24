lista_compras=["banana", "laranja", "maça"]
for i in lista_compras:
    print(i)

alunos=[]
num_alunos=0
num_alunos=int(input("Quantos alunos existem na sala?"))
for i in range(num_alunos):
    alunos.append(input("Digite o nome do aluno:"))

for y in range(num_alunos):
    print(alunos[y],y)

verif_vetor=input("Digite o nome de um aluno:")
for x in range(num_alunos):
    if verif_vetor==alunos[x]:
        print("O nome:", alunos[x],x)

notas=[]
soma=0
cont=0
for i in range(5):
    notas.append(int(input("Digite a nota:")))
for x in range(5):
    soma+=notas[x]
media=soma/5
print(media)
for y in range(5):
    if media>=notas[y]:
        cont+=1
print(cont)

A=[]
M=[]
for i in range(10):
    A.append(int(input("Digite um numero: ")))
x=int(input("Digite o multiplicador dos numeros: "))
for j in range(10):
    M.append(A[j]*x)
print(A)
print(x)
print(M)

numeros=[]
for i in range(5):
    numeros.append(int(input("Digite um número: ")))
for j in range(4,-1,-1):
    print(numeros[j])
