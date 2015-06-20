#!/usr/bin/python

import first
from resources import Pmf
from resources import thinkstats

def _prob_interval(pmf, start, end):
    if start > end:
        print "Interval start should be greater than interval end"
        return

    sum_p = 0.0
    for week in range(start, end + 1):
        sum_p += pmf.Prob(week)    
    
    return sum_p 

def prob_early(pmf):
    return _prob_interval(pmf, 0, 37)

def prob_on_time(pmf):
    return _prob_interval(pmf, 38, 40)

def prob_late(pmf):
    return _prob_interval(pmf, 41, 50)

def main():
    stats = first.First()
    records_first, records_other = stats.partition_live_birds()
    
    preg_lengths = map(lambda record: record.prglength, records_first)
    pmf = Pmf.MakePmfFromList(preg_lengths)
     
    print 'Probability of early first birth is: ', prob_early(pmf)
    print 'Probability of timely first birth is: ', prob_on_time(pmf)
    print 'Probability of late first birth is: ', prob_late(pmf)
    
if __name__ == '__main__':
    main()

