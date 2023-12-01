frase = 'Curso em Video de Python'
frase2 = '    aprenda python  '
dividido = frase.split()

#fatiamento:
# usar ''' para printar texto grande
print(frase[1::2])

#metodos para analise:
#len(frase)
#impime e conta quantas letras ó existente ja com o fatiamento
print(frase.count('o',3,13))
#enconta qual a posiçao da frase determinada
print(frase.find('deo'))
#remove os espaços inuteis do inicio e fim da frase
print(frase2.strip())

print('a variavel frase contem: ', len(frase), 'posiçoes')

#tansformaçao:

#substitui uma palavra pela outra
print(frase.replace('Python','android'))

#o metodo upper tranforma as letras q nao sao maiusculas em maiusculas
print(frase.upper())
print(frase.lower())

#captalize joga todos caracteres para minusculos e a primeira fica em Maiusculo
print(frase.capitalize())

#title faz o captalize de palavra por palavra. todoas as iniciais de palavras fica em maiuscula
print(frase.title())

#strip remove os espaços escedentes do começo e do fim da frase
print(frase2.strip())

#rstrip remove os espaços da direita
#lstrip remove os espaços da esquerda

#divisao:
#split divide uma string em varias partes/lista, o resultado da divisao sera ula lista de substrings.
print(frase.split())

print('-'.join(frase))

print(dividido[4][0])