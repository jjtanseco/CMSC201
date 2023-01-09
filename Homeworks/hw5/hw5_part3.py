# File: hw5_part3.py
# Author: Joby Tanseco
# Date: 10/7/2016
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# This program counts down from 101 with certain messages placed
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():

    #starts countdown from 101
    for num in range(101, 0, -1):

        #determines if divisible by 5 or 6
        mod5 = num % 5
        mod5 = int(mod5)

        mod6 = num % 5
        mod6 = num % 6
        
        #if divisible by 5 and 6
        if mod5 == 0 and mod6 == 0:
            print("Thirty days hath September.")

        #if divisible by 5
        elif mod5 == 0:
            print("Where do you see yourself in five years?")


        #if divisible by 6
        elif mod6 == 0:
            print("I'll believe six impossible things before breakfast.")

        #otherwise
        else:
            print(num)

main()
