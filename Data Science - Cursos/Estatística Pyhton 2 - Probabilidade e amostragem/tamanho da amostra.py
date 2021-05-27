import numpy as numpy
import scipy
from scipy.stats import norm

# O valor do gasto médio dos clientes de uma loja de conveniência é de R$ 45,50. 
# Assumindo que o desvio padrão dos gastos é igual a R$ 15,00,
# Qual deve ser o tamanho da amostra para estimarmos a média populacional com um nível de significância de 10%?
# Considere que o erro máximo aceitável seja de 10%.
print('------')
print('Exercício um - população INFINITA')
media = 45.5
desvio_padrao = 15
significancia = 0.1
confianca = 0.9
erro_max = 0.1

# Área da função Z
area = confianca /2
area_z = area + 0.5
z = norm.ppf(area_z)

# Erro percentual
erro_percentual = media * erro_max

# Cálculo do tamanho da amostra
amostra = (z *(desvio_padrao / erro_percentual)) ** 2
print('Total da amostra:' + '%0.0f' % amostra)
print('------')


# Um fabricante de farinha verificou que, em uma amostra aleatória formada por 200 sacos de 25 kg de um lote formado por 2.000 sacos,
# apresentou um desvio padrão amostral do peso igual a 480 g.
# Considerando um erro máximo associado à média populacional igual a 0,3 kg e um nível de confiança igual a 95%.
# Qual tamanho de amostra deveria ser selecionado para obtermos uma estimativa confiável do parâmetro populacional?
print('------')
print('Exercício dois - população FINITA')
populacao = 2000
amostra2 = 200
desvio2 = 0.48
erro_max = 0.3
confianca2 = 0.95

# Área da função Z 
area2 = confianca2 / 2
area_z2 = area2 + 0.5
z2 = norm.ppf(area_z2)

# Cálculo do resultado
# resultado = ((z**2) * (desvio ** 2) * tamanho_da_populacao )/(((z ** 2)*(desvio ** 2)) + ((erro_max ** 2 )* (tamanho_da_populacao - 1)))
resultado = ((z2 ** 2) * (desvio2 ** 2) * populacao) / ((z2 ** 2) * (desvio2 ** 2) + ((erro_max ** 2) * (populacao - 1)))
print('Tamanho da amostra confiável: ' + '%0.0f' % resultado + ' sacos')
print('------')
