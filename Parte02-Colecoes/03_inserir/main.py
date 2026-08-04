import os

#LINK - Funções
def limpaTela():
  os.system('cls' if os.name=='nt' else 'clear')

#TODO - Programa Principal
nomes=[]

while(True):
  limpaTela()
  nome = input("Nome:").strip().title()
  nomes.append(nome)
  opcao = input('\n\nDeseja Continuar?\n\n S | N : ').strip().upper()
  if (opcao != "S"):
    limpaTela()
    for i,nome in enumerate(nomes, start=1):
      print(f'{i} - Nome: {nome}')
    break

