# File: FILENAME.py
# Author: Joshua Julian Tanseco
# Date: 9/19/2016
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# makes a shopping list application
# Collaboration:
# COLLABORATION WAS NOT ALLOWED FOR THIS ASSIGNMENT

def main():

    item1 = input("What would you like to buy first? " )
    print("You are buying ", item1)
    amount1 = input("How many would you like to buy? " )
    amount1 = int(amount1)
    
    item2 = input("What would you like to buy second? " )
    print("You are buying ", item2)
    amount2 = input("How many would you like to buy? " )
    amount2 = int(amount2)

    item3 = input("What would you like to buy third? " )
    print("You are buying ", item3)
    amount3 = input("How many would you like to buy? " )
    amount3 = int(amount3)

    totalNumber = amount1 + amount2 + amount3
    print("You are buying ", totalNumber, " items:")
    print(amount1, item1)
    print(amount2, item2)
    print(amount3, item3)

main()
    
