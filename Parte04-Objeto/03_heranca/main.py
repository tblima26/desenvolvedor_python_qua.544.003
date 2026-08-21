from models import PessoaFisica, PessoaJuridica
import os

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def main():
  limpar()
  pf = PessoaFisica('Maria Silva', 'maria@email.com', '(11) 98888-7777')
  pf.exibirDados()
  input('\n\nObrigado por usar nossos serviços!')
  limpar()
  pj = PessoaJuridica("Tech Solutions Ltda", "contato@techsolutions.com", "12.345.678/0001-99")
  pj.exibirDados()
  input('\n\nObrigado por usar nossos serviços!')
  limpar()

if __name__ == "__main__":
  main()