#!/usr/bin/env python3

# ---------------------------------------------------------------
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
# ---------------------------------------------------------------

"""
Assignment 9 Problem 1
"""

from sys import flags
from typing import List, Tuple

def finitePrimeHack(t: int, n: int, e: int) -> Tuple[int, int, int]:
    """
    Hack RSA assuming there are no primes larger than t
    """
    ListPrime = [] # initiate an empty list of Prime Numbers
    for num in range(0, t+1):  
        if num > 1:  # Only if the number is bigger than 1
            for i in range(2,num):  
                if (num % i) == 0:  # If it is a composite number, then ignore
                    break  
            else:  
                ListPrime.append(num) # Add the Prime number to the list

    p = 0 # Set the default value of p is equal to 1
    q = 0 # Set the default value of q is equal to 1

    for i in ListPrime: # Loop in prime number list
        for j in ListPrime: # Loop in prime number list again
            if i*j == n: # if p*q is equal to n
                if (i <= j): # AND p is smaller than q
                    p = i # Find p
                    q = j # Find q
                    break

    m = (p-1)*(q-1) # Use the formula from the notes to find the m
    e = e % m # initiate
    d = 0 # Set the default value of d is equal to 1

    for i in range(1,m): # loop m number of times
        if ((e * i) % m == 1): # find the right value for i that is between 0 and m
            d = i # Call this i, d
    
    finalList = [p, q, d] # finalList is p, q and d

    return finalList # return the final list


def test():
    "Run tests"
    assert finitePrimeHack(100, 493, 5) == [17, 29, 269]
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking


# Invoke test() if called via `python3 a5p1.py`
# but not if `python3 -i a5p1.py` or `from a5p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()

    ################### IGNORE THE REST - it was used for testing ###########################################
    # finitePrimeHack(100, 493, 5)

    k1 = finitePrimeHack(70000, 2448536107, 2328775521)
    print(k1)
    k2 = finitePrimeHack(25000000000,2357022193,1635820081)
    print(k2)
    # k3 = finitePrimeHack(2**14,7739,79)
    # print(k3)
    # k4 = finitePrimeHack(2**14,8137,79)
    # print(k4)
    # k5 = finitePrimeHack(2**14,4757,103)   
    # print(k5)
