# -*- coding: utf-8 -*-

def words(s):
    occur = {}

    if "\n" in s:
        s = s.replace("\n", " ")
    if "\t" in s:
        s = s.replace("\t", " ")

    lwrds = s.split(" ")

    for w in lwrds:
        key = ""

        try:
            key = int(w)
        except ValueError:
            key = w

        if not key in occur.keys():
            occur[key] = lwrds.count(w)
            
    if "" in occur.keys():
        del(occur[""])

    return occur
