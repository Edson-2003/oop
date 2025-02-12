class Ponto:
  def __init__(self, x:float = 0.0, y:float = 0.0) -> None:
    self.x = x
    self.y = y
  
  @property
  def x(self) -> float:
    return self.__x
  
  @x.setter
  def x(self, x) -> None:
    self.__x = x

  @property
  def y(self) ->float:
    return self.__y
  
  @y.setter
  def y(self, y) -> None:
    self.__y = y
    
  def __repr__(self) -> str:
    return f'({self.x}, {self.y})'
  
  def __add__(self, outro:'Ponto') -> 'Ponto':
    return Ponto(self.x + outro.x, self.y + outro.y)
  
  def __sub__(self, outro:'Ponto') -> 'Ponto':
    return Ponto(self.x - outro.x, self.y - outro.y)
  
  def __mul__(self, outro:'Ponto') -> 'Ponto':
    return Ponto(self.x * outro.x, self.y * outro.y)
  
  def __rmul__(self, n:float) -> 'Ponto':
    return Ponto(self.x * n, self.y * n)

x = Ponto(3, 2)
y = Ponto(2, 2)

print(x)
print(x+y)
print(x-y)
print(x*y)
print(2*x)