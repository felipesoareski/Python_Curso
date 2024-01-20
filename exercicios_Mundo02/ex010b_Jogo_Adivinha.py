from random import randint

while True:
    numero_pensado = randint(0,5)

    chute = 0
    cont = 0

    print('O computador pensou em um numero de 0 a 5, tente adivinhar! ')

    while chute != numero_pensado:
        chute = int(input('Qual foi o numero pensado? '))
        cont += 1
        if chute == numero_pensado:
            print('Parabens! Voce acertou!')
            c = str(input('Deseja jogar novamente? [S/N]')).upper()
            if c == 'N':
                break
            elif c != 'S':
                print('Opção invalida. encerrando o jogo')
                break
        elif chute > numero_pensado:
            print('Menos..., Tente novamente!')
        else:
            print('Mais..., Tente novamente!')
    if c == 'N':
        break
print('fim de jogo')
print(f'vc usou {cont} palpites!')