r1 = float(input('Digite o valor da Primeira Reta: '))
r2 = float(input('Digite o valor da Segunda Reta: '))
r3 = float(input('Digite o valor da Reta Reta: '))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('É possível formar um Triângulo!')
else:
    print('Não é possível formar um triângulo!')