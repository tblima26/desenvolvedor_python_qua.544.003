from models import PessoaFisica, PessoaJuridica
import os

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def main():
  limpar()
  pf = PessoaFisica("João Silva", "joao@email.com", "123.456.789-00")
  pj = PessoaJuridica("Empresa Exemplo LTDA", "contato@empresa.com", "12.345.678/0001-99")

  # Testando os acessos
  print(f"PF: {pf.nome} - CPF: {pf.cpf}")
  print(f"PJ: {pj.nome} - CNPJ: {pj.cnpj}")
  
if __name__ == "__main__":
  main()
