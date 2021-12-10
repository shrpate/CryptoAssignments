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
Problem 3
Version 1.2
"""

from sys import flags
import a6p2


def bestSuccessor(mapping, ciphertext, frequencies, n):

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    originalMapping = mapping # OriginalMapping is the mapping we were given.

    # Find out the ngram score of this mapping and it is so far the "best"
    # So assign this score as the bestKeyScore
    bestKeyScore = a6p2.keyScore(originalMapping, ciphertext, frequencies, n)
    
    # Original magging is, by far, the best mapping as we only have 1.
    bestMapping = originalMapping.copy()

    # loop twice
    for key1 in range(len(LETTERS)): # 0 to 26 (number of char in LETTERS)
        for key2 in range(key1+1, len(LETTERS)): # x to 26 (currectkey, x, to number of char in LETTERS)
            
            keyONE = LETTERS[key1] # Get the char at the currect LETTER position (eg. C)
            keyTWO = LETTERS[key2] # SAME as above. It will be a char after the key above (eg. Q. It cannot be "A")

            TempMapping = originalMapping.copy() # Use the temporary as original mapping

            value1 = TempMapping.get(keyONE) # Get value of key 1
            value2 = TempMapping.get(keyTWO) # Get value of key 2

            TempDict = {keyONE: value2, keyTWO:value1} # swap the values
            TempMapping.update(TempDict) # Updated the dict with swapped values

            # After swapping the values, get it's score
            score = a6p2.keyScore(TempMapping, ciphertext, frequencies, n)

            if score == bestKeyScore: # if the new score is equal to the best score,
                # Use the function given to us to break ties and find out the best mapping
                bestMapping = breakKeyScoreTie(originalMapping, TempMapping, bestMapping)
            
            elif score > bestKeyScore: # if the new score is better than the currect best,
                bestKeyScore = score # new best score is obtained.
                bestMapping = TempMapping.copy() # Thus, currect mapping is new best mapping.
    
    # In the end, return the best mapping. (could be original or newly obtained mapping with best ngram score)    
    return(bestMapping)

def breakKeyScoreTie(originalMapping, successorMappingA, successorMappingB):
    """
    Break the tie between two successor mappings that have the same keyscore

    originalMapping: mapping the the other parameters are successors to
    successorMappingA: mapping that has had two keys swapped
    successorMappingB: mapping that has had two other keys swapped

    Example usage:
    originalMapping = {"A": "A", "B": "B", "C": "C"}
    # Mapping with B and C switched
    successorMappingA = {"A": "A", "B": "C", "C": "B"}
    # Mapping with A and C switched
    successorMappingB = {"A": "C", "B": "B", "C": "A"}

    # AC < BC so this function will return successorMappingB
    assert breakKeyScoreTie(originalMapping, successorMappingA, successorMappingB) == successorMappingB

    """
    aSwapped = "".join(sorted(k for k, v in (
        set(successorMappingA.items()) - set(originalMapping.items()))))
    bSwapped = "".join(sorted(k for k, v in (
        set(successorMappingB.items()) - set(originalMapping.items()))))
    return successorMappingA if aSwapped < bSwapped else successorMappingB


def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    assert breakKeyScoreTie({"A": "A", "B": "B", "C": "C"}, {"A": "A", "B": "C", "C": "B"}, {
                            "A": "C", "B": "B", "C": "A"}) == {"A": "C", "B": "B", "C": "A"}
    assert breakKeyScoreTie({"A": "A", "B": "B", "C": "C", "D": "D"}, {
                            "A": "B", "B": "A", "C": "C", "D": "D"}, {"A": "A", "B": "B", "C": "D", "D": "C"}) == {"A": "B", "B": "A", "C": "C", "D": "D"}


if __name__ == "__main__" and not flags.interactive:
    test()
