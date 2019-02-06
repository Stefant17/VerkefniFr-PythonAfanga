def duplicates(s):
  a = []
  
  for item in range(len(s)):
    for item2 in range(len(s)):
      if item < item2 and s[item] == s[item2] and s[item] not in a:
        a += [s[item]]
  return a