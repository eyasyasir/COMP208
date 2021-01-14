# Author: Eyas Hassan
# Assignment 3, Question 1

# Return an nxn matrix with snowflakes in the given regions.
# If regions is None, return a matrix with one snowflake spanning the entire matrix.
def make_snowflake(n, regions=None):
    
    # checking and raising of ValueErrors, ValueError string arguments for cause of error.
    # conditions to meet not mentioned in the assignmnet have been denoted with upperase comments.
    if type(n) != int: 
        raise ValueError("n is not of type int")
    
    if n % 2 == 0:
        raise ValueError("n is not odd")
    
    if n <= 0:
        raise ValueError("n is less than or equal to zero")
    
    if regions != None:
        if type(regions) != type([]):
            raise ValueError("regions is of a type other than list or NoneType")
        for i in regions: # VALUE ERROR RASIED OUTSIDE OF THE ONES GIVEN IN ASSIGNMENT INSTRUCTIONS
            if type(i) != type(()):
                raise ValueError("one or more elements in list regions is of type other than tuple")
    
    if regions == []:
        raise ValueError("regions is an empty list")
    
    if regions != None:
        for i in range(len(regions)):
            a = regions[i][0]
            b = regions[i][1]
            
            if b % 2 != 0: # VALUE ERROR RASIED OUTSIDE OF THE ONES GIVEN IN ASSIGNMENT INSTRUCTIONS
                raise ValueError("one of the specified region sizes is not even")
            
            if (b + a) > n:
                raise ValueError("a tuple in the regions list has a value that would put the bottom-right corner of the snowflake out of the bounds of the given matrix size")
    
    # snowflake is initialized by setting it to a matrix of dots (blank canvas)
    snowflake = make_dot_matrix(n)
    
    if regions != None: # checking if user has specified any regions, this block wil execute if regions are defined
        for i in range(len(regions)):
            a = regions[i][0]
            b = regions[i][1]
            
            # changing elements in first row to include "+" at corners and "*" in the middle, also changing middle element
            # of last row to "*"
            snowflake[a][a], snowflake[a][b + a], snowflake[a][(b // 2) + a], snowflake[a + b][(b // 2) + a] = "+", "+", "*", "*"
            
            # loop which iterates through each row in range [1, b)
            for r in range(1, b):
                # for middle row of matrix, all elements are changed to "*"
                if r == b // 2:
                    for c in range(b + 1):
                        snowflake[(b // 2) + a][c + a] = "*"
                # for other rows of matrix in the specified range, "*" changed in the appropriate positions
                else:
                    snowflake[a + r][a + r], snowflake[a + r][(b // 2) + a], snowflake[a + r][a + (b - r)] = "*", "*", "*"
            
            # first and last elements in last row of matrix changed to "+", center element in matrix range is changed to "@"
            snowflake[a + b][a], snowflake[a + b][a + b], snowflake[(b // 2) + a][(b // 2) + a] = "+", "+", "@"
    
    # executes if user has not specifiec region (i.e. regions is of NoneType)
    else:
        # first row of matrix: first and last elements changed to "+", middle element changed to "*"
        snowflake[0][0], snowflake[0][-1], snowflake[0][(n - 1) // 2] = "+", "+", "*"
        
        # itereates through rows of matrix in range [1, n)
        for r in range(1, n):
            # all elements of middle row changed to "*"
            if r == (n - 1) // 2:
                for c in range(n):
                    snowflake[(n - 1) // 2][c] = "*"
            # elements along the diagonals and middle are changed to "*" 
            else:
                snowflake[r][r], snowflake[r][(n - 1) // 2], snowflake[r][-(r + 1)] = "*", "*", "*"
        
        # last row of matrix: first and last elements changed to "+"
        # center of matrix: element changed to "@"
        snowflake[-1][0], snowflake[-1][-1], snowflake[(n - 1) // 2][(n - 1) // 2] = "+", "+", "@"
    
    return snowflake
    


# Make an empty, nxn matrix filled with dots ('.')
def make_dot_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for i in range(n):
            row.append(".")
        matrix.append(row)
    return matrix

# Prints the given snowflake to the screen.
def print_snowflake(snowflake):
    for row in snowflake:
        print("".join(row))

# Example code as shown in the assignment PDF is below
# You can un-comment each line to test your code,
# but make sure to remove and/or comment all lines below before you submit.

# Example 1
# print_snowflake(make_snowflake(1))

# Example 2
# print_snowflake(make_snowflake(3))

# Example 3
# print_snowflake(make_snowflake(5))

# Example 4
# print_snowflake(make_snowflake(13))

# Example 5
# print_snowflake(make_snowflake(101, regions=[(10, 20), (40, 60)]))

# Example 6
# print_snowflake(make_snowflake(2))

# Example 7
# print_snowflake(make_snowflake(5, regions=[(100, 5)]))
