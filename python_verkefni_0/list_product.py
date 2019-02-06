def list_product(l1, l2):
  b= len(l1)
  c = []
  for i in range(b):
    c += [l1[i]*l2[i]]
  return c