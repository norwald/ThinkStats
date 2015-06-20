#!/usr/bin/python

from resources import survey

class First:

    """
    Calculates number of live birds

    Args:
     list of pregnancy records

    Returns:
     number of live birds
    """
    def calc_live_births(self):
        live_births = 0
        for record in self.get_records():
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
    def partition_live_birds(self):
        first_births = []
        other_births = []
        for record in self.get_records():
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
    def average_preg(self, records):
        prg_sum = 0.0
        for record in records:
            prg_sum += record.prglength
   
        return float(prg_sum/len(records))
    
    def get_records(self):
        return self.table.records

    def __init__(self):
        self.table = survey.Pregnancies()
        self.table.ReadRecords()

def main():
    first = First()
    print 'Number of pregnancies: ', len(first.get_records())
    print 'Number of live births: ', first.calc_live_births()
    
    first_births, other_births = first.partition_live_birds()
    print 'Number of first-time births', len(first_births)
    print 'Number of not first-time births', len(other_births)

    avg_first_births = first.average_preg(first_births)
    avg_other_births = first.average_preg(other_births)

    print 'Average duration of first-time pregnancies', avg_first_births
    print 'Average duration of not first-time pregnancies', avg_other_births
    print 'Pregnancy duration difference in days: ', (avg_first_births - avg_other_births) * 7


if __name__ == "__main__":
    main()

