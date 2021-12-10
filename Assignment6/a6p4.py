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
Problem 4
"""

from sys import flags
import a6p3
import a5p1_Module

def breakSub(ciphertext, textFile, n):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

     # Uses the function from assignment 5 to give the mapping using frequency analysis
    mapping = a5p1_Module.freqDict(ciphertext) # Mapping Dictionary
    d = {" ": " "} # add the space character mapping to itself
    mapping.update(d) # Update the mapping dict so that it includes the space character as well

    frequencies = {}                    # FORGOT TO MAKE THIS - I JUST MADE THIS LOOP. EVERYHTING ELSE IS UNCHANGED
    for i in range(len(LETTERS)):
        d = {LETTERS[i]:textFile[i]}
        frequencies.update()
    
    BestMapping = a6p3.bestSuccessor(mapping, ciphertext, frequencies, n) # Obtains the best mapping from a6p3

    # Another function of Assginment 5 is used here to decipher the ciphered text using the bestMapping.
    BestDecipherment = a5p1_Module.freqDecrypt(BestMapping, ciphertext)

    # return the best deciphered text possible using the Hill-Climbing Substitution cipher
    return(BestDecipherment)
        
def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    
if __name__ == "__main__" and not flags.interactive:
    test()
