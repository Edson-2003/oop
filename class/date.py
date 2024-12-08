class date:
  def __init__(self, dia:int, mes:int, ano:int) -> None:
    self.ano = ano
    self.mes = mes
    self.dia = dia
  
  @property
  def ano(self) -> int:
    return self.__ano
  
  @property
  def mes(self) -> int:
    return self.__mes

  @property
  def dia(self) -> int:
    return self.__dia
  
  @ano.setter
  def ano(self, ano:int) -> None:
    if(ano < 1900):
      print("o ano deve ser maior que 1900")
      return
    self.__ano = ano
    return
  
  @mes.setter
  def mes(self, mes:int) -> None:
    if(mes > 12):
      print("o mes deve ser menor que 12")
      return
    self.__mes = mes
    return

  @dia.setter
  def dia(self, dia:int) -> None:
    if(self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or self.mes == 9 or self.mes == 11):
      if(dia > 31):
        print("data invalida")
        return
      self.__dia = dia
    if(self.mes == 1):
      return

    

    
  def __str__(self) -> str:
    return f"{self.dia}/{self.mes}/{self.ano}"