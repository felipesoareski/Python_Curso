decimal = int(input('Digite um numero inteiro: '))

print('\033[33m----\033[m'*10)

print('[1] para \033[1;35mBINARIO\033[m')
print('[2] para \033[1;35mOCTAL\033[m')
print('[3] para \033[1;35mHEXADECIMAL\033[m')

print('\033[33m----\033[m'*10)

escolha = input('Escolha o numero da opçao desejada para conversão: ')

if escolha == '1':
    n = bin(decimal)
    base = 'BINARIO'

elif escolha == '2':
    n = oct(decimal)
    base = 'OCTAL'

elif escolha == '3':
    n = hex(decimal)
    base = 'HEXADECIMAL'
else:
    print('opçao invalida')



print(f'\033[1;32m{decimal}\033[m convertido para {base} é: \033[1;32m{n[2:]}\033[m')


