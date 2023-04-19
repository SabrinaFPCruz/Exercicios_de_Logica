sele_opcao=5
while sele_opcao!=6:
    n1=float(input("Digite o primeiro número: "))
    n2=float(input("Digite o segundo número: "))
    while True:
        sele_opcao = input("O que deseja fazer com os números: ")
            match sele_opcao:
                case 1:
                    soma=n1+n2
                    print(soma)
                case 2:
                        subtr=n1-n2
                        print(subtr)
                case 3:
                        mult=n1*n2
                        print(mult)
                case 4:
                        divi=n1/n2
                        print(divi)
                case 5:
                        break
                case 6:
                    resp=6
                    break
