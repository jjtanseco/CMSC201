# File:    capitals.py
# Started: by Dr. Gibson
# Author:  Joshua Julian Tanseco
# Date:    11/15/2016
# Section: 18
# E-mail:  tanseco1@umbc.edu
# Description:
#   This file contains python code that reads in a list of
#   states and their capitals, stores it in a dictionary,
#   and then allows the user to list all options (states),
#   or to show the capital of a specified state.
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself. 

QUIT     = "exit"
SHOW_ALL = "list"


# convertToDict() takes in the filename and converts to a dict
# Input:          a file object
# Output:         a dictionary containing the file contents
def convertToDict(fileContents):
    dict1 = {}

    # write the rest of the function (including the return)





def main():

    stateCapFile = open("stateCaps.txt")
    # a function call to convertToDict goes here

    stateCapDict = {}

    for line in stateCapFile:

        line = line.strip()
        state, capital = line.split(",")

        stateCapDict[state] = capital


    stateCapFile.close()

    print("Welcome to the State Capital Lookup System")
    # message with all the prompts for the user
    msg = "\n\tPlease enter the state you want the capital of.\n" + \
        "\t(Use '" + SHOW_ALL + "' for choices, or '" + \
        QUIT + "' to quit): "

    choice = input(msg)

    # this should be a while loop that runs until the user chooses to "exit"
    # MAKE SURE TO USE THE CONSTANTS DEFINED AT THE TOP OF THE FILE!!!
    while choice != QUIT:
        # inside the loop: if the user enters "list", show all the states
        if choice == SHOW_ALL:
            for item in stateCapDict.keys():
                print(item)
            print("")

        # inside the loop: otherwise; check if the state exists
        else:

            # if the state exists, print its capital
            if choice in stateCapDict.keys():

                print("The capital of ", choice, " is ", stateCapDict[choice])
                print("")

            # otherwise, print that it is not a state
            else:
                print("Sorry, ", choice, " is not a state.)")


        # at the end of the while loop, get a new user input
        choice = input(msg)

    print("Thank you for using the State Capital Lookup System!")
main()

    

