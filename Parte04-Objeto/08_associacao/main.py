from models import Endereco, Pessoa

def main():
  end = Endereco("SP", "São Paulo")
  pessoa = Pessoa("João", end)
  pessoa.apresentarEndereco()

  end2 = Endereco('','')
  p2 = Pessoa('',end2)

  end2.cidade = 'Brasilia'
  end2.uf = 'DF'
  p2.nome = 'Pedro Henrique'
  p2.apresentarEndereco()
if __name__ == "__main__":
  main()