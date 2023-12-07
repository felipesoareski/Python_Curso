m = float(input('Digite a Nota da 1° prova: '))
m2 = float(input('Digite a Nota da 2° prova: '))
media = (m + m2) / 2
print(f'Sua media é {media}')

if media < 5.0:
    print('\033[31mREPROVADO\033[m')
elif media >= 5.0 and media <= 9.9:
    print('\033[33mRECUPERAÇÃO\033[m')

elif media >= 7 and media <= 10:
    print('\033[32mAPROVADO\033[m')
