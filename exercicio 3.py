nome=input("Digite seu nome: ")
idade=int(input("Dgite sua idade: "))
salario=float(input("Digite seu salário: "))
perce_sal=float(input("Qual o seu percentual de aumento: "))
aumen_sal=(perce_sal/100)*salario+salario
print("Seu nome é",nome,"\nSua idade",idade,"\nE seu salário era",salario,"\nE com o aumento ficou",aumen_sal,)