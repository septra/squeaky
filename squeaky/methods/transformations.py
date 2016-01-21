import pandas as pd

def categorize(column, max_val, min_val, binwidth):
    """Take in list of numbers (Column) and user-specified binwidth (binwidth)
        and return the mapping of values to bins"""
    #max_val = max(column)
    #min_val = min(column)
    labels = [ "{0} - {1}".format(i, (i + binwidth - 1))
                for i in range(min_val, max_val + binwidth, binwidth)
             ]
    groups = pd.cut(column,
                    range(min_val-1, max_val + binwidth*2, binwidth),
                    right=True,
                    labels=labels)
    zipped = {}
    for n, entry in enumerate(column):
        zipped[entry] = groups[n]
    return zipped
