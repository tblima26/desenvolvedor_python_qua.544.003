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
  del nomes[indice]

  '''
  #REVIEW -  - Metodo 1
  nomes.remove(nome)
  Objetivo: Remove o primeiro valor encontrado na lista.
  #REVIEW -  - Metodo 2
  nomes.pop(indice)
  Objetivo: Remove o elemento pelo indice e retorna o valor removido.
  '''

  print(f'\n\n{nome} Foi removido da lista!\n\n')
  for nome in nomes:
    print(nome)
else:
  print(f'{nome} não encontrado.')