'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
vel =  float(input('digite a velocidade registrada:'))
distancia = (vel - 80) -1
multa =  7.00 * distancia
if vel > 80:
    print('voce ultrapassou a velocidade de 80km/h e foi MULTADO!')
    print(f'O valor da multa é de R${multa:.2f}')
else:
    print('Voce esta detro da normalidade!')
print('----Voce é quem dirige sua vida!----')