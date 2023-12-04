'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('qual é o valor do seu salario? '))
aumento1 = salario * (15/100)
aumento2 = salario * (10/100)

if salario <= 1250:
    print(f'Seu aumento é de 15%, seu salario sera: R${aumento1+salario:.2f}')

else:
    print(f'Seu aumento é de 10%, seu salário será: R${aumento2+salario:.2f}')

print('---Parabens pelo aumento!---')