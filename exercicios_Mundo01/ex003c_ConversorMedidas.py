# escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
s = 'Conversor de medida'
a = 'made by felipe'
print(f'!!Bem vindo!!  \n {s:=^50}')
n = float(input('medida em metros: '))

cm = n * 100
mn = n * 1000

print(f'cm >> {cm}\nmn >> {mn} \n {a:=^50}')
