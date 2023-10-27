import math

#leia as medidas
co = float(input('digite o comprimento do cateto oposto do treiangulo retangulo: '))
ad = float(input('digite o comprimento do cateto adjacente: '))

#calcule o quadrado de cada Cateto
quadrado_a = co ** 2
quadrado_b = ad ** 2

#soma os quadrados dos catetos
soma= quadrado_a + quadrado_b

#calcule a raiz quadrada da soma
Hipotenusa = math.sqrt(soma)
print(f'o comprimento da hipotenusa é: {Hipotenusa:.2f}')