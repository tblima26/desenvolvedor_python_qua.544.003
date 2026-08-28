import os
from models import Pessoa

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def main():
  limpar()
  pessoa1 = Pessoa("Ana", 25, 1.68)
  print(pessoa1)
  print(f'Idade usando o int: {int(pessoa1)}')
  print(f'Tamanho do nome: {len(pessoa1)}')
  print(f'{"=" * 30}')
  pessoa2 = Pessoa("Carlos", 42, 1.80)
  print(pessoa2)
  print(f'Tamanho do nome: {len(pessoa2)}')
  print(f'Idade usando o int: {int(pessoa2)}')
  print(f'{"=" * 30}')
  pessoa3 = Pessoa("Beatriz", 19, 1.60)
  print(pessoa3)
  print(f'Tamanho do nome: {len(pessoa3)}')
  print(f'Idade usando o int: {int(pessoa3)}')
  print(f'{"=" * 30}\n')
  del pessoa1
  del pessoa2
  del pessoa3
  print(f'\n\n{"=" * 12} FIM {"=" * 12}')

if __name__ == "__main__":
  main()