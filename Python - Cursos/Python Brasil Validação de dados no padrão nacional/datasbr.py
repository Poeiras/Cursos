from datetime import datetime
from datetime import timedelta


class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_ano = [
            'Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Maio',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outubro',
            'Novembro',
            'Dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_ano[mes_cadastro - 1]

    def dia_semana(self):
        lista_diasemana = [
            'Segunda',
            'Terça',
            'Quarta',
            'Quinta',
            'Sexta',
            'Sábado',
            'Domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        return lista_diasemana[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() + timedelta(days=365) - self.momento_cadastro
        return tempo_cadastro
