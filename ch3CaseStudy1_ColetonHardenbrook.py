""""
Chapter 3 Cast Study : An Investment Report
Coleton Hardenbrook
Date: 09/15/2020
Objective: This program will compute an investment report. The program will use
a simplified form of compount interest. Interest will be computed once each year
and added to the total amount invested. The program will than output a report in tabular format.
"""
#variables

#user inputes
startBalance= float(input("enter the investment amount: ")) #input request for user's starting amount of money
years = int(input("enter the number of years: "))           #input request total years to run calculations
rate= int(input("enter the rate as a percentage: "))        #input request for user's rate of growth

#display header

#computation and display as rows
rate= rate/100                                              #convert user input to percentage

totalInterest = 0.0                                         #initiliaze variable for interest growth 

print("%4s%28s%10s%16s" % \
      ("Year", " Starting Balance",
       "Interest","Ending Balance"))                                        #set format for interger justification
                                                            # set row titles

for year in range(1,years+1):                              # for loop to calculate results for each year
     interest = startBalance * rate               
     endBalance= startBalance + interest                    # print display rows with justification
     print("%4d%18.2f%10.2f%16.2f" % \
           (year,startBalance, interest, endBalance))
startBalance= endBalance
totalInterest += interest
       
#display total

print("Ending balance: $%0.2f" %endBalance)                  #end Balance print
print("Total interest earned: $%0.2f" % totalInterest)       #total interest earned print
