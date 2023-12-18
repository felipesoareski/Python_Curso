'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que 
forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0 
cont = 0
for numero in range(1,7):
    n1 = int(input(f'digite o {numero} valor: '))
    if n1 % 2 == 0:
        cont += 1 
        soma += n1
print(f'Voce informou {cont} numeros PARES e a soma é {soma}')
  