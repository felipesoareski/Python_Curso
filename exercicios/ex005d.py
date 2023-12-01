#faça um programa que leia uma frase pelo teclado e mostre 
    #quantas vezes aparece a letra 'A'
    #em que posiçao ela aparece pela primeira vez
    #em que posiçao ela aparece a ultima vez
print('Analise da letra "A"')
frase = str(input('digite uma frase: ')).strip().lower()

print(f'A letra A apareceu: {frase.count("a")} vezes na frase\nA primeira letra A apareceu na posiçao {frase.find("a")+1}\nA ultima letra A apareceu na posiçao: {frase.rfind("a")+1}')