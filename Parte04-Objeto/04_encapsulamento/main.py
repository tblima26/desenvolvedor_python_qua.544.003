from models import Pessoa
import os

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def main():
  limpar()
  aluno = Pessoa("Maria Silva", "123.456.789-00", "maria@email.com")
  print(aluno.nome) 
  print(aluno.cpf)  
  print(aluno.email)
  
if __name__ == "__main__":
  main()
