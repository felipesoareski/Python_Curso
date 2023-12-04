#crie um programa que leia os 3 seguimentos de um triangulo e mostre se é possivel formar um triangulo
print('\033[01;04;36m----Vamos formar um triangulo!----\033[m')
a = float(input('Primeiro segmento '))
b = float(input('Segundo segmento '))
c = float(input('Terceiro numero '))

if a < (b + c) and b < (c + a) and c < (a + b):
    print('\033[01;32mVoce FORMOU um triangulo!\033[m')
else:
    print('\033[1;31mOs seguimentos acima NÃO PODEM FORMAR triangulo!\033[m')