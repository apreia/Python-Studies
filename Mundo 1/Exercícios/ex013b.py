preco = float(input('Preço do produto R$'))

avista = preco - (preco * 10 / 100)
print('O preço do produto pagando a vista é R${}'.format(avista))

aprazo = preco + (preco * 8 / 100)
print('O preço do produto pagando à prazo é R${}'.format(aprazo))