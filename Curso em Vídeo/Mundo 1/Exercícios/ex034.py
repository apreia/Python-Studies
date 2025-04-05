salario = float(input('Digite seu salário R$'))

if salario > 1250:
    novo_salario = salario + salario * 0.1
    print('Seu novo salário será de R${:.2f}'.format(novo_salario))
else:
    novo_salario = salario + salario * 0.15
    print('Seu novo salário será de R${:.2f}'.format(novo_salario))