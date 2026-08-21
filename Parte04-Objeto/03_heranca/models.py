class Pessoa:
  def __init__(self, nome, email):
    self.email = email
    self.nome = nome

  def exibirDados(self):
    print(f'Nome: {self.nome}')
    print(f'Email: {self.email}')


class PessoaFisica(Pessoa):
  def __init__(self,nome,email, cel):
    super().__init__(nome,email)
    self.cel = cel
  
  def exibirDados(self):
    super().exibirDados()
    print(f'Cel: {self.cel}')

class PessoaJuridica(Pessoa):
  def __init__(self, nome, email,cnpj):
    super().__init__(nome, email)
    self.cnpj = cnpj
  
  def exibirDados(self):
    super().exibirDados()
    print(f'CNPJ: {self.cnpj}')