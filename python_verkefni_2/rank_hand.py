import re

def rank_hand(l):
  number_cards = []
  color_cards = []
  cards = ''
  str_nbr= ''
  cards = cards.join(l)
  for i in range(0,10,2):
    number_cards.append(cards[i])
  for i in range(1,10,2):
    color_cards.append(cards[i])
  number_cards.sort()
  str_nbr= ''.join(number_cards)
  #check if all cards are from the same sort 
  if all(x == color_cards[0] for x in color_cards):
      #check if all cards are uniqe
    if ((len(number_cards)) == (len(set(number_cards)))): 
      #check if all cards are letters
      if str_nbr.isalpha():
        return 9
    #check if straight flush with letters and numbers
    if(re.search('[8][9][J][Q][T]', str_nbr))or (re.search('[7][8][9][J][T]', str_nbr))or (re.search('[6][7][8][9][T]', str_nbr))or (re.search('[2][3][4][5][A]', str_nbr)or (re.search('[9][J][K][Q][T]', str_nbr))):
      return 8
    #check if straight flush with no letters
    if(str_nbr.isdigit()):
      if(((int(str_nbr[0]))== (int(str_nbr[1])-1)) and ((int(str_nbr[0]))  == (int(str_nbr[2])-2)) and ((int(str_nbr[0])) == (int(str_nbr[3])-3)) and ((int(str_nbr[0])) == (int(str_nbr[4])-4))):
        return 8
    #if all same color then at least it is a flush 
    return 5
  #check if regular flush with letters and numbers
  if(re.search('[8][9][J][Q][T]', str_nbr))or (re.search('[7][8][9][J][T]', str_nbr))or (re.search('[6][7][8][9][T]', str_nbr))or (re.search('[2][3][4][5][A]', str_nbr)or (re.search('[9][J][K][Q][T]', str_nbr))or(re.search('[A][J][K][Q][T]', str_nbr))):
    return 4
   #check if regular flush with no letters
  if(str_nbr.isdigit()):
    if(((int(str_nbr[0]))== (int(str_nbr[1])-1)) and ((int(str_nbr[0]))  == (int(str_nbr[2])-2)) and ((int(str_nbr[0])) == (int(str_nbr[3])-3)) and ((int(str_nbr[0])) == (int(str_nbr[4])-4))):
      return 4
   #4 of a kind 
  for i in number_cards: 
    if ( number_cards.count(i) == 4):
      return 7
    # full house and 3 pair
    if ( number_cards.count(i) == 3):
      for f in number_cards:
        if(number_cards.count(f) == 2 and i != f):
          return 6
      return 3

   #two pair and full house check
    if ( number_cards.count(i) == 2):
      for f in number_cards:
        if(number_cards.count(f)== 2 and i != f):
          return 2
        if(number_cards.count(f) == 3 and i != f):
          return 6
      return 1
  return 0