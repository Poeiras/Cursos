# url = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

# Validando URL
url = 'a   e   xxx   '
url = url.replace(' ', '')
url = url.strip()

if url == '':
    raise ValueError('URL vazia')
else:
    pass

# Método find
indice_interrogacao = url.find('?')

# Fatiamento
url_base = url[:indice_interrogacao]
url_parametro = url[indice_interrogacao + 1:]

# Método Len
parametro_busca = 'moedaDestino'
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametro[indice_valor:]

# Múltiplo parâmetro
indice_ecomercial = url_parametro.find('&', indice_valor)
if indice_ecomercial == -1:
    valor_mp = url_parametro[indice_valor:]
else:
    valor_mp = url_parametro[indice_valor:indice_ecomercial]

print('\n' + url + '\n')
print(url_base + '\n')
print(url_parametro + '\n')
print(valor + '\n')
print(valor_mp + '\n')
