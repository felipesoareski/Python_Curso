print('----Vamos formar um triangulo!----')
a = float(input('Primeiro segmento '))
b = float(input('Segundo segmento '))
c = float(input('Terceiro numero '))

if a < (b + c) and b < (c + a) and c < (a + b):
    print('Voce FORMOU um triangulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triangulo!')

