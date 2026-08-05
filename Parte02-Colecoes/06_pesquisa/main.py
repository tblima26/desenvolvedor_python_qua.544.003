cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Salvador",
    "Brasília",
    "Fortaleza",
    "Belo Horizonte",
    "Manaus",
    "Curitiba",
    "Recife",
    "Porto Alegre",
    "Florianópolis",
    "Salvador",
    "Belém",
    "Goiânia",
    "Vitória",
    "Natal"
]

pesquisa = input('Pesquisar Cidade: ').title().strip()

#NOTE - 1 
print('Cidade encontrada' if pesquisa in cidades else f'Cidade {pesquisa} inexistente')

'''
#REVIEW - 2 Modo
if(pesquisa in cidades):
  print('Cidade encontrada!')
else:
  print(f'Cidade {pesquisa} não está na Lista')
'''