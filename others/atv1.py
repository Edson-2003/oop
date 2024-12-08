'''
crie um programa em python que defina uma função que some dois numeros quaisquer e retorne o resultado da soma
teste sua função lendo dois valores do usuario
'''



def soma( a:int, b:int):
  return a + b

def main():
  a = int(input("digite um valor inteiro:"))
  b = int(input("digite outro valor inteiro:"))

  print(soma(a, b))
  return 0


main()
