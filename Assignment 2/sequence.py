# Author: [Eyas Hassan]
# Assignment 1, Question 1

def fetch(numbers): #function returning the smallest integer not in user_list or 1 if list is empty
    if len(numbers) == 0: #if 'user_list' is empty, 1 is returned for fucntion 'fetch()'
        return 1
    else: #otherwise while loop is used to find the smallest integer and returns it
        i = 1 #1 is smallest possible integer in list
        while i in numbers: #checking to see if number is in the list using a for loop
            i = i + 1 #if it is, the next integer is checked until the first one that is not in the list is found
            if i == len(numbers): #if list contains sequential integers, the integer greter than the last element in the list is returned
                return i + 1
        return i #smalles integer not in the list is returned

def get_list_from_input(): #function which creates a list of numbers from user input until 'done' is entered
    user_list = [] #empty list created, assigned to 'user_list'
    user_input = input("Enter number(s): ") #prompting user to enter numbers
    
    while user_input != "done": #while loop which runs until user enters 'done'
        
        if "," in user_input: #checking for ',' in user_input, if true they are removed using a delimtter and '.split()' method to create a list
            delimiter = ","
            new_entries = user_input.split(delimiter) #after ',' removed, list is assigned to variable 'new_entries'
            
            for i in range(len(new_entries)): #for loop iterates through every element in list 'new_entries'
                new_entries[i] = int(new_entries[i]) #each element in list is turned into integer type
            
            user_list.extend(new_entries) #'new_entries' are appended to 'user_list' using '.extend()' method
            
        else: #if no commas are present in user input, it is appended to list 'user_list'
            new_entries = int(user_input) #turned into integer type
            user_list.append(new_entries) #integer is appended to list 'user_list' using '.append()' method
            
        for i in range(len(user_list)): #for loop iterates through elemts of 'user_list and removes any values less than 1
            
            if user_list[i] < 1:
                user_list.pop(i) #'.pop()' method is used to do this
                
        user_input = input("Enter number(s): ") #user is asked to enter input again
        
    return user_list #once user enters 'done', function 'get_list_from_input()' returns the list 'user_list'

numbers = get_list_from_input() #assigning value of function 'get_list_from_input()' to variable 'numbers'
print(fetch(numbers)) #value of function 'fetch()' is printed (i.e. smallest integer not in list)
