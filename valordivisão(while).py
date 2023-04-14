valor1=float(input("Digite o primeiro valor: "))
valor2=float(input("Digite o segundo valor: "))
while valor2 == 0:
    print("Numero invalido, digite novamente")
    valor2=float(input())
resultado=valor1/valor2
print(resultado)
