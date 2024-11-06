l = [[1,2],3,[4,5,6]]
l2 = [1,2,3]


def nested_sum(l):
  ret = 0
  for i in len(l):
    ret = ret + sum(l[i])
  return ret

nested_sum(l)
