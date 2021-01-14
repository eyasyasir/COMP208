# Author: [Eyas Hassan]
# McGill ID: [260776234]
# Assignment 1, Question 3

import random

# Given a dictionary d and value v,
# find and return the key associated with that value.
# (From the slides.)
def reverse_lookup(d, v):
    for key in d:
        if d[key] == v:
            return key
    return None

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`~-=_+[]{}|;\':",./<>? '

def create_cypher_dictionary(): #function creating dictionary where each character in 'LETTERS' is a key and assigned a random double digit value
    random.seed(1337) # important - please keep this line here.
    cypher = {} # create empty dictionary

    for key in LETTERS: #for loop iterating through every character in 'LETTERS'
        if key not in cypher: #if the character is not in dictionary 'cypher' it is assigned a random double digit value
            cypher_copy = dict(cypher) #creating copy of dictionary to iterate over and avoid infinite loop
            cypher[key] = str(random.randint(0,9)) + str(random.randint(0,9)) #double digit value assigned to each key
            if len(cypher) > 1: #if statement in order to avoid infinite loop of assigning random value to first key in dictionary
                while cypher[key] in cypher_copy.values(): #while loop checks to ensure there are no duplicate values in dictionary, crosschecking with the copy of the dictionary
                    cypher[key] = str(random.randint(0,9)) + str(random.randint(0,9)) #double digit value assigned to each key
    return cypher # return the completed cypher dictionary

def encrypt(s):
    cypher = create_cypher_dictionary() # get the cypher dictionary
    encrypted_s = ""
    
    for letter in s: #for loop iterates over every character in 's' and replaces it with the key's corresponding value from dictionary 'cypher'
        encrypted_s = encrypted_s + cypher[letter] #composing string of encrypted 's'
    return encrypted_s #value of 'encrypted_s' is returned for function 'encrypt_s'

def decrypt(s): #function which decrypts the encrypted 's' and returns the decrypted string
    cypher = create_cypher_dictionary() # get the cypher dictionary
    decrypted_s = ""
    
    i = 0
    while i < len(s): #while loop to iterate over every two characters in string 's' (since each decryptedc character corresponds to two encrypted character)
        v = s[i] + s[i + 1] #composing double digit string to use as value in reverse lookup
        decrypted_s = str(decrypted_s) + str(reverse_lookup(cypher, v)) #'reverse_lookup()' function is called to obtain key from dictionary 'cypher' using its value. This is then composed to form decrypted string
        i = i + 2 #iteration over every two characters because of double digit values
    return decrypted_s #value of 'decrypted_s' is returned for function 'decrypt_s'
    
def encrypt_multiple_times(s, n): #function encrypting 's' 'n' number of times
    n = int(n)
    
    for i in range(n): #for loop used to call function 'encrypt()' 'n' number of timed
        encrypt(s)
        s = encrypt(s)
    return s #value of 's' is returned for function 'encrypt_multiple_times()'


# Source: https://en.wikipedia.org/wiki/Most_common_words_in_English
COMMON_WORDS = [" the ", " be ", " to ", " of ", " and ", " a ", " in ", " that ", " have ", " I ", " it ", " for ", " not ", " on ", " with ", " he ", " as ", " you ", " do ", " at "]

def decrypt_multiple_times(s): #funciton which decrypts 's' until common words are recognized
    cypher = create_cypher_dictionary() # get the cypher dictionary
    
    i = 0
    while i < 21: #while loop is used to iterate over every element in list 'COMMON_WORDS'
        if i == 20: #if loop iterates through all elements without finding a common word, function 'decrypt()' is called and the iteration is reset to start from first element
            decrypt(s)
            s = decrypt(s)
            i = 0
        elif COMMON_WORDS[i] not in s: #if common word is not in 's' the next common word in list is checked by increasing the loop vairable by 1
            i += 1
        else: #if a common word is found
            return s #value of 's' is returned for function 'decrypt_multiple_times()' (i.e. decrypted string)


s = input("Enter text to encrypt: ") #user prompted for their input

i = 0
while i < 21: #while loop to ensure common words exist in user input and call encryption and decryption functions otherwise
    if i == 20:
        print("Invlaid input.") #if no common words found in 's', "invalid input" is printed to screen and loop ends
        i += 1
    elif COMMON_WORDS[i] not in s: #checking for common word in 's', if not found, next common word in list is checked by increasing loop variable by 1
        i += 1
    else: # otherwise the encryption and decryption functions are called
        print("Encrypted string:", encrypt(s))
        print("Decrypted string:", decrypt(encrypt(s)))

        salted_s = encrypt_multiple_times(s, 2)
        print("Encrypted x2 string:", salted_s)
        print("Decrypted x2 string:", decrypt_multiple_times(salted_s))
        i = 21 #setting loop vairable to value making condition false in order to end loop
