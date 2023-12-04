# os operadores aritimeticos sao:
#       + adiçao
#       - subtraçao
#       * multiplicaçao
#       / divisao - pode retornar valor float
#        ** potencia
#       // divisao inteira
#        %  resto da divisao
# ordem de precedencia
#       1- ()parenteses
#       2- **potencias
#       3- * / // %
#       4- + -
#.....................................................
# para quebrar linha no print \n  
# para juntar pint end=' '

nome = input('olá!, Qual seu nome?  ')
print(f'prazer te conhecer !{nome:=^20}!')
symbo = '-'
print(symbo*30)
n = int(input('digite um numero! '))
n2 = int(input('digite outro numero '))
print(symbo*30)
s = n + n2
su = n - n2
m = n * n2
d = n / n2
di = n // n2
r = n % n2
po = n ** n2

print(f'a soma é:{s:_>10}\na subtraçao é:{su:_>10}\na multiplicaçao é:{m:_>10}\na divisao é:{d:.1f}\na divisao inteiro é:{di:_>10}\no resto da divisao é:{r:_>10}\na potencia é{po:_>10} ')