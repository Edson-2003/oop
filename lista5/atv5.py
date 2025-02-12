class Retangulo:
  def __init__(self, altura:float = 0.0, largura:float = 0.0 ) -> None:
    self.altura = altura
    self.largura = largura
  
  @property
  def altura(self) -> float:
    return self.__altura
  
  @altura.setter
  def altura(self, altura:float) -> None:
    if(altura < 0.0):
      return
    self.__altura = altura
  
  @property
  def largura(self) -> float:
    return self.__largura
  
  @largura.setter
  def largura(self, largura:float) -> None:
    if(largura < 0.0):
      return
    self.__largura = largura

  def area(self) -> float:
    return self.altura * self.largura

  def __lt__(self, outro:'Retangulo') -> bool:
    return (self.area() < outro.area())
  
  def __gt__(self, outro:'Retangulo') -> bool:
    return (self.area() > outro.area())

  def __eq__(self, outro:'Retangulo') -> bool:
    return (self.area() == outro.area())


r1 = Retangulo(3, 4) # Área = 12
r2 = Retangulo(2, 6) # Área = 12
r3 = Retangulo(5, 2) # Área = 10
print(r1 == r2) # Resultado esperado: True
print(r1 > r3) # Resultado esperado: True
print(r3 < r2)