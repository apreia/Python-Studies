velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado em R${}'.format(multa))
else:
    print('Tenha uma boa viagem!')