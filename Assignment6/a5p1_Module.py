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
Subsititution cipher frequency analysis
"""

from sys import flags
from collections import Counter # Helpful class, see documentation or help(Counter)

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def freqDict(ciphertext: str) -> dict:
    """
    Analyze the frequency of the letters
    """
    if len(ciphertext) == 0: # If the input given is empty. 
        raise Exception("Ciphered text string to be decrypted is Empty")
    
    # Find of the lenght of the Letters in the text excluding any symbols, punctuations and spaces. 
    ciphertextLengthNOsymbol = 0
    for char in (ciphertext.upper()):
        if char in LETTERS:
            ciphertextLengthNOsymbol += 1

    Dict = {} # Add the characters to the Dictionary. 
    for char in (ciphertext.upper()):
        if char in LETTERS:
            if char in Dict: 
                Dict[char] += 1 # Increment if already exists
            else: 
                Dict[char] = 1 # Add it if it does not exist

    # Add the defualt value of "0" to the Characters that is not part of the input text.
    for letter in LETTERS:
        if letter not in Dict.keys():
            Dict[letter] = 0

    # Turn the frequency from number to percentage
    # New value (frequncy of characters) of the keys will be in percentage.
    for key, value in Dict.items():
        newValue = (value*100/ciphertextLengthNOsymbol)
        Dict[key] = newValue

    # Frequncy Statistics provided to us
    ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    ETAOIN = list(ETAOIN) # Conver to list

    # Sort the Dictionary items by values in decending order
    # Such that the most frequent letter appears in the first place. 
    sortedDict = (sorted(Dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
    swappedList = [] # Initializing a list which will have correspoting letter instead of % frequency.

    # For loop below breaks the tie (if frequency is same) by 
    # taking the first letter in the ETAOIN.
    i = 0 # iterator used to swap the percentage for the corresponding letter.
    for items in sortedDict:
        if items[1] > 0: # Only if the value is greater than 0
            items = list(items)
            swappedList.append([items[0], ETAOIN[i]]) # Append the letter at the "i"th position
            i += 1                                    # then increment the i
        else:
            swappedList.append([items[0], "0"]) # If value is 0, then just append "0"

    # Return the dictionary instead of the list
    return (dict(swappedList))

def freqDecrypt(mapping: dict, ciphertext: str) -> str:
    """
    Apply the mapping to ciphertext
    """

    ciphertextList = [] # Conver the string to list and uppercase all the characters
    for elements in ciphertext:
        ciphertextList.append(elements.upper())


    decipheredList = []     # initialize a list
    for i in ciphertextList:
        if i in LETTERS: # If the currect character is a Letter
            if i in ciphertextList: # And i is in the character's list
                index =  ciphertextList.index(i) # Find out it's index in ciphertextList
                decipheredList.append(mapping.get(i)) # Append the value based on the mapping
                ciphertextList.remove(i)              # remove the i from the ciphered list
                ciphertextList.insert(index, "_")     # and insert a black there instead so that
                                                      # in next loop it is not recognize.
        else:           # if I is anything other than a letter
            decipheredList.append(i) # then just append it without minipulating it
    deciphered = "".join(decipheredList) # join the deciphered list

    return deciphered # And return it

def test():
    # TEST 1 - was given
    assert type(freqDict("A")) is dict
    assert freqDict("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")["A"] == "E"

    # TEST 2 - simple one
    text = "AAAABBBCCD"
    mapping = freqDict(text)
    assert freqDecrypt(mapping, text) == "EEEETTTAAO"

    # TEST 3 - to check every letter with a decreasing frequnecy to check if frequency works.
    A = "A"*26
    B = "B"*25
    C = "C"*24
    D = "D"*23
    E = "E"*22
    F = "F"*21
    G = "G"*20
    H = "H"*19
    I = "I"*18
    J = "J"*17
    K = "K"*16
    L = "L"*15
    M = "M"*14
    N = "N"*13
    O = "O"*12
    P = "P"*11
    Q = "Q"*10
    R = "R"*9
    S = "S"*8
    T = "T"*7
    U = "U"*6
    V = "V"*5
    W = "W"*4
    X = "X"*3
    Y = "Y"*2
    Z = "Z"*1

    ciphertext = A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z
    mapping = freqDict(ciphertext)
    assert freqDecrypt(mapping, ciphertext) == "EEEEEEEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTTTTTAAAAAAAAAAAAAAAAAAAAAAAAOOOOOOOOOOOOOOOOOOOOOOOIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSSSSSSSSSHHHHHHHHHHHHHHHHHHHRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLCCCCCCCCCCCCCCCUUUUUUUUUUUUUUMMMMMMMMMMMMMWWWWWWWWWWWWFFFFFFFFFFFGGGGGGGGGGYYYYYYYYYPPPPPPPPBBBBBBBVVVVVVKKKKKJJJJXXXQQZ"

# Invoke test() if called via `python3 a5p1.py`
# but not if `python3 -i a5p1.py` or `from a5p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()