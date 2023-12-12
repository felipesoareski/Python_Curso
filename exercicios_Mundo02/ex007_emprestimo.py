'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qaual o seu salario atual? '))
anos = int(input('Quantos anos voce quer parar? '))

valor_parcela = casa // (anos*12)
porcento = 30/100
calculo = porcento*salario

if valor_parcela <= calculo:
    print('Empréstimo aprovado')
    print(f'total de parcelas de: {anos*12}')
    print(f'Valor da parcela é de: {valor_parcela:.2f}')

else:
    print('Emprestimo negado!')
