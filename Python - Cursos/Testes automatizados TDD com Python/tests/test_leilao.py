from unittest import TestCase
from dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):
    def setUp(self):
        self.lucas = Usuario('Lucas', 150)
        self.cao = Usuario('Cão', 200)
        self.afrodite = Usuario('Afrodite', 250)

        self.lance_lucas = Lance(self.lucas, 100)
        self.lance_cao = Lance(self.cao, 150)
        self.lance_afrodite = Lance(self.afrodite, 200)

        self.leilao = Leilao('Celular')

    def test_avalia_simples(self):
    # O teste deve retornar o maior e o menor valor adicionados em ordem crescente
        self.leilao.propoe(self.lance_lucas)
        self.leilao.propoe(self.lance_cao)

        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_unico_lance(self):
    # O teste deve retornar o mesmo valor para o menor e o maior lance
        self.leilao.propoe(self.lance_lucas)

        self.assertEqual(100, self.leilao.menor_lance)
        self.assertEqual(100, self.leilao.maior_lance)

    def test_multi_lances(self):
    # O teste deve retornar o maior e o menor valor num leião de 3+ lances
        self.leilao.propoe(self.lance_lucas)
        self.leilao.propoe(self.lance_cao)
        self.leilao.propoe(self.lance_afrodite)

        menor_esperado = 100
        maior_esperado = 200

        self.assertEqual(menor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_esperado, self.leilao.maior_lance)

    def test_leilao_sem_lance(self):
    # O teste deve permitir propor um lance caso o leilão não tenha lances
        self.leilao.propoe(self.lance_lucas)
        self.assertEqual(1, len(self.leilao.lances))

    def test_novo_lance(self):
    # Se o usuário for diferente, permitir um novo lance
        self.leilao.propoe(self.lance_lucas)
        self.leilao.propoe(self.lance_cao)
        quantidade_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances)

    def test_ultimo_lance(self):
    # Se o usuário for o mesmo do último lance, não permite um novo lance
        try:
            self.leilao.propoe(self.lance_lucas)
        except ValueError:
            quantidade_lances = len(self.leilao.lances)
            self.assertEqual(1, quantidade_lances)
