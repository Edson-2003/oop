t = [1, 2, 5, 7, 3, 4]

def middle(l):
  l.pop()
  l.pop(0)
  return l

print(middle(t))