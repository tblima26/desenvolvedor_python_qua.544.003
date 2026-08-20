import os
from models import Pessoa

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def main():
  limpar()
  homem = Pessoa("", 0, "", 0.0)
  homem.nome = "Carlos Silva"
  homem.idade = 30
  homem.email = "carlos@email.com"
  homem.altura = 1.78
  mulher = Pessoa("Ana Souza", 28, "ana@email.com", 1.65)

  print(f'{"=" *25}')
  print(f'--- Programa ---')
  print(f'{"=" *25}')
  homem.exibir()
  print(f'{"=" *25}')
  mulher.exibir()
  print(f'{"=" *25}')


if __name__ == "__main__":
  main()