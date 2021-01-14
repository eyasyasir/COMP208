# Author: [Eyas Hassan]
# McGill ID: [260776234]
# Assignment 1, Question 2

def find_first(s, letter): #function which searches for first parenthesis '(' from left of string
    for i in range(len(s)): #for loop evaluates every characte in string 's' and compares it to variable 'letter', if true, the index at which the condition is true is returned (i.e position of '(')
        if s[i] == letter:
            return i
    return None #if there are no paranthesis in the string, none is returned

def find_last(s, letter): #function which searches for last parenthesis ')' from left of string
    i = -1
    while i >= (- len(s)): #while loop evaluates every characte in string 's' and compares it to variable 'letter', if true, the index at which the condition is true is returned (i.e position of ')')
        if s[i] == letter:
            return i
        i = i - 1
    return None #if there are no paranthesis in the string, none is returned

def get_comma_phrase(s): #funtion which replaces '(' with ',' and removes ')' from string 's'
    letter = "(" #setting variable 'letter' to string '(' in order to call function 'find_first()'
    a = find_first(s, letter) #function 'find_first()' is called with parameters 's' and 'letter', assigned to variable 'a'
    letter = ")" #setting variable 'letter' to string ')' in order to call function 'find_first()'
    b = find_last(s, letter) #function 'find_last()' is called with parameters 's' and 'letter', assigned to variable 'b'
    phrase = s[a + 1 : b] #string slicing on 's' to give segment of string 's' between '(' and ')', assigned to variable ' phrase
    phrase = "{}".format(",") + phrase #'.format()' method is used to insert ',' in the beginning of 'phrase', assigned to variable 'phrase'
    s = s[ : a] + phrase #altered segment of 's' ('phrase') is added to unaltered segment of 's', assigned to variable 's'
    return s #function returns value of 's'

def get_comma_string(s): #function which counts how many paranthesis pairs exist in 's' and calls fucntion 'get_comma_phrase()' the required number of times
    counter = 0
    for parenthesis in range(len(s)): #iterating through every character in string 's'
        if s[parenthesis] == "(": #if a paranthesis '(' is found, the counter is updated
            counter += 1
    i = 0
    while i < counter: #while loop which runs until all parenthesis pairs are removed from 's'
        s = get_comma_phrase(s)
        i = i + 1
    return s #function returns value of 's'

s = input("Enter text: ") #taking user input and assigning it to variable 's'
print(get_comma_string(s)) #value of function 'get_comma_string(s)' is printed to screen
