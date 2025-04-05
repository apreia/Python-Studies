distancia = float(input('Qual é a distância da viagem em Km? '))

if distancia <= 200:
    passagem = 0.5 * distancia
    print('O valor da passagem dessa viagem ficou no valor de R${}'.format(passagem))
else:
    passagem = 0.45 * distancia
    print('O valor da passagem dessa viagem ficou no valor de R${}'.format(passagem))