n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))

if n1 > n2:
    print(f'O maior numero é {n1}')
elif n1 < n2:
    print(f'o maior numero é {n2}')
elif n1 == n2:
    print('Nao existe maior numero\nOs dois sao iguais.')
