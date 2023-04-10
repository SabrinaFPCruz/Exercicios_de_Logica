time1 = input("Digite o nome do 1° time: ")
num_Gol1 = int(input("Quantos gols esse time fez? "))
time2 = input("Digite o nome do 2° time: ")
num_Gol2 = int(input("Quantos gols esse time fez? "))
if num_Gol1 != num_Gol2:
    if num_Gol1 > num_Gol2:
        print("O", time1,"é o ganhador")
    else:
        print("O", time2, "é o ganhador")
else:
    print("Empate")
