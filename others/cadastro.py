class Cadastro:
    def __init__(self, login:str, senha:str):
        self.setLogin(login)
        self.setSenha(senha)
    
    def getLogin(self):
        return self.__login
    
    def getSenha(self):
        return self.__senha
    
    def setLogin(self, novoLogin:str):
        if len(novoLogin) >= 5 and len(novoLogin) <= 15:
            self.__login = novoLogin
        else:
            print("Login inválido")
    
    def setSenha(self, novaSenha:str):
        if len(novaSenha) >= 8:
            self.__senha = novaSenha
        else:
            print("Senha inválida")


c1 = Cadastro("abcdefg", "12345678")
print(c1.getLogin(), c1.getSenha())
c1.setSenha("1234")
print(c1.getLogin(), c1.getSenha())
