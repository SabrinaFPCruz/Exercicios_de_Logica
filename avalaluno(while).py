novoCal="Ss"
while novoCal in "Ss":
    n1 = float(input("Digite a primeira nota:"))
    while n1 > 10 or n1 <0:
        n1=float(input("Nota errada, digite novamente: "))
    n2=float(input("Digite a segunda nota: "))
    while n2>10 or n2<0:
        n2=float(input("Nota errada, digite novamente: "))
    media=(n1+n2)/2
    print(media)
    novoCal=input("Deseja fazer um novo calculo?(s/n)")
