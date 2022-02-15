"""
CH 3- project 9: sum calculator
Coleton Hardenbrook
Date: 09/18/2020
Objective: this program will allow the user to input a set of numbers, dictate when their set ends, and compute/ouput
the summation of the provided number set.
"""

#userinput and variables
theSum=0.0
number= float(input("please enter a number or press enter to end input: "))
while number != "" :   
         number2= number
         theSum+=float(number2)
         number=input("enter the next number:")
         #while loop to incrementaly add sum of numbers in list
print("the sum is",theSum,".")   #output

          
