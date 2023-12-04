'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
print('----impar ou par?----')
num = int(input('digite um numero: '))
if num % 2 == 0:
    print(f'o numero {num} é PAR')
else:
    print(f'o numero {num} é IMPAR')