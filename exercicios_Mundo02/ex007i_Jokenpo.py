import random
from time import sleep

objeto = ['Pedra','Papel','Tesoura']
pc = random.choice(objeto)
print('-- Pedra -- Papel -- tesoura --')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
voce = int(input('Qual sua jogada? '))
                           
if voce == 1:
    voce = 'Pedra'
elif voce == 2:
    voce = 'Papel'
elif voce == 3:
    voce = 'Tesoura'
else:
    print('Opçao invalida, Jogue outra vez')


sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=*'*10)
if voce == pc:
    print(f'O PC jogou {pc}\nvoce jogou {voce}')
    print('-=*'*10)
    print('voce venceu')
else:
    print(f'O PC jogou {pc}\nvoce jogou {voce}')
    print('-=*'*10)
    print('Voceu perdeu')