def sum_two(a,b):
  print(a)
  print(b)
  return a + b

sum_two(1,2)

def mod_sum(n):
  b= 0
  for item in range(n):
    if item%3 == 0:
      b += item
    elif item%5 == 0:
      b += item
  return b

print(mod_sum(8))
def sum_no_3(n):
  b= 0
  for item in n:
    if ((item-3)% 10) != 0:
      b += item
  return b

print(sum_no_3([1, 13, 15, 1]))

def sum_first(l , n):
  if (len(l) < n):
    return sum(l)
  return sum(l[0:n])

print(sum_first([-1,2,3,-4,5,-6,7,8,9,10], 7))

def list_product(l1, l2):
  b= len(l1)
  c = []
  for i in range(b):
    c += [l1[i]*l2[i]]
  return c

print(list_product([1,2,3,4,5,6], [1,2,3,4,5,6]))

def remove_empty(li):
  c = []
  for i in li:
    if i != '':
      c.append(i)
  return c

print(remove_empty(['python', '', '', 'is', 'awsome']))

def decript(li):
  a = len(li)
  b = ''
  for i in range(0, a, 3):
    b += li[i]
  return b

print(decript('AQltQptoAaQPcmokPY ToaFKtBe WEdvAagrwpknDJ!yX'))

def gymnastics(li):
  a = len(li)
  if a < 3:
    return sum(li)
  li.sort()
  li.pop(a-1)
  li.pop(0)
  a = len(li)
  return int((sum(li))/a)

print(gymnastics([1,13,15,2]))

def boom(n):
  s = []
  for i in range(1,n+1):
    if i % 7 == 0:
      s.append('BOOM')
    elif '7' in str(i):
      s.append('boom')
    else:
      s.append(str(i))
    
  return s



print(boom(20))
