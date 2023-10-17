#faça um programa que leia a largura e a altura de uma parede em metros
#calcule a sua area e a quantidade de tinta nescessaria para pintala
#sabendo q cada litro de tinta pinta uma area de 2m².
larg = float(input('Qual a largura da parede?  >> '))
alt =  float(input('qual a altura? >> '))

area = larg * alt 

print(f'a area é {area:=^12}m²')

c = area /  2

print(f'para pintar uma area de >> {area}m²\né nescessario >> {c}L')
