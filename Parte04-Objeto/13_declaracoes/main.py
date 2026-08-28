from models import Pessoa 
import os

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def main():
  limpar()
  pessoa = Pessoa('Thiago',36,1.75)
  print(pessoa)

if __name__ == "__main__":
  main()