real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.74
euro = real / 6.16

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar Є{:.2f}'.format(real, euro))