import random

# solicita o nome de cada aluno
a1 = input('digite o nome do primeiro aluno para sorteio: ')
a2 = input('digite o nome do segundo aluno: ')
a3 = input('digite o nome do segundo aluno: ')
a4 = input('digite o nome do segundo aluno: ')

#cria uma lista com os nomes recebidos
alunos = [a1, a2, a3, a4]

#sorteia um indice aleatorio dentro do intervalo de 0 a 3
nsorteado = random.randint(0,3)

#obtem o nome do aluno sorteado ultilizando o indice sorteado
sortudo = alunos[nsorteado]

#exibe o nome do sorteado
print(f'o sorteado é {sortudo}')
