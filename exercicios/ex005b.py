# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
print('analise da inicial de cidade "santo"')
nome = str(input('digite o nome de uma cidade: ')).strip()
print(nome[:5].upper() == 'SANTO')

cid = str(input('digite uma cidade')).strip()
div =  cid.split()

print('santo' in div[0].lower())