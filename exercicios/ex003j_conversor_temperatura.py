#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('qual a temperatura em °C: '))

f = c * (9/5) + 32

print(f'A temperatura de \n{c:=>10}°C corresponde a {f}°F!======')
