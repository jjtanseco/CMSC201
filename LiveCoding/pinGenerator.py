#11/15/16


import random

MIN_PIN = 0000

MAX_PIN = 9999


def main():



    logins = dict()

    while True:

        name = input("Please enter your username (CTRL+C to quit): ")

        #this means the name already exists
        if name in logins: 
            print("The pin for name is ", logins[name])

        else:
            #generate a random pin for them
            newPin = random.randrange(MIN_PIN, MAX_PIN + 1, 1)

            logins[name] = newPin

            print("The pin for the new user", name, "is", newPin)

    #need to generate random pin

    #need to import random

    #need constants: minimum and maximum

    #ask user for username

    #create dictionary

    #check if name is in dictionary

    


main()
