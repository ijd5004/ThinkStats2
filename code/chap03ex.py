from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2

def PmfMean(pmf):
    """Returns the mean of a PMF

    pmf: Pmf object

    returns: value from Pmf
    """
    mean = 0.0

    for value, prob in pmf.Items():
        mean += value*prob

    return mean

def PmfVar(pmf):
    """Returns the variance of a PMF

    pmf: Pmf object

    returns: value from Pmf
    """
    mean = PmfMean(pmf)

    var = 0.0

    for value, prob in pmf.Items():
        var += prob*(value - mean)**2

    return var


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    first_pmf = thinkstats2.Pmf(firsts.prglngth)

    # test PmfMean    
    tsmean = first_pmf.Mean()
    mean = PmfMean(first_pmf)
    print('PMF mean of firsts preg length', mean, tsmean)
    assert mean == tsmean, mean

    # test PmfVar
    tsvar = first_pmf.Var()
    var = PmfVar(first_pmf)
    print('PMF var of firsts preg length', var, tsvar)
    assert var == tsvar, var

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)