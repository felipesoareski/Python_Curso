from datetime import date

borndate = int(input('ano de nascimento? '))
ano_atual = date.today().year
idade = ano_atual - borndate
if idade < 18:
    print(f'Quem nasceu em {borndate} tem {idade} ano {ano_atual}.')
    print(f'Ainda faltam {18-idade} para o alistamento.\nSeu alistamento sera em {(18-idade)+ano_atual}')
elif idade == 18:
    print(f'Quem nasceu em {borndate} tem {idade} ano em {ano_atual}.')
    print('Voce tem que se alista IMEDIATAMENTE!')
elif idade > 18:
    print(f'Quem nasceu em {borndate} tem {idade} anos em {ano_atual}.')
    print(f'Voce ja deveria ter se alistado a {idade-18} anos')
    print(f'Seu alistamento foi em {ano_atual -(idade-18)}')
