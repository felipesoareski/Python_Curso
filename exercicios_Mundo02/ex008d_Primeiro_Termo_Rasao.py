'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

#decimo = primeiro_ermo + (10*razao)
 
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(primeiro_termo,primeiro_termo+10*razao,razao):
    print(c, end=' -> ')
print('ACABOU')