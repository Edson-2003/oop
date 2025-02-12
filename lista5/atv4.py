class SuperLista:
  def __init__(self) -> None:
    self.__list = []

  def __gt__ (self, valor) -> None:
    self.__list.append(valor)

  def __repr__(self) -> str:
    if(not self.__list): 
      return "Lista Vazia"
    return '\n'.join([f'[{i}] = {valor}' for i, valor in enumerate(self.__list)])
  
l = SuperLista()
print(l) 

l > 10
l > 'Adoro programar'
l > 42

print(l) 