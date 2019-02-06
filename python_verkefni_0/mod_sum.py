def mod_sum(n):
  b= 0
  for item in range(n):
    if item%3 == 0:
      b += item
    elif item%5 == 0:
      b += item
  return b