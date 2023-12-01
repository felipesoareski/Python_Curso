from random import randint
from time import sleep

numero_pensado = randint(0,5)
print('-=-'*21)
print('O computador pensou em um numero de 0 a 5. Tente adivinhar!... ')
print('-=-'*21)
chute = int(input('qual foi o numero q pensei? '.capitalize()))
print('PROCESSANDO...')
sleep(3)

if chute == numero_pensado:
    print('PARABENS!--> Voce acertou!<--')
elif chute > 5:
    print('voce chutou acima do valor limite!'.capitalize())
    print('---Tente outra vez!---')
else :
    print('---voce errou!---'.capitalize())
    print(f'o numero que o computador escolheu foi: {numero_pensado}'.capitalize())
    print('---Tente novamente!---')
