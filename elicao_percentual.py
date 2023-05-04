eleitores=int(input("Qual o total de eleitores da região: "))
vot_nulo=int(input("Quantos desses votaram nulo? "))
vot_branco=int(input("Quantos desses votaram branco? "))
vot_valid=int(input("Quantos tiveram votos validos? "))
perc_nulo=(vot_nulo/eleitores)*100
perc_branco=(vot_branco/eleitores)*100
perc_valid=(vot_valid/eleitores)*100
if vot_valid+vot_branco+vot_nulo==eleitores:
    print(f'A região teve {perc_nulo:,.0f}% votos nulos')
    print(f'A região teve {perc_branco:,.0f}% votos brancos')
    print(f'A região teve {perc_valid:,.0f}% votos válidos')
else:
    print(f'Votos inválido')