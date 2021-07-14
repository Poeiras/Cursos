from acessocep import BuscaEndereco

cep = 35680239
obj_cep = BuscaEndereco(cep)
bairro, cidade, uf = obj_cep.acessa_via_cep()
print(bairro, cidade, uf)