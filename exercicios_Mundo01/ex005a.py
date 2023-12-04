#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num =  int(input('digite um numero de 0 a 9999: '))
unidade = num % 10
dezena = num // 10 %10
centena = num // 100 %10
milhar = num // 1000 %10

print('unidade:', unidade)
print('dezena:', dezena)
print('centena:', centena)
print('milhar:', milhar )
