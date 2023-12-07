from datetime import date

borndate = int(input('ANO de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - borndate

print(f'Sua idade é {idade}')

if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade > 14 and idade <=19:
    print('Sua categoria é JUNIOR')
elif idade == 20:
    print('Sua categoria é SENIOR')
else:
    print('sua categoria é MASTER')


