def boom(n):
  s = []
  for i in range(1,n+1):
    if i % 7 == 0:
      s.append('boom!')
    elif '7' in str(i):
      s.append('boom!')
    else:
      s.append(str(i))
    
  return s