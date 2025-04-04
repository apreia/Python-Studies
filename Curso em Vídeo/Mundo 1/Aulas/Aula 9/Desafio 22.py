nome = input('Digite seu nome: ')

nomeLetrasMaisculas = nome.upper()
print(nomeLetrasMaisculas)

nomeLetrasMinusculas = nome.lower()
print(nomeLetrasMinusculas)

qtd_letrasSemEspaco = nome.replace(' ','')
print(len(qtd_letrasSemEspaco))

qtdLetrasPrimeiroNome = nome.split()
print(len(qtdLetrasPrimeiroNome[0]))