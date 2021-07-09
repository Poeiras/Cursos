import re as RegEx

padrao_url = RegEx.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
url = 'https: // www.bytebank.com.br / cambio'
url2 = 'https://www.bytebank.com/cambio'
match = padrao_url.match(url)

if not match:
    raise ValueError('URL inválida')
else:
    print('\n' + str(match))
# https: // www.bytebank.com.br / cambio
