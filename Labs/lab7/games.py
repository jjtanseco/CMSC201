# File: games.py
# Author: Joby Tanseco
# Date: 10/18/2016
# Section: 18
# E-mail: tanseco1@umbc.edu
# Description: This program helps decide what game to play
# 
# Collaboration: During lab, collaboration between
# students is allowed, although I understand I still
# must understand the material and complete the
# assignment myself.


def main():

    #Part 5B

    #initializing the games list
    games = ["Twister", "Dodgeball", "Capture the Flag",
    "Hide and Seek", "Croquet", "Ring Toss", "Ping Pong"]

    #lists the games
    for i in range(len(games)):

        print(i + 1, "-", games[i])

    #Part 5C

    #set vote not equal to zero
    vote = 1
    
    #makes vote list
    voteList = [0, 0, 0, 0, 0, 0, 0]

    #sentinel loop to ask for votes
    while vote != 0:
        
        vote = int(input("What game would  you like to play? (0 to quit): "))

        #part 5D
        #adds vote to corresponding item
        if vote > 0 and vote <= 7:
            voteList[vote - 1] += 1
        
    print(voteList)

    #Part 5E

    #For loop to print who has what vote
    for x in range(len(games)):
        print(games[x], "has", voteList[x], "votes")
    
main()


