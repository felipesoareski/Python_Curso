nome = str(input('qual é seu nome? ')).lower()
if nome == 'taina':
    print('nome top!')
else:
    print('nome comum')
print(f'seja bem vindo {nome}')

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2) / 2
print('--------media minima 6.0----------')
print(f'sua media é {m:-^11}')
if m >= 6:
    print(f'Parabens! sua media é {m} voce esta APROVADO!')
else:
    print('REPROVADO! estude mais!')
