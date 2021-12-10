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
Assignment 7 Problem 1
"""

from sys import flags
import sys
import vigenereCipher
import random
import a6p1_MODIFIED

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def antiKasiski(key: str, plaintext: str):
    """
    Thwart Kasiski examination 
    """
    n = 3   # Least number of patters. If patters of 3 doesn't exist, patterns of 4,5,6...,n will not exist.
    
    plaintext = list(plaintext) # En-List the plaintext
    encrypted = vigenereCipher.encryptMessage(key, plaintext) # Encrypt the plaintext using vigenereCipher
    ngramsEncrypted = a6p1_MODIFIED.ngrams(encrypted, n) # Get the ngram of the encrypted text.
    
    finalText = [] # Initiate the final
    loopCount = 0 # Loop Count in while loop below
    Run = True

    while Run: # Run the while loop if True.
        loopCount += 1 # increment the loop count
        for item in ngramsEncrypted: # Take the item in the ngram.
            count = ngramsEncrypted.count(item) # Count how many times it occurs in the list of ngrams
            if count>1: # if it occurs more than multiple times:
                index = ngramsEncrypted.index(item) # Find it's index
                plaintext.insert((index+n), "-") # Insert a dash at that index before the word.

                # Split the plaintext into 2 parts. 1st part is done and 2nd part still needs to be worked on.
                plaintext = (("".join(plaintext))).split("-") # So split the plaintext into two parts at "-"
                finalText.append(plaintext[0]) # Append the 1st part into finalText.
                plaintext = list(plaintext[1]) # Reccursively solve the 2nd part.

                encrypted = vigenereCipher.encryptMessage(key, plaintext) # Encrypt the 2nd part again.
                ngramsEncrypted = a6p1_MODIFIED.ngrams(encrypted, n) # Get the ngram of the 2nd part that is encrypted.
                break # Then break to loop with the updated Encrypted ngram in next iteration.
        
        if loopCount > 1000: # Support the while loop recursion upto 1000 dashes inputs - can be increased of course!
            Run = False # After the loop iterates more than loopCount times, stop running the while loop.

    finalText.append("".join(plaintext)) # Once iterations are done, append the remaining part to finalText.
    
    randomChar = LETTERS[random.randint(0,25)] # Get a random letter from LETTERS
    finalText = (randomChar.join(finalText)) # join the finalText list with this Random Letter
    
    return(finalText) # Return this finalText that is joint with a random letter

def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking


# Invoke test() if called via `python3 a5p1.py`
# but not if `python3 -i a5p1.py` or `from a5p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()

    # -------xxx--------THIS WAS FOR TESTING PURPOSES --------xxx--------
    # Otext = "THOSEPOLICEOFFICERSOFFEREDHERARIDEHOMETHEYTELLTHEMAJOKETHOSEBARBERSLENTHERALOTOFMONEY"
    # text = antiKasiski("WICK", Otext)
    # print(text)