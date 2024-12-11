class pagamento:
  def __init__(self, valor:float, data:str):
    self.valor = valor
    self.data = data
  
  @property
  def valor(self) -> float:
    return self.__valor
  
  @valor.setter
  def valor(self, valor:float) -> None:
    self.__valor = valor

  @property
  def data(self) -> str:
    return self.__data
  
  @data.setter
  def data(self, data:str) -> None:
    self.__data = data

  def ProcessaPagamento(self):
    print("processando pagamento generico")


class PagamentoCartao(pagamento):
  def __init__(self, valor:float, data:str, numero_cartao:str, validade:str) -> None:
    super().__init__(valor, data)
    self.numero_cartao = numero_cartao
    self.validade = validade
  
  @property
  def numero_cartao(self) -> str:
    return self.__numero_cartao
  
  @numero_cartao.setter
  def numero_cartao(self, numero_cartao:str) -> None:
    self.__numero_cartao = numero_cartao

  @property
  def validade(self) -> str:
    return self.__validade
  
  @validade.setter
  def validade(self, validade:str) -> None:
    self.__validade = validade
  
  def ProcessaPagamento(self):
    print("realizado via cartao")


class PagamentoPix(pagamento):
  def __init__(self, valor:float, data:str, chave_pix:str) -> None:
    super().__init__(valor, data)  
    self.chave_pix = chave_pix

  @property
  def chave_pix(self) -> str:
    return self.__chave_pix
  
  @chave_pix.setter
  def chave_pix(self, chave_pix:str) -> None:
    self.__chave_pix = chave_pix
  
  def ProcessaPagamento(self):
    print("realizado via pix")

p1 = pagamento(10, "11/12/24")
p1.ProcessaPagamento()

p2 = PagamentoCartao(10, "11/12/24", "1234", "08/30")
p2.ProcessaPagamento()

p3 = PagamentoPix(10, "11/12/24", "1234")
p3.ProcessaPagamento()
