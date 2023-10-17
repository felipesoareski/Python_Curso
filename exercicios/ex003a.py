# faça um programa que leia um numero inteiro o seu sucessor e seu antecessor!

n = int(input('digite um numero: '))
print(f'seu antecessor é << {n - 1}\nseu sucessor é >> {n+1}')

#crie um algoritimo q leia um numero e mostre o seu dobro, triplo e raiz quadrada!

n = int(input('digite um numero: '))
d = n * 2 
t = n * 3
r = n **(1/2)
print(f'o dobro é {d}\no triplo é: {t}\na raiz quadrada é: {r:.2f}')