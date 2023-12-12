'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

title = 'LOJA CURSO EM VIDEO'
print(f'{title:=^50}')

total = float(input('Valor da compra: '))

print('[1] à vista Dinheiro/cheque')
print('[2] à vista cartao ')
print('[3] 2x no cartao S/Juros')
print('[4] 3x ou mais no cartao')

opcao = int(input('digite a opçao '))

if opcao == 1:
    desconto = total * (10/100)
    print(f'Desconto de 10%: R${desconto:.2f} Novo valor: R${total-desconto:.2f}')
elif opcao == 2:
    desconto = total * (5/100)
    print(f'Desconto de 05%: R${desconto:.2f} Novo valor: R${total-desconto:.2f}')
elif opcao == 3:
    print(f'Sua compra sera parcelada em: 2x de R${total/2} Sem Juros\nTotal: R$', total)

elif opcao == 4:
    n = int(input('Numero de parcelas: '))
    juros = 20/100
    print('Juros de 20%,')
    print(f'Sua compra será parcelada em {n}x de R${(juros*total+total)/n:.2f} com Juros')
    print(f'Total R${juros*total+total:.2f}')
else:
    print('Opçao invalida')
