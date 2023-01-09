# File: hw2_part1.py
# Author: Joshua Julian Tanseco
# Date: 9/19/16
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# this program gives a total price based on unit price and amount being bought
# Collaboration:
# COLLABORATION STATEMENT GOES HERE

def main():
    
    bookPrice = input("What is the price of the book? ")
    bookPrice = float(bookPrice)
    copyAmount = input("How many copies do you want? ")
    copyAmount = int(copyAmount)
    subTotal = bookPrice + copyAmount
    print("subtotal =", subTotal)
    tax = subTotal * 0.06
    shipping = copyAmount * 6.95
    total = subTotal + tax + shipping
    print("The total cost is $", total)

main()

