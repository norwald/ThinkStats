#!/usr/bin/python

import survey


"""
Calculates average of list of numbers

Args:
 list of numbers

Returns:
 average of numbers in list

"""
def Average(list):
    return float(sum(list)/len(list))


"""
Calculates number of live birds

Args:
 list of pregnancy records

Returns:
 number of live birds
"""
def CalcLiveBirths(preg_records):
    live_births = 0
    for record in preg_records:
        if record.outcome == 1:
            live_births += 1

    return live_births

"""
Partitions live birds in first-time birds and other

Args:
 list of pregnancy records

Returns:
 tupple (records first-time babies, records other babies)
"""
def PartitionLiveBirds(preg_records):
    first_births = []
    other_births = []
    for record in preg_records:
        if record.outcome == 1:
            if record.birthord == 1:
                first_births.append(record)
            else:
                other_births.append(record)
 
    return first_births, other_births

"""
Calculate average birth length

Args: 
 list of pregnancy records

Returns:
 average pregnancy length of list's elements
"""
def AveragePreg(records):
    prg_sum = 0.0
    for record in records:
        prg_sum += record.prglength
   
    return float(prg_sum/len(records))

def init():
   table = survey.Pregnancies()
   table.ReadRecords()
   return table

def main():
    table = init()
    print 'Number of pregnancies: ', len(table.records)
    print 'Number of live births: ', CalcLiveBirths(table.records)
    
    first_births, other_births = PartitionLiveBirds(table.records)
    print 'Number of first-time births', len(first_births)
    print 'Number of not first-time births', len(other_births)

    avg_first_births = AveragePreg(first_births)
    avg_other_births = AveragePreg(other_births)

    print 'Average duration of first-time pregnancies', avg_first_births
    print 'Average duration of not first-time pregnancies', avg_other_births
    print 'Pregnancy duration difference in days: ', (avg_first_births - avg_other_births) * 7


if __name__ == "__main__":
    main()
