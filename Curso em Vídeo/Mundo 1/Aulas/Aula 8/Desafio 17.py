from math import sqrt

cateto_oposto = float(input('Digite o Cateto Oposto: '))
cateto_adjacente = float(input('Digite o Cateto Adjacente: '))

hipotenusa = sqrt(cateto_oposto * cateto_oposto + cateto_adjacente * cateto_adjacente)

print('A hipotenusa do cateto oposto {} e do cateto adjacente {} é {}'.format(cateto_oposto, cateto_adjacente, hipotenusa))