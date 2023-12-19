''' Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''
maior = 0
menor = 0

for c in range(1,4):
    peso = float(input(f'Pesoa da {c}º pessoa: '))
    if c == 1 :
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso lido foi {maior}Kg.\nO menor peso lido foi {menor}Kg.')
