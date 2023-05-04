resp="s"
while resp == "s" or resp=="S":
    anos=int(input("Digite quantos anos de vida você tem: "))
    mes=int(input("Digite quantos meses de vida você tem: "))
    dia=int(input("Digite quantos dias de vida você tem: "))
    dias_vivos=(anos*365)+(mes*30)+dia
    print(dias_vivos)
    resp=input("Deseja realizar um novo calculo? (s/n) ")