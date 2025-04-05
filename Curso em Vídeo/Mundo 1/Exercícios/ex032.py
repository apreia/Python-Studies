import datetime

ano = int(input('Digite o ano. Caso queira analisar o ano atual digite 0 '))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))