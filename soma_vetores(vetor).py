A=[]
B=[]
C=[]
tamanho_vetor=int(input("Qual tamanho deseja que seu vetor tenha: "))
for a in range(tamanho_vetor):
    A.append(int(input("Digite um numero: ")))
    B.append(int(input("Digite outro numero: ")))

for c in range(tamanho_vetor):
    C.append(A[c]+B[c])

print(A)
print(B)
print(C)