# File:    semester.py
# Started: by Dr. Gibson
# Author:  tanseco1
# Date:    10/4/16
# Section: 18
# E-mail:  tanseco1@umbc.edu 
# Description:
#   This file contains python code that asks the user for their
#   courses, then goes through the list and asks them for their
#   raw grade for each course, removes the course from the list, 
#   and calculates and prints their average grade for the semester.

def main():

    # constant for the sentinel value, and an empty list to start
    COURSE_SENTINEL = "NONE"
    courseList = []

    # populate the course list
    course = input("What course did you take? ('NONE' to stop): ")

    #### YOU NEED TO PUT A WHILE LOOP HERE
    while course != "NONE":

        # save the course and ask for another
        courseList.append(course)
        course = input("What course did you take? ('NONE' to stop): ")
    
    # create variables to help calculate the student's average
    amount = len(courseList)
    counter = 0
    counter = float(counter)

    # go through the course list; continue while the list is not empty
    while courseList != []:

        # ask about their grade for each course and save it to the total
        print("What did you get for the course ", courseList[0], "?")
        grade = input()
        grade = float(grade)
        counter = grade + counter
        # remove() the course from the list
        courseList.remove(courseList[0])

    # calculate their average raw grade
    average = counter / amount
    average = float(average)

    # print out their average raw grade
    print("Your average raw grade is ", average,".")

main()
