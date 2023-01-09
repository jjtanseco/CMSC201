# File: hw3_part3.py
# Author: Joshua Julian Tanseco
# Date: 9/28/2016
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description:
# This programs asks if a temperature is in Kelvin or Celsius then if its cold
# Collaboration:
# I did not collaborate with anyone on this assignment

def main():

    temp = input("Please enter the temperature: ")
    temp = int(temp)

    measure = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if measure == "C":
        if temp <= 0:
            print("At this temperature, water is a solid.")
        elif temp >= 100:
            print("At this temperature, water is gas.")
        else:
            print("At this temperature, water is liquid.")


    elif measure == "K":
        if temp <= 273.15:
            print("At this temperature, water is a solid.")
        elif temp >= 375.15:
            print("At this temperature, water is gas.")
        else:
            print("At this temperature, water is liquid.")



main()
