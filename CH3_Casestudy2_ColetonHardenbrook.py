"""
Chapter 3: Case study 2: Newton.py
Coleton Hardenbrook
Date: 09/15/2020
Objective: we will use this program to compute the square root of a number. The program will import the math module and
perform succesful approximations using a while loop.
"""
#import module
import math
#recieve inputs
x=float(input("Enter a positive number: "))    # convert to float type and request user input

#intialize variables

tolerance= 0.000001
estimate= 1.0

#calculate approximation
while True:
    estimate= (estimate + x/estimate) / 2                     
    difference= abs(x-estimate**2)
    if difference <= tolerance:
        break                                       # sets estimate variable  and conditions to run loop
                                                    # loop will break if tolerance is greater than difference
#output results
print("The program's estimate:", estimate)
print("python's estimate:     ", math.sqrt(x))
