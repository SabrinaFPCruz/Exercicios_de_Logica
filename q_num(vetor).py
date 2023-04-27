A=[]
cont=0
for a in range(5):
    A.append(float(input("Digite um numero:")))
x=float(input("Digite um valor: "))
for b in range(5):
    if x==A[b]:
        cont+=1
print("O valor:", x, "apareceu",cont, "vezes, dentro do vetor")