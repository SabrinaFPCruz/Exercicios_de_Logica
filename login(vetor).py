nomes=[]
senhas=[]
cont=0

for a in range(3):
    nomes.append(input("Digite seu nome: "))
    senhas.append(input("Digite a senha: "))
loginNomes=input("Digite seu login: ")
loginSenha=input("Digite sua senha: ")
for b in range(3):
    if loginNomes==nomes[b] and loginSenha==senhas[b]:
        print("Login efetuado")
        break
    else:
        cont+=1
if cont==5:
    print("Usuário não encontrado")
