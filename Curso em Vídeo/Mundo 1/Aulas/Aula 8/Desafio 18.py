from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo: '))
radiano = radians(angulo)

print('O seno do ângulo {} é {:.2f}'.format(angulo, sin(radiano)))
print('O cosseno do ângulo {} é {:.2f}'.format(angulo, cos(radiano)))
print('A tangente do ângulo {} é {:.2f}'.format(angulo, tan(radiano)))