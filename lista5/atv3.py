class Relogio:
  def __init__(self, hh:int = 0, mm:int = 0, ss:int = 0) -> None:
    self.hh = hh
    self.mm = mm
    self.ss = ss

  @property
  def hh(self) -> int:
    return self.__hh

  @hh.setter
  def hh(self, hh:int) -> None:
    if(hh > 23):
      print("Horário digitado invalido")
      return
    else:
      self.__hh = hh

  @property
  def mm(self) -> int:
    return self.__mm
  
  @mm.setter
  def mm(self, mm:int) -> None:    
    if(mm > 60):
      print("Horário Digitado inválido")
      return
    else:
      self.__mm = mm

  @property
  def ss(self) -> int:
    return self.__ss
  
  @ss.setter
  def ss(self, ss:int) -> None:
    if(ss > 60):
      print("Horário digitado invalido")
    else:
      self.__ss = ss
  
  def  __repr__(self) -> str:
    return f'{self.hh}:{self.mm}:{self.ss}'
  
  def __eq__(self, outro:'Relogio') -> bool:
    if(self.hh == outro.hh):
      if(self.mm == outro.mm):
        if(self.ss == outro.ss):
          return True
    return False
  
  def __gt__(self, outro:'Relogio') -> bool:
    if(self.hh > outro.hh):
      return True
    
    if((self.hh == outro.hh) and (self.mm > outro.mm)):
      return True
    
    if((self.hh == outro.hh) and (self.mm == outro.mm) and (self.ss > outro.ss)):
      return True
    
    return False


  def __lt__(self, outro:'Relogio') -> bool:
    if(self.hh < outro.hh):
      return True
    
    if((self.hh == outro.hh) and (self.mm < outro.mm)):
      return True
    
    if((self.hh == outro.hh) and (self.mm == outro.mm) and (self.ss < outro.ss)):
      return True
    
    return False
  
  def __add__(self, outro:'Relogio') -> 'Relogio':
    hh = self.hh
    mm = self.mm
    ss = self.ss

    ss += outro.ss
    if(ss > 60):
      mm += 1
      ss -= 60
    
    mm += outro.mm
    if(mm > 60):
      hh+= 1
      mm -= 60

    hh += outro.hh
    if(hh > 24):
      hh -= 24
    
    return Relogio(hh,mm,ss)



  def __sub__(self, outro:'Relogio') -> 'Relogio':
    if(self < outro):
      print("O primeiro horário deve ser maior que o segundo")
      return None
    hh = self.hh
    mm = self.mm
    ss = self.ss
    
    if(self.ss < outro.ss):
      ss += 60
      mm -= 1
      ss -= outro.ss
    
    else:
      ss -= outro.ss
    
    if(mm < outro.mm):
      mm += 60
      hh -= 1
      mm -= outro.mm
    else:
      mm -= outro.mm

    hh -= outro.hh
    return Relogio(hh,mm,ss)
  

h1 = Relogio(18,37,32)
h2 = Relogio(20,0,30)

print(h1)
print(h2)
h3 = h1 + h2
print(h3)
h4 = h3 - h2
print(h4)
h4 = h2 - h3
print(h4)
print(h1 == h2)
print(h1 == Relogio(18,37,32))
print(h3 > h3)
print(h3 > h2)
print(h2 > h3)
print(h1 < h2)