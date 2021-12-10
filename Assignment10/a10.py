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
Assignment 10
"""

from sys import flags

PUNCTUATION = ' ,.!?@#$%^&*()~`+-' # Defind common punctuations
sampleDict = {} # For Problem 1
sampleDPD = {} # For Problem 2

def computeSSDs(text):
    if text in sampleDict: # If the SSDs is already created for the text:
        return (sampleDict.get(text)) # Return the value of the "text"
    else: # If it is not calculated already, then calculate it
        freqList = [] # List of frequencies
        try:
            for char in text: # For char in the given text
                if (char not in PUNCTUATION) and (char.isalpha()==True) : # If it is not a punctuation
                    freq = (text.count(char)/len(text)) # Count it's frequency
                    if freq not in freqList: # if that frequency is not in the list already
                        freqList.append(freq) # append that frequency to the list
        except: # except
            True # Just continue
        freqList = sorted(freqList, reverse=True) # Sort that FreqList in decreasing order
        d = {text:freqList} # create a dictionary with text being the key and FreqList is value
        sampleDict.update(d) # Updated the created dictionary into sampleDict.
        return (sampleDict.get(text)) # Return The sampleDict's value of the key:"text"


def cliSSD(ciphertext: str, files): 
    ciphertext = ciphertext.lower() # Lower the ciphertext
    SSDsList = [] # SSDsList initiated
    finalDict = {} # FinalDict to be returned

    for sample in files: # loop len of files number of times
        text = open(sample, encoding='UTF-8', errors="ignore").read() # Open the i-th sample text
        text = text.lower() # Lower the sample text
        SSDsList.append(computeSSDs(text)) # compute the SSDS and append it to the SSDsList
    
    cipherFreq = [] # To get the cipher Frequency
    try: # Try the following
        for char in ciphertext: # get char of the ciphertext
            if char not in PUNCTUATION: # Make sure it is not a punctuation
                freq = (ciphertext.count(char)/len(ciphertext)) # get it's frequency
                if freq not in cipherFreq: # if the freq is not already in CipherFreq,
                    cipherFreq.append(freq) # Then append this frequency to CipherFreq list
    except:
        True # Except just continue
    cipherFreq = sorted(cipherFreq, reverse=True) # Sort this list in the decreasing order. 

    length = 0 # Set length to 0
    j = 0 # J is for incrementing purposes
    for SSDs in SSDsList: # Loop SSDs in the SSDsList
        length = max(len(SSDs), len(cipherFreq)) # Set the length to max of SSDs or cipherFreq
        sumP = 0 # Set sum equal to 0
        for i in range(length): # loop length number of times
            try:
                sumP = sumP + (SSDs[i] - cipherFreq[i])**2 # Calculate the sum based on the given formula
            except:
                if len(SSDs) > len(cipherFreq): # if one is bigget than the other
                    sumP = sumP + (SSDs[i] - 0)**2 # if one of it is out of range, set it equal to 0
                else: # If the other is bigger
                    sumP = sumP + (0 - cipherFreq[i])**2 # if other of it is out of range, set it equal to 0

        d = {files[j]: sumP} # create a dictionary with key being the sample file and value is the sum
        finalDict.update(d) # Update the finalDict
        j += 1 # increment

    return (finalDict) # Return the final Dictionary

def computeDPD(text):
    if text in sampleDPD: # If the text is already in Sample DPD
        return (sampleDPD.get(text)) # Return the sampleDPD value of the key - "text"
    else: #if it doesn't already exist,
        textMinipulate = text.lower() # lower the text
        textMinipulate = textMinipulate.split() # split the text to get words
        
        pattern = [] # initiate to find patters
        for word in textMinipulate: # For each word in the text
            decompDict = {} # This is the decomposition dictionary
            for char in word: # for every char in that word,
                count = word.count(char) # Count that char in the word
                d = {char: count} # Create a dictionary with key=char and value=count
                decompDict.update(d) # update the dictionary
            tup = [] # initiate the tuple
            for key, value in decompDict.items(): # for the key and value in dict
                tup.append(value) # Append the value to the tuple
            pattern.append(sorted(tup, reverse=True)) # append theSort the tuple in ascending order in pattern
        
        textDict = {} # Initiate text dictionary
        for item in pattern: # for item in the patterns
            count = (pattern.count(item)/len(pattern)) # find the frequency of the pattern
            d = {tuple(item): count} # Create a dictionary with key being the tuple and value being the freq
            textDict.update(d) # Update the dictionary
        
        d = {text: textDict} # create a dictionary with text being the key and textDict being the value
        sampleDPD.update(d) # Update the dictionary
        return (sampleDPD.get(text)) # Return the dictionary's value of the key: "text"

def cliDPD(ciphertext: str, files):
    # ciphertext = "SEEMS BEAMS WERE" # just for initial testing
    ciphertext = ciphertext.lower() # lower the ciphertext
    ciphertext = ciphertext.split() # split the cipher text into words
    
    pattern = [] # initiate to find patters
    for text in ciphertext: # For each word in the text
        decompDict = {} # This is the decomposition dictionary
        for char in text: # for every char in that word,
            count = text.count(char) # Count that char in the word
            d = {char: count} # Create a dictionary with key=char and value=count
            decompDict.update(d) # update the dictionary
        tup = [] # initiate the tuple
        for key, value in decompDict.items(): # for the key and value in dict
            tup.append(value) # Append the value to the tuple
        pattern.append(sorted(tup, reverse=True)) # append theSort the tuple in ascending order in pattern
    
    ciphertextDict = {} # initiate ciphertextDict
    for item in pattern: # for each tuple in the pattern
        count = (pattern.count(item)/len(pattern)) # get the frequency of the tuple
        d = {tuple(item): count} # create a dictionary with tuple being the key and count being the value
        ciphertextDict.update(d) # update the dictionary
    
    DPDList = [] # initiate the list of DPD
    for sample in files: # for each sample,
        text = open(sample, encoding='UTF-8', errors="strict").read() # open the sample file
        text = text.lower() # lower the text read above
        DPDList.append(computeDPD(text)) # Compute the DPD of text and append it to the list
    
    finalDict = {} # Initiate the frequency
    j = 0 # for incrementing purposes
    for DPD in DPDList: # For each DPD in the list
        sumP = 0 # initiate the sum
        for key, value in ciphertextDict.items(): # for the key and value i the dict,
            try:
                sumP = sumP + (value - DPD.get(key))**2 # Use the formula given in the questions
            except:
                sumP = sumP + (value - 0)**2 # If the value doesn't exist, use "0"

        d = {files[j]: sumP} # create the dictionary with sample file name being the key and sum being the value
        finalDict.update(d) # update the dictionary
        j += 1 # increment for next loop
    
    return (finalDict) # return the finalDict
  
def test():
    print("\n")


if __name__ == "__main__" and not flags.interactive:
    test()


    # -------------------------Code below was used for text and Q3 and Q4-------------------------------
    # text1 = cliSSD(open("texts/ciphertext_en_1.txt", "rt", encoding="utf8").read(), ["texts/sample_en.txt", "texts/sample_es.txt"])
    # print(text1)
    # text2 = cliDPD(open("texts/ciphertext_en_1.txt", "rt", encoding="utf8").read(), ["texts/sample_en.txt", "texts/sample_es.txt"])
    # print(text2)
    # -----------------------------code below was used for Q3 and Q4------------------------------------
    # l = ["bg", "de", "el", "en", "es", "fr", "it", "nl", "pl", "ru"]

    # for i in l:
    #     for j in range(10):
    #         string = "texts/ciphertext_" + i + "_" + str(j) + ".txt"

    #         text = cliDPD(open(string, "rt", encoding="utf8").read(), ["texts/sample_en.txt", "texts/sample_es.txt", "texts/sample_bg.txt", "texts/sample_de.txt", "texts/sample_el.txt", "texts/sample_fr.txt", "texts/sample_it.txt", "texts/sample_nl.txt", "texts/sample_pl.txt", "texts/sample_ru.txt"])
    #         fileName = min(text, key=text.get)
            
    #         finalAnswer = string + " " +  fileName + "Score: "
    #         print(finalAnswer)