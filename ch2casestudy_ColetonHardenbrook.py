"""program: Taxform.py
   Author: Coleton Hardenbrook
   Last date modified: 09/10/2020
   this program is used to calculate
   tax returns. It is based on tax laws and
   user input of wages."""
import math

#initialize the constants
TAX_RATE= 0.20
STANDARD_DEDUCTION= 10000.0
DEPENDENT_DEDUCTION= 3000.0

#REQUEST THE INPUTS
grossIncome= float(input("enter the gross income: "))          
numDependents = int(input("enter the number of dependents: "))

#compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                (DEPENDENT_DEDUCTION * numDependents)
incomeTax= taxableIncome * TAX_RATE

#display the income tax
print("the income tas is $" + str(round(incomeTax,2)))
