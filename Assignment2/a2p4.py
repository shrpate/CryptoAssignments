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
CMPUT 331 Assignment 2 Student Solution
September 2020
Author: Shridhar Patel
"""

def decryptMessage(key:list, message: str):
    messageList = [] # initialize an empty list

    # Put the message in the list; each character separated by comma
    for letter in message:
        messageList.append(letter)

    decipheredMessage=['x' for i in range(len(message))] # initialize an empty final empty list

    i=0 # to increment through the message, letter by letter. 
    for col in key:
        if (int(len(message)) % (len(key))) == 0:
            # Only if the len(message) is divisible by the len(key)
            for row in range(int(len(message)/len(key))):

                    # Take the current letter and copy it in the given position in the decipheredMessage list.
                    decipheredMessage[(col-1) + len(key)*row] = messageList[i]
                    i = i+1 # Next letter
        else:
            try:
                # Try because we are adding "+1" here in the for loop below so if the index goes 
                # out of range,then stop because that means it is done. 
                for row in range(int(len(message)/len(key))+1):
                     # Take the current letter and copy it in the given position in the decipheredMessage list.
                    decipheredMessage[(col-1) + len(key)*row] = messageList[i]
                    i = i+1 # Next letter.
            except:
                pass # if it goes out of range then exit because that means it is done deciphering. 

    return ("" . join(decipheredMessage))

def decryptMystery():
    messageFile = open("mystery.txt","r", encoding="utf8") # Open the ciphered text file

    # Use the decryptMessage function above with the following key given. 
    decipheredText = decryptMessage([8,1,6,2,10,4,5,3,7,9], (messageFile.read())) 

    decryptFile = open("mystery.dec.txt", "w+") # Create a new file in the "write" mode

    try:
        decryptFile.write(decipheredText) # Try writting the file (shouldn't be any error as the key is hard coded)
        print("'mystery.dec.txt' was successfully created in the current directory.\n\n") # If successful, print this. 
    except:
        print('Error occured, please check the message and try again.\n\n') # Print this if it fails.
    
    return decipheredText


def test():
    assert decryptMessage([2,4,1,5,3], "IS HAUCREERNP F") == "CIPHERS ARE FUN"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
