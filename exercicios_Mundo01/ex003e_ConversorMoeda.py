#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolars ela pode comprar.. considere dolar:1,00=real:3,27  
real = float(input('Quantos reais voce tem na carteira? R$'))
dolar = 5.04
conv = real / dolar 
print(f'voce pode comprar U${conv:.2f} Dollars!')