# File: milesPerWeek.py 
# Author: YOUR NAME 
# Date: TODAY'S DATE 
# Section: YOUR SECTION NUMBER 
# E-mail: USERNAME@umbc.edu 
# Description: In this lab, we make a program that asks how much you drive to work each week, and the program tells 
#  you how many miles you drive and how much time you spend on the road each week.
# Collaboration: During lab, collaboration between students is allowed, 
# although I understand I still must understand the material 
# and complete the assignment myself. 

def main():
    
    milesEachWay = input("How many miles do you drive each way to work?: ")
    milesEachWay = int(milesEachWay)
    
    days = input("How many days do you drive to work each week?: ")
    days = int(days)

    milesWeekly = 2 * milesEachWay * days
    print("You drive", milesWeekly, "miles per week.")

    MILESPERHOUR = 57
    hours = milesWeekly / 57
    print("At 57 mph, you spend", hours, "hours commuting in the car each week.")

main()
