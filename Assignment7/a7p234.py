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
Assignment 7 Problems 2, 3, and 4
"""

from sys import displayhook, flags
from typing import Tuple
import vigenereHacker


def stringIC(text: str):
    """
    Compute the index of coincidence (IC) for text
    """
    
    N = len(text) # N is the length of the given text
    ValueDict = {} # Initiate a value Dictionary

    for char in text: # For characters in text:
        if char in ValueDict: # if that char is in Value dictionary already:
            value = ValueDict.get(char) # Get that char's value
            newValue = value+1 # increment that value
            updateNewValue = {char:newValue} # update the new value
            ValueDict.update(updateNewValue) # update the Dictionary with new value

        else: # if that char is not in Value dictionary:
            initiate = {char:1} # Make that char a key and give it a value of 1.
            ValueDict.update(initiate) # update the key,value in the dictionary.
    
    c = 0 # Sum - starts at 0
    for key,value in ValueDict.items(): # Get the value from the Dictionary
        c += value*(value-1) # Add the current value to Sum 
    
    IC = c/(N*(N-1)) # Calculate the IC from the given formula.
    return IC # Return the IC

def subseqIC(ciphertext: str, keylen: int):
    """
    Return the average IC of ciphertext for 
    subsequences induced by a given a key length
    """

    IC = 0 # start the IC at 0
    for i in range(keylen): # get keylen number of different subsequences
        subsequence = vigenereHacker.getNthSubkeysLetters(i+1, keylen, ciphertext) # get the subsequence at 1,2,3...n
        IC = IC + stringIC(subsequence) # keep summing the IC for each subsequences.
    
    AVG = IC/keylen # find out the average by diving the total IC with keylen

    return AVG # return the average

def keyLengthIC(ciphertext: str, n: int):
    """
    Return the top n keylengths ordered by likelihood of correctness
    Assumes keylength <= 20
    """

    Dict = {} # initialize the dictionary
    for i in range(1,21): # Find keylen up to 20 (21-1 = 20).
        AVG = subseqIC(ciphertext, i) # Get the average IC of keylen from 1,2,3...20
        d = {i:AVG} # make i the key and average the value.
        Dict.update(d) # update the dictionary with this key,value
    
    sortedDict = (sorted(Dict.items(), key=lambda x: x[1], reverse=True)) # Sort the Dictionary by values.

    KeyList = [] # initial Keylist (without tie breaking) - initialization
    finalList = [] # final Keylist (WITH tie breaking) - initialization

    for i in range(n): # get top "n" keylens
        KeyList.append(sortedDict[i][0]) # append into KeyList for further tie-breaking

    # Perform the tie-breaking
    try:
        for i in range(len(KeyList)):
            if ((Dict.get(KeyList[i])) == (Dict.get(KeyList[i+1])) and KeyList[i]<KeyList[i+1]): # if the next keylen is bigger and the values are same:
                finalList.append(KeyList[i+1]) # append the next keylen instead the current
            elif ((Dict.get(KeyList[i])) == (Dict.get(KeyList[i-1])) and KeyList[i]>KeyList[i-1]): # if the previous keylen is smaller and the values are same:
                finalList.append(KeyList[i-1]) # append the previous key instead the current
            else:
                finalList.append(KeyList[i]) # if tie breaking is not needed - simply append to finalList

    except: # just continue when it goes out of index
        True
            
    finalList.append(KeyList[-1]) # it will go out of index and miss the last keylen - so append the last to finalList
        
    return(finalList) # return this finalList after tie-breaking process.


def test():
    "Run tests" # Given tests by the TA
    assert stringIC("ABA") == 1 / 3
    assert keyLengthIC('MLWJNMUDUVGPGJGQCYEILSNXKXZXEERRWSYMAIKXTVWLHQWMXWLVTWWLYSJTLWAZGQWGMWWOXRHKHQTEXQXHNV', 8) == [17, 19, 10, 12, 4, 16, 2, 5]
    assert keyLengthIC('DLCAYGMOZBSUXJMHNSWTQYZCBXFOPYJCBYKRRIQOEPOWMWIROWRMEQOWDYVYCWGQRKORRCITORNBSKLPCWJMEV', 8) == [12, 6, 3, 15, 19, 9, 4, 13]
    assert keyLengthIC('OPKUHMTODMWCRSSONWHXYSIIIXJZTGDLHFKVCMYINVVWQHMZIFXTEUZALSEEJWKBVSIAXJIXZVVVBQSPGHNUYE', 8) == [11, 16, 9, 13, 18, 7, 3, 8]
    # the test Below takes care of tie-breaking - instead of 8, 15 - it will be 15, 8 as 15 is > and their values are ==
    assert keyLengthIC('VTTKNKOZVKQICZHZVJGIUAKYKVTTFTBKSIZVTTMXCDTMHOQIYLVOPMXURDLTUEXAGOQCNLGHTHITABVEGYUINT', 8) == [14, 16, 5, 9, 10, 15, 8, 7]

    # This function is ignored in our marking


# Invoke test() if called via `python3 a5p1.py`
# but not if `python3 -i a5p1.py` or `from a5p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()