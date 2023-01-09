# File: hw5_part4.py
# Author: Joby Tanseco
# Date: 10/7/2016
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# This program checks whether a string contains another, smaller string
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():

    #set variables
    string1 = input("First (longer) string: ")
    #make lowercase
    string1.lower()
    
    string2 = input("Second (shorter) string: ")

    string2.lower()
    #Create empty lists
    list1 = []

    list2 = []
    #turn strings into lists
    for i in string1:

        list1.append(i)

    for i in string2:

        list2.append(i)

#but for some reason I can't make the strings lowercase so idk what to do now

    print(list1, list2)

main()
