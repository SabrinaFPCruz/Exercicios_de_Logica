nomes=[]
senhas=[]

for a in range(5):
    nomes.append(input("Digite seu nome: "))
    senhas.append(input("Digite a senha: "))
for b in range(5):
    print("Na posição:",b,"está o nome:", nomes[b], "e senha:",senhas[b])