# Author: [Eyas Hassan]
# Assignment 1, Question 1

from math import exp # importing the exp function from math module

def gaussian_2D(x, y, A, xO, yO, sigmaX, sigmaY): # defining gaussian function that takes user inputs x, y, A, xO, yO, sigmaX, and sigmaY
    square_deltaX = (x - xO) * (x - xO) # square of the difference between the x-center and x-value
    square_deltaY = (y - yO) * (y - yO) # square of the difference between the y-center and y-value
    sqaure_sigmaX = sigmaX * sigmaX # square of the x-spread
    sqaure_sigmaY = sigmaY * sigmaY # square of the y-spread
    return A * exp(- ((square_deltaX / (2 * sqaure_sigmaX)) + (square_deltaY / (2 * sqaure_sigmaY))))

x = float(input("Enter value for x: ")) # assigning user input, as a float, to variable x
y = float(input("Enter value for y: ")) # assigning user input, as a float, to variable y
A = float(input("Enter value for A: ")) # assigning user input, as a float, to variable A
xO = float(input("Enter value for xO: ")) # assigning user input, as a float, to variable xO
yO = float(input("Enter value for yO: ")) # assigning user input, as a float, to variable yO
sigmaX = float(input("Enter value for sigmaX: ")) # assigning user input, as a float, to variable sigmaX
sigmaY = float(input("Enter value for sigmaY: ")) # assigning user input, as a float, to variable sigmaY

print(gaussian_2D(x, y, A, xO, yO, sigmaX, sigmaY)) # executing gaussian_2D function with x, y, A, xO, yO, sigmaX, and sigmaY as arguments
