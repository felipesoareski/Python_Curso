print('----Vamos fazer u triangulo----')
a = float(input('primeiro segmento '))
b = float(input('segundo segmento '))
c = float(input('terceiro segmento '))

if a < b + c and b < a + c and c < a + b:
    print('voce formou um tiangulo')
else:
    print('Voce nao pode formar triangulo')


if a == b and a == c:
    print('EQUILATERO, todos os lados sao iguais')

elif a != b and a != c and b != a and b != c:
    print('ESCALENO, todos os lados diferente')
else:
    print('ISOSCELES, dois lados iguais')
