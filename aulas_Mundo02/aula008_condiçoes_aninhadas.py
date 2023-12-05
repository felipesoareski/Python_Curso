nome = str(input('qual seu nome ')).capitalize().strip()

if nome == 'taina':
    print(f'que nome bonito{nome}'.capitalize())

elif nome in ['Pedro','Rafael','Felipe','Jefferson'.capitalize()]:
    print('nome comum'.upper())

elif nome in 'Ana Claudia Maria'.capitalize():
    print('nome fora de moda')

else:
    print('seu nome é normal')
print(f'tenha um bom dia {nome}')
