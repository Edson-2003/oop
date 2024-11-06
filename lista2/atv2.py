dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def concatdict(d1,d2):
  d={}
  for key, value in d1.items():
    d[key] = value
  
  for key, value in d2.items():
    d[key] = value
  return d

print(concatdict(dict1, dict2))