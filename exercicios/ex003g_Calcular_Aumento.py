# faça um algoritimo que leia um preço de um produto e mostre seu novo preço,
# com aumento de 5%.

preço = float(input('qual o valor do produto? >> '))

aumento = 5/100
novo_preço = preço + (preço * aumento)

print(f'o preço com aumento de 5% é de R${novo_preço} ')
