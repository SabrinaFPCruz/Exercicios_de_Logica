G = 5,80
E = 4,90
tCombustivel= input("Qual o tipo de combustível(G=Gasolina e E=Etanol): ")
if tCombustivel in "GgEe":
    qLitros = float(input("Quantos litros você deseja? "))
    if tCombustivel in "Gg":
        print(qLitros*5.80)
    else:
        print(qLitros*4.90)
else:
        print("Combustível inválido")