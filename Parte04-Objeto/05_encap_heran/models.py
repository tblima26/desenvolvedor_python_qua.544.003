#SECTION - PESSOA
class Pessoa:
  def __init__(self, nome, email):
    self.__nome = nome
    self.__email= email 

  @property # get
  def nome(self):
    return self.__nome

  @nome.setter # set
  def nome(self, nome):
    self.__nome = nome

  @property # get
  def email (self):
    return self.__email

  @email.setter # set
  def email (self,email):
    self.__email= email

#SECTION - PESSOA FISICA
class PessoaFisica(Pessoa):
  def __init__(self, nome, email,cpf):
    super().__init__(nome, email)
    self.__cpf = cpf

  @property # get
  def cpf (self):
    return self.__cpf
  
  @cpf.setter # set
  def cpf(self,cpf):
    self.__cpf = cpf

#SECTION - PESSOA JURIDICA
class PessoaJuridica(Pessoa):
  def __init__(self, nome, email, cnpj):
    super().__init__(nome, email)
    self.__cnpj = cnpj

  @property # get
  def cnpj (self):
    return self.__cnpj
  
  @cnpj.setter # set
  def cnpj(self,cnpj):
    self.__cnpj = cnpj