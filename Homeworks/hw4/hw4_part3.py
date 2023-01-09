# File: hw4_part3.py
# Author: Joby Tanseco
# Date: 10/5/16
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# This programs asks for the user to input a valid UMBC username
# Collaboration:
# Collaboration was not allowed on this assignment

def main():

#set variable and constants
    userName = input("Please enter your username: ")
    MAX = 8
    MIN = 2


#start loop
    while len(userName) < MIN or len(userName) > MAX or \
            (userName[-1] != "1" and len(userName) < MAX):

#Cannot be less than minimum        
        if len(userName) < MIN:
            print("Usernames must have 2 or more characters")
            userName = input("Please enter your username: ")

#Cannot be more than max        
        elif len(userName) > MAX:
            print("Usernames must be shorter than 8 characters")
            userName = input("Please enter your username: ")

#cannot be under max and without a one
        elif len(userName) < MAX and userName[-1] != "1":
            print("Username must end in 1")
            userName = input("Please enter your username: ")
        else:
            print("That username works!")
    print("Thank you for choosing ", userName)            

main()
    
