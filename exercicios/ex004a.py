import math

#leia as medidas
co = float(input('digite o comprimento do cateto oposto do treiangulo retangulo: '))
ad = float(input('digite o comprimento do cateto adjacente: '))

#calcule o quadrado de cada Cateto
hi = math.hypot(co, ad)
print(f'o comprimento da hipotenusa é: {hi:.2f}')