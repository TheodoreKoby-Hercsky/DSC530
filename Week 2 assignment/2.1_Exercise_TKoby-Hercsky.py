#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DSC 530-T302
week 2
2.1 Exercise: Prepairing for Exploratory Data Analysis
Author: Theodore Koby-Hercsky
06/16/2021
"""

## Display Hello World Message
print('Hello World!')

## Add, Subtract, Multiply, and Divide two numbers
Number_one = 50
print("First Number:", Number_one)
Number_two = 5
print("Second Number:", Number_two)

# Add numbers
print('Numbers added equals:',(Number_one + Number_two))
# Subtract numbers
print('Numbers subtracted equals:',(Number_one - Number_two))
# Multiply numbers
print('Numbers multiplied equals:',(Number_one * Number_two))
# Divide numbers
print('Numbers divided equals:',(Number_one / Number_two))

## Concatenate two strings together
String_one = "In my summer semester I am taking one class titled:"
String_two = " Data Exploration and Analysis"
Both_strings = String_one + String_two
print('Concatenate two strings:',Both_strings)

## Create a list of 4 items and append an item
List_one = ['one', 2, 'three', 4]
print('first list printed:',List_one)
## Append an item to your list
List_one.append('five')
print('List with append:',List_one)

## Create a tuple with 4 items
tuple_one = ("Golden", 1, "retriever", 2)
print('My tuple: ', tuple_one)

"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy as np
import sys

import nsfg
import thinkstats2


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass


def ValidatePregnum(resp):
    """Validate pregnum in the respondent file.

    resp: respondent DataFrame
    """
    # read the pregnancy frame
    preg = nsfg.ReadFemPreg()

    # make the map from caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(preg)
    
    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadFemResp()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(resp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)

