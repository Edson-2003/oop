class Fracao():
  def __init__(self, numerador, denominador):
    self.numerador = numerador
    self.denominador = denominador

  
  
  @property
  def numerador(self):
    return self.__numerador
  
  @numerador.setter
  def numerador(self, numerador) -> None:
    self.__numerador = numerador

  @property
  def denominador(self):
    return self.__denominador
  
  @denominador.setter
  def denominador(self, denominador) -> None:
    self.__denominador = denominador

  def mdc(self):
    a = self.numerador
    b = self.denominador
    while b != 0:
      a, b = b, a % b
    return abs(a)

  def simplifica(self):
    mdc = self.mdc()
    self.numerador = self.numerador//mdc
    self.denominador = self.denominador//mdc
  
  def __mul__(self, outro:'Fracao') -> 'Fracao':
    
    restultado = Fracao(self.numerador * outro.numerador, self.denominador * outro.denominador)
  
    return restultado.simplifica()
	
  def __add__(self, outro:'Fracao') -> 'Fracao':
    if self.denominador == outro.denominador:
      resultado = Fracao((self.numerador + outro.numerador), self.denominador)
      return resultado.simplifica()
    else:
      resultado = Fracao((self.numerador * outro.denominador) + (outro.numerador * self. denominador), self.denominador * outro.denominador)
      return resultado.simplifica()

  def __sub__(self, outro:'Fracao') -> 'Fracao':
     if self.denominador == outro.denominador:
      resultado = Fracao((self.numerador + outro.numerador), self.denominador)
      return resultado.simplifica()
     else:
      resultado = Fracao((self.numerador * outro.denominador) - (outro.numerador * self. denominador), self.denominador * outro.denominador)
      return resultado.simplifica()

  def __truediv__(self, outro:'Fracao') -> 'Fracao':
    return Fracao((self.numerador * outro.denominador),(outro.numerador * self.denominador)).simplifica()
  
  def __repr__(self) -> str:
    return f'{self.numerador}/{self.denominador}'



f1 = Fracao(1,2)
f2 = Fracao(2,4)
m = f1 * f2
a = f1 + f2
s = f1 - f2
d = f1/f2
print(m)
print(a)
print(s)
print(d)