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

pesquisa = input('Pesquisar Cidade: ').strip().title()
if pesquisa in cidades :
  posicao = cidades.index(pesquisa)
  print(f'Posição: {posicao} Cidade: {pesquisa}')
else:
  print('Cidade não encontrada')

#LINK - Modo 2
'''
for posicao, cidade in enumerate(cidades):
  if cidade == pesquisa:
    print(f'Posição: {posicao} | Cidade: {cidade}')
else:
  print('Cidade não encontrada.')
  '''