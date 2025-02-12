from random import uniform




Nivel_Critico = 0.5

class Robo:
  def __init__(self, nome:str) -> None:
    self.nome = nome
    self.vida = uniform(0,1)

  @property
  def vida(self) -> float:
    return self.__vida
  
  @vida.setter
  def vida(self, valor) -> None:
    if(valor <= 0.009):
      self.__vida = 0.0
      return
    
    if(valor > 1.0):
      self.__vida = 1.0
      return
    
    self.__vida = valor

  def __repr__(self) -> str:
    return f'Nome:{self.nome} - Vida:{self.vida:0.2f} ❤'
  
  def __add__(self, outro):
    nome1 = self.nome.split('-')
    nome2 = outro.nome.split('-')
    return type(outro)(f'{nome1[0]}-{nome2[0]}')
  
  def precisa_medico(self) -> bool:
    if(self.vida < Nivel_Critico):
      return True
    return False