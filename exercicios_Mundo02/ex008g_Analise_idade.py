'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
hoje = date.today().year
print(hoje)
maior = 0
menor = 0

for c in range(1,8):
    p1 = int(input(f'Em q ano a {c}º nasceu? '))
    if hoje - p1 >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.\nE também tivemos {menor} pessoas menores de idade.')
