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
  indice = nomes.index(nome)
  nomes[indice] = input('Novo Nome: ').strip().title()
  print(f'\n\nNome alterado com sucesso.\n\n')
  for nome in nomes:
    print(nome)
else:
  print(f'{nome} não encontrado.')