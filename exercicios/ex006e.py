n1 = input('digite um numero: ')
n2 = input('digite outro numero: ')
n3 = input('Digite outro numero: ')

if n1 > n2 and n1 > n3:
    print(f'O maior numero é {n1} ')
elif n1 < n2 and n1 <n3:
    print(f'O menor numero é {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior numero é {n2}')
elif n2 < n1 and n2 < n3:
    print(f'O menor é {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior numero é {n3}')
elif n3 < n1 and n3 < n2:
    print(f'O menor é {n3}')