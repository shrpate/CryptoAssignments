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
Nomenclator cipher
"""

import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789' # Added Level for a check while deciphering. 

def translateMessage(key, message, mode): # Same translateMessage function as simpleSubCipher.py

    """
    Encrypt or decrypt using a nomenclator.
    Takes a substitution cipher key, a message (plaintext or ciphertext),
    a codebook dictionary, and a mode string ('encrypt' or 'decrypt')
    specifying the action to be taken. Returns a string containing the
    ciphertext (if encrypting) or plaintext (if decrypting).
    """

    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # Loop through each symbol in message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it
            translated += symbol

    return translated


# This function replaces key words given in the codebook with one of it's values (chooses randomly) in the message.
def initialEncryption(key, codebook, message):
    messageLOWER = (message.lower().strip(" ")).split() # Splits the message and puts it into a list. And lowers it.
    keyList = []    # Empty list - List of keys
    for key, value in codebook.items():
        keyList.append(key) # Append all the Keys into the KeyList.


    # If the key appears in message, swap it for one of it's values.
    # Choose any one of the values of the key, randomly, to swap with as the assignment suggests
    for key in (keyList):
        # If the key is in message, then enter.
        # If the key appears more than one time, reapeat the process. Values used to replace the key might be different each time.
        while (key.lower()) in messageLOWER:
            RANDOMVALUE = random.randint(0,((len(codebook.get(key)))-1)) # Choose a random value from all the values of the key.
            value = ((codebook.get(key))[RANDOMVALUE]) # one of the corresponding values of the key.
            index = messageLOWER.index(key.lower()) # Find where the word is located
            del messageLOWER[index] # Delete that word
            messageLOWER.insert(index, value) # And instead, insert one of it's value from the codebook

    messageLOWER = " ".join(messageLOWER) # Join the list to make the sentence.
    return (messageLOWER)

def encryptMessage(key, codebook, message):

    # First use initialEncryption to swap the keys for one of it's values.
    message = initialEncryption(key, codebook, message) 
    # Then use the translateMessage function to encrypt further.
    return translateMessage(key, message, 'encrypt')


def initialDecryption(key, codebook, message):
    messageLOWER = (message.lower().strip(" ")).split() # Splits the message and puts it into a list. And lowers it.
    
    ValueList=[] #Empty list of Values
    for element in messageLOWER:
        for char in element: # look at each charater in the list.
            if char in NUMBERS: # If it is a number (a codebook value), 
                ValueList.append(char) # append it in ValueList
    
    # This function finds the key for the given value. I don't thing python has anyting inbuilt to do this.
    def keyFinder(findKeyFor):
        for key, value in codebook.items(): # Here, value will be a list of values.
            for subValues in value: # Sub-values here will be one of the value in the list of value from above.
                if findKeyFor == subValues: # if the value we passed in argument matches the subvalue we are at,
                    return(key)             # Then return it's key.

    for value in ValueList:
        index = messageLOWER.index(value) # Find the index of the value in the message
        del messageLOWER[index] # Delete that value at that index
        messageLOWER.insert(index, (keyFinder(value))) # And put the key of that value at the index
    
    messageLOWER = " ".join(messageLOWER) # Join the list of the deciphered message and make it a sentence.
    return (messageLOWER)


def decryptMessage(key, codebook, message):
    # Use the translateMessage function to decrypt the message first.
    message = translateMessage(key, message, 'decrypt')
    # Then swap the values in the message for it's key from the codebook.
    return initialDecryption(key, codebook, message)


def test():
    # Provided test.
    key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    message = 'At the University of Alberta, examinations take place in December and April for the Fall and Winter terms.'

    codebook = {'university':['1', '2', '3'], 'examination':['4', '5'], 'examinations':['6', '7', '8'], 'WINTER':['9']}


    cipher = encryptMessage(key, codebook, message)
    decipher = decryptMessage(key, codebook, cipher)

    print("Original Message: ", message)
    print("Enciphered Message: ", cipher)
    print("Deciphered Message: ", decipher)

    # End of provided test.

if __name__ == '__main__':
    test()

