d = float(input('Digite a distância da viagem: '))

if d <= 200:
    print('O preço da passagem é de R${:.2f}'.format(d * 0.5))
else:
    print('O preco da passagem é de R${:.2f}'.format(d * 0.45))