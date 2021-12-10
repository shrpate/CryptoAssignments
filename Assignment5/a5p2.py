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

def evalDecipherment(text1: str, text2: str) -> [float, float]:
    """
    docstring
    """
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_" # Adding an underscore if there is a "blank" in the text

    keyAccuracy = 0 # TWO types of accuracy.
    deAccuracy = 0

    text1List = list(text1.upper()) # Convert it to list and upper case it. 
    text2List = list(text2.upper())
    text1Char = [] # Create two new empty list. 
    text2Char = []

    # For next two for loops, append just the characters in the approriate
    # list as created above. Ignore the symbols, spaces etc.
    for char in (text1List):
        if char in LETTERS:
            text1Char.append(char)
    for char in (text2List):
        if char in LETTERS:
            text2Char.append(char)

    # Count the decryption accuracy
    for i in range(len(text1Char)):
        if text1Char[i] == text2Char[i]:
            deAccuracy += 1
    deAccuracy = (deAccuracy/len(text1Char)) # convert the number into fraction (dividing by length).

    checkedChar = [] # Initialize a checked Character list.
    i = 0 # for incrementing
    for char in text2Char: # if the character in Text 2 of Character's list
        if char not in checkedChar: # And if the Character is not already checked. 
            if char == text1Char[i]: # If the Character is same as the text1 at "i"th position
                keyAccuracy += 1     # Then increment the Key Accuracy
                checkedChar.append(char) # And put the character in the checked list
        i +=1 # increment the i
    
    lengthKeyAccuracyChar = [] # Length of the Key's in total. 
    for char in text1Char: # check the Characters in Text 1 Character's list
        if char not in lengthKeyAccuracyChar: # if the Character is not accounted for already
            lengthKeyAccuracyChar.append(char) # then count it.
    # Divide the total count of Key accuracy by it's length to obtain the fraction.
    keyAccuracy = (keyAccuracy/len(lengthKeyAccuracyChar))

    return([keyAccuracy,deAccuracy]) # Return both Key and Decryption Accuracy. 

def test():
    "Run tests"
    # TEST 1 - Given to us in the question
    text1 = "this is an example"
    text2 = "tsih ih an Ezample"
    assert evalDecipherment(text1, text2) == [0.7272727272727273, 0.7333333333333333]

if __name__ == '__main__' and not flags.interactive:
    test()