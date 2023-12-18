'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''
n = int(input('digite um numero inteiro: '))
co = 0 

print(f'os divisores de {n}sao: ')

for c in range(1, n+1):
    if n%c == 0:
        print('\033[04;33m', end=' ')
        co +=1
    else:
        print('\033[0;31m', end=' ')
    print(c , end=' ')
print('\033[m')

print(f'O numero {n} foi divisivel \033[0;33m{co}\033[m vezes')

if co == 2:
    print('Por isso ele é PRIMO.') 
else:
    print(f'O numero foi divisivel {co} vezes\nPor isso ele NAO É PRIMO.')
