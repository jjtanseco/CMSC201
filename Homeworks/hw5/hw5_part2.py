# File: hw5_part2.py
# Author: Joby Tanseco
# Date: 10/7/2016
# Section: 18
# E-mail: tanseco@umbc.edu
# Description:
# This programs asks user for a the width and height of a box/
# and i make it
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():


    #asks for heiht and width variables
    width = input("Please enter the width of the box: ")
    width = int(width)
    
    height = input("Please enter the height of the box: ")
    height = int(height)

    middle = width - 2
    middle = int(middle)

    #asks for materials
    outline = input("Please enter a symbol for the box outline: ")

    fill = input("Please enter a symbol for the box fill: ")

    endLine = outline * width

    inside = outline + (fill * middle) + outline

    print(endLine)

#begin for loop.
    for line in range(0, height - 2):
        
        print(inside)
        
    print(endLine)
main()
