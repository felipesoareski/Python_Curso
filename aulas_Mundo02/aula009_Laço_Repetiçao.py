#calculadora
n = int(input('digite um numero '))
for c in range(0,11):
    print(f'{n} x {c} = {c*n}')

#pulando passos
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: ')) 
for c in range(i, f+1, p):
    print(c)
print('fim')
#soma
s = 0
for c in range(0,5):
    n = int(input('digite um numero '))
    s += n
print('o soma é',s)

#de frente para tras
for c in range(6,0, -2):
    print(c)
print('fim')