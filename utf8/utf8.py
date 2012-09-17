#!/usr/bin/env python

import sys


def parse(li):
  t = li.rstrip().split()
  a = "".join(t[2:5])
  b = t[-1]
  return a,b

def main(filename):  
  fp = open(filename, "r")
  ls = fp.readlines()
  fp.close()
  s = []
  for l in ls:
    if not l.startswith("#"):
      a, b = parse(l)
      x = int(a, 16)
      y = ord(b[0]) * 65536 + ord(b[1]) * 256 + ord(b[2])
      if x != y:
        print x,y
      else:
        s.append(b)
    else:
      sys.stderr.write(l)
  return s

if __name__ == "__main__":
  s = main(sys.argv[1])
  s.sort()

  t = 0
  for w in s:
    print 'u"%s",'%w,
    t = t + 1
    if t % 25 == 0:
      print


"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  t = [ i for i in range(s[0], s[-1]+1) ]
#  print s[0], s[-1], t[0], t[-1]
  
  
#  print len(s)
#  print len(t)#

#  for i in s:
#    print i


#  for i in s:
#    t.remove(i)
#  for i in t:
#    try:
#      print unichr(i),
#    except:
#      pass

"""
