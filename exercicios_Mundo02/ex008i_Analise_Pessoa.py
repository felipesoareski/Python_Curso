'''desenvolva um programa que leia o nome,idade e sexo de 4 pessoas, no final do programa mostre:
a media de idade do grupo
quem é o homem mais velho
quantas mulheres tem menos de 21 anos'''
acumulador_idade = 0
maior = 0
menor = 0 
homemVelho = ''
mulheres = 0
for c in range(1,5):
    print(F'----{c} PESSOA----')
    nome = str(input('NOME: ')).strip().title()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [F/M]: ')).strip()
    acumulador_idade += idade
    if c == 1 and sexo in 'Mm':
        maior = idade
        homemVelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        homemVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
    

media_idade = acumulador_idade / 4
print('---'*6)
print(f'media idade é {media_idade}')
print(f'O homem mais velho é {homemVelho} e tem {maior} anos')
print(f'{mulheres} mulheres tem menos de 20 anos')
print('---'*6)
