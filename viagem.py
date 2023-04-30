
print("-------------Opções-------------\n"
      "(1) Região Norte\n"
      "(2) Região Nordeste\n"
      "(3) Região Centro-Oeste\n"
      "(4) Região Sul")
viagem=int(input("Para aonde voce deseja viajar? "))
viagemRetorno=input("Deseja incluir passagem de volta? ")
if viagemRetorno in "Ss":
    if viagem==1:
        print("A viagem custará: R$ 900")
    if viagem==2:
        print("A viagem custará: R$ 650")
    if viagem==3:
        print("A viagem custará: R$ 600")
    if viagem==4:
        print("A viagem custará: R$ 550")
else:
    if viagem == 1:
        print("A viagem custará: R$ 500")
    if viagem == 2:
        print("A viagem custará: R$ 350")
    if viagem == 3:
        print("A viagem custará: R$ 350")
    if viagem == 4:
        print("A viagem custará: R$ 300")