#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual o valor do produto? R$'))
promoçao = float(input('qual o valor de desconto em %? '))

p = promoçao /100 #valor convertido em %
New_preço = preço - (preço * p)
desconto = preço - New_preço

print(f'o novo preço é de R${New_preço:.2f}')
print(f'e desconto é de R${desconto:.2f} ')
