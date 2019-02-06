def sum_no_3(n):
  b= 0
  for item in n:
    if ((item-3)% 10) != 0:
      b += item
  return b