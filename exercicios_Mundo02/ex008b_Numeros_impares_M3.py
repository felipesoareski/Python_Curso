'''Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
 e que se encontram no intervalo de 1 até 500.'''

soma = 0
cont = 0

for c in range(1, 501, 2):

    if c % 3 == 0 and c < 500:
        cont = cont + 1
        soma += c
   
print(f'soma de {cont} valores sao {soma}')