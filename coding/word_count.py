#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import datetime
import string
import codecs

from cncharset import cn_char_dict
 
CHANESE = u"！”#￥%&‘（）*+，-。/：；《=》？@【、】……——`『』|～"
ASCII = unicode(string.whitespace + string.printable)
OTHERS = u"¤· “”"

DEL_SET = CHANESE + ASCII + OTHERS

def is_not_blank(char):
  if char in DEL_SET:
    return False
  return True

def delete_blank_char(li):
  return filter(is_not_blank, li)

def parse_line(li, word_len=2):
  chars = delete_blank_char(li)
  return [ chars[i:i+word_len] for i in range(0, len(chars) - word_len + 1) ]

def main(datafile, word_len=2):
  fp = codecs.open(datafile, "r", "utf-8")
  lines = fp.readlines()
  d = {}
  for li in lines:
    for word in parse_line(li, word_len):
      d[word] = d[word] + 1 if d.has_key(word) else 1
  return d

def print_dict(d):
  l = sorted(d, key=d.get, reverse=True)
  for k in l:
    print k.encode('utf8'), d[k]

"""
usage:
$ prog file [wordlen]
"""

if __name__ == "__main__":
  start = datetime.datetime.now()
  
  argc = len(sys.argv)
  if argc == 3:
    d = main(sys.argv[1], int(sys.argv[2]))
  elif argc == 2:
    d = main(sys.argv[1])
  else:
    d = main("test.in")

  print_dict(d)
  
  for k in d.iterkeys():
    if len(k) > 1: 
      break
    if k not in cn_char_dict:
      print >> sys.stderr, k.encode("utf8"),
  end = datetime.datetime.now()

  print >> sys.stderr, "Start at:", start 
  print >> sys.stderr, "End at:", end




