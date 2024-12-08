class ponto2D:
  def __init__(self, x:float = 0.0 , y:float = 0.0):
    self.x = x
    self.y = y
  
  @property
  def x(self):
    return self.__x
  
  @x.setter
  def x(self, x:float):
    self.__x = x

  @property
  def y(self): 
    return self.__y
  
  @y.setter
  def y(self, y:float):
    self.__y = y
  
  def __str__(self):
    return f"x: {self.x} y: {self.y}"
  
  def compara(self, ponto: 'ponto2D'):
    return self.x == ponto.x and self.y == ponto.y
  
  def distancia(self, ponto: 'ponto2D'):
    a = (ponto.x - self.x) ** 2
    b = (ponto.y - self.y) ** 2
    return (a + b) ** 0.5

  def clone(self):
    return ponto2D(self.x, self.y)


class circulo:
  def __init__(self, raio:float, ponto: 'ponto2D' = ponto2D()):
    self.raio:float = raio
    self.ponto: 'ponto2D' = ponto.clone()

  @property
  def raio(self):
    return self.__raio
  
  @raio.setter
  def raio(self, raio:float):
    self.__raio:float = raio

  @property
  def ponto(self):
    return self.__ponto

  @ponto.setter
  def ponto(self, ponto):
    self.__ponto = ponto 
  
  def inflar(self, valor:float):
    self.raio += valor
  
  def desinflar(self, valor:float):
    self.raio -= valor

  def mover(self, ponto: 'ponto2D'):
    self.ponto = ponto.clone()

  def area(self):
    return 2 * 3.141592 * self.raio
  
  def __str__(self):
    return f"o raio do circulo é {self.raio} e esta localizado em {self.ponto}"



ponto = ponto2D(1,1)
raio = 2

forma = circulo(raio, ponto)
forma.inflar(2)
print(forma)
forma.desinflar(2)
print(forma)
print(forma.area())