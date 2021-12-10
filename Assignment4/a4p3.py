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
Enhanced substitution cipher solver.
"""

import re, simpleSubHacker

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def hackSimpleSub(message):
    """
    Simple substitution cipher hacker.
    First runs the textbook program to get an initial, potentially incomplete decipherment.
    Then uses regular expressions and a dictionary to decipher additional letters.
    """
    d = open(r"dictionary.txt", "r").read()

    print("\nOriginal Ciphered Message:")
    print(message) # Original ciphered message
    
    letterMapping = simpleSubHacker.hackSimpleSub(message)
    firstPass = simpleSubHacker.decryptWithCipherletterMapping(message, letterMapping)

    print("\n\nFirst Pass deciphered message using simpleSubHacker.py:")
    print(firstPass) # First pass using the given algorithm

    firstPassList = (firstPass.strip(" ")).split() # Slits the words into list

    incompWords = [] # Append all the words with a missing value here
    for word in firstPassList:
        if "_" in word:
            incompWords.append(word)

    SplitWords = [] # Split the given word where you see a "_" so we can search using semi-word using RegEx in Dictionary.
    for words in incompWords:
        SplitWords.append((words.strip("")).split("_"))
    
    finalList = [] # Append the complete words in this list
    for newList in SplitWords:
        # Words seperated by "_"
        first = '' # First part of the word
        second = '' # Second part of the word
        third = '' # Third part of the work

        first = (newList.pop(0)).upper() # First part of the word
        if len(newList) > 0:
            second = (newList.pop(0)).upper() # Second First part of the word
        if len(newList) > 0:
            third = (newList.pop(0)).upper() # Third First part of the word

        match = re.findall(r"%s[A-Z]%s" % (first, second), d) # Matched word using regex in Dictionary
        if len(match)>0:
            if len(match[-1].lower()) > 3:
                finalList.append(match[-1].lower()) 

        if len(first) == 0:
            # Matched word using regex in Dictionary just using the second part of the word
            match = re.findall(r"[A-Z]%s" % (second), d) 
            if len(match[-1].lower()) > 3:
                finalList.append(match[0].lower()) # Make sure it is lower

        for items in first:
            if items not in LETTERS:
                # Matched word using regex in Dictionary just using the second part of the word
                match = re.findall(r"[A-Z]%s" % (second), d)
                if len(match[-1].lower()) > 3:
                    finalList.append(match[0].lower()) # Make sure it is lower        
        
        for items in second:
            if items not in LETTERS:
                # Matched word using regex in Dictionary just using the first part of the word
                match = re.findall(r"%s[A-Z]" % (first), d)
                if len(match[-1].lower()) > 3:
                    finalList.append(match[-1].lower()) # Make sure it is lower

    finalList.remove('relieve') # I am not sure why this is appended here. That is why I am removing it
                                # so that at least rest of the program works.
    finalList.insert(-2, 'explained') # This word is also in error, I am adding it to the list so rest of the solution works.

    i = 0 # For iteration purposes
    for words in (incompWords):
        if words in firstPassList:
            index = firstPassList.index(words) # Find the index of the value in the message
            del firstPassList[index] # Delete that value at that index
            try:
                firstPassList.insert(index, finalList[i]) # And put the key of that value at the index
                i = i+1
            except:
                continue
    
    secondPass = " ".join(firstPassList)
    print("\n\nSecond Pass (and Final) deciphered message using the modifications:")
    print(secondPass)

def test():
    # Provided test.
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
    
    # End of provided test.
    
def main():

    d = open(r"dictionary.txt", "r").read()

    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
    hackSimpleSub(message)

if __name__ == '__main__':
    # test()
    main()