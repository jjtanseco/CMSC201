# File: hw2_part2.py
# Author: Joshua Julian Tanseco
# Date: 9/19/2016
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# This program seperates the dollars and cents in a price
# Collaboration:
# COLLABORATION WAS NOT PERMITTED IN THIS ASSIGNMENT

def main():

    price = input("What is the price?" )
    price = float(price)
    priceDollars = int(price)
    priceCents = price - priceDollars
    cents = priceCents * 100
    print("The number of dollars is: ", priceDollars)
    print("The number of cents is: ", cents)

main()
