#!/usr/bin/python

from resources import Pmf

def remaining_lifetime(pmf, age):
    rem = Pmf.Pmf()
    for val, prob in pmf.Items():
        if val > age:
            rem.incr(val - age, prob)
    
    rem.Normalize()
    return rem
