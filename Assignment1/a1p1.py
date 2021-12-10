#!/usr/bin/python3

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
CMPUT 331 Assignment 1 Student Solution
September 2020
Author: Shridhar Patel
"""

# every symbol that can be encrypted or decrypted
LETTERS = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

def encrypt(message: str, key: str):
    # Initialize the empty string of encrypted message
    eMessage = ''

    key = LETTERS.find(key) # shift every letter by "key" number

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # number of the given letter
            num = num + key # shifted number by the "key" amount

            # Create Wrapper to go from Z to A again so index doesn't go out of range
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            # keep adding encrypted letters to existing eMessage
            eMessage = eMessage + LETTERS[num]
        else:
            eMessage = eMessage + symbol # keep it as it is if not a letter (ie. !%123 etc.)

    return eMessage 

def decrypt(message: str, key: str):
    # Initialize the empty string of original/decrypted message
    dMessage = ''

    key = LETTERS.find(key) # shift every letter back by "key" number

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # number of the given letter
            num = num - key # shifted number back by the "key" amount
            
            # Create Wrapper to go from Z to A again so index doesn't go out of range
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            # keep adding decrypted letters to existing dMessage
            dMessage = dMessage + LETTERS[num]
        else:
            dMessage = dMessage + symbol # keep it as it is if not a letter (ie. !%123 etc.)
    return dMessage

def test():
    assert decrypt(encrypt("foo", "g"), "g") == "foo"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
