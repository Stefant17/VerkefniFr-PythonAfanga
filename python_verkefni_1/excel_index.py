def excel_index(s):
  final = 0
  s = s.upper()
  s = s.replace(" ", "")
  a = len(s)
  for number in range(a):
    final += (((ord(s[number]))-64)*(26**(a-(number+1))))
  return final
