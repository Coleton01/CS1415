"""
Module 1
Coleton Hardenbrook
09/10/2020
This program will be used to calculate the total dollar amount needed
to buy each student a drone.
"""

#required inputs and variable intiation
num1= int(input("please enter the number of students: "))
num2= float(input("what does a single drone cost?"))

if num1>0 and num2>0:

#calculate
    total= num1*num2

#output
    print("you will need $",str(total),"to purchase the drones")
else:
    print("error, please run again, your values are not greater than zero")
            
