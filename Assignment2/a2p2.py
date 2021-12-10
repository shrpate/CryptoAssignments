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

def encryptMessage(key:list, message: str):
    messageList = [] # initialize an empty list

    # Put the message in the list; each character separated by comma
    for letter in message:
        messageList.append(letter)

    cipheredMessage=[] # initialize an empty final empty list

    # append whole column at key[0] then the column at key[1] and so on.    
    for col in key:
        # If len(message) is divisible by len(key)
        if (len(message) % len(key)) == 0:
            # Append the charaters cipheredMessage
            for row in range(int(len(message)/len(key))):
                # picks out a whole column specified by the key and then moves on
                currentLetter = messageList[(col-1) + len(key)*row]
                cipheredMessage.append(currentLetter)
        
        #If len(message) is not divisible by len(key)
        else:
            try:
                # Using the "try" becuase we are adding the +1 in the for loop which gives an index error 
                # when it goes out of range. So when it throws an error, stop because it is already done. 
                for row in range(int(len(message)/len(key))+1):
                    # picks out a whole column specified by the key and then moves on
                    currentLetter = messageList[(col-1) + len(key)*row] # Row 1, Row 2 ... Row n (whole column)
                    cipheredMessage.append(currentLetter)
            except:
                pass

    return ("" . join(cipheredMessage))

def test():
    assert encryptMessage([2,4,1,5,3], "CIPHERS ARE FUN") == "IS HAUCREERNP F"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
