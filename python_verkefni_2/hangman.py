
def hangman(origin, state, caracters):
  caracters = caracters
  is_allowed = 0
  allowed_caracters = 'abcdefghijklmnopqrstuvxyz'
  final = []
  index_caracters = []
  for i in range(len(state)):
    if state[i] != '-':
      index_caracters.append(i)
  with open(origin) as f:
    for a in f.read().splitlines():
      d = index_caracters.copy()
      d.reverse()
      if (len(a)) == (len(state)):
        for b in range(len(a)):
            if b in index_caracters:
              if a[b] == state[b]:
                d.pop()
              else: 
                break
        if  len(d) == 0:
         is_allowed = 0
         for e in range(len(a)):
            if a[e].isupper():
              is_allowed = -1
              break
            if ((a[e]) in (list(caracters))):
              if e not in index_caracters:
               is_allowed = -1
               break
            for i in range(len(allowed_caracters)):
               if (a[e]) not in (list(allowed_caracters)):
                  is_allowed = -1
                  break
                
         if (is_allowed == 0):
           final.append(a)
           is_allowed = -1
  f.close()
  return final
