class cadastro:
  def __init__(self, login, senha):
    self.__login = login
    self.__senha = senha
  
  def setLogin(self, newLogin, senha):
    if(senha == self.__senha):
      if(len(newLogin) >= 5 and len(newLogin) <= 15):
        self.__login == newLogin
        return
    
    