from models import PessoaFisica, PessoaJuridica
import os

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def main():
  limpar()
  pf = PessoaFisica(
      "Carlos Souza", 
      "(21) 99888-7766", 
      "carlos@email.com", 
      35, 
      5000.00
  )
  print(f'\n{"="*35}\n')
  print(str(pf)) 
  print(len(pf))       
  print(float(pf))
  del(pf)
  print(f'\n{"="*35}\n')
  pj = PessoaJuridica(
    nome="Tech Soluções LTDA",
    fone="(11) 3333-4444",
    email="contato@techsolucoes.com",
    cnpj="12.345.678/0001-99",
    valor_mercado=1500000.00
  )
  print(str(pj))       # Exibe a string descritiva da empresa
  print(len(pj))       # Retorna o tamanho do CNPJ (18 caracteres contando os símbolos)
  print(float(pj))
  del(pj)
  print(f'\n{"="*35}\n')

if __name__ == "__main__":
  main()