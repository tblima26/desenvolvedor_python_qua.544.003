class Pessoa:
  #NOTE - método construtor
  def __init__(self,nome,idade,email,altura):
    self.nome = nome
    self.idade = idade
    self.email = email
    self.altura = altura

  #NOTE - método construtor
  def exibir(self):
    print(f"Nome: {self.nome}.")
    print(f"Idade: {self.idade} anos")
    print(f"E-mail: {self.email}.")
    print(f"Altura: {self.altura} metros")