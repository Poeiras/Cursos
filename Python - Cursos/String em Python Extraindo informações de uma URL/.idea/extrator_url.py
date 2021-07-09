import re as RegEx

endereco = 'Rua dona mundica 463, 35680239'

padrao = RegEx.compile('[0-9]{5}[-]{0,2}[0-9]{3}')
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print('\n' + cep)
else:
    pass