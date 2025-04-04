from math import hypot

CO = float(input('Comprimento do cateto oposto: '))
CA = float(input('Comprimento do cateto adjacente: '))
hi = hypot(CO, CA)

print('A hipotenusa vai medir {:.2f}'.format(hi))