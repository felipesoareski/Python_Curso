salario = float(input('qual o seu salario antes do aumento? '))
aumento = float(input('qual o valor do aumento em % ? '))


porcento = aumento /100

soma = salario + ( salario * porcento  )

print(f'seu amento com {porcento}% é de: {soma:.2f}')
