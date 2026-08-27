class Motor:
  def __init__(self, potencia):
    self.__potencia = potencia

  @property
  def potencia(self):
    return self.__potencia

  @potencia.setter
  def potencia(self, potencia):
    self.__potencia = potencia

  def obterMotor(self):
    return f"Potência: {self.__potencia}"

class Carro:
  def __init__(self, modelo, potencia):
      self.__modelo = modelo
      self.__motor = Motor(potencia)

  @property
  def modelo(self):
      return self.__modelo

  @modelo.setter
  def modelo(self, modelo):
      self.__modelo = modelo

  def apresentarCarro(self):
      print(f"Modelo: {self.modelo}")
      if self.__motor:
          print(f"Motor: {self.__motor.obterMotor()}")
      else:
          print("Motor: Não informado")
          