from random import randint

numero_sorteado = randint(0,5)
print('Pensei em um número entre 0 e 5!')

numero = int(input('Qual é o número em que pensei? '))

if numero == numero_sorteado:
    print('Você ganhou! O número que escolhi foi {}'.format(numero_sorteado))
else:
    print('Você perdeu! O número que escolhi foi {}'.format(numero_sorteado))