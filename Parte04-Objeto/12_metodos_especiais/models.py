class Pessoa:
  # NOTE - Metodo Dunder
  def __init__(self,nome, idade, altura):
    self.__nome = nome
    self.__idade = idade
    self.__altura = altura

# Getters
  def get_nome(self): return self.__nome
  def get_idade(self): return self.__idade
  def get_altura(self): return self.__altura

  # Setters
  def set_nome(self, nome): self.__nome = nome
  def set_idade(self, idade): self.__idade = idade
  def set_altura(self, altura): self.__altura = altura

  def __str__(self):
    return f'Nome: {self.get_nome()} - Idade: {self.get_idade()} - Altura: {self.get_altura()}'
  
  def __len__(self):
    return len(self.get_nome())
  
  def __int__(self):
    return self.get_idade()

  def __del__(self):
    print(f"Objeto {self} destruido com sucesso! 💣")