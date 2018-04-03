#!/usr/bin/env/python
"""
Module: chap01ex
Engineer: Ian Davis
Date: January 21, 2018
Revision History:
The purpose of this module is to evaluate pregnancy data.

The program will read in a .dat file.
The program will print the counts for the number
of pregnancies each respondent has had.
The program should cross-validate the results with
the total number of records in the pregnancy file
"""

import nsfg

# Read in 2002 pregnancy data
preg = nsfg.ReadFemPreg()

# Print pregnancy number counts
pcount = preg.pregnum.value_counts().sort_index()
print 'Pregnancy value counts:'
print pcount

# Cross-validate results
#tnum = 0
#for value in pcount:
#    tnum = tnum + value

resp = nsfg.ReadFemResp()
errnum = 0
for caseid in resp.caseid:
    reccount = preg[preg.caseid==caseid].pregnum    #record count per caseid
    pvalue = resp[resp.caseid==caseid].pregnum      #pregnum for each caseid
    indx = pvalue.keys()    #should only be 1 key
    if pvalue[indx[0]] != len(reccount):
        errnum+=1

print '\n'
print 'Number of times pregnum did not match number of records:', errnum
