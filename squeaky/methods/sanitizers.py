import re
import pandas as pd

def remove_digits(arg):
    """
    Removes any digits in the passed object.
    Accepts: String, List of Strings, Pandas series Object

    eg:
    squeaky.remove_digits(["hello123", "442 Avenue"])
    >>> ["hello", "Avenue"]
    """
    return remove_functionality(arg, "[0-9]")

def remove_letters(arg):
    """
    Removes any letters in the passed object.
    Accepts: String, List of Strings, Pandas series Object

    eg:
    squeaky.remove_letters(["hello123", "442 Avenue"])
    >>> ["123", "442 "]
    """
    return remove_functionality(arg, "[A-Za-z]")

def remove(arg, chars):
    """
    Removes a user-specified range of characters.
    Accepts: String, List of Strings, Pandas series Object

    eg:
    squeaky.remove(["hello123", "442 Avenue"], "e2")
    >> ["hllo13", "44 Avnu"]
    """
    return remove_functionality(arg, "[%s]" % chars)

def remove_functionality(arg, regexp):
    if type(arg) == str:
        return re.sub(r'%s' % regexp, '', arg)

    elif type(arg) == list:
        return map(lambda x: re.sub(r'%s' % regexp, '', x), arg)

    elif type(arg) == pd.core.series.Series:
        return arg.apply(lambda x: re.sub(r'%s' % regexp, '', x))
