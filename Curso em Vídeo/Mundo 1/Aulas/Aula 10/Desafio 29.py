velocidade_carro = float(input('Qual é a velocidade do carro? '))

multa = (velocidade_carro - 80) * 7

if velocidade_carro > 80:
    print('Você foi multado em {}'.format(multa))