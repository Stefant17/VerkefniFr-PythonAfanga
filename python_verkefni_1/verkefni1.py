def cdo(n):
  a = []
  a = n.split()
  a.sort()
  str = ' '.join(a)
  return str

print(cdo('in theory there is no difference between theory and practice'))

def duplicates(s):
  a = []
  
  for item in range(len(s)):
    for item2 in range(len(s)):
      if item < item2:
        if s[item] == s[item2]:
          a += [s[item]]
  return a

print(duplicates([1,2,3,4,2,4, 'item', 'item']))

def flattend(n):
  print("á eftir að gera")
  return n 
flattend([2,3,4])

def rm_duplicates(n):
  a = []
  n.sort()
  for item in range(len(n)-1):
    if n[item] == n[item+1]:
      a.append(n[item])
  return a

print(rm_duplicates([18, 7, 1, 15, 15, 1, 19]))

def scarmble(li, li2):
  a = []
  for number in li2:
    a.append(li[number])
  return a

print(scarmble([100, 42, 4, 1337], [1,3,2,0]))

def excel_index(s):
  a = len(s)
  final = 0
  for number in range(a):
    final += (((ord(s[number]))-64)*(26**(number)))
  return 'wrong in mushak'

print(excel_index('LOL'))

def birthdays(s):
  a = []
  s =[x.split() for x in s.splitlines()]
  for id in range(len(s)):
    for id2 in range(len(s)):
      if id< id2:
        if s[id] == s[id2]:
          a.append(s[id])
  return a

print(birthdays('''0212862149
0407792319
0212849289
1112792819
0407992939
0212970299'''))

def process_ls(n):
  b = n.split()
  a = n.splitlines()[0]
  l = len(a.split())
  c = []
  for a in range(l):
    for i in range(a,len(b),l):
      c.append(b[i])
  return c

print(process_ls("""acpid.pid console-kit-daemon.pid lock pm-utils sdp upstart-socket-bridge.pid
acpid.socket crond.pid mdm.pid postgresql sendsigs.omit.d upstart-udev-bridge.pid
apache2 crond.reboot mdm_socket pppconfig shm user
apache2.pid cups motd resolvconf udev utmp
avahi-daemon dbus mount rsyslogd.pid udisks wicd
console dhclient.pid network samba udisks2 wpa_supplicant
ConsoleKit initramfs plymouth screen upstart-file-bridge.pid"""))