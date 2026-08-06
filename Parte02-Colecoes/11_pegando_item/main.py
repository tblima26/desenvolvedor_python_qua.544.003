nomes = [
    "Mariana",
    "Carlos",
    "Vinicius",
    "Ana",
    "Rafael",
    "Helena",
    "Pedro",
    "Gabriel",
    "Sofia",
    "Lucas",
    "Beatriz",
    "Thiago",
    "Isabela",
    "Daniel",
    "Fernanda",
    "João",
    "Valentina",
    "Eduardo",
    "Nicolas",
    "Olivia"
]

nome = input('Pesquisar Nome: ').strip().title()
if nome in nomes:
  posicao = nomes.index[nome]
  nomeDel = nomes.pop(posicao)
  print(f'\n\n----------------')
  print(f'Nome Tirado: {nome}')
  print(f'----------------')
  print(f'Lista')
  for nome in nomes:
    print(nome)
  print(f'----------------')
else:
  print(f'\n\n{nome} não encontrado.')