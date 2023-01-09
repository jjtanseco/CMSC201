# File: hw8.py
# Author: Joshua Julian Tanseco
# Date: 11/21/2016
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# This program gives the user the option to look at who is in what
# house, and to suggest a house to be put in.
# Collaboration:
# I did not collaborate with anyone on this assignment

import random

PRINT_HOUSE = 1
PRINT_HOUSES = 2
SORT_HOUSE = 3
EXIT_PROGRAM = 4


# makeDict:       Makes dictionary that has all the houses and their 
#                 members as the house value
# INPUT:          a 2D list: each line of the file
# OUTPUT:         a dictionary with lists as its values; houses and 
#                 their members
def makeDict(myFile):

    myDict = {}

    for line in myFile:
        tempList = line.split(", ")

        if tempList[0] not in myDict.keys():

            myDict[tempList[0]] = [tempList[1]]

        else: 
            myDict[tempList[0]].append(tempList[1])

    return myDict


# printOneHouse(): prints the name of all the members in a house
# INPUT:           a Dictionary, the name of the houses and members
# OUTPUT:          None. (prints the house and its members)
def printOneHouse(myDict):

    house = input("What house's members would you like to print? ")

    while house not in myDict.keys():

        print("There is no house by the name of " + house)
        house = input("What house's members would you like to print? ")


    print("\nThe members of the House of " + " are: \n")

    for member in myDict[house]:
        print(member, end = "")


# printAllHouses(): prints out the name of all the houses and their
#                   members
# INPUT:            a Dictionary, the houses and all it's members
# OUTPUT:           None (but prints out all of houses and their members
def printAllHouses(myDict):

    for house in myDict:

        print("\nThe members of house " + house + " are \n")

        for member in myDict[house]:
            print(member, end = "")



# houseSort():     picks a random house for user influenced by userchoice
# INPUT:           a dictionary, the houses
# OUTPUT:          the chosen house
def houseSort(myDict):

    #makes a list of houses
    houseList = []
    for key in myDict.keys():
        houseList.append(key)

    #asks user for name and house preference
    name = input("What is the person's name? ")

    house = input("What house do they prefer? ")

    while  house not in houseList:

        print("That is not a real house")
        house = input("What house do they prefer? ")

    print(house)
    print(houseList)
    houseAmount = len(houseList)

    #increases the amount of that house in the list
    for item in range(houseAmount):
        houseList.append(house)

    #gets random integer
    sort = random.choice(houseList)

    message = (name + " is placed in house " + house)
    return message


# printMenu()      
def printMenu():
    
    message = (str(PRINT_HOUSE) +  " - Print a single house \n" \
                   + str(PRINT_HOUSES) + " - Print all the houses \n" \
                   + str(SORT_HOUSE) + " - Sort a new person into a house \n" \
                   + str(EXIT_PROGRAM) + " - Exit the program \n")

    print(message)


def fakeMain():

    houseFile = open("GoT.txt", "r")
    houseList = houseFile.readlines()

    x = makeDict(houseList)
    print(x)

    print(x.keys())
    printAllHouses(x)

    houseSort(x)


#fakeMain()



def main():

    #opens file to read, then converts it into a dictionary
    fileName = input("Please enter filename to load: ")
    houseFile = open(fileName, "r")
    houseList = houseFile.readlines()

    #loops menu and input until they wish to exit
    houseDict = makeDict(houseFile)

    menuChoice = 0
    while menuChoice != 4:
        
        printMenu()

        menuChoice = int(input("Please enter a number between 1 and 4: "))

        # makes sure its between 1 and 4
        while menuChoice < 1 or menuChoice > 4:
            menuChoice = int(input("Please enter a number between 1 and 4: "))

        #runs printOneHouse()
        if menuChoice == PRINT_HOUSE:

            printOneHouse(houseDict)

        # runs printAllHouses()
        elif menuChoice == PRINT_HOUSES:
            print("you pressed 2")
            printAllHouses(houseDict)

        # runs houseSort()
        elif menuChoice == SORT_HOUSES:

            sortMessage = houseSort(houseDict)

            print(sortMessage)

    #ends
    print("thanks for using this house sorting thing")


main()
