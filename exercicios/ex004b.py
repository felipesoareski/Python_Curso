from math import sin, cos, tan, radians
c = float(input('digite o angulo: '))

sen = sin(radians(c))
coss = cos(radians(c))
tang = tan(radians(c))

print(f'o seno é: {sen:.2f}\no valor do cosseno é: {coss:.2f}\no tangent é: {tang:.2f}')