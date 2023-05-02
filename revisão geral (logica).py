#programa que mostre na tela "Hello Word"
print("Hello Word")

#programa que solicite o nome do usuário e depois mostre o nome na tela
nome=input("Digite seu nome: ")
print(nome)

#programa para ler o nome de uma pessoa, a sua idade e o seu salário e mostre essas informações na tela.
name=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
salario=float(input("Digite seu salário: "))
print("Seu nome é:",name,"sua idade é",idade,"e seu salário é:",salario)

#algoritmo que receba 2 notas e calcule a média aritmética
n1=float(input("Digite um nota: "))
n2=float(input("Digite outra nota: "))
media=(n1+n2)/2
print(media)

#Ler 2 números, efetuar as 4 operações matemáticas e mostrar os resultados.
n_1=float(input("Digite um número: "))
n_2=float(input("Digite um número: "))
soma=n_1+n_2
subt=n_1-n_2
mult=n_1*n_2
divi=n_1/n_2
print("Essa é o resultado da soma: ",soma)
print("Essa é o resultado da subtração: ",subt)
print("Essa é o resultado da multiplicação: ",mult)
print("Essa é o resultado da divisão: ",divi)

#Crie um algoritmo que armazene esses dois valores nessas duas variáveis, e efetue a troca dos valores
A=5
B=10
x=0

x=A
A=B
B=x

#algoritmo que leia a idade de uma pessoa e diga em qual ano ela nasceu
idade=int(input("Digite a sua idade: "))
ano=int(input("Digite o ano: "))
nascimento=ano-idade
print(nascimento)

#Escreva um programa que recebe uma temperatura em Fahrenheit e converte para Celsius
temp_F=int(input("Qual a temperatura do ambiente?(em Fahrenheit) "))
temp_C=(temp_F-32)*(5/9)
print("A temperatura em Fahrenheit é:", temp_F,", logo em Celsius é:", temp_C)

#programa que recebe um tempo dado em segundos e calcula quantos dias, horas, minutos e segundos ele representa
seg=int(input("Digite o número total de segundo? "))
minutos=seg//60
horas=minutos//60
dias=horas//24
print("Este numero:",seg,", representa:",seg,"segundos,",minutos,"minutos,",horas,"horas, e",dias," dia(s).")

#A locadora de carros SAI DA FRENTE está fazendo uma promoção e está alugando carros no período junino por R$ 30,00 a
# diária. Além disso, a locadora cobra R$ 0,01 por quilômetro rodado. Como é período de São João, a locadora quer fidelizar
# os clientes e está dando 10% de desconto no valor total do aluguel de qualquer carro.

dias=int(input("Quantos dias a você ficou com o carro?(1 a 30) "))
km=int(input("Quantos quilômentros você andou?(1 a 1000) "))
desconto=10
v_Total=(dias*30+km*0.01)*0.90
print(f'Você ficou com o carro por {dias} dias e andou por {km} km, logo você terá que pagar: R$ {v_Total:,.2f}')



"""------------ESTRUTURA DE REPETIÇÃO------------"""


#Receba 2 números do usuário e mostre eles em ordem crescente
num_1=int(input("Digite um número: "))
num_2=int(input("Digite um número: "))
if num_1>num_2:
    print(num_1,num_2)
else:
    print(num_2,num_1)

#receba as 3 notas de um aluno e verifique se ele está aprovado, em recuperação ou reprovado.
nota1=float(input("Digite uma nota: "))
nota2=float(input("Digite uma nota: "))
nota3=float(input("Digite uma nota: "))
media_nota=(nota1+nota2+nota3)/3
if media_nota>=7:
    print("Aprovado")
elif media_nota>=4:
    print("Recuperação")
else:
    print("Reprovado")

#Receba um número, do usuário e diga se ele é par ou ímpar
n=int(input("Digite um número: "))
if n%2==0:
    print("O número é par")
else:
    print("O número é ímpar")

#algoritmo que leia um número diferente de zero e diga se este número é positivo ou negativo
num=int(input("Digite um numero: "))
if num !=0:
    if num>0:
        print("Esse número",num, "é maior que zero")
    else:
        print("Esse número é menor que zero")
else:
    print("Erro, digite um número diferente de zero")


#algoritmo que receba 3 números e informe qual o maior entre eles.
num1=int(input("Digite um número: "))
num2=int(input("Digite um número: "))
num3=int(input("Digite um número: "))
if num1>num2 and num1>num3:
    print(num1)
if num2>num3 and num2>num1:
    print(num2)
if num3>num1 and num3>num2:
    print(num3)


"""------------COMANDOS DE REPETIÇÃO-----------"""


#Ler uma variável de numero inteiro e mostrar a tabuada desse número.
numero=int(input("Digite um número: "))
for x in range(1,11):
    print("A tabuada de", numero, "Vezes ", x, "é:",numero * x, " \n ")

#receba um nome de uma pessoas e mostre letra por letra
nomes=input("Digite seu nome: ")
for letra in nomes:
    print(letra)

#Faça um programa que mostre na tela, a contagem de 1 ate 10
for contagem in range(1,11):
    print(contagem)

#imprima os números de 1 (inclusive) a 10 (inclusive) em ordem crescente.
for ordem in range(1,11):
    print(ordem, end=" ")

#imprima os números de 1 (inclusive) a 10 (inclusive) em ordem crescente.
for ordem in range(9,-1):
    print(ordem, end=" ")

#Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive).
number=int(input("Digite um numero: "))
while number<=0:
    number = int(input("Digite um numero: "))
    for contador in range(1,number+1):
        print(contador)

#Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.
cont=0
for i in range(10):
    valor=int(input("Digite um número: "))
    if valor<0:
        cont+=1
print(cont)

#Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.
media_range=0
soma_range=0
for soma_media in range(10):
    valor=float(input("Digite uma nota: "))
    soma_range+=valor
media_range=soma_range/10
print(media_range)

#(WHILE)Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.
cont=0
soma=0
while cont>10:
    num=int(input("Digite um numero: "))
    soma+=num
    cont+=1
media=soma/10
print(media)

#Faça um código que receba o número de alunos de uma sala de aula e depois solicite as notas desses alunos,
#no final, mostre a média aritmética da turma.

soma=0
num_Alunos=int(input("Quantos alunos existem na sala? "))
for alunos in range(num_Alunos):
    notas_alunos=float(input("Digite a nota do aluno: "))
    soma+=notas_alunos
media=soma/num_Alunos
print(media)

#Faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo valor recebido
"""caso o segundo valor digitado, seja zero, solicite
novamente o valor, informando que só
aceitaremos valores diferentes de zero"""

n_1=float(input("Digite um valor:"))
n_2=float(input("Digite outro valor: "))
while n_2 <=0:
    n_2 = float(input("Valor errado, digite novamente outro valor: "))
    div=n_1//n_2
    print(div)

#Escreva um código para ler as notas da 1a. e 2a. avaliações de um aluno, calcule e imprima a média desse aluno.
resp="Ss"
while resp in "Ss":
    nota1=float(input("Digite a nota: "))
    while nota1 <0 or nota1 >10:
        nota1=float(input("Nota invalida, digite novamente: "))
    nota2=float(input("Digite a nota: "))
    while nota2<0 or nota2>10:
        nota2=float(input("Nota invalida, digite novamente: "))
media=(nota1+nota2)/2
print(media)
resp=input("Deseja realizar outro calculo? ")


"""------------VARIAVEIS COMPOSTAS------------"""

#Perguntar ao usuário quantos alunos tem na sala e criar um array, unidimensional
#com o nome de todos os alunos da sala
aluno=[]
alunos=int(input("Quantos alunos existem na sala? "))
for a in range(alunos):
    aluno.append(input("Digite o nome do aluno: "))
    print(a,aluno[a])
a_luno=input("Digite o nome do aluno a ser pesquisado: ")
for alu in range(alunos):
    if a_luno == aluno[alu]:
        print(aluno[alu])
        break
    else:
        print("Aluno não encontrado")
        break

#Escreva um código que permita a leitura das notas de uma turma de 5 alunos e
#guarde num vetor, Calcular a média da turma e contar quantos alunos obtiveram
#nota acima desta média calculada. Escrever a média da turma e o resultado da contagem
cont=0
soma=0
notas=[]
for a in range(5):
    notas.append(float(input("Digite uma nota: ")))
    soma+=notas[a]
media=soma/5
for b in range(5):
    if notas[b]>=media:
        cont+=1
print(f'A media da turma é: {media} e {cont} possuem a nota maior ou igual a media')

#Ler um vetor A de 10 números. logo em seguida, ler mais um número e guardar em uma variável X.
A=[]
M=[]
for a in range(10):
    A.append(int(input("Digite um numero: ")))

"""Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X."""
x=int(input("Digite o multiplicador: "))
for b in range(10):
    M.append(A[b]*x)
print(A)
print(x)
print(M)

#Faça um código para ler 20 números e armazenar em um vetor
num=[]
for a in range(20):
    num.append(int(input("Digite um numero: ")))
for b in range(19,-1,-1):
    print(num[b])

#Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array diferente
nomes=[]
senhas=[]
cont=0
for a in range(5):
    nomes.append((input("Cadastre seu nome: ")))
for b in range(5):
    senhas.append(float(input("Cadastre sua senha: ")))
nome_login=input("Digite seu nome: ")
senha_login=float(input("Digite sua senha: "))
for c in range(5):
    if nome_login != nomes[c] and senha_login==senhas[c]:
        print("Login efetuado com sucesso")
        break
    else:
        cont+=1
if cont==5:
    print("Cadastro não encontrado")

#Faça um código para ler um valor N qualquer (que será o tamanho dos vetores).
# Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma
A=[]
B=[]
Soma=[]
N=int(input("Qual tamanho dos vetores? "))
for a in range(N):
    A.append(int(input("Digite um numero: ")))
for b in range(N):
    B.append(int(input("Digite um numero: ")))
for c in range(N):
    Soma.append(A[c]+B[c])
print(A)
print(B)
print(Soma)

#Faça um código para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas
#vezes esse número aparece no vetor.
num=[]
cont+=1
for a in range(10):
    num.append(int(input("Digite um numero: ")))
x=int(input("Digite um número: "))
for b in range(10):
    if x==num[b]:
        cont+=1
print(cont)

#Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela
nome=[]
for i in range(5):
    nome.append(input("Digite um nome: "))
print(nome)

"""o programa deve mostrar também os nomes na ordem inversa"""
for j in range(4,-1,-1):
    print(nome, end=" ")

#algoritmo que leia 30 valores do tipo inteiro e armazene-os em um vetor
valores=[]
soma=0
cont=0
for a in range(30):
    valores.append(int(input("Digite um valor: ")))

"""todos os números pares que existem no vetor"""
for b in range(30):
    if valores[b]%2==0:
        print(valores[b])

"""o menor e o maior valor existente no vetor"""
maior=valores[0]
menor=valores[0]
for c in range(30):
    if c>maior:
        maior=c
for d in range(30):
    if d<menor:
        menor=d
print(maior)
print(menor)

"""quantos dos valores do vetor são maiores que a média desses valores"""
for e in range(30):
    soma+=valores[e]
    media=soma/30

for f in range(30):
    if valores[f]>=media:
        cont+=1
print(cont)
