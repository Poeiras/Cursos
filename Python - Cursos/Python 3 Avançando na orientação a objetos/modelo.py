class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self, numero):
        self._likes += numero

    def __str__(self):
        return f'\n' \
               f'Nome: {self._nome}\n'\
               f'Ano: {self.ano}\n'\
               f'Likes: {self._likes}'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome}\n'\
               f'Ano: {self.ano}\n'\
               f'Likes: {self._likes}\n'\
               f'Duração: {self.duracao} minutos'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} \n' \
               f'Ano: {self.ano} \n' \
               f'Likes: {self._likes} \n' \
               f'Duração: {self.temporadas} temporadas'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


atlanta = Serie('atlanta', 2018, 2)
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

atlanta.dar_like(2)
vingadores.dar_like(5)
tmep.dar_like(3)
demolidor.dar_like(1)

filmes_e_series = [atlanta, vingadores, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tem o filme ou não? {demolidor in playlist_fim_de_semana} \n')
print(f'Tamanho da lista: {len(playlist_fim_de_semana)} \n')
for programa in playlist_fim_de_semana:
    print(programa)
