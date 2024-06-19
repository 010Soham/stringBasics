"""
Problem Statement: Write a Python function that uses the brute force method to find all starting indices of the occurrences of a pattern in a given text. Return a list of these indices. If no occurrences are found, return an empty list.

Example:

Input:
Text (str): "test testing test tested"
Pattern (pattern): "test"
Expected Output: [0, 5, 15] (indices of each occurrence of "test" in the string)
"""


def func1(string,pattern):
    occurences = []
    
    if len(pattern) == 0:
        return occurences
    
    possibleStartingIndices = len(string) - len(pattern) +1

    

    for i in range(possibleStartingIndices):
        strI = i
        patternI = 0

        while strI < len(string)  and patternI < len(pattern) and string[strI] == pattern[patternI]:
            strI+=1
            patternI+=1

        if patternI == len(pattern) and occurences[0] == -1:
            occurences.append(i)

        
    return occurences


inputText = "test testing test tested"
patternText = "test"
print(func1(inputText,patternText) )



