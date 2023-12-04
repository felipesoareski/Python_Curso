#Mudar cores no terminal

#  style           text                back
#  0                30(branco)         40(branco)
#  1                31(vermelho)       41(vermelho)
#  4(sublinhado)    32(verde)          42(verde)
#  7(inverte)       33(amarelo)        43(amarelo)
#                   34(roxo)           44(roxo)
#                   35(rosa-pink)      45(rosa-pink)
#                   36(azul)           46(azul)
#                   37(cinza)          47(cinza)

a = 5
b = 10 

print('\033[07;37mOla mundo\033[m')
print('\033[07;37;42mOla mundo\033[m'*5)
print('\033[1;4;36mOla mundo\033[m')
print(f'Os valores sao \033[01;04;32m{a}\033[m e \033[1;4;32m{b}\033[m')

cores = {'limpa': '\033[m',
         'verdeNegritoSub':'\033[1;4;32m',
         'vermelhoNegritoSub':'\033[1;4;31m',
         'roxoNegritoSub':'\033[1;4;34m',
         'rosa-PinkNegritoSub':'\033[1;4;34m'}

nome = input('ola, qual o seu nome? ')
print(f'é um pra zer te conhecer {cores["verdeNegritoSub"]}{nome}{cores["limpa"]}')