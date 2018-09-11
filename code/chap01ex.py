"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import pandas as pd
import sys
import re

#import nsfg
#import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)

    # Read the code book!

    # Use gzip to unzip the .gz file
    # example:
    #import gzip
    #f = gzip.open('file.txt.gz', 'rb')
    #file_content = f.read()
    #f.close()

    # The data file has fixed column widths
    # Dictionary file contains information for each variable
    # Need to read in dictionary file
    # D:\stat\ThinkStats2\code\2002FemResp.dct
    CNUM, VTYPE, VLEN, VNAME, VDESC = [], [], [], [], []
    colnumo = 0     #last pass column number
    for line in file("2002FemResp.dct"):
        array1 = line.split()
        if len(array1) > 4:
            colnum = re.sub('[^0-9]','',array1[0])      #keep digits only
            vartype = re.sub('[0-9]','',array1[1])      #remove digits (i.e. str12)
            varlen = re.sub('[^0-9]','',array1[3])
            varname = array1[2]
            desc   = ' '.join(array1[4:]) #combine the last 'n' indexes into 1 string
            #print(colnum, vartype, varlen, varname, desc)
            CNUM.append(int(colnum))
            VTYPE.append(vartype)
            VLEN.append(int(varlen))
            VNAME.append(varname)
            VDESC.append(desc)

    # VNAME will be used for the column names in the dataframe
    # Can't use the description also. Maybe just create a 
    # dictionary for variable names and descriptions
    VARDESC = dict(zip(VNAME, VDESC)) # **need a better naming conv**

    # Read in data file
    with open('2002FemResp.dat', 'r') as data_file:
        rawdata = data_file.read()
        rawdata = rawdata.split('\n')

    # In what order do I manipulate the data and build the dataframe?
    # Read the lines and get the variables one at a time.
    # Once I have finished getting a column of data, append it to the
    # data frame.

    # Test: Get indexes from .dat file
    INDX = []
    start = CNUM[0]-1       #0
    end = start + VLEN[0]   #12
    for i in range(len(rawdata)):
        INDX.append(int(rawdata[i][start:end].strip()))

    # Creat log file for debuggin
    log = open('chap01ex.log', 'w')

    # When creating the Data Frame, do we use the caseid's as the index,
    # or give them a column in the data frame?
    # df = pd.DataFrame(data, index=INDX, columns=VNAME)
    data = {}
    for i in range(len(VNAME)):
        log.write('variable name: '+VNAME[i]+'\n')
        dvalues = []
        start = CNUM[i]-1
        end = start + VLEN[i]
        for j in range(len(rawdata)):
            # Determine if the value is an int, float, or other?
            # What about a ":" ? ...time? ...maybe just leave as string?
            if VTYPE[i] == 'str':
                dvalues.append(str(rawdata[j][start:end].strip()))
            elif (VTYPE[i] == 'byte') \
                 or (VTYPE[i] == 'float') \
                 or (VTYPE[i] == 'double'):
                try:
                    dvalues.append(float(rawdata[j][start:end].strip()))
                except ValueError:
                    # try to print errors, but ignore strings with whitespace only
                    if rawdata[j][start:end].strip(' '):
                        print('byte:', rawdata[j][start:end])
                        log.write('byte, '+str(rawdata[j][start:end])+', '+str(j)+'\n')
                    dvalues.append(np.nan)
            else:       # this else assumes only integers are left
                try:
                    dvalues.append(int(rawdata[j][start:end].strip()))
                except ValueError:
                    if rawdata[j][start:end].strip(' '):
                        print('int:', rawdata[j][start:end])
                        log.write('int, '+str(rawdata[j][start:end])+', '+str(j)+'\n')
                    dvalues.append(np.nan)
        data[VNAME[i]] = dvalues
    log.close()
    # Is this redundant below? I already made a dictionary that contains
    # the variable names. Do I need it again? Does "data" need to be a dict?
    df = pd.DataFrame(data, index=INDX, columns=VNAME)


    # Variables used in the book: caseid, prglngth, outcome,
    # pregordr, birthord, birthwgt_lb & birthwgt_oz, agepreg, 
    # finalwgt

    # Need a function to clean the variables we will use
    # agepreg - listed in centiyears
    # birthwgt_* - can have alternate codes (i.e. 97 - don't know)

    # Validate imported data by calculating some sums and
    # comparing to the published data.
    return df


if __name__ == '__main__':
    main(*sys.argv)
