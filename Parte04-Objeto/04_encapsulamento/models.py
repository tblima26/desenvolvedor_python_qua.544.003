class Pessoa:
  '''
    # REVIEW - Atributos Public, Protected e Private
    # Uso do "_" antes do atributo.
    self.nome = nome # public
    self._cpf = cpf # protected
    self.__email= email # private
  '''

  def __init__(self, nome, cpf, email):
    self.__nome = nome
    self.__cpf = cpf 
    self.__email= email 

  # get
  @property
  def nome(self):
    return self.__nome

  # set
  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @property
  def cpf (self):
    return self.__cpf

  @cpf.setter
  def cpf(self,cpf):
    self.__cpf = cpf

  @property
  def email (self):
    return self.__email

  @email.setter
  def email (self,email):
    self.__email= email

