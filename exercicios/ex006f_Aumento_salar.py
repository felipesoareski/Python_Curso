salario = float(input('qual é o valor do seu salario? '))
aumento1 = salario * (15/100)
aumento2 = salario * (10/100)

if salario <= 1250:
    print(f'Seu aumento é de 15%, seu salario sera: R${aumento1+salario:.2f}')

else:
    print(f'Seu aumento é de 10%, seu salario sera: R${aumento2+salario:.2f}')

print('---Parabens pelo aumento!---')