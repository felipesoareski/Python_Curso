'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

Aula Anterior'''

print('----Vamos fazer um triangulo----')
a = float(input('primeiro segmento '))
b = float(input('segundo segmento '))
c = float(input('terceiro segmento '))

if a < b + c and b < a + c and c < a + b:
    print('voce formou um tiangulo')
else:
    print('Voce nao pode formar triangulo')
    exit()

if a == b == c:
    print('EQUILATERO, todos os lados sao IGUAIS')

elif a != b != c != a:
    print('ESCALENO, todos os lados DIFERENTES')
else:
    print('ISOSCELES, dois lados IGUAIS')
