from random import randint
from time import sleep
from bots import Robo
from bots import RoboLutador
from bots import RoboMedico


def verifica(equipe):
    return isinstance(equipe, tuple) \
        and len(equipe) == 2 \
        and isinstance(equipe[0], RoboLutador) \
        and isinstance(equipe[1], RoboMedico)

def simulacao(Equipe1:tuple, Equipe2:tuple) -> tuple:
  if(not verifica(Equipe1)):
    print('Devido a equipe 1 ser invalida a batalha esta cancelada')
    return None
  
  if(not verifica(Equipe2)):
    print('Devido a equipe 2 ser invalida a batalha esta cancelada')
    return None

  print(f'Equipe 1 Lutador: {Equipe1[0].nome} e Médico: {Equipe1[1].nome}')
  print(f'Equipe 2 Lutador: {Equipe2[0].nome} e Médico: {Equipe2[1].nome}')
  
  n = 1
  while((Equipe1[0].vida > 0.0) and (Equipe2[0].vida > 0.0)):
    if(Equipe1[0].vida < 0.1 and randint(0,1)):
        Equipe1[1].curar(Equipe1[0])
     
    if(Equipe2[0].vida < 0.1 and randint(0,1)):
        Equipe2[1].curar(Equipe2[0]) 
    
    print(f'Round {n}')
    Equipe1[0].atacar(Equipe2[0])
    print(f'Lutador: {Equipe1[0].nome} Vida: {Equipe1[0].vida:0.2f}')
    print(f'Lutador: {Equipe2[0].nome} Vida: {Equipe2[0].vida:0.2f}')
    n += 1
    sleep(0.5)
    
  
  if(Equipe1[0].vida > 0.0):
		 return Equipe1
  return Equipe2
     




r0 = Robo('carlinhos')
r1 = RoboLutador('charles')
r2 = RoboMedico('drauzio')
print(r0)
print(r1)
print(r2)

r3 = r0 + r1
print(r3)
print(type(r3))
r4 = r2 + r0
print(r4)
print(type(r4))

Lutadores = (r1, RoboLutador('rocky'))
Medicos = (r2, RoboMedico('cassiano'))

print(simulacao((Lutadores[0], Medicos[0]), (Lutadores[1], Medicos[1])))

