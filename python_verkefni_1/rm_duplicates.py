def rm_duplicates(n):
  n.sort()
  a = n.copy()
  for item in range(len(n)-1):
    if n[item] == n[item+1]:
      a.remove(n[item])
  return a
