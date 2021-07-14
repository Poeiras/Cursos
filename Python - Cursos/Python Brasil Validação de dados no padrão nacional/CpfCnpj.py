from validate_docbr import CPF
from validate_docbr import CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError('Documento inválido')


class DocCPF:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido')

    def valida(self, documento):
        valida = CPF()
        return valida.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format()


class DocCNPJ:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido')

    def valida(self, documento):
        valida = CNPJ()
        return valida.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format()
