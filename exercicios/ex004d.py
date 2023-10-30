from random import shuffle
a1 = str(input('primeiro aluno: '))
a2 = str(input('segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a3 = str(input('quarto aluno: '))
a4 = str(input('quinto aluno: '))

lista = [a1, a2, a3, a4]

shuffle(lista)

print('a ordem de apresentaçao será: ', lista)
