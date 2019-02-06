import json
import urllib.request

def count_names(t):
  fjoldi1 = 0
  fjoldi2 = 0
  url = 'http://mooshak.ru.is/~python/names.json'
  responce = urllib.request.urlopen(url)
  data = responce.read()
  a = json.loads(data)
  for i in a:
    if (i['Nafn']).startswith(t):
      fjoldi1 += int(i['Fjoldi1'])
      fjoldi2 += int(i['Fjoldi2'])
  tup = (fjoldi1, fjoldi2)
  return tup
