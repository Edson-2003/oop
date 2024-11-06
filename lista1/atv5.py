def is_sorted(l:list):
  t = l
  t.sort()
  for i in range(0,len(l)):
    if(l[i] != t[i]):
      return False
  return True

l1:list = [1, 2, 2]
l2:list = ['b', 'a']

print(is_sorted(l1))
print(is_sorted(l2))