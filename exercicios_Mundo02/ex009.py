palin = str(input('digite uma frase: ')).strip().upper().split()
junto = ''.join(palin)
contador = ''
for frase in range(len(junto)-1,-1,-1):
    contador += junto[frase]

print(junto,contador)
if junto == contador:
    print('temos um palindromo')
else:
    print('nao forma palindromo')
