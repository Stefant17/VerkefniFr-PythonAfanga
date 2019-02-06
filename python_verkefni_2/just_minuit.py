def jam(string):
  persons = []
  final = {}
  strung = ''
  #create list of all people in string
  for i in string.splitlines():
    b = i.split(',')
    for a in range(1,len(b)-1):
      strung += b[a]
      if(' with ' in b[a]):
        if ((b[a].split(' with ', 1))[1].strip()) not in persons:
          persons.append(b[a].split(' with ')[1].strip())
        if (b[a].split(' with ')[0].strip()) not in persons:
          persons.append(b[a].split(' with ')[0].strip())
      if ' plus ' in b[a]:
        b[a] = b[a].replace('plus', '')
      if (' and ' in b[a]):
        if (b[a].split(' and ')[0]).strip() not in persons:
          persons.append(b[a].split(' and ')[0].strip()) 
        if (b[a].split(' and ')[1]).strip() not in persons:
          persons.append(b[a].split(' and ')[1].strip())
      if(' with ' not in b[a] and ' and ' not in b[a] and ' plus ' not in b[a]):
        if b[a].strip() not in persons:
          persons.append(b[a].strip())
  #create a string that does not contain the first or last colom (date and subject) ("strung")
  #count how manny times that persons name appears in string
  persons.sort()
  for i in persons: 
    a = strung.count(i)
    final[i] = a
  return final
