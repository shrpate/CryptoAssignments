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

import detectEnglish

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
    eMessage_NO_SYMBOL = '' # just the letters that needs to be encrypted.

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # number of the given letter

            # To make sure the key is aleays repeating and is bigger than the message
            # The if statement is to make sure the Key doesn't get bigger than necessary to save memory
            if len(key) < len(message): 
                key = key*50

            # This is the reason a eMessage_NO_SYMBOL was initialized. 
            # It makes sure to ignore the spaces and other symbol while finding the 
            # num by adding the right letter of the key to current num.
            num = num + LETTERS.find(key[len(eMessage_NO_SYMBOL)])

            # Create Wrapper to go from Z to A again so index doesn't go out of range
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            # keep adding encrypted letters to existing eMessage
            eMessage = eMessage + LETTERS[num]
            eMessage_NO_SYMBOL = eMessage_NO_SYMBOL + LETTERS[num]
        else:
            eMessage = eMessage + symbol # keep it as it is if not a letter (ie. !%123 etc.)

    return eMessage 

def decrypt(message: str, key: str):
    # Initialize the empty string of original/decrypted message
    dMessage = ''
    dMessage_NO_SYMBOL = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # number of the given letter

            # To make sure the key is aleays repeating and is bigger than the message
            # The if statement is to make sure the Key doesn't get bigger than necessary to save memory
            if len(key) < len(message):
                key = key*50

            # This is the reason a eMessage_NO_SYMBOL was initialized. 
            # It makes sure to ignore the spaces and other symbol while finding the 
            # num by adding the right letter of the key to current num.
            num = num - LETTERS.find(key[len(dMessage_NO_SYMBOL)])
            
            # Create Wrapper to go from Z to A again so index doesn't go out of range
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            # keep adding decrypted letters to existing dMessage
            dMessage = dMessage + LETTERS[num]
            dMessage_NO_SYMBOL = dMessage_NO_SYMBOL + LETTERS[num]
        else:
            dMessage = dMessage + symbol # keep it as it is if not a letter (ie. !%123 etc.)
    return dMessage

def test():
    assert decrypt(encrypt("foo", "g"), "g") == "foo"

from sys import flags

def assignment4():
    dictionary = open("dictionary.txt", "r", encoding="utf8")
    dictionaryList = (dictionary.read().splitlines())
    for i in range(len(dictionaryList)):
        decrypted = decrypt("Koxvcj osuqofr oql lctbfp wkmrres cqs ymra cssmnfdbw wn dnhk bhg qcfsev'r qdxadhzlby cmr wpe qqplb tq vvlkh ks wv ookmu.", dictionaryList[i])

        if detectEnglish.isEnglish(decrypted):
                print('\nPossible encryption hack:')
                print('Key %s: %s' % (dictionaryList[i], decrypted[:200]))
                print('\nEnter D for done, or press Enter')
                response = input('> ')
    print("Hack Failed")

if __name__ == "__main__" and not flags.interactive:

    #test()
    assignment4()
    
