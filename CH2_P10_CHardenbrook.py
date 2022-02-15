"""
CH2-Project 10: payroll Calculator
Coleton Hardenbrook
date: 09/10/2020
this program will take inputs from an employee and calulate thier paycheck.
"""

#initialize variables

hourlywage=float(input(" please enter your hourly wage: "))
totalreghours= float(input("please enter your regular hours: "))
totalOThours= float(input("please enter your overtime hours: "))

#calculation
Totalpay= (hourlywage*totalreghours) + ((1.5*hourlywage) * totalOThours)

#output
print("your weekly wage will be: $ ",Totalpay)
      
