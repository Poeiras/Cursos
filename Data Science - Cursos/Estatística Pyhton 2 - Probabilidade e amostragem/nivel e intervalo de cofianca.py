import numpy as np
import scipy 
from scipy.stats import norm

# Para estimar o valor médio gasto por cada cliente de uma grande rede de fast-food, foi selecionada uma amostra de 50 clientes.
# Assumindo que o valor do desvio padrão da população seja de R$ 6,00 
# e que esta população se distribui normalmente, obtenha a margem de erro desta estimativa para um nível de confiança de 95%.
print('--------------')
print('Exercício um')
amostra = 50
desvio  = 6
n_con   = 0.95

# O nível de confiança é a área da função 0.95 | Cálculo de Z
area1 = 0.95 / 2
area_z = 0.5 + area1
z = norm.ppf(area_z)
print('Área Z: ') 
print(area_z)
print('Resultado Z:')
print('%0.2f' % z)

# Erro inferencial
raiz_amostra = np.sqrt(amostra)
sigma = desvio / raiz_amostra
erro_inferencial = (z * sigma)
print('Erro inferencial: ' + '%0.2f' % erro_inferencial)

# Uma amostra aleatória simples de 1976 itens de uma população normalmente distribuída,
# com desvio padrão igual a 11, resultou em uma média amostral de 28.
# Qual o intervalo de confiança de 90% para a média populacional?
print('--------------')
print('Exercício dois')
amostra2 = 1976
desvio2 = 11
media2 = 28
n_con2 = 0.9

# Cálculo Z
area2 = 0.9 / 2
area_z2 = area2 + 0.5
z2 = norm.ppf(area_z2)
print('Área Z: ') 
print(area_z2)
print('Resultado Z:')
print('%0.2f' % z2)

# Erro inferencial
raiz_amostra2 = np.sqrt(amostra2)
sigma2 = desvio2 / raiz_amostra2
erro_inferencial2 = z2 * sigma2
print('Erro inferencial: ' + '%0.2f' % erro_inferencial2)

# Intervalo de confiança
intervalo2 = norm.interval(alpha = 0.9, loc = media2, scale = sigma2)
print('Intervalo de confiança: ')
print(intervalo2)
print('--------------')
