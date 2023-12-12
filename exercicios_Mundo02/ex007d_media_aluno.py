'''Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

m = float(input('Digite a Nota da 1° prova: '))
m2 = float(input('Digite a Nota da 2° prova: '))
media = (m + m2) / 2
print(f'Sua media é {media:.1f}')

if media < 5.0:
    print('\033[31mREPROVADO\033[m')
elif media >= 5.0 and media <= 9.9:
    print('\033[33mRECUPERAÇÃO\033[m')

elif media >= 7 and media <= 10:
    print('\033[32mAPROVADO\033[m')
