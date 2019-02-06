def gymnastics(li):
  a = len(li)
  if a < 3:
    return int(sum(li)/a)
  li.sort()
  li.pop(a-1)
  li.pop(0)
  a = len(li)
  return int((sum(li))/a)

print(gymnastics([27,4]))