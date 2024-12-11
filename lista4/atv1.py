class funcionario:
  def __init__(self, nome:str, cpf:str, salario:float, departamento:str):
    self.nome = nome
    self.cpf = cpf
    self.salario = salario
    self.departamento = departamento

  @property
  def nome(self) -> str:
    return self.__nome
  
  @nome.setter
  def nome(self, nome:str) -> None:
    self.__nome = nome

  @property
  def cpf(self) -> str:
    return self.__cpf
  
  @cpf.setter
  def cpf(self, cpf:str) -> None:
    self.__cpf = cpf

  @property
  def salario(self) -> str:
    return self.__salario 
  
  @salario.setter
  def salario(self, salario:str) -> None:
    self.__salario = salario

  def bonificar(self) -> None:
    self.salario += self.salario*(10/100)


class gerente(funcionario):
  def __init__(self, nome:str, cpf:str, salario:float, departamento:str, senha:str) -> None:
    super().__init__(nome, cpf, salario, departamento)
    self.senha = senha
  
  @property
  def senha(self) -> str:
    return self.__senha

  @senha.setter
  def senha(self, senha:str) -> None:
    self.__senha = senha

  def bonificar(self) -> None:
    self.salario += self.salario * (15/100)

  def autenticar_senha(self, senha) -> bool:
    return self.senha == senha


edson = funcionario("edson","1234",100,"Chão de fabrica")

edson.bonificar()
print(edson.salario)

arnaldo = gerente("arnaldo", "1234", 100,"gerencia senior", "1234")

arnaldo.bonificar()
print(arnaldo.salario)

print(arnaldo.autenticar_senha("1"))
print(arnaldo.autenticar_senha("1234"))