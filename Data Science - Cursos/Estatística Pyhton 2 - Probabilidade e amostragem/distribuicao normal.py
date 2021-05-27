import numpy as np
import scipy as scipy
from scipy.stats import norm

# Exercício 1
# A aplicação de uma prova de estatística em um concurso apresentou um conjunto de notas normalmente distribuídas. 
# Verificou-se que o conjunto de notas tinha média 70 e desvio padrão de 5 pontos.
# Qual a probabilidade de um aluno, selecionado ao acaso, ter nota menor que 85?
m1 = 70
dpadrao1 = 5
z1 = (85 - m1) / dpadrao1
r1 = norm.cdf(z1).round(4)
print('Exercício 1: ' + '% 0.4f' % r1)

# Exercício 2
# O faturamento diário de um motorista de aplicativo segue uma distribuição aproximadamente normal,
# Com média R$ 300,00 e desvio padrão igual a R$ 50,00. 
# Obtenha as probabilidades de que, em um dia aleatório, o motorista ganhe: 
# a) Entre R$ 250,00 e R$ 350,00
# b) Entre R$ 400,00 e R$ 500,00

# Cálculo a
print('--------------------')
m2 = 300
dpadrao2 = 50
z_sup1 = (350 - m2) / dpadrao2
z_inf1 = (250 - m2) / dpadrao2
z_sup1 = norm.cdf(z_sup1)
z_inf1 = norm.cdf(z_inf1)
res1 = z_sup1 - z_inf1
print('Exercício 2a: ' + '%0.4f' % res1)

# Cálculo b
z_sup2 = (500 - m2) / dpadrao2
z_inf2 = (400 - m2) / dpadrao2
z_sup2 = norm.cdf(z_sup2)
z_inf2 = norm.cdf(z_inf2)
res2 = z_sup2 - z_inf2
print('Exercício 2b: ' + '%0.4f' % res2)

# Exercício 3
# O Inmetro verificou que as lâmpadas incandescentes da fabricante XPTO apresentam uma vida útil normalmente distribuída,
# com média igual a 720 dias e desvio padrão igual a 30 dias. Calcule a probabilidade de uma lâmpada, escolhida ao acaso, durar:
# a) Entre 650 e 750 dias
# b) Mais que 800 dias
# c) Menos que 700 dias

# Cálculo a
print('--------------------')
m3 = 720
dpadrao3 = 30
z_sup3 = (750 - m3) / dpadrao3
z_inf3 = (650 - m3) / dpadrao3
z_sup3 = norm.cdf(z_sup3)
z_inf3 = norm.cdf(z_inf3)
res3a = z_sup3 - z_inf3
print('Exercício 3a: ' + '%0.4f' % res3a)

# Cálculo b
z3b = (800 - m3) / dpadrao3
res3b = 1 - norm.cdf(z3b)
print('Exercício 3b: ' + '%0.4f' % res3b)

#Cálculo c
z3c = (700 - m3) / dpadrao3
res3c = norm.cdf(z3c)
print('Exercício 3c: ' + '%0.4f' % res3c)

# Exercício 4
# Utilizando a tabela padronizada, ou o ferramental disponibilizado pelo Python,
# Encontre a área sob a curva normal para os valores de Z abaixo:
# a) Z < 1,96
# b) Z > 2,15
# c) Z < -0,78
# d) Z > 0,59
e4z1 = norm.cdf(1.96)
e4z2 = 1 - norm.cdf(2.15)
e4z3 = norm.cdf(-0.78)
e4z4 = 1 - norm.cdf(0.59)
print('--------------------')
print('Exercício 4a: ' + '%0.4f' % e4z1)
print('Exercício 4b: ' + '%0.4f' % e4z2)
print('Exercício 4c: ' + '%0.4f' % e4z3)
print('Exercício 4d: ' + '%0.4f' % e4z4)
