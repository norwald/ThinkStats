#!/usr/bin/python

import math
import first
from resources import thinkstats

def main():
    first_stats = first.First()
    first_births, other_births = first_stats.partition_live_birds()
    
    first_births_gestation = map(lambda record: record.prglength, first_births)
    other_births_gestation = map(lambda record: record.prglength, other_births)
    
    first_mean, first_var = thinkstats.MeanVar(first_births_gestation)
    other_mean, other_var = thinkstats.MeanVar(other_births_gestation)

    print 'First pregnancies duration summary'
    print "mean: {0} variance: {1} standard deviation {2}".format(first_mean, first_var, math.sqrt(first_var))

    print 'Other pregnancies duration summary:'
    print "mean: {0} variance: {1} standard deviation {2}".format(other_mean, other_var, math.sqrt(other_var))


if __name__ == "__main__":
    main()
