#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2020 Shridhar Patel
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
Linear Congruential Generator
"""

from sys import flags

def lcg(a, b, m, r0):
    """
    Generate random numbers using 
    R_i+1 = (aR_i + b) (mod m) 
    for i = 1 to i = 10 
    r0: seed value to begin at
    """
    FinalList = [] # Final list to be returned

    for i in range(0, 10):
        r = ((a*r0 + b) % m) # The formula given to us
        FinalList.append(r) # Append to the list
        r0 = r # Defind the new r0 as current r
        
    return FinalList 
    


def test():
    "Run tests"
    # Provided test
    assert lcg(22695477, 1, 2**32, 42) == [953210035, 3724055312, 1961185873, 1409857734,
                                          3384186111, 3302525644, 1389814845, 444192418,
                                          2979187595, 2537979336]

if __name__ == '__main__' and not flags.interactive:
    test()
