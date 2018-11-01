"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    # input argument is a Hist object; custom built by author
    # Get the list of values. Loop through values to get a list
    # of frequencies. Get the max frequency. Find index of value
    # for associated max frequency.

    v = hist.Values()
    f = []
    for value in v:
        f.append(hist.Freq(value))

    mv = v[f.index(max(f))]

    return mv


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    # Use built-in sort function
    # write function for "key" that takes second 
    # element as sort variable

    def takeSecond(elem):
        return elem[1]

    v = hist.Values()
    comb = []
    for value in v:
        comb.append((value,hist.Freq(value)))

    comb.sort(key=takeSecond, reverse=True)

    return comb


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
