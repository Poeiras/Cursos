import numpy as np
import scipy as scipy

# O número médio de clientes que entram em uma padaria por hora é igual a 20. 
# Obtenha a probabilidade de, na próxima hora, entrarem exatamente 25 clientes.
m1 = 20
k1 = 25
r1 = (np.e ** (-m1) * (m1 ** k1)) / (np.math.factorial(k1))
print('Exercício 1: ' + '%0.3f' % r1)
