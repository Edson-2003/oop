class student:
  def __init__(self, name, age):
    self.__name = name
    self.__age

  @property
  def name(self):
    return self.__name
  
  @property
  def age(self):
    return self.__age/

  @name.setter
  def name(self, name:str):
    if(name != "")
      self.__name = name

  @age.setter
  def age(self, age):
    if(age > 0):
      self.__age = age
    else
      self.__age = 0




mys = student("edson", -1)
print(mys.nome, " ", )
      
