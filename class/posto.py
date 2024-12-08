class BC:
  def __init__(self, ValorLitro, QuantidadeComustivel):
    self.__QuantidadeCombustivel = QuantidadeCombustivel
    self.__ValorLitro = ValorLitro

  @property
  def QuantidadeComustivel(self):
    return self.__QuantidadeComustivel

  @property
  def ValorLitro(self):
    return self.__ValorLitro

  @ValorLitro.setter
  def ValorLitro(self, ValorLitro):
    if(ValorLitro < 0):
      print("O valor a da gasolina deve ser maior ou igual a zero, substituiremos o valor por zero")
      self.__ValorLitro = 0

    self.__ValorLitro = ValorLitro

  @QuantidadeComustivel.setter
  def QuantidadeComustivel(self, QuantidadeComustivel):
    if(QuantidadeComustivel < 0):
      print("a quantidade de gasolina deve ser maior ou igual a zero, substituiremos a quantidade por zero")
      