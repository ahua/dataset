#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import jieba
import operator
import string

def get_str(f):
    with open(f) as fp:
        return fp.read()

def get_token_list(s):
    return jieba.cut(s, cut_all=True)

d = {}

def get_sorted_d(token_list):
    for token in token_list:
        if d.has_key(token):
            d[token] += 1
        else:
            d[token] = 1

    data = []
    sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_d

def format(k, v):
    try:
        k = k.encode("utf8")
    except:
        pass
    return "%s %s" % (k, v)


if __name__ == "__main__":
    s = get_str(sys.argv[1])
    token_list = get_token_list(s)
    sorted_d = get_sorted_d(token_list)
    for k, v in sorted_d:
        print format(k, v)

        

