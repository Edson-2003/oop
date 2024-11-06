k = 15

def func(k):
  d = {}
  for i in range(1, k+1):
    d[i] = i*i
  return d

print(func(k))