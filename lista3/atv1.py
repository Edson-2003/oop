class date:
  def __init__(self, dia:int, mes:int, ano:int) -> None:
    self.ano = ano
    self.mes = mes
    self.dia = dia

  @property
  def ano(self) -> int:
    return self.__ano
  
  @ano.setter
  def ano(self, ano:int) -> None:
    if(ano < 1900):
      print("o ano minimo é 1900")
      self.__ano = -1
      return
    self.__ano = ano
    return

  @property
  def mes(self) -> int:
    return self.__mes

  @mes.setter
  def mes(self, mes:int) -> None:
    if(mes > 12 and mes > 0):
      print("o mes é invalido")
      self.__mes = -1
      return
    self.__mes = mes
    return

  @property
  def dia(self) -> int:
    return self.__dia  

  @dia.setter
  def dia(self, dia:int) -> None:
    if(dia < 1):
      print("data invalido")
      self.__dia = -1
      return
          
    if(self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or self.mes == 8 or self.mes == 10 or self.mes == 12):
      if(dia > 31):
        print("data invalida")
        self.__dia = -1
        return
      self.__dia = dia
    
    if(self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11):
      if(dia > 30):
        print("data invalida")
        self.__dia = -1
        return
      self.dia = dia
    
    if(self.mes == 2):
      if(dia > 28):
        print("data invalida")
        self.__dia = 1
        return
      self.dia = dia

  def jump(self) -> None:
    if(self.dia == 28):
      if(self.mes == 2):
        self.dia = 1
        self.mes = 3
        return
      self.dia += 1
      return

    if(self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11):
      if(self.dia == 30):
        self.dia = 1
        self.mes += 1
        return
      self.dia += 1
      return
    
    if(self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or self.mes == 8 or self.mes == 10 or self.mes == 12):
      if(self.dia == 31):
        if(self.mes == 12):
          self.dia = 1
          self.mes = 1
          return
        else:
          self.dia = 1
          self.mes += 1
          return
      self.dia += 1
      return
      

  def __str__(self) -> str:
    return f"{self.dia}/{self.mes}/{self.ano}"
  




data1 = date(31,3,2015)
data2 = date(29, 2, 1956)

print(data2)
print(data1)
data1.jump()
print(data1)