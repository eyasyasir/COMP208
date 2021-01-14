# Author: [Eyas Hassan]
# Assignment 1, Question 4

def vink_sequence(n, k ,j): # defining function vink_sequenct that takes argument n, k, j
    if n == 1: # boolean condition checking if user input is equal to 1
        return 1 # if true, the function returns 1
    elif n % 2 == 0: # if first statement is false, boolean condition uses modulo to check if n is an even number
        next_term = n // 2 # if true, the value n/2 is assigned to variable next_term
    else: # if previous statement is false, n is even, therefore; next_term is assigned value 3n + k
        next_term = (3 * n) + k
    for i in range(j - 2): # range j - 2 is takes into account first two terms of sequence (n and next_term in lines 9 or 11), the index starts at 0, and that the loop runs for range - 1 times
        if next_term % 2 == 0: # see line 9 comment
            next_term = next_term // 2
        elif next_term % 2 != 0: # see line 10 comment
            next_term = (3 * next_term) + k
        if next_term == 1: # boolean condition checking if next_term is equal to 1
            return i + 3 # if true, the function returns i + 3
        elif i == (j - 3): # if the j-th term is reached the function returns -1
            return -1

n = int(input("Enter n: ")) # taking user input as integer and assigning it to variable n (first term)
k = int(input("Enter k: ")) # taking user input as integer and assigning it to variable k (addition term if term in sequence is odd)
j = int(input("Enter j: ")) # taking user input as integer and assigning it to variable j (number of terms to check)

if n <= 0 or k < 0 or j <= 0: # boolean conditions restriciting user input for vairables n, k, and j to positive numbers
    print("Invalid input.") # if statement is true, "Invalid input." is printed to screen
else: # if previous statement is false, function vink_sequence with arguments n, k, and j is executed and the result is printed to screen.
    print(vink_sequence(n, k, j))
