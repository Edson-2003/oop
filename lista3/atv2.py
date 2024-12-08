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
  


ponto1 = ponto2D()
ponto2 = ponto2D()

print(ponto1.compara(ponto2))

ponto2 = ponto2D(3.5, 3.5)
print(ponto1.compara(ponto2))

print(ponto1.distancia(ponto2))
ponto2 = ponto1.clone()

print(ponto1.compara(ponto2))

