n1 = input('digite um numero: ')
n2 = input('digite outro numero: ')
n3 = input('Digite outro numero: ')

maior = n1
menor = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'o maior numero é {maior}'.capitalize())

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3 
print(f'o menor numero é {menor}'.capitalize())