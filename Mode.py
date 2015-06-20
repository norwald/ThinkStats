#!/usr/bin/python

def find_mode(hist, top_n):
    print top_n
    if top_n > len(hist.Items()):
        return 'top_n argument greater than histogram elements!'
   
    return sorted(hist.Items(), key=lambda freq: -freq[1])[0:top_n]

