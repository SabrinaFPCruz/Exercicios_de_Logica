tDentro=0
tFora=0
for x in range(10):
    num=int(input("Digite um número:"))
    if num >=10 and num <=20:
        tDentro=tDentro+1
    elif num >=20:
        tFora=tFora+1
print(tDentro)
print(tFora)
