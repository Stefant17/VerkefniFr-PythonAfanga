def countdown(fil, s):
  b = []
  c = list(s)
  with open(fil) as f:
    for i in f.read().splitlines():
      if len(i)<4:
        break
      c = list(s)
      for l in range(len(i)):
        if c.__contains__(i[l]):
          if(l == len(i)-1):
            b.append(i)
          c.pop(c.index(i[l]))
        else: 
          break
    f.close()
  return b