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
  

class retangulo:
  def __init__(self, altura: float, largura: float, ponto: 'ponto2D'):
    self.altura = altura
    self.largura = largura
    self.ponto = ponto.clone()

  @property
  def altura(self):
    return self.__altura

  @altura.setter
  def altura(self, altura: float):
    self.__altura = altura

  @property
  def largura(self):
      return self.__largura

  @largura.setter
  def largura(self, largura: float):
    self.__largura = largura

  @property
  def ponto(self):
    return self.__ponto

  @ponto.setter
  def ponto(self, ponto):
      if not isinstance(ponto, ponto2D):
          raise TypeError("O ponto deve ser uma instância de ponto2D.")
      self.__ponto = ponto

  def mover(self, ponto: 'ponto2D'):
      self.ponto = ponto.clone()

  def area(self):
      return self.altura * self.largura

  def intersecao(self, outro: 'retangulo'):
      x1_min, y1_min = self.ponto.x, self.ponto.y
      x1_max, y1_max = x1_min + self.largura, y1_min + self.altura

      x2_min, y2_min = outro.ponto.x, outro.ponto.y
      x2_max, y2_max = x2_min + outro.largura, y2_min + outro.altura

      return not (x1_max <= x2_min or x1_min >= x2_max or 
                  y1_max <= y2_min or y1_min >= y2_max)

  def __str__(self):
      return (f"Retângulo(altura={self.altura}, largura={self.largura}, "
              f"ponto=({self.ponto.x}, {self.ponto.y}))")


ponto1 = ponto2D(0, 0)
ponto2 = ponto2D(3, 3)
ponto3 = ponto2D(5, 5)

# Criando instâncias de retangulo
ret1 = retangulo(4, 3, ponto1)
ret2 = retangulo(2, 2, ponto2)
ret3 = retangulo(2, 2, ponto3)

# Testando a área
print(f"Área do Retângulo 1: {ret1.area()}")  # Esperado: 12
print(f"Área do Retângulo 2: {ret2.area()}")  # Esperado: 4

# Testando interseção
print(f"Retângulo 1 e Retângulo 2 se sobrepõem? {ret1.intersecao(ret2)}")  # Esperado: True
print(f"Retângulo 1 e Retângulo 3 se sobrepõem? {ret1.intersecao(ret3)}")  # Esperado: False

# Testando mover o retângulo
print("Movendo o Retângulo 1 para (6, 6)...")
ret1.mover(ponto2D(6, 6))
print(ret1)  # Nova posição do retângulo 1
print(f"Retângulo 1 e Retângulo 3 se sobrepõem após mover? {ret1.intersecao(ret3)}")  # Esperado: False    