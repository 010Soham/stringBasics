'''
Problem Statement: Modify the existing brute force string matching algorithm to return the index of the last occurrence of the pattern in the text instead of the first. If the pattern is not found, return -1.

Example:

Input:
Text (str): "hellohello"
Pattern (pattern): "lo"
Expected Output: 7 (index of the last 'l' in the second "hello" in the text)
'''

def func1(str,pattern):
    if len(pattern) == 0:
        return -1
    
    last_occurence = -1
    
    for i in range(len(str)-len(pattern)+1):
        stri=i
        patterni = 0

        while stri < len(str) and patterni < len(pattern) and str[stri] == pattern[patterni]:
            stri+=1
            patterni+=1

        if patterni == len(pattern):
            last_occurence = i

    return last_occurence


inputText = "hellohello"
patternText = "lo"
print(func1(inputText,patternText) )
