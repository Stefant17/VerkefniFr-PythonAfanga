import re
def process_ls(n):
  b = re.split(r'\s{2,}|\n', n)
  d = n.splitlines()[0]
  l = len(d.split())
  c = []
  print(len(b))
  for a in range(l):
    for i in range(a,len(b),6):
      c.append(b[i])
  return c