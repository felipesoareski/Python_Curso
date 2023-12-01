ano = int(input('Digite um ano qualquer: '))
if ano % 400 == 0:
    print('é bissexto')
elif ano % 100 == 0:
    print('nao é Bissexto')
elif ano % 4 == 0 :
    print('é Bissixto')
else: 
    print('nao é bissexto')