"""
Chapter 3: Project 11 - lucky sevens
Coleton Hardenbrook
Date: 09/18/2020
Objective: This program will display the futility of playing the casino game
"lucky sevens".  User input will requre a dollar amount for a total bet,
program will calculate rolls based on pot size and continue counting until
pot is empty. Program will then print the number of rolls it took to break
the player's pot. It will also display the maximum amount within the pot.
"""
#import and variables
from random import randint

count=0                            #variable for counting rolls
tempPot=0                          #variable for counting maxpot

#input
totalPot=int(input("please enter your maximum bet: "))


#while loop to add to pot
while totalPot > 0 :
    count+=1
    roll=randint(1,12)            #random roll generator
    if roll > 7:
        print("you lose your",count,"roll")
        totalPot= totalPot -1     #calculate total pot if losing
        
    elif roll< 7:
        print("you lose your",count,"roll")
        totalPot= totalPot -1
    elif roll == 7:
        print("you WON your",count,"roll.")
        totalPot=totalPot + 4
        if tempPot<totalPot:
                tempPot=totalPot        #variable counter for max pot winnings
                
 #outputs               
print(" you ran out of money on your roll #",count)
print(" you had $",tempPot,"as your highest amount of money.")
