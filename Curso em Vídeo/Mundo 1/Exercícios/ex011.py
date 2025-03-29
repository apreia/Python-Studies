larg = float(input('largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt
tinta = area / 2

print('A dimensão da parede é de {} x {} e sua área é de {}m²'.format(larg,alt,area))
print('Para pintar essa parede, você precisará de {}l de tinta!'.format(tinta))