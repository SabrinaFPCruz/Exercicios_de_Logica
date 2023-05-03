
print("(Q) Quadrado\n(T)Triangulo \n(C)Circulo")
form_geo=input("Qual forma geometrica deseja realizar o calculo?")
while form_geo in "Qq":
    lados_q=float(input("Qual o tamanho dos lados do quadrado? "))
    a_q=float(input("Qual altura do quadrado? "))
    b_q=float(input("Qual a base do quadrado? "))
    area_q=a_q*b_q
    peri_q=lados_q**2
    print(area_q)
    print(peri_q)
    break
while form_geo in "tT":
    lados_t=float(input("Qual o tamanho dos lados do traingulo? "))
    base_t=float(input("Qual a base do triangulo? "))
    altu_t=float(input("Qual a altura do triangulo? "))
    area_t=(base_t*altu_t)//2
    peri_t=lados_t*3
    print(area_t)
    print(peri_t)
    break
while form_geo in "cC":
    raio_c=float(input("Qual o raio do circulo? "))
    diam_c=raio_c*2
    area_c=3.14*(raio_c)**2
    print(area_c)
    print(diam_c)
    break
    
