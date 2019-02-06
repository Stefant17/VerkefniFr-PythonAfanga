import re
def valid(s):
  c = s
  sum = 0
#  for i in range(0, 10, 2):
#    sum += int(c[i]) 
#  for i in range(1,10, 2):
#    a = int(c[i])*2
#    if a >9:
#     a = (int(str(a)[0]))+(int((str(a)[1])))
#     sum += a
#  if sum%10 != 0:
#    return False
  s.split()
  s[0].join(s[1])
  if re.search('((([0-2][0-9])|([3][0]))(([0][469])|([1][0]))[0=9][0-9][2-9][0-9][0-9][09])|((([0-2][0-9])|([3][1]))(([0][^469])|([1][02]))[0=9][0-9][2-9][0-9][0-9][09]|)|((([0-1][0-9])|([2][0-8]))[0][2][0=9][0-9][2-9][0-9][0-9][09])', s):
    return True
  return False