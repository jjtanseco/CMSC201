# File: hw4_part2.py
# Author: Joby Tanseco
# Date: 10/4/16
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# THIS PROGRAM GIVES THE REMAINDER OF TWO NUMBERS WITHOUT THE MOD OPERATOR
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():

    #asks for first
    firstNum = input("Please enter first number: ")
    #asks for second number
    secondNum = input("Please enter the second number: ")
    secondNum = int(secondNum)
    finalNum = int(firstNum)
    
    #loop to mimic mod
    while finalNum >= secondNum:
        finalNum = finalNum - secondNum
    
    #Visual
    print(firstNum, "%", secondNum, " = ", finalNum)

main()
