import re as regex


class ExtratorURL:
    def __init__(self, url):
        # Salva a URL em um atributo do objeto
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        # Retorna a url removendo espaços em branco
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        # Valida se a url está vazia
        if not self.url:
            raise ValueError('URL vazia')

        # Regex para conferir o padrão da url
        padrao_url = regex.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('URL inválida, fora do padrão')

    def get_url_base(self):
        # Retorna a url base
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        # Retorna os parâmetros da url
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        # Retorna o valor do parâmetro busca
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_ecomercial = self.get_url_parametros().find('&', indice_valor)

        if indice_ecomercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_ecomercial]
        return valor

    def __eq__(self, other):
        return self.url == other.url

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return (self.url +
                '\n' +
                "Parâmetros: " +
                self.get_url_parametros() +
                '\n' +
                'URL base: ' +
                self.get_url_base())


site = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'
t1 = ExtratorURL(site)
t2 = ExtratorURL(site)
print(id(t1))
print(id(t2))
