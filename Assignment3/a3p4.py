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
Linear Congruential Hacker
"""

from sys import flags

def crack_lcg(m, r1, r2, r3):
    """
    Return the values a and b that would be used to LCG generate r1, r2, and r3
    r1 = (a * r0 + b) % m 
    r2 = (a * r1 + b) % m
    ...
    returns [a, b] or [0, 0] if no solution 
    """
    
    # Solve for b using eq 3
    # b = r3 - r2*a % m -- Solve "b"  for  once you find "a" with this equation

    # Solve for a using eq 2 and the re-written form of eq 3
    # r2 = (r1*a + r3 - r2*a) % m - INITIAL STEPS in a3p3 in a3.txt
    # r2 = (a*(r1-r2) + r3) % m

    if (r1 - r2) == 0:
        a = 0 # We already know, "a" is 0
    else:
        # We do not need to worry about dividing by 0 because it is taken care of above
        a = (r2 - r3)/(r1 - r2) # Expression for a using eq 2 and 3

        top = (r2 - r3)  # Define top
        
        # First Make sure that  top is divisible by the bottom
        # If it is not divisible, add modulo to the top until it is divisible.
        while (top % (r1 - r2)) != 0:
            top = top + m
        
        a = int((top / (r1 - r2)) % m)  # Using the new "top" value

        while (a<0):
            a = a + m      # To make sure "a" is always a positive value

    # b = r3 - r2*a % m ------- Re-written form of eq 3

    b = int(r3 - r2*a % m) # Solve for "b" using the value of "a" found above

    while (b<0):
        b = b + m      # To make sure "b" is always a positive value

    return [a, b]

def test():
    """
    Basic tests for crack_lcg
    """

    # Test cases created using a3p2.py

    try:
        assert crack_lcg(475, 23, 20, 436) == [178, 201] # Test from Q3
        assert crack_lcg(654321, 34, 34, 34) == [0, 34]
        assert crack_lcg(1234567890, 795041, 18285943, 420576689) == [23, 0]
        assert crack_lcg(3456, 2568, 1602, 288) == [123, 234]
        print("All test PASSED")
    except:
        print("One or more test FAILING")


if __name__ == "__main__" and not flags.interactive:
    test()
