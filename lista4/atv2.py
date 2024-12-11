class FormaGeometrica:
  def __init__ (self, area:float, perimetro:float):
    self.area = area
    self.perimetro = perimetro

  @property
  def area(self) -> float:
    return self.__area
  
  @area.setter
  def area(self, area:float) -> None:
    self.__area = area

  @property
  def perimetro(self) -> float:
    return self.__perimetro
  
  @perimetro.setter
  def perimetro(self, perimetro:float) -> None:
    self.__perimetro = perimetro

class retangulo(FormaGeometrica):
  def __init__(self, lados:list) -> None:
    self.lados = lados
    super().__init__(self.calcula_area(), self.calcula_perimetro())

  @property
  def lados(self) -> list:
    return self.__lados
  
  @lados.setter
  def lados(self, lados:list) -> None:
    self.__lados = lados
  
  def calcula_area(self) -> float:
    return (self.lados[0] * self.lados [1])
  
  def calcula_perimetro(self) -> float:
    return (self.lados[0] * 2) + (self.lados[1] *2)


class triangulo(FormaGeometrica):
  def __init__(self, lado1:float, lado2:float, lado3:float) -> None:
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3
    
    super().__init__(self.calcula_area(), self.calcula_perimetro())

  @property
  def lado1(self) -> float:
    return self.__lado1
  
  @lado1.setter
  def lado1(self, lado:float) -> None:
    self.__lado1 = lado
  
  @property
  def lado2(self) -> float:
    return self.__lado2
  
  @lado2.setter
  def lado2(self, lado:float) -> None:
    self.__lado2 = lado
  
  @property
  def lado3(self) -> float:
    return self.__lado3
  
  @lado3.setter 
  def lado3(self, lado:float) -> None:
    self.__lado3 = lado

  def calcula_perimetro(self) -> float:
    return self.lado1 + self.lado2 + self.lado3
  
  def calcula_area(self) -> float:
    s = self.calcula_perimetro() / 2
    return (s * ( s - self.lado1) * ( s - self.lado2) * ( s - self.lado3))** 0.5
  


ret = retangulo([2.0, 4.0])
print(ret.calcula_area())
print(ret.calcula_perimetro())

tri = triangulo(6.0, 8.0, 10.0)
print(tri.calcula_perimetro())
print(tri.calcula_area())