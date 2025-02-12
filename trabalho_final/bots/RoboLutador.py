from random import random, uniform

from .Robo import Robo

Dano_Maximo = 0.4

class RoboLutador(Robo):
  
  def __init__(self, nome:str) -> None:
    super().__init__(nome)
    self.forca = uniform(Dano_Maximo, 1.0)

  def atacar(self, outro) -> None:
    outro.vida *= (1 - self.força)

  def atacar(self, outro) -> None:
    outro.vida *= 1- self.forca
    if(isinstance(outro, RoboLutador)):
      self.vida *= 1 - outro.forca
  
  def __repr__(self) -> str:
    return f'{super().__repr__()} - Tipo: Lutador 🥊 - Força: {self.forca} ⚔'
  
  def __add__(self, outro):
    nome1 = self.nome.split('-')
    nome2 = outro.nome.split('-')
    return type(self)(f'{nome1[0]}-{nome2[0]}')