# File: hw4_part1.py
# Author: Joby Tanseco
# Date: 10/4/16
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# This program will ask for an input repeatedly until it is valid
# Collaboration:
# Collaboration was not allowed for this assignment

def main():
    
    #set constants
    MIN = 4
    MAX = 12

    #set variables
    userName = ""
    userName = input("Please enter a Username: ")


    #start loop
    while len(userName) < MIN or len(userName) > MAX:
        #cannot be under minimum
        if len(userName) < MIN:
            print("That username is too short, try again.")

        #Cannot be over max
        elif len(userName) > MAX:
            print("That username is too long, try again.")
        
        #restarts loop
        userName = "basic"
        userName = input("Username must be 4-12 characters: ")

    #final message
    print("Thank you for choosing ", userName, "!")



main()
