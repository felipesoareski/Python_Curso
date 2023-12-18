'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços. Exemplos de palíndromos:'''

palin = str(input('digite uma frase: ')).strip().upper().split()
junto = ''.join(palin)
inverso = ''

for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
 
print(f'A frase {junto} ao inverso é: {inverso}')

if junto == inverso:
    print('temos um palindromo!')
else:
    print('nao é palindromo')

