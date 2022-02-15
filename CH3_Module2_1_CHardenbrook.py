"""
Module 3:  pick a number
Authors: Group 8- Landen, Caden, Coleton Hardenbrook
Date: 09/20/2020
objective: This program will request user input and output a specific program
correlating to the input chosen.

"""

#input for variable
choice=int(input("please enter a number, 1-5: "))

# decision tree for input

if choice ==1:
     #input and set variables
    print("You have chosen option 1, the program will count the distance a bouncing ball will travel")
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

elif choice==2:
    print("You have chosen option 2, this program will calculate your rate of pay.")
    #initialize variables

    hourlywage=float(input(" please enter your hourly wage: "))
    totalreghours= float(input("please enter your regular hours: "))
    totalOThours= float(input("please enter your overtime hours: "))
    
    #calculation
    Totalpay= (hourlywage*totalreghours) + ((1.5*hourlywage) * totalOThours)

    #output
    print("your weekly wage will be: $ ",Totalpay)

elif choice ==3:
    print("you have chosen option 3, this program will calculate a sum for you.")
    #userinput and variables
    theSum=0.0
    number= float(input("please enter a number or press enter to end input: "))
    while number != "" :   
         number2= number
         theSum+=float(number2)
         number=input("enter the next number:")
         #while loop to incrementaly add sum of numbers in list
    print("the sum is",theSum,".")   #output

elif choice == 4:
    print("You have chosen option 4, the game Lucky Sevens will now be played.")
    
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

elif choice ==5:
    from random import randint
    print("you have chosen option 5, this program will randomly generate the grade that should be given for this assignment.")
    answer=input("would you like to have this project graded for you? (Y or N):")
     
    if answer == "Y":
         print("This assignment is worth",randint(90,100),"percent")
    elif answer == "N":
         print("have a nice day!")
    else:
         print("You have entered an invalid input, please use the letters Y or N to indicate your choice.")
