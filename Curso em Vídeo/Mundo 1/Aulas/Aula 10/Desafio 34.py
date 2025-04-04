salario = float(input('Digite seu salário: '))

if salario > 1250:
    novo_salario = salario + salario * 0.1
else:
    novo_salario = salario + salario * 0.15

print('Seu novo salário é de R${}'.format(novo_salario))