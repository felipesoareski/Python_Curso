'''
1 peregunte a distancia em km de uma viagem
2 calcule R$0,50 por km
3 calcule R$045 por km
3 se o km for menor ou igual a 200km
    entao o preço é R$0,50 por km
4 se nao, 
    RS0,45
            '''

print('---'*8)
print('Preço da passagem por KM')
print('---'*8)
km = float(input('Digite a distancia da viagem em km: '))
if km <= 200:
    print(f'O valor da sua viagem é de R${km*0.5:.2f}')
else:
    print(f'O valor da sua viagem é de R${km*0.45:.2f}')