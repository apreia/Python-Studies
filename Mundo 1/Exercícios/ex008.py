medida = float(input('Distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a {}km'.format(medida,km))
print('A medida de {}m corresponde a {}hm'.format(medida,hm))
print('A medida de {}m corresponde a {}dam'.format(medida,dam))
print('A medida de {}m corresponde a {:.0f}dm'.format(medida,dm))
print('A medida de {}m corresponde a {:.0f}cm'.format(medida,cm))
print('A medida de {}m corresponde a {:.0f}mm'.format(medida,mm))