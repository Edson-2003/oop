'''
crie um programa em python que inicia uma lista vazia,
leia um inteiro n do usuario e "aumente" a lista incrementalmente contenro os inteiros de 1 a n
'''


def preencher(l:list, n:int):
  if(len(l) != 0):
    print("lista não esta vazia")
    return l
  else:
    for i in range(n):
      l.append(i + 1)
    return l



def main():
  n:int = int(input("digite um inteiro qualquer:"))
  l = []
  l = preencher(l, n)
  print(l)
  return 0

main()

