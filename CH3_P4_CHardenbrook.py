"""
CH3- Project 4: A ball's Distance
Coleton Hardenbrook
Date :09/18/2020
Objective:  This program will calculate the total distance a ball travels, including bouncing, when a user inputs a
defintive height.  The user will be able to enter height and the number of bounces the ball will preform. An output
of total distance will be produced.
"""

#input and set variables
height=float(input("please enter the height (in meters) the ball will be dropped from: "))#set variable height
bounceIndex= float(input("please enter the height reached for the ball's first bounce in meters: "))  #set bounce index
bounciness =int(input(" please enter the total amount of bounces the ball will perform: ")) # set variable bounce
totalDistance=0    #variable counter set for incremental bounces
bounceIndex2= (bounceIndex / height)          # computes bounce index for ball drop
    

while bounciness > 0: 
    totalDistance= (height+totalDistance)           # compute initial bounce distance
    height= (height*bounceIndex2)
    totalDistance= (totalDistance + height) #total dstance final calculation using index ratio
    bounciness -=1                                  

print ("total distance travelled is:", totalDistance,"meters")
