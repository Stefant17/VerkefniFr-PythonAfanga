import csv
import datetime
def release_days(cast,dates,actors):
  actor = []
  monday = []
  tuesday = []
  wednesday = []
  thursday = []
  friday = []
  saturday = []
  sunday = []
  titles = {}
  with open(cast) as ca:
    with open(dates) as da:
      cas = csv.DictReader(ca)
      for row in cas:
        for i in range(len(actors)):
          if row['name'] == str(actors[i]):
            c = [row['title']] + [row['year']]
            actor.append(c)
      dat = csv.DictReader(da)
      for raw in dat:
        for b in actor:
          if b[0] == raw['title'] and b[1] == raw['year'] and raw['country'] == 'USA':
            datee = datetime.date(int(raw['date'].split('-')[0]),int(raw['date'].split('-')[1]),int(raw['date'].split('-')[2]))
            datee = datee.strftime('%A')
            if datee == 'Monday':
              monday.append(raw['title'])
            if datee == 'Tuesday':
              tuesday.append(raw['title'])
            if datee == 'wednesday':
              wednesday.append(raw['title'])
            if datee == 'Thursday':
              thursday.append(raw['title'])
            if datee == 'Friday':
               friday.append(raw['title'])
            if datee == 'Saturday':
              saturday.append(raw['title'])
            if datee == 'Sunday':
              sunday.append(raw['title'])
  if(monday != None):
      titles[1] = monday
  if(tuesday != None):
     titles[2] = tuesday
  if(wednesday != None):
     titles[3] = wednesday
  if(thursday != None):
     titles[4] = thursday
  if(friday != None):
     titles[5] = friday
  if(saturday != None):
     titles[6] = saturday
  if(sunday != None):
     titles[7] = sunday
  return titles