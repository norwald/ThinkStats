#!/usr/bin/python

import first
from resources import Pmf
from resources import thinkstats

def _conditional(pmf, week):
    cond_pmf = Pmf.Pmf()

    for period in range(week, 50):
        cond_pmf.Incr(period, pmf.Prob(period))
    
    cond_pmf.Normalize()
    return cond_pmf.Prob(week)
       


def main():
    stats = first.First()
    records_first, records_other = stats.partition_live_birds()
    live_births = records_first + records_other

    preg_lengths = map(lambda record: record.prglength, live_births)
    pmf = Pmf.MakePmfFromList(preg_lengths)
    print 'Conditional probability of born in week 39, not born before: ', _conditional(pmf, 39)


if __name__ == '__main__':
    main()

