'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitaçao novamente até ter um valor correto'''
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo [F/M]: ')).upper()
    
    if sexo == 'M' or sexo == 'F':
        print('sexo registrado com sucesso!', sexo)
        break
    else:
        print('Dado invalido! tente novamente! ')
print('fim')
