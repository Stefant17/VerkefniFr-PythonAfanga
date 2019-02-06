import itertools
import json
import re 
def css_properties(css):
  tuples = []
  css = css.split('{')
  for i in css:
    a = i.split('}')[0]
    a = a.splitlines()
    for b in a:
      b = b.split(';')
      for c in b:
        c.strip()
        if ':' in c:
          c = c.split(':')
#        for l in range(len(c)):
#          c[l].strip()
          tuples.append(tuple(c))
  return  tuples

  #kominn m]e -etta fyrir utan tarf ad stripa og tad er ekki haegt


print(css_properties("""
#LasVegas .billboard { text-decoration: blink; }

.ninja, #Snowden { visibility: hidden; }


.oliveoil
{
  z-index: 1;
}
.water
{
  z-index: 0;
}

#poop {
  float  : none  ;
  color  : brown ;

  width  : 15cm  ;
  height : 120cm ;
}

.God { position: absolute; display: none; }
#blackhole { padding: -9999em; }

.word {  font-family:    "Comic Sans", "Times New Roman", sans-serif  ;  }
"""))