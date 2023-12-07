decimal = int(input('Digite um numero inteiro: '))

print('\033[33m----\033[m'*10)

print('[1] para \033[1;35mBINARIO\033[m')
print('[2] para \033[1;35mOCTAL\033[m')
print('[3] para \033[1;35mHEXADECIMAL\033[m')

print('\033[33m----\033[m'*10)

escolha = input('Escolha o numero da opçao desejada para conversão: ')

if escolha == '1':
    n = bin(decimal)
    print(f'\033[1;32m{decimal}\033[m convertido para BINÁRIA é: \033[1;32m{n[2:]}\033[m')
    

elif escolha == '2':
    n = oct(decimal)
    print(f'\033[1;32m{decimal}\033[m convertido para OCTAL é: \033[1;32m{n[2:]}\033[m')
       

elif escolha == '3':
    n = hex(decimal)
    print(f'\033[1;32m{decimal}\033[m convertido para HEXADECIMAL é: \033[1;32m{n[2:]}\033[m')
    
else:
    print('\033[31mOpçao invalida\033[m')
