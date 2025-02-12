from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor
    
    @abstractmethod
    def processar_pagamento(self):
        pass

class CartaoCredito(Pagamento):
    def processar_pagamento(self):
        print(f"Pagamento de {self.valor} via Cartão de Crédito aprovado")

class Boleto(Pagamento):
    def processar_pagamento(self):
        print(f"Boleto de {self.valor} gerado para pagamento")

class Pix(Pagamento):
    def processar_pagamento(self):
        print(f"Pix de {self.valor} foi processado")

pagamentos: list[Pagamento] = [
    Pix(300),
    CartaoCredito(49.90),
    Boleto(1000),
    Pix(5.49),
    CartaoCredito(199.95),
]

for pag in pagamentos:
    pag.processar_pagamento()
