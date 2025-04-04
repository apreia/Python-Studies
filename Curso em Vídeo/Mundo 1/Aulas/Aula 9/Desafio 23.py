n = str(input('Digite um número entre 0 a 9999: ')).zfill(4)

unidade = n[3]
print('Unidade:',unidade)

dezena = n[2]
print('Dezena:',dezena)

centena = n[1]
print('Centena', centena)

milhar = n[0]
print('Milhar', milhar)