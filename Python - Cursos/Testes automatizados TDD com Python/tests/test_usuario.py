from dominio import Usuario, Leilao
from excecoes import LanceInvalido
import pytest


@pytest.fixture()
def lucas():
    return Usuario('Lucas', 150)


@pytest.fixture()
def leiloado():
    return Leilao('Breja')


def test_subtracao_carteira(lucas, leiloado):
# Teste para subtrair o valor de carteira após um lance
    lucas.propoe_lance(leiloado, 50)
    assert lucas.carteira == 100


def test_lance_valido(lucas, leiloado):
# Teste deve permitir propor lance quando o valor do lance é menor que o valor da carteira
    lucas.propoe_lance(leiloado, 100)
    assert lucas.carteira == 50


def test_lance_igual_carteira(lucas, leiloado):
# Teste deve permitir propor lance quando o valor é igual ao valor da carteira
    lucas.propoe_lance(leiloado, 150)
    assert lucas.carteira == 0


def test_lance_maior_carteira(lucas, leiloado):
# Teste não deve permitir propor lance quando o valor é maior que valor da carteira
    with pytest.raises(LanceInvalido):
        lucas.propoe_lance(leiloado, 250)
