# Author: [Eyas Hassan]
# Assignment 1, Question 2

from turtle import * # imports all functions from turtle module

speed("fastest") # pointer speed set to fastest setting

def circles(radius1, radius2): # defining the function which draws the circles, taking the radii of the two circles as arguments
    circle(radius1) # draws circle of radius = radius1
    left(90) # rotates pointer by 90 degrees to the left
    up() # lifts up pen (i.e. no line is drawn when movement occurs past this point)
    forward(radius1 - radius2) # moving towards the center of the circle
    down() # puts pen down (i.e. line is drawn when movement occurs past this point)
    right(90) # rotates pointer by 90 degrees to the right
    circle(radius2) # draws circle of radius = radius2

radius1 = 100 # assigning desired radius of circle 1 to variable radius1
radius2 = 50 # assigning desired radius of circle 2 to variable radius2

circles(radius1, radius2) # executes circles function taking radius1 and radius2 as arguments

up() # lifts up pen (i.e. no line is drawn when movement occurs past this point)
goto(100, -100) # moves pointer to coordinates (100, -100)
down() # puts pen down (i.e. line is drawn when movement occurs past this point)

def polygon(number_of_sides): # defining the function which draws polygons taking the desired number of sides (number_of_sides) as the argument
    for i in range (number_of_sides): # for loop that executes for (number_of_sides) times
        forward(50) # length of each side of the polygon
        left(360 / number_of_sides) # angle between two adjacent sides as a function of number_of_sides

number_of_sides = 5 # frist polygon is a pentagon, assigning 5 to variable number_of_sides

polygon(number_of_sides) # executes polygon function taking number_of_sides as the argument

up() # lifts up pen (i.e. no line is drawn when movement occurs past this point)
goto(-150, -150) # moves pointer to coordinates (-150, -150) to draw second polygon
down() # puts pen down (i.e. line is drawn when movement occurs past this point)

number_of_sides = 8 # second polygon is an octagon, assigning 8 to variable number_of_sides

polygon(number_of_sides) # executes polygon function taking number_of_sides as the argument

up() # lifts up pen (i.e. no line is drawn when movement occurs past this point)
goto(300, -200) # moves pointer to coordinates (-150, -150) to draw letter E
down() # puts pen down (i.e. line is drawn when movement occurs past this point)

left(180)  # rotates pointer by 180 degrees to the left
forward(30) # moves pointer by 30 points to draw top horizontal part of letter E
left(90) # rotates pointer by 90 degrees to the left
forward(90) # moves pointer by 90 points to draw long vertical part of letter E
left(90) # rotates pointer by 180 degrees to the left
forward(30) # moves pointer by 30 points to draw bottom horizontal part of letter E

up() # lifts up pen (i.e. no line is drawn when movement occurs past this point)
goto(270, -245) # moves pointer to coordinates (-270, -245) to draw middle horizontal part of letter E
down() # puts pen down (i.e. line is drawn when movement occurs past this point)

forward(30) # moves pointer by 30 points to draw middle horizontal part of letter E
