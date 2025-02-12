class Fracao():
  def __init__(self, numerador, denominador):
    self.__numerador = numerador
    self.__denominador = denominador

  def __mul__(self, outro:'Fracao') -> 'Fracao':
    novo_numerador = self.numerador * outro.numerador
    novo_denominador = self.denominador * outro.denominador
    
    return Fracao(novo_numerador, novo_denominador)

  @property
  def numerador(self):
    return self.__numerador
  
  @property
  def denominador(self):
    return self.__denominador

  def __str__(self):
    return f'{self.__numerador}/{self.__denominador}'

f1 = Fracao(2,3)
result = f1 * f1
print(result)
