import numpy as np
import scipy as scipy
from scipy.special import comb
from scipy.stats import binom

# Uma moeda, perfeitamente equilibrada, é lançada para o alto quatro vezes. 
# Utilizando a distribuição binomial: 
# obtenha a probabilidade de a moeda cair com a face coroa voltada para cima duas vezes.
# Ensaios = 4 / 2 possibilidades
n1 = 4
# 2 possibilidades
p1 = 1/2
# Chance de acerto
q1 = 1 - p1
# Quantos sucessos
k1 = 2
# Cálculo
combina1 = comb(2,1)
prob1 = 1 / combina1
r1 = binom.pmf(k1,n1,p1)
print('Exercício 1: ' + '% 0.3f' % r1)

# Um dado, perfeitamente equilibrado, é lançado para o alto dez vezes. 
# Utilizando a distribuição binomial:
# # Obtenha a probabilidade de o dado cair com o número cinco voltado para cima PELO MENOS (cumulativo) três vezes.
n2 = 10
p2 = 1/6
q2 = 1 - p1
k2 = 2
# O binômio usado deve ser Survival function (1 - cumulativo (cdf)) 
r2 = binom.sf(k2, n2, p2)
print('Exercício 2: ' + '% 0.2f' % r2 )


# Suponha que a probabilidade de um casal ter filhos com olhos azuis seja de 22%. 
# Em 50 famílias, com 3 crianças cada uma, quantas podemos esperar que tenham dois filhos com olhos azuis?
p3 = 0.22
n3 = 3
k3 = 2
# Binômio
r3 = binom.pmf(k3, n3 , p3)
t3 = 50 * r3
print('Exercício 3: ' + '% 0.2f' % t3) 
