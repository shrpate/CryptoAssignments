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

def encryptMessage(key:int, message: str):

    # Initialize an empty matrix of dim i x j
    # where i = len(message) and j = key     
    matrix = [['0' for i in range(len(message))] for j in range(key)]            
      
    GoingDown = False # Direction by default is up
    row, col = 0, 0 # Initial pointer
      
    for letter in range(len(message)):
        # Vertical pointer. Change the direction of the pointer if on top row or last row
        if (row == 0) or (row == key - 1): 
            GoingDown = not GoingDown # Flip the direction
          
        # Copy the "letter" the pointer is pointing at, into the given matrix position.
        matrix[row][col] = message[letter] 
        col += 1 # move the pointer along
          
        # GO to the next row based on the direction
        # If direction is down, then next row is below it.
        # If direction is up then the next row is above it. 
        if GoingDown: 
            row += 1
        else: 
            row -= 1
    
    # Now read the matrix and ignore all the initial "0" values while reading it. 
    # Write the data text into cipheredMessage
    cipheredMessage = [] # Empty list to write the parsed data
    for i in range(key): 
        for j in range(len(message)): 
            if matrix[i][j] != '0': 
                cipheredMessage.append(matrix[i][j]) # append the letter into the list
    return("" . join(cipheredMessage)) 
   
def decryptMessage(key:int, message: str):

    # Initialize an empty matrix of dim i x j
    # where i = len(message) and j = key     
    matrix = [['0' for i in range(len(message))] for j in range(key)]   

    row, col = 0, 0 # Initial pointer

    for i in range(len(message)): 
        if row == 0: 
            GoingDown = True # if at first row, start going down
        if row == key - 1: 
            GoingDown = False # if at last row, start going up

        matrix[row][col] = 'x' # Place a marker where you need to write.
        col += 1
          
        # Go to the next row based on the direction
        # If direction is down, then next row is below it.
        # If direction is up then the next row is above it. 
        if GoingDown: 
            row += 1
        else: 
            row -= 1
    
    pointer = 0 # Finds the markers which were placed earlier and writes at that position.
    for i in range(key): 
        for j in range(len(message)): 
            if ((matrix[i][j] == 'x') and (pointer < len(message))): 
                matrix[i][j] = message[pointer] # Copy the letter at the pointer into the matrix
                pointer += 1
    
    decipheredMessage = [] # Empty list to write the parsed data
    row, col = 0, 0
    for i in range(len(message)): 
        if row == 0: 
            GoingDown = True # if at first row, start going down
        if row == key - 1: 
            GoingDown = False # if at last row, start going up

        # If this is a "x", ignore as it is just a marker
        if (matrix[row][col] != 'x'): 
            decipheredMessage.append(matrix[row][col]) # append the letter into the list
            col += 1

        if GoingDown: 
            row += 1
        else: 
            row -= 1
    return("".join(decipheredMessage))

def test():
    assert decryptMessage(3, encryptMessage(3, "CIPHERS ARE FUN")) == "CIPHERS ARE FUN"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
