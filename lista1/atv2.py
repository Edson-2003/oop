t = [1, 2, 3]

def cumsum(l):
  l2 = []
  for i in range(len(l) + 1):
    soma = 0
    if(i == 0):
      l2.append(l[0])
    else:
      for j in range(i):
        soma += l[j]
      l2.append(soma)
  return l2

print(cumsum(t))
