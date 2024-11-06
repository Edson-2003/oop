class pessoa:
  def __init__(self, nome:str, sobrenome:str):
    self.nome = nome
    self.sobrenome = sobrenome
  pass

#uso de objetos da classe
p1 = pessoa("edson", "augusto")
print(p1.nome)
print(p1.sobrenome)

