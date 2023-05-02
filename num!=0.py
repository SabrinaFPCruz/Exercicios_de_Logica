resp="Ss"
n1=int(input("Digite um numero:(Diferente de zero) "))
while resp=="Ss":
    n1=int(input("Número inválido, digite novamente: "))
    if n1 >0:
        print(f'O número {n1},é positivo')
    elif n1<0:
        print(f'O numero {n1}, é negativo')
    else:
        print("Número inválido")

    resp=input("Deseja realizar um novo calculo?(s/n) ")
