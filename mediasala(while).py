contNotas=0
n=1

contAluno = int(input("Quantos alunos existem na sala: "))
while n <= contAluno:
    notas = float(input("Quais as notas dos alunos: "))
    contNotas+=notas
    n+=1
media=contNotas/contAluno
print(media)