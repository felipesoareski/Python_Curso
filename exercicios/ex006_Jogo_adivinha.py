from random import randint
from time import sleep

cores = {'limpa':'\033[m',
         'azul':'\033[01;36m',
         'vermelho':'\033[01;31m',
         'amarelo':'\033[01;33m',
         'cinza':'\033[30m',
         'verde':'\033[01;32m',
         'rosa':'\033[01;35m'}

numero_pensado = randint(0,5)
print(f'{cores["amarelo"]}-=-{cores["limpa"]}'*21)
print(f'{cores["rosa"]}O computador pensou em um numero de 0 a 5. Tente adivinhar!... {cores["limpa"]}')
print(f'{cores["amarelo"]}-=-{cores["limpa"]}'*21)
chute = int(input('qual foi o numero q pensei? '.capitalize()))
print(f'{cores["cinza"]}PROCESSANDO...{cores["limpa"]}')
sleep(3)

if chute == numero_pensado:
    print(f'{cores["verde"]}PARABENS!--> Voce acertou!<--{cores["limpa"]}')
elif chute > 5:
    print(f'{cores["amarelo"]}voce chutou acima do valor limite!{cores["limpa"]}'.capitalize())
    print(f'{cores["vermelho"]}---Tente outra vez!---{cores["limpa"]}')
else :
    print(f'{cores["vermelho"]}---voce errou!---{cores["limpa"]}'.capitalize())
    print(f'o numero que o computador escolheu foi:{cores["azul"]} {numero_pensado}{cores["limpa"]}'.capitalize())
    print(f'{cores["vermelho"]}---Tente novamente!---{cores["limpa"]}')
