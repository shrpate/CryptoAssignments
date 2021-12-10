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
Problem 2
"""

from sys import flags

def keyScore( mapping: dict, ciphertext: str, frequencies: dict, n: int ) -> float:

    ciphertext = list(ciphertext) # Enlist the ciphertext. No cleanup required as it is already been done for us.

    # Attempt to decipher.
    deciphere = []
    for value in ciphertext:
        newValue = mapping.get(value) # Get the the letter that the currect letter is mapping to.
        deciphere.append(newValue) # Append it to decipher list.

    # another deciphering list    
    ngramDecipher = []
    loop = (len(deciphere)-n+1) # Define the length once again
    for i in range(loop): # Loop this for loop as definded above
        for j in range(n):
            try: # if it goes out of range, then that means it is done, so just continue
                ngramDecipher.append(deciphere[j+i]) # Append to ngramDecipher.
            except:
                continue # if out of range, then just continue. It means it is done

    i = 0
    # Join the characters as one ngram
    for j in range(int(len(ngramDecipher)/n)):
        # So now, ngramDecipher will be the list of ngrams as desired
        ngramDecipher[i : n+i] = [''.join(ngramDecipher[i : n+i])] # Join the characters in ngrams strings
        i = i+1 # increment

     # Make a copy so the ngramDecipher list is not mest up as the list will need to be edited.
    duplicateNgramDecipher = ngramDecipher.copy()

    score = 0 # currect score is 0
    for key,value in frequencies.items():
        c = 0 # find out how many times it occurs. Currently it is 0
        while key in duplicateNgramDecipher:
            c += 1 # if the key appears in the list, increment.
            duplicateNgramDecipher.remove(key) # After incrementing it, remove it from the list so it is not counted twice.
        score += c*value # Use the formula given to us. NewScore = currectscore + (c(g)*f(g))
    # Return the accumulated ngram score
    return(score)

def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking

if __name__ == "__main__" and not flags.interactive:
    test()