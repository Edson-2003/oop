sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New York"}

def extract(l, d):
  dict = {}
  for i in range(len(l)):
    dict[l[i]] = d[l[i]]
  return dict


print(extract(["name", "age"], sample_dict))