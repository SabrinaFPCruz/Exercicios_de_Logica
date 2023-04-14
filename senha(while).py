pin="123"
tentativas=1
senha=input("Digite a senha: ")
while senha !=pin:
    tentativas = tentativas + 1
    senha=input("Incorreta, tente novamente: ")
    if tentativas>2 and senha !=pin:
        print("Senha bloqueada")
        break
else:
    print("Acesso Liberado")
