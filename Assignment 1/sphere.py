# Author: [Eyas Hassan]
# McGill ID: [260776234]
# Assignment 1, Question 3

from math import * # imports all varialbes/functions from the math module

def volume(): # defining a function that outputs radius and surface area given volume
    radius = ((3 * data_value) / (4 * pi)) ** (1 / 3) # expressing radius in terms of volume (user's input)
    surface_area = 4 * pi * (radius * radius) # surface area in terms of radius
    print("The radius is", radius, "and the surface area is", str(surface_area) + str(".")) # printing radius and surface area, str is used to remove space between surfce area value and "."
    
def surface_area(): # defining a function that outputs radius and volume given surface area
    radius = sqrt(data_value / (4 * pi))
    volume = (4 / 3) * pi * (radius * radius * radius)
    print("The radius is", radius, "and the volume is", str(volume) + str("."))
    
def radius(): # defining a function that outputs volume and surface area given radius
    radius = data_value
    volume = (4 / 3) * pi * (radius * radius * radius)
    surface_area = 4 * pi * (radius * radius)
    print("The volume is", volume, "and the surface area is", str(surface_area) + str("."))
    
data_type = input("What piece of data do you have? ") # assigning user input to variable data_type

if data_type != "volume" and data_type != "surface area" and data_type != "radius": # boolean arguments used to restric user input (data_type) to radius, volume, or surface area
    print("Invalid input.")
else: # if user input matches radius, volume, or surface area then the following is executed
    data_value = float(input("Enter the number: ")) # user input is recorded, converted into a float, and assigned to data_value variable
    if data_value < 0: # boolean arguments used to restric user input (data_value) to a positive number
            print("Invalid input.")
    elif data_type == "volume": # if data_type is volume, then the volume function is exectued
        volume()
    elif data_type == "surface area": # if data_type is surface area, then the surface area function is exectued
        surface_area()
    elif data_type == "radius": # if data_type is radius, then the radius function is exectued
        radius()