'''Crie um programa que leia o nome completo de uma pessoa e motre:
- o nome com todas as letras maiusculas 
- o nome coom todas as leteras minusculas
- quantas letras ao todo(sem considerar espaços)
- quantas letras tem o primeiro nome

# Metodo 5Q's para montar um algoritimo:


1- quais sao os dados de entrada necessarios?
2- oq devo fazer com estes dados?
3- quais sao as restriçoes deste problema?
4- qual é o resultado esperado? 
5- qual é a sequencia de passos a ser feitas para chegar ao resultado esperado? 
-------------------------------------------------------------------------------

respostas:

1- nome completo
2- usar metodos de fatiamento
3-
4- mostrar os resultados de fatiamento
5- 
    1- perguntar o nome completo para o usuario
    2- guardar a informaçao
    3- ultilizar metodo upper para mostar nome em maiusculo
    4- mostrar nome em maiusculo
    5- ultilizar metodo lower para mostrar nome em minusculo
    6- mostrar nome em minusculo
    7- ultilizar metodo para contar quantas letras ao todo(sem espaços)
    8- mostrar quantidade de letras
    9- ultilizar metodo para contar letras
    10- mostrar quantidade de letras do primeiro nome

pseudocodigo:

    input: receber os dados
    print: mostrar o resultado
    
'''
nome =  input('digite um nome completo: ')
print('Seu nome em maiusculo é: ',nome.upper())
print('Seu nome em minusculos: ',nome.lower())

space = nome.replace(' ','')

print(f'Seu nome tem ao todo {len(space.strip())} letras' )


dividido = nome.split()

print(f'seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])}')