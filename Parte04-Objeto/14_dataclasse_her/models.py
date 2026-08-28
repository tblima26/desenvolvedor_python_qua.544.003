from dataclasses import dataclass

@dataclass
class Pessoa:
  nome: str
  fone: str
  email: str

@dataclass
class PessoaFisica(Pessoa):
  idade: int
  salario: float

  def __str__(self):
    return f"Nome: {self.nome}\nIdade: {self.idade}\nSalário: R$ {self.salario:.2f}"
  
  def __len__(self):
    return self.idade
  
  def __float__(self):
    return float(self.salario)
  
  def __del__(self):
      print(f"💣💣 Objeto {self.nome} destruido com sucesso! ")

@dataclass
class PessoaJuridica(Pessoa):
  cnpj: str
  valor_mercado: float

  def __str__(self):
    return f"Empresa: {self.nome}\nCNPJ: {self.cnpj}\nContato: {self.fone}"

  def __len__(self):      
    return len(self.cnpj)

  def __float__(self):
    return float(self.valor_mercado)

  def __del__(self):
      print(f"💣💣 Objeto {self.nome} destruido com sucesso! ")
