import os
from models import Departamento, Empresa

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def main():
  departamento = Departamento('RH')
  empresa = Empresa('Nike', departamento)
  limpar()
  print(empresa.detalhes())

if __name__ == "__main__":
  main()