def decrypt(li):
  a = len(li)
  b = ''
  for i in range(0, a, 3):
    b += li[i]
  return b