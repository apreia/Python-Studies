largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
qtdTinta = area / 2

print('A área da parede é de {} e será necessário {}L de tinta para pinta-lá!'.format(area, qtdTinta))