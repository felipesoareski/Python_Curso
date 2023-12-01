print('----Vamos formar um triangulo!----')
a = int(input('digite um numero '))
b = int(input('digite outro um numero '))
c = int(input('digite outro um numero '))

if a < (b + c) :
    print('Voce formou um triangulo!')

elif b < (c + a):
    print('Voce formou um triangulo!')
elif c < (a + b):
    print('Voce formou um triangulo!')
else:
    print('Infelizmente voce nao conseguiu, tente outra vez!')

