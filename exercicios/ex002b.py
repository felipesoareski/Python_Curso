# faça um programa que leia pelo teclado e mostre o seu tipo primitivo e todas as informaçoes possivel sobre ele

n1 = input('digite algo: ')

print(type(n1))
print('é numerrico? ', n1.isnumeric())
print('é decimal? ', n1.isdecimal())
print('é alfabetico? ', n1.isalpha())
print('é alfanumerico? ', n1.isalnum())
print('esta em maiuscula? ',n1.isupper())
print('esta em minuscula?' , n1.islower())
print('esta captalizado? ', n1.istitle())
