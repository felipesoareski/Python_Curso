acumulador_idade = 0
maior = 0
menor = 0 
for c in range(1,3):
    print(F'----{c} PESSOA----')
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [F/M]: '))
    acumulador_idade += idade
    if c == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = nome


media_idade = acumulador_idade / 3
print(f'media idade é {media_idade}')
print(f'a pessoa mais velha é {maior}')
