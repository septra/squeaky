import re
import pandas as pd

def remove_digits(arg):
    return remove_functionality(arg, "[0-9]")

def remove_letters(arg):
    return remove_functionality(arg, "[A-Za-z]")

def remove(arg, chars):
    return remove_functionality(arg, "[%s]" % chars)

def remove_functionality(arg, regexp):
    if type(arg) == str:
        return re.sub(r'%s' % regexp, '', arg)

    elif type(arg) == list:
        return map(lambda x: re.sub(r'%s' % regexp, '', x), arg)

    elif type(arg) == pd.core.series.Series:
        return arg.apply(lambda x: re.sub(r'%s' % regexp, '', x))
