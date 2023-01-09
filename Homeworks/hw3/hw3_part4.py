# File: hw3_part4.py
# Author: Joshua Julian Tanseco
# Date: 9/28
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# This program asks the user the day of the month, and will respond will weekday
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():

    month = input("Please enter the day of the month: ")
    month = int(month)

    WEEK = (7)

    weekDay = month % 7

    if month > 30:
        print("That is an invalid day of the month.")
    elif weekDay == 1:
        print("Today is Sunday!")
    elif weekDay == 2:
        print("Today is Monday!")
    elif weekDay == 3:
        print("Today is Tuesday!")
    elif weekDay == 4:
        print("Today is Wednesday!")
    elif weekDay == 5:
        print("Today is Thursday!")
    elif weekDay == 6:
        print("Today is Friday!")
    elif weekDay == 7:
        print("Today is Saturday!")
    print("Have a good day!")

main()
