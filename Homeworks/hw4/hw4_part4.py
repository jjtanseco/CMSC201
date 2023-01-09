# File: hw4_part4.py
# Author: Joby Tanseco
# Date: 10/5/2016
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# This program constantly changes the hailstone height
# Collaboration:
# COllaboration was not allowed in this assignment

def main():

    #Variables and constants    
    END_HEIGHT = 1

    height = input("Please give me a positive integer: ")
    height = int(height)

    print("Hail is currently at height ", height)


    #loop continues as long as height is not 1
    while height > END_HEIGHT:
        evenOdd = height % 2

        #divide by two if even
        if evenOdd == 0:
            height = height / 2
            print("Hail is currently at height ", height)

        #multiply by 3 and add 1 if odd
        else:
            height = (height * 3) + 1
            print("Hail is currently at height ", height)
    print("Hail stopped at height ", 1)

main()
