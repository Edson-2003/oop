class atleta:
  def __init__(self, aponsentado:bool, peso:float):
    self.aposentado = aponsentado
    self.peso = peso

  @property
  def aponsentado(self) -> bool:
    return self.__aposentado
  
  @aposentado.setter
  def aposentado(self, aposentado) -> None:
    self.__aposentado = aposentado
  @property
  def peso(self) -> float:
    return self.__peso
  
  @peso.setter
  def peso(self, peso:float) -> None:
    self.__peso = peso

  def aposentar(self):
    if(not self.aposentado):
      self.aposentado( not self.aposentado)



class corredor(atleta):
  def __init__(self, aponsentado, peso):
    super().__init__(aponsentado, peso)
  
  def correr(self):
    return
  
class nadador(atleta):
  def __init__(self, aponsentado, peso):
    super().__init__(aponsentado, peso)

  def nadar(self):
    return
  
class ciclista(atleta):
  def __init__(self, aponsentado, peso):
    super().__init__(aponsentado, peso)

  def pedalar(self):
    return

class triatleta(corredor, nadador, ciclista):
  def __init__(self, aponsentado, peso):
    super().__init__(aponsentado, peso)
