
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

def createdict(keys, values):
  d = {}
  for i in range(len((keys))):
    d[keys[i]] = values[i]
  return d

d = createdict(keys, values)
print(d)