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

elif valor_parcela > calculo:
    print('Emprestimo negado!')
