from leilao.dominio import Usuario, Lance, Leilao

lucas = Usuario('Lucas', 100)
cao = Usuario('Cão', 100)

lance_lucas = Lance(lucas, 100)
lance_cao = Lance(cao, 150)

leilao = Leilao('Celular')
leilao.lances.append(lance_cao)
leilao.lances.append(lance_lucas)

for lance in leilao.lances:
    print('O usuário {} deu o lance de R${}'.format(lance.usuario.nome, lance.valor))


