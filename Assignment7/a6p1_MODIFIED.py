#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 2.0
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
Problem 1
"""

from sys import flags
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ' # Letters WITH the "space" character

def ngrams(textFile, n: int) -> dict:

    # Read the given file and Capitalize all letters
    # f = open(textFile, encoding="utf8")
    text = textFile.upper()
    
    # Clean up the letters and remove any symbols. Store it as list. 
    textList = []
    for i in text:
        if i in LETTERS:
            textList.append(i)

    ngram = [] # N-Gram list 
    loop = (len(textList)-n+1) # Define the number of loops required to make the ngram List.

    # loop this for loop as definded above by the loop variable
    for i in range(loop):
        for j in range(n):
            # Try and if it throws an index error, that means it is done so in that case the continue. 
            try:
                ngram.append(textList[j+i]) # Append the current ngram into the nGram list. 
            except:
                continue # if it is out of range, just continue because this means it is done. 
    
    # Join the ngram characters into one single ngram. So this will be a list of actual ngrams as
    # shown in Q1 example of nGram List.
    i = 0
    for j in range(int(len(ngram)/n)):
        # Below is the link that was used for this:
        # https://www.geeksforgeeks.org/python-merge-list-elements/
        ngram[i : n+i] = [''.join(ngram[i : n+i])]
        i = i+1

    # # Create a the Dictionary that is to be returned. # FREQUENCY CODE IS ELIMINATED 
    # ngramDict={}
    # for item in ngram:
    #     if item in ngramDict:
    #         value = ((ngramDict.get(item))*len(ngram)) # Find out the percent of time it occurs in ngramDict
    #         newValue = ((value+1)/len(ngram)) # Convert the percent value to an integer and increment it. 
    #         ngramDict.update({item: newValue}) # Update the dict with the updated values. 
    #     else:
    #         value = (1/len(ngram)) # if the ngram is not in the dict, put it in. 
    #         ngramDict.update({item: value}) # Update the dict with value 1/length of ngram list.

    # # once the Dict is ready, return it.
    # return(ngramDict)

    return (ngram)

def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking

if __name__ == "__main__" and not flags.interactive:
    test()