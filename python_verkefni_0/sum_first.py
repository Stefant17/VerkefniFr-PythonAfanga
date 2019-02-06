
def sum_first(l , n):
  if (len(l) < n):
    return sum(l)
  return sum(l[0:n])