total = float(input('Valor da compra: '))

print('[1] à vista Dinheiro/cheque')
print('[2] à vista cartao ')
print('[3] 2x no cartao S/Juros')
print('[4] 3x ou mais no cartao')

opcao = int(input('digite a opçao '))

if opcao == 1 :
    desconto = total * (10/100)
    print(f'Desconto de 10%: R${desconto:.2f} Novo valor:{total-desconto:.2f}')
elif opcao == 2:
    desconto = total * (5/100)
    print(f'Desconto de 05%: R${desconto:.2f} Novo valor:{total-desconto:.2f}')
elif opcao == 3:
    print('Total: ', total)   

elif opcao == 4:
    n = int(input('Numero de parcelas: '))
    juros = 20/100
    print(f'Juros de 20%, Total R${juros*total+total:.2f}')
else:
    print('Opçao invalida')

