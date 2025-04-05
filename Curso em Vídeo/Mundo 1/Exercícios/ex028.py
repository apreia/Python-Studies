import random

numero_sorteado = print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
numero_sorteado = random.randint(0,5)

numero = int(input('Em que número eu pensei? '))

if numero_sorteado == numero:
     print('Você ganhou! O número sorteado foi {}'.format(numero_sorteado))
else:
    print('Eu ganhei! O número sorteado foi {}'.format(numero_sorteado))