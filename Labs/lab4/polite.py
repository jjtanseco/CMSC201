# File:        polite.py 
# Author:      Joshua Julian Tanseco 
# Date:        9/27/2016 
# Section:     18 
# E-mail:      tanseco1@umbc.edu 
# Description: This program tells the user if they have manners or not 
#               
# Collaboration: During lab, collaboration between students is allowed, 
#                although I understand I still must understand the material 
#                and complete the assignment myself. 


def main():

    word = input("Please enter a word: ")

    if word == "please" or word == "thanks" or word == "pardon":

        print("Your manners are impeccable!")

    else:
        print("How utterly rude!")

main()
