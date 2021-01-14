# Author: [Eyas Hassan]
# Assignment 1, Question 4

AUTHOR = "Eyas Hassan"
ROOM_NAME = "Dungeon"

def escape_room():
    print("You find yourself in a dark room. A candle lies on a small table in front of you, providing a small amount of light. You cannot see any door or exit. However, there is a man wearing a name tag that reads 'Euler'. Next to him there is what seems to be a keypad on one of the walls.") #Printing room description with objects, and person (Euler)
    
    euler_message = "I've hit my head on my way down here and have forgotten the missing piece to my beautiful equation, I'm trapped..." #String to print when talking to euler, assigned to variable euler_message
    
    candle_message = "The candle is tall and thin. You decide to pick it up to examine the rest of the room more closely. You think you can make out half of a mathematical equation on the walls: e to the power i times pi..." #String to print when examining candle, assigned to variable candle_message
    
    keypad_message = "It is a standard keypad, with digits from 0-9. Looking closely, you think you can make out half of a mathematical equation scratched into the wall above it: = 0..." #String to print when examining keypad, assigned to variable keypad_message
    
    commands = {"talk to euler" : euler_message, "examine candle" : candle_message , "examine keypad" : keypad_message} #Dictionary with all possible commands as keys and messages to display as variables
    
    answer_commands = ["press 1", "enter 1", "press key 1", "enter key 1" ] #List of special commands that return True for function escape_room
    
    def possible_commands(): #Defining function that returns string of possible commands that user can enter
        
        full_string = "" #assigning blank string to variable 'full_string'
        for key in commands: #for loop which iterates through keys in dictionary 'commands'
            part_string = key + ", "
            full_string = full_string + part_string
        
        string = full_string[: (len(full_string) - 2)] #string slicing removes last two character ', ' in string 'full_string', assigned to variable 'string'
        
        return string #variable 'string' is returned for function 'possible_commands()'
    
    while True: #while loop which runs forever until user enter one of the special commands in list 'answer_commands'
        cmd = input("> ") #prompting user for their input
        
        if cmd.lower() == "commands": #'.lower()' method is used to turn string 'cmd' into lower case letters
            print(possible_commands()) #if boolean expression above evaluates to true, the value of function 'possible_commands' is returned
        
        elif cmd.lower() in commands: #if user input is a key in 'commands' dictionary, the values in 'commands' dictionary are printed
            print(commands[cmd.lower()])
            
        elif cmd.lower() in answer_commands: #if user input is an element of list 'answer_commands' a string is printed and the function 'escape_room()' returns True value
            print("A secret door opens!")
            return True
            
        else: #if none of the previous statements are true, the user has entered an invalid input and so a string is printed to screen
            print("Invalid command.")
        # turn command to lowercase
        # print appropriate message
        
        # check if command is one of the 2 special commands
        
        # return True if user has entered correct answer


# Calling the function so that it runs when we run the file.
escape_room()
