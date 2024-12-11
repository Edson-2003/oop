class ContaBancaria:
  def __init__(self, nome:str, saldo:float) -> None:
    self.nome = nome
    self.saldo = saldo
  
  @property
  def nome(self) -> str:
    return self.__nome

  @nome.setter
  def nome(self, nome:str) -> None:
    self.__nome = nome
  
  @property
  def saldo(self) -> float:
    return self.__saldo

  @saldo.setter
  def saldo(self, saldo:str) -> None:
    self.__saldo = saldo

  def depositar(self, valor:float) -> None:
    self.saldo += valor

  def sacar(self, valor:float) -> None:
    if valor <= self.saldo:
      self.saldo -= valor
      return
    else:
      print("o saldo é insuficiente")


  def exibe_saldo(self) -> None:
    print(f'o saldo da conta e {self.saldo}')

class ContaCorrete(ContaBancaria):
  def __init__(self, nome:str, saldo:float, cheque_especial:float) -> None:
    super().__init__(nome, saldo)
    self.cheque_especial = cheque_especial
  
  @property
  def cheque_especial(self) -> float:
    return self.__cheque_especial
  
  @cheque_especial.setter
  def cheque_especial(self, valor:float) -> None:
    self.__cheque_especial = valor

  def sacar(self, valor) -> None:
    if (valor <= self.saldo + self.cheque_especial):
      if(valor <= self.saldo):
        self.saldo -= valor
        return
      else:
        valor -= self.saldo
        self.saldo = 0
        self.cheque_especial -= valor
        return

class ContaPoupanca(ContaBancaria):
  def __init__(self, nome:str, saldo:float, taxa_juros:float) -> None:
    super().__init__(nome, saldo)
    self.taxa_juros = taxa_juros

  @property
  def taxa_juros(self) -> float:
    return self.__taxa_jurus

  @taxa_juros.setter
  def taxa_juros(self, taxa:float) -> None:
    if(taxa >= 1):
      taxa = taxa / 100
    self.__taxa_jurus = taxa
    return

  def aplica_juros(self):
    self.saldo += (self.saldo * self.taxa_juros)



c1 = ContaBancaria("conta1", 0.0)
c1.sacar(10)
c1.depositar(10)
print(f'o saldo final da conta bancaria e {c1.saldo}')
c2 = ContaCorrete("conta2",0.0,100.0)
c2.sacar(10)
c2.depositar(10)
print(f'o saldo final da conta corrente e {c2.saldo}')
c3 = ContaPoupanca("conta3", 0.0, 0.15)
c3.sacar(10)
c3.depositar(100)
print(f'o saldo da poupanca e {c3.saldo}')
c3.aplica_juros()
print(f'saldo final da poupanca e {c3.saldo}')



  
