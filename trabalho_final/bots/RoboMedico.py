from random import uniform

from .Robo import Robo



class RoboMedico(Robo):
  def __init__(self, nome:str) -> None:
    super().__init__(nome)
    self.poder_de_cura = uniform(0,1)


  def curar(self, outro) -> None:
    if(self.vida >= outro.vida):
      outro.vida += self.poder_de_cura
      print(f'Médico curou: {outro.nome}')
    
  def __repr__(self) -> str:
    return f'{super().__repr__()} Tipo: Médico - Poder de cura {self.poder_de_cura}'
  
  def __add__(self, outro):
    nome1 = self.nome.split('-')
    nome2 = outro.nome.split('-')
    return type(self)(f'{nome1[0]}-{nome2[0]}')