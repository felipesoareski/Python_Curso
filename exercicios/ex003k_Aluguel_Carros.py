#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('quantos dias alugado? '))
km = float(input('Qauantos km rodados? '))

diaria = 60
kmr = 0.15

c = diaria * dias + km * kmr
print(f'O total a pagar é R${c:.2f}' )