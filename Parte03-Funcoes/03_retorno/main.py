#NOTE - Funções com Retorno
def boasVindas(nome):
  print(f'{"=" *30}')
  print(f'--- 🤣 Olá, {nome} 🤣 ---')
  print(f'{"=" *30}')

def lerNome():
  nome = input('\nNome: ').strip().title()
  return nome

#NOTE - Main
boasVindas(lerNome())